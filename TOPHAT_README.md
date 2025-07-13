# TopHat Playwright Automation Scripts

This package contains both Python and TypeScript implementations of Playwright automation scripts for testing the TopHat website (tophat.com). Both versions validate the presence of 4 key elements on the website and provide detailed reporting.

## 📦 Package Contents

```
tophat_scripts/
├── TOPHAT_README.md                    # 📖 This comprehensive guide
├── tophat_scripts_python/              # 🐍 Python implementation
│   ├── common/lib.py                   # Core automation functions
│   ├── settings/settings.py            # Configuration settings
│   ├── Locators/locator.yaml           # Element definitions
│   ├── main_script.py                  # Main execution script
│   ├── requirements.txt                # Python dependencies
│   └── README.md                       # Python-specific instructions
└── tophat_scripts_typescript/          # 📘 TypeScript implementation
    ├── common/lib.ts                   # Core automation functions
    ├── settings/settings.ts             # Configuration settings
    ├── Locators/locator.yaml            # Element definitions
    ├── main_script.ts                   # Main execution script
    ├── package.json                     # Node.js dependencies
    ├── tsconfig.json                    # TypeScript configuration
    └── README.md                        # TypeScript-specific instructions
```

## 🎯 What These Scripts Do

Both implementations perform identical testing:

1. **Opens Browser**: Launches a Chromium browser instance (headless mode)
2. **Navigates to URL**: Goes to https://www.tophat.com/
3. **Validates Elements**: Checks for 4 key elements:
   - **Create Your Account** button
   - **In-Class Engagement** feature button
   - **Interactive Content** feature button
   - **AI-Enhanced Tools** feature button
4. **Reports Results**: Provides detailed success/failure reporting
5. **Cleanup**: Properly closes browser and resources

## 🔍 Tested Elements

All locators have been tested and confirmed working on TopHat:

| Element | Locator | Expected Text | Status |
|---------|---------|---------------|--------|
| Create Your Account | `a:has-text('Create Your Account')` | "Create Your Account" | ✅ Validated |
| In-Class Engagement | `button:has-text('In-Class Engagement')` | "In-Class Engagement" | ✅ Validated |
| Interactive Content | `button:has-text('Interactive Content')` | "Interactive Content" | ✅ Validated |
| AI-Enhanced Tools | `button:has-text('AI-Enhanced Tools')` | "AI-Enhanced Tools" | ✅ Validated |

## 🐍 vs 📘 Python vs TypeScript Comparison

| Feature | Python Version | TypeScript Version |
|---------|----------------|-------------------|
| **Language** | Python 3.7+ | TypeScript/Node.js 16+ |
| **Setup Complexity** | Medium (virtual env) | Medium (npm install) |
| **Dependencies** | playwright, PyYAML | @playwright/test, js-yaml |
| **Execution** | `python main_script.py` | `npm start` |
| **Performance** | Fast | Fast |
| **Debugging** | Python debugger | Node.js debugger |
| **IDE Support** | Excellent | Excellent |
| **Learning Curve** | Easy (if familiar with Python) | Easy (if familiar with JS/TS) |

## 🚀 Quick Start Guide

### Choose Your Version

**Choose Python if:**
- You're more comfortable with Python
- Your team primarily uses Python
- You want simpler dependency management
- You prefer Python's syntax and ecosystem

**Choose TypeScript if:**
- You're more comfortable with JavaScript/TypeScript
- Your team primarily uses Node.js
- You want modern async/await patterns
- You prefer TypeScript's type safety

### Python Quick Start

```bash
# Navigate to Python version
cd tophat_scripts_python

# Create virtual environment
python -m venv playwright_env

# Activate virtual environment
source playwright_env/bin/activate  # Linux/macOS
# or
playwright_env\\Scripts\\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Run the test
python main_script.py
```

### TypeScript Quick Start

```bash
# Navigate to TypeScript version
cd tophat_scripts_typescript

# Install dependencies
npm install

# Install Playwright browsers
npx playwright install chromium

# Run the test
npm start
```

## 📊 Expected Output (Both Versions)

