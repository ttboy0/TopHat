# Playwright Python Automation Scripts - TopHat

This project contains Python-based Playwright automation scripts for testing the TopHat website. The scripts validate the presence of 4 key elements on the website and provide detailed reporting.

## 📁 Project Structure

```
tophat_scripts_python/
├── common/
│   └── lib.py                # Common functions and PlaywrightManager class
├── settings/
│   └── settings.py           # Global configuration settings
├── Locators/
│   └── locator.yaml          # Element locators and expected values
├── main_script.py            # Main execution script
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 🎯 What This Script Does

1. **Opens Browser**: Launches a Chromium browser instance
2. **Navigates to URL**: Goes to https://www.tophat.com/
3. **Validates Elements**: Checks for 4 key elements:
   - Menu navigation button
   - In-Class Engagement feature button
   - Interactive Content feature button
   - AI-Enhanced Tools feature button
4. **Reports Results**: Provides detailed success/failure reporting
5. **Cleanup**: Properly closes browser and resources

## 🛠️ Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Internet connection

## 📦 Installation & Setup

### Step 1: Clone or Extract Project

Extract the project files to your desired directory.

### Step 2: Navigate to Project Directory

```bash
cd tophat_scripts_python
```

### Step 3: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv playwright_env

# Activate virtual environment
# On Windows:
playwright_env\\Scripts\\activate

# On macOS/Linux:
source playwright_env/bin/activate
```

### Step 4: Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### Step 5: Verify Installation

```bash
# Check if Playwright is installed correctly
playwright --version

# Verify Python dependencies
pip list
```

## 🚀 Execution

### Method 1: Direct execution (Recommended)

```bash
# Make sure virtual environment is activated
source playwright_env/bin/activate  # On macOS/Linux
# or
playwright_env\\Scripts\\activate   # On Windows

# Run the script
python main_script.py
```

### Method 2: Using Python module execution

```bash
python -m main_script
```

### Expected Output

```
🚀 Starting Playwright Automation Test for TopHat
============================================================
Target URL: https://www.tophat.com/
Browser: chromium
============================================================

📖 Step 1: Opening browser and navigating to URL...
Navigating to: https://www.tophat.com/
Successfully navigated to: https://tophat.com/

🔍 Step 2: Validating elements from locator data...

Validating 4 elements...

Validating: Menu navigation button
  Locator: button:has-text('Menu')
  Expected text: 'Menu'
  ✅ SUCCESS: Text matches - 'Menu'

Validating: In-Class Engagement feature button
  Locator: button:has-text('In-Class Engagement')
  Expected text: 'In-Class Engagement'
  ✅ SUCCESS: Text matches - 'In-Class Engagement'

Validating: Interactive Content feature button
  Locator: button:has-text('Interactive Content')
  Expected text: 'Interactive Content'
  ✅ SUCCESS: Text matches - 'Interactive Content'

Validating: AI-Enhanced Tools feature button
  Locator: button:has-text('AI-Enhanced Tools')
  Expected text: 'AI-Enhanced Tools'
  ✅ SUCCESS: Text matches - 'AI-Enhanced Tools'

==================================================
🎉 All element validations PASSED!
==================================================

📊 Step 3: Final Results
============================================================
🎉 TEST PASSED: All elements validated successfully!
============================================================

🧹 Step 4: Cleaning up resources...
Browser closed successfully.

✅ Test execution completed.
```

## ⚙️ Configuration

### Modifying Target URL

Edit `settings/settings.py`:

```python
# Change the base URL or specific path
BASEURL = "https://www."
URL = BASEURL + "your-target-site.com/"
```

### Changing Browser

Edit `settings/settings.py`:

```python
# Options: chromium, firefox, webkit
BROWSER = "firefox"
```

### Modifying Elements to Test

Edit `Locators/locator.yaml`:

```yaml
elements:
  your_element:
    locator: "text=Your Element Text"
    expected_text: "Your Element Text"
    description: "Description of your element"
```

## 🧪 Running Tests

### Headless Mode

To run in headless mode, modify `common/lib.py`:

```python
# Change headless=False to headless=True
self.browser = self.playwright.chromium.launch(headless=True)
```

### Different Browsers

Install additional browsers:

```bash
# Install Firefox
playwright install firefox

# Install WebKit (Safari)
playwright install webkit
```

Then update `settings/settings.py` to use "firefox" or "webkit".

## 🐛 Troubleshooting

### Common Issues

1. **Browser not found**
   ```bash
   # Reinstall browsers
   playwright install
   ```

2. **Import errors**
   ```bash
   # Ensure virtual environment is activated
   source playwright_env/bin/activate
   
   # Verify dependencies are installed
   pip list
   ```

3. **Permission errors**
   ```bash
   # On Linux/macOS, you might need to install system dependencies
   playwright install-deps
   ```

4. **Virtual environment issues**
   ```bash
   # Recreate virtual environment
   rm -rf playwright_env
   python -m venv playwright_env
   source playwright_env/bin/activate
   pip install -r requirements.txt
   ```

5. **Element not found**
   - Check if website structure has changed
   - Update locators in `Locators/locator.yaml`
   - Use browser developer tools to inspect elements

### Debug Mode

For debugging, you can modify the script to add pauses:

```python
# Add this in main_script.py after opening URL
input("Press Enter to continue...")
```

## 📝 Customization

### Adding New Elements

1. Open `Locators/locator.yaml`
2. Add new element following the existing pattern:

```yaml
elements:
  new_element:
    locator: "css=.your-css-selector"
    expected_text: "Expected Text"
    description: "Description of new element"
```

### Custom Validation Logic

Modify `common/lib.py` in the `validate_element_from_data` method to add custom validation logic.

## 🔧 Advanced Usage

### Running with Different Timeouts

Modify `settings/settings.py`:

```python
TIMEOUT = 60000  # 60 seconds
```

### Custom Viewport Size

```python
VIEWPORT = {"width": 1920, "height": 1080}
```

### Environment Variables

You can override settings using environment variables:

```bash
export TOPHAT_URL="https://staging.tophat.com/"
export TOPHAT_BROWSER="firefox"
python main_script.py
```

## 📊 Exit Codes

- `0`: All tests passed successfully
- `1`: One or more tests failed or error occurred

## 🔍 Project Dependencies

### Runtime Dependencies
- `playwright`: Browser automation library
- `PyYAML`: YAML parsing library

### Development Dependencies
- None (minimal setup for production use)

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all prerequisites are met
3. Ensure virtual environment is activated
4. Check that Playwright browsers are installed

## 📄 License

This project is provided as-is for educational and testing purposes.

