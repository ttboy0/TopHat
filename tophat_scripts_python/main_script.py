#!/usr/bin/env python3
"""
Main script for TopHat Playwright automation testing
"""

import sys
import os
from pathlib import Path

# Add project directories to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import project modules
from settings import settings
from common.lib import PlaywrightManager

def main():
    """
    Main function to execute the Playwright automation test
    """
    print("🚀 Starting Playwright Automation Test for TopHat")
    print("=" * 60)
    print(f"Target URL: {settings.URL}")
    print(f"Browser: {settings.BROWSER}")
    print("=" * 60)
    
    # Initialize Playwright manager
    playwright_manager = PlaywrightManager()
    
    try:
        # Step 1: Open browser and navigate to URL
        print("\\n📖 Step 1: Opening browser and navigating to URL...")
        page = playwright_manager.open_url(settings.URL, settings.BROWSER)
        
        # Step 2: Validate elements from locator data
        print("\\n🔍 Step 2: Validating elements from locator data...")
        locator_file = project_root / "Locators" / "locator.yaml"
        validation_result = playwright_manager.validate_element_from_data(str(locator_file))
        
        # Step 3: Report final results
        print("\\n📊 Step 3: Final Results")
        print("=" * 60)
        if validation_result:
            print("🎉 TEST PASSED: All elements validated successfully!")
            exit_code = 0
        else:
            print("❌ TEST FAILED: Some element validations failed!")
            exit_code = 1
        print("=" * 60)
        
    except Exception as e:
        print(f"\\n💥 CRITICAL ERROR: {str(e)}")
        print("Test execution failed!")
        exit_code = 1
        
    finally:
        # Step 4: Cleanup
        print("\\n🧹 Step 4: Cleaning up resources...")
        playwright_manager.teardown()
        
    print("\\n✅ Test execution completed.")
    sys.exit(exit_code)

if __name__ == "__main__":
    main()