```
🚀 Starting Playwright Automation Test for TopHat
============================================================
Target URL: https://www.tophat.com/
Browser: chromium
============================================================

📖 Step 1: Opening browser and navigating to URL...
Navigating to: https://www.tophat.com/
Warning: Current URL (https://tophat.com/) doesn't match expected URL (https://www.tophat.com/)

🔍 Step 2: Validating elements from locator data...

Validating 4 elements...

Validating: Create Your Account button
  Locator: a:has-text('Create Your Account')
  Expected text: 'Create Your Account'
  ✅ SUCCESS: Text matches - 'Create Your Account'

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

Both versions share the same configuration structure:

### Changing Target URL

**Python** (`settings/settings.py`):
```python
BASEURL = "https://www."
URL = BASEURL + "your-target-site.com/"
```

**TypeScript** (`settings/settings.ts`):
```typescript
export const BASEURL = "https://www.";
export const URL = BASEURL + "your-target-site.com/";
```

### Changing Browser

**Python**: Update `BROWSER = "firefox"` in `settings/settings.py`
**TypeScript**: Update `export const BROWSER = "firefox"` in `settings/settings.ts`

Options: `chromium`, `firefox`, `webkit`

### Modifying Elements to Test

Both versions use the same `Locators/locator.yaml` file:

```yaml
elements:
  your_element:
    locator: "text=Your Element Text"
    expected_text: "Your Element Text"
    description: "Description of your element"
```

## 🧪 Testing Different Browsers

### Install Additional Browsers

**Python**:
```bash
playwright install firefox webkit
```

**TypeScript**:
```bash
npx playwright install firefox webkit
```

### Update Configuration

Change the browser setting in the respective settings file and run the tests.

## 🐛 Common Troubleshooting

### Browser Installation Issues

```bash
# Python
playwright install-deps
playwright install

# TypeScript
npx playwright install-deps
npx playwright install
```

### Permission Errors (Linux/macOS)

```bash
# Install system dependencies
sudo npx playwright install-deps
```

### Virtual Environment Issues (Python)

```bash
# Recreate virtual environment
rm -rf playwright_env
python -m venv playwright_env
source playwright_env/bin/activate
pip install -r requirements.txt
```

### Node Modules Issues (TypeScript)

```bash
# Clean and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Element Not Found Errors

1. Check if TopHat website structure has changed
2. Update locators in `Locators/locator.yaml`
3. Use browser developer tools to inspect elements
4. Test with visible browser mode for debugging

## 🔧 Advanced Configuration

### Headless Mode

Both versions run in headless mode by default for server environments. To enable visible browser:

**Python** (`common/lib.py`):
```python
self.browser = self.playwright.chromium.launch(headless=False)
```

**TypeScript** (`common/lib.ts`):
```typescript
this.browser = await chromium.launch({ headless: false });
```

### Custom Timeouts

**Python** (`settings/settings.py`):
```python
TIMEOUT = 60000  # 60 seconds
```

**TypeScript** (`settings/settings.ts`):
```typescript
export const TIMEOUT = 60000; // 60 seconds
```

### Custom Viewport

**Python** (`settings/settings.py`):
```python
VIEWPORT = {"width": 1920, "height": 1080}
```

**TypeScript** (`settings/settings.ts`):
```typescript
export const VIEWPORT = { width: 1920, height: 1080 };
```

## 📈 Success Metrics

- ✅ **100% Test Pass Rate**: All 4 elements validate successfully
- ✅ **Cross-Platform**: Works on Windows, macOS, and Linux
- ✅ **Multiple Browsers**: Supports Chromium, Firefox, and WebKit
- ✅ **Headless Operation**: Runs in server environments
- ✅ **Comprehensive Logging**: Detailed success/failure reporting
- ✅ **Proper Cleanup**: No resource leaks

## 🎓 TopHat-Specific Notes

### URL Handling
- TopHat redirects `www.tophat.com` to `tophat.com`
- Both scripts handle this redirect gracefully
- Warning message is normal and expected

### Element Selection Strategy
- Uses text-based selectors for reliability
- Focuses on main feature navigation buttons
- Avoids mobile-only elements (like hamburger menu)
- Tested with desktop viewport (1280x720)

### Performance Considerations
- Scripts run in headless mode for speed
- Uses optimized browser arguments for stability
- Includes proper wait strategies for element loading

## 🤝 Support

For issues or questions:

1. **Check Prerequisites**: Ensure Python 3.7+/Node.js 16+ is installed
2. **Verify Dependencies**: Run installation commands again
3. **Check Browser Installation**: Ensure Playwright browsers are installed
4. **Review Logs**: Check console output for specific error messages
5. **Test Connectivity**: Ensure internet access to tophat.com

## 📄 License

This project is provided as-is for educational and testing purposes.

---

**Choose your preferred version and follow the respective README.md for detailed setup instructions!**

