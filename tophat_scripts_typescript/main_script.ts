#!/usr/bin/env node
/**
 * Main script for TopHat Playwright automation testing
 */

import * as path from 'path';
import { PlaywrightManager } from './common/lib';
import * as settings from './settings/settings';

async function main(): Promise<void> {
    console.log("🚀 Starting Playwright Automation Test for TopHat");
    console.log("=".repeat(60));
    console.log(`Target URL: ${settings.URL}`);
    console.log(`Browser: ${settings.BROWSER}`);
    console.log("=".repeat(60));

    // Initialize Playwright manager
    const playwrightManager = new PlaywrightManager();
    let exitCode = 0;

    try {
        // Step 1: Open browser and navigate to URL
        console.log("\\n📖 Step 1: Opening browser and navigating to URL...");
        await playwrightManager.openUrl(settings.URL, settings.BROWSER);

        // Step 2: Validate elements from locator data
        console.log("\\n🔍 Step 2: Validating elements from locator data...");
        const locatorFile = path.join(__dirname, "Locators", "locator.yaml");
        const validationResult = await playwrightManager.validateElementFromData(locatorFile);

        // Step 3: Report final results
        console.log("\\n📊 Step 3: Final Results");
        console.log("=".repeat(60));
        if (validationResult) {
            console.log("🎉 TEST PASSED: All elements validated successfully!");
            exitCode = 0;
        } else {
            console.log("❌ TEST FAILED: Some element validations failed!");
            exitCode = 1;
        }
        console.log("=".repeat(60));

    } catch (error) {
        console.error(`\\n💥 CRITICAL ERROR: ${error}`);
        console.log("Test execution failed!");
        exitCode = 1;

    } finally {
        // Step 4: Cleanup
        console.log("\\n🧹 Step 4: Cleaning up resources...");
        await playwrightManager.teardown();
    }

    console.log("\\n✅ Test execution completed.");
    process.exit(exitCode);
}

// Execute main function
if (require.main === module) {
    main().catch((error) => {
        console.error("Unhandled error:", error);
        process.exit(1);
    });
}

