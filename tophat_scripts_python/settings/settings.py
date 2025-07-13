"""
Global settings for Playwright automation scripts
"""

# Base URL configuration
BASEURL = "https://www."

# Target URL
URL = BASEURL + "tophat.com/"

# Browser configuration
BROWSER = "chromium"  # Options: chromium, firefox, webkit

# Browser options
HEADLESS = False  # Set to True for headless mode
TIMEOUT = 30000   # Default timeout in milliseconds
VIEWPORT = {"width": 1280, "height": 720}  # Browser viewport size

