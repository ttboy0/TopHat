"""
Common library functions for Playwright automation
"""

import yaml
import os
from playwright.sync_api import sync_playwright, Browser, Page, BrowserContext
from typing import Dict, Any, Optional

class PlaywrightManager:
    def __init__(self):
        self.playwright = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None

    def open_url(self, url: str, browser_type: str = "chromium") -> Page:
        """
        Opens a URL in the specified browser and returns the page object.
        
        Args:
            url (str): The URL to navigate to
            browser_type (str): Browser type (chromium, firefox, webkit)
            
        Returns:
            Page: Playwright page object
        """
        try:
            # Initialize Playwright
            self.playwright = sync_playwright().start()
            
            # Launch browser based on type
            browser_args = [
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--disable-web-security',
                '--disable-features=VizDisplayCompositor'
            ]
            
            if browser_type.lower() == "chromium":
                self.browser = self.playwright.chromium.launch(
                    headless=True,
                    args=browser_args
                )
            elif browser_type.lower() == "firefox":
                self.browser = self.playwright.firefox.launch(headless=True)
            elif browser_type.lower() == "webkit":
                self.browser = self.playwright.webkit.launch(headless=True)
            else:
                raise ValueError(f"Unsupported browser type: {browser_type}")
            
            # Create context and page
            self.context = self.browser.new_context(viewport={"width": 1280, "height": 720})
            self.page = self.context.new_page()
            
            # Navigate to URL
            print(f"Navigating to: {url}")
            self.page.goto(url, timeout=30000)
            
            # Wait for page to load
            self.page.wait_for_load_state("networkidle")
            
            # Assert current URL matches expected URL
            current_url = self.page.url
            if not current_url.startswith(url.rstrip('/')):
                print(f"Warning: Current URL ({current_url}) doesn't match expected URL ({url})")
            else:
                print(f"Successfully navigated to: {current_url}")
            
            return self.page
            
        except Exception as e:
            print(f"Error opening URL {url}: {str(e)}")
            self.teardown()
            raise

    def validate_element_from_data(self, yaml_file_path: str) -> bool:
        """
        Validates elements on the page based on data from YAML file.
        
        Args:
            yaml_file_path (str): Path to the YAML file containing element data
            
        Returns:
            bool: True if all validations pass, False otherwise
        """
        if not self.page:
            raise RuntimeError("Page not initialized. Call open_url first.")
        
        try:
            # Load YAML data
            with open(yaml_file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
            
            if 'elements' not in data:
                raise ValueError("YAML file must contain 'elements' key")
            
            elements = data['elements']
            all_passed = True
            
            print(f"\\nValidating {len(elements)} elements...")
            
            for element_name, element_data in elements.items():
                try:
                    locator = element_data['locator']
                    expected_text = element_data['expected_text']
                    description = element_data.get('description', element_name)
                    
                    print(f"\\nValidating: {description}")
                    print(f"  Locator: {locator}")
                    print(f"  Expected text: '{expected_text}'")
                    
                    # Find element using locator
                    element = self.page.locator(locator).first
                    
                    # Check if element is visible
                    if not element.is_visible():
                        print(f"  ❌ ERROR: Element '{description}' is not visible on the page")
                        all_passed = False
                        continue
                    
                    # Get actual text from element
                    actual_text = element.text_content().strip()
                    
                    # Compare expected vs actual text
                    if actual_text == expected_text:
                        print(f"  ✅ SUCCESS: Text matches - '{actual_text}'")
                    else:
                        print(f"  ❌ ERROR: Text mismatch for '{description}'")
                        print(f"     Expected: '{expected_text}'")
                        print(f"     Actual: '{actual_text}'")
                        all_passed = False
                        
                except Exception as e:
                    print(f"  ❌ ERROR: Failed to validate '{description}': {str(e)}")
                    all_passed = False
            
            print(f"\\n{'='*50}")
            if all_passed:
                print("🎉 All element validations PASSED!")
            else:
                print("❌ Some element validations FAILED!")
            print(f"{'='*50}")
            
            return all_passed
            
        except Exception as e:
            print(f"Error validating elements: {str(e)}")
            return False

    def teardown(self):
        """
        Closes the browser and cleans up resources.
        """
        try:
            if self.page:
                self.page.close()
                self.page = None
                
            if self.context:
                self.context.close()
                self.context = None
                
            if self.browser:
                self.browser.close()
                self.browser = None
                
            if self.playwright:
                self.playwright.stop()
                self.playwright = None
                
            print("Browser closed successfully.")
            
        except Exception as e:
            print(f"Error during teardown: {str(e)}")


def load_locator_data(yaml_file_path: str) -> Dict[str, Any]:
    """
    Utility function to load locator data from YAML file.
    
    Args:
        yaml_file_path (str): Path to the YAML file
        
    Returns:
        Dict[str, Any]: Loaded YAML data
    """
    try:
        with open(yaml_file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error loading YAML file {yaml_file_path}: {str(e)}")
        raise

