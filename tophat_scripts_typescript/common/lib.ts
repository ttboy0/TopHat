/**
 * Common library functions for Playwright automation
 */

import * as yaml from 'js-yaml';
import * as fs from 'fs';
import { chromium, firefox, webkit, Browser, Page, BrowserContext } from 'playwright';

interface ElementData {
    locator: string;
    expected_text: string;
    description?: string;
}

interface LocatorData {
    elements: { [key: string]: ElementData };
}

export class PlaywrightManager {
    private browser: Browser | null = null;
    private context: BrowserContext | null = null;
    private page: Page | null = null;

    /**
     * Opens a URL in the specified browser and returns the page object.
     */
    async openUrl(url: string, browserType: string = "chromium"): Promise<Page> {
        try {
            // Launch browser based on type
            const browserArgs = [
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--disable-web-security',
                '--disable-features=VizDisplayCompositor'
            ];

            switch (browserType.toLowerCase()) {
                case "chromium":
                    this.browser = await chromium.launch({ 
                        headless: true,
                        args: browserArgs
                    });
                    break;
                case "firefox":
                    this.browser = await firefox.launch({ headless: true });
                    break;
                case "webkit":
                    this.browser = await webkit.launch({ headless: true });
                    break;
                default:
                    throw new Error(`Unsupported browser type: ${browserType}`);
            }

            // Create context and page
            this.context = await this.browser.newContext({
                viewport: { width: 1280, height: 720 }
            });
            this.page = await this.context.newPage();

            // Navigate to URL
            console.log(`Navigating to: ${url}`);
            await this.page.goto(url, { timeout: 30000 });

            // Wait for page to load - use domcontentloaded instead of networkidle for better reliability
            await this.page.waitForLoadState("domcontentloaded");
            
            // Add a small delay to ensure elements are rendered
            await this.page.waitForTimeout(2000);

            // Assert current URL matches expected URL
            const currentUrl = this.page.url();
            if (!currentUrl.startsWith(url.replace(/\/$/, ''))) {
                console.log(`Warning: Current URL (${currentUrl}) doesn't match expected URL (${url})`);
            } else {
                console.log(`Successfully navigated to: ${currentUrl}`);
            }

            return this.page;

        } catch (error) {
            console.error(`Error opening URL ${url}: ${error}`);
            await this.teardown();
            throw error;
        }
    }

    /**
     * Validates elements on the page based on data from YAML file.
     */
    async validateElementFromData(yamlFilePath: string): Promise<boolean> {
        if (!this.page) {
            throw new Error("Page not initialized. Call openUrl first.");
        }

        try {
            // Load YAML data
            const fileContent = fs.readFileSync(yamlFilePath, 'utf8');
            const data = yaml.load(fileContent) as LocatorData;

            if (!data.elements) {
                throw new Error("YAML file must contain 'elements' key");
            }

            const elements = data.elements;
            let allPassed = true;

            console.log(`\\nValidating ${Object.keys(elements).length} elements...`);

            for (const [elementName, elementData] of Object.entries(elements)) {
                try {
                    const { locator, expected_text, description = elementName } = elementData;

                    console.log(`\\nValidating: ${description}`);
                    console.log(`  Locator: ${locator}`);
                    console.log(`  Expected text: '${expected_text}'`);

                    // Find element using locator
                    const element = this.page.locator(locator).first();

                    // Check if element is visible
                    if (!(await element.isVisible())) {
                        console.log(`  ❌ ERROR: Element '${description}' is not visible on the page`);
                        allPassed = false;
                        continue;
                    }

                    // Get actual text from element
                    const actualText = (await element.textContent())?.trim() || '';

                    // Compare expected vs actual text
                    if (actualText === expected_text) {
                        console.log(`  ✅ SUCCESS: Text matches - '${actualText}'`);
                    } else {
                        console.log(`  ❌ ERROR: Text mismatch for '${description}'`);
                        console.log(`     Expected: '${expected_text}'`);
                        console.log(`     Actual: '${actualText}'`);
                        allPassed = false;
                    }

                } catch (error) {
                    console.log(`  ❌ ERROR: Failed to validate '${elementData.description || elementName}': ${error}`);
                    allPassed = false;
                }
            }

            console.log(`\\n${'='.repeat(50)}`);
            if (allPassed) {
                console.log("🎉 All element validations PASSED!");
            } else {
                console.log("❌ Some element validations FAILED!");
            }
            console.log(`${'='.repeat(50)}`);

            return allPassed;

        } catch (error) {
            console.error(`Error validating elements: ${error}`);
            return false;
        }
    }

    /**
     * Closes the browser and cleans up resources.
     */
    async teardown(): Promise<void> {
        try {
            if (this.page) {
                await this.page.close();
                this.page = null;
            }

            if (this.context) {
                await this.context.close();
                this.context = null;
            }

            if (this.browser) {
                await this.browser.close();
                this.browser = null;
            }

            console.log("Browser closed successfully.");

        } catch (error) {
            console.error(`Error during teardown: ${error}`);
        }
    }
}

/**
 * Utility function to load locator data from YAML file.
 */
export function loadLocatorData(yamlFilePath: string): LocatorData {
    try {
        const fileContent = fs.readFileSync(yamlFilePath, 'utf8');
        return yaml.load(fileContent) as LocatorData;
    } catch (error) {
        console.error(`Error loading YAML file ${yamlFilePath}: ${error}`);
        throw error;
    }
}

