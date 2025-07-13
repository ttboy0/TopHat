# Playwright TypeScript Automation Scripts - TopHat

This project contains TypeScript-based Playwright automation scripts for testing the TopHat website. The scripts validate the presence of 4 key elements on the website and provide detailed reporting.

## 📁 Project Structure

```
tophat_scripts_typescript/
├── common/
│   └── lib.ts                # Common functions and PlaywrightManager class
├── settings/
│   └── settings.ts           # Global configuration settings
├── Locators/
│   └── locator.yaml          # Element locators and expected values
├── main_script.ts            # Main execution script
├── package.json              # Node.js dependencies and scripts
├── tsconfig.json             # TypeScript configuration
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

- Node.js 16.0 or higher
- npm (Node Package Manager)
- Internet connection

## 📦 Installation & Setup

### Step 1: Clone or Extract Project

Extract the project files to your desired directory.

### Step 2: Navigate to Project Directory

```bash
cd tophat_scripts_typescript
```

### Step 3: Install Dependencies

```bash
# Install Node.js packages
npm install

# Install Playwright browsers
npx playwright install chromium
```

### Step 4: Verify Installation

```bash
# Check if Playwright is installed correctly
npx playwright --version

# Check TypeScript compilation
npm run build
```

## 🚀 Execution

### Method 1: Using npm scripts (Recommended)

```bash
# Build and run the script
npm run start

# Or run the test command
npm test
```

### Method 2: Manual compilation and execution

```bash
# Compile TypeScript to JavaScript
npm run build

# Run the compiled JavaScript
node main_script.js
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

Edit `settings/settings.ts`:

```typescript
// Change the base URL or specific path
export const BASEURL = "https://www.";
export const URL = BASEURL + "your-target-site.com/";
```

### Changing Browser

Edit `settings/settings.ts`:

```typescript
// Options: chromium, firefox, webkit
export const BROWSER = "firefox";
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

To run in headless mode, modify `common/lib.ts`:

```typescript
// Change headless: false to headless: true
this.browser = await chromium.launch({ headless: true });
```

### Different Browsers

Install additional browsers:

```bash
# Install Firefox
npx playwright install firefox

# Install WebKit (Safari)
npx playwright install webkit
```

Then update `settings/settings.ts` to use "firefox" or "webkit".

## 📝 Available npm Scripts

```bash
# Build TypeScript files
npm run build

# Build and run the script
npm run start

# Run tests (alias for start)
npm test

# Clean compiled JavaScript files
npm run clean
```

## 🐛 Troubleshooting

### Common Issues

1. **Browser not found**
   ```bash
   # Reinstall browsers
   npx playwright install
   ```

2. **TypeScript compilation errors**
   ```bash
   # Check TypeScript configuration
   npx tsc --noEmit
   
   # Reinstall dependencies
   rm -rf node_modules package-lock.json
   npm install
   ```

3. **Permission errors**
   ```bash
   # On Linux/macOS, you might need to install system dependencies
   npx playwright install-deps
   ```

4. **Module not found errors**
   - Ensure all dependencies are installed: `npm list`
   - Check that TypeScript compilation was successful: `npm run build`

5. **Element not found**
   - Check if website structure has changed
   - Update locators in `Locators/locator.yaml`
   - Use browser developer tools to inspect elements

### Debug Mode

For debugging, you can modify the script to add pauses:

```typescript
// Add this in main_script.ts after opening URL
await new Promise(resolve => {
    console.log("Press Ctrl+C to continue...");
    process.stdin.once('data', resolve);
});
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

Modify `common/lib.ts` in the `validateElementFromData` method to add custom validation logic.

## 🔧 Advanced Usage

### Running with Different Timeouts

Modify `settings/settings.ts`:

```typescript
export const TIMEOUT = 60000; // 60 seconds
```

### Custom Viewport Size

```typescript
export const VIEWPORT = { width: 1920, height: 1080 };
```

### TypeScript Development

For development with TypeScript:

```bash
# Watch mode for automatic compilation
npx tsc --watch

# Type checking without compilation
npx tsc --noEmit
```

## 📊 Exit Codes

- `0`: All tests passed successfully
- `1`: One or more tests failed or error occurred

## 🔍 Project Dependencies

### Runtime Dependencies
- `@playwright/test`: Playwright testing framework
- `playwright`: Playwright browser automation
- `js-yaml`: YAML parsing library

### Development Dependencies
- `typescript`: TypeScript compiler
- `@types/node`: Node.js type definitions
- `@types/js-yaml`: js-yaml type definitions

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all prerequisites are met
3. Ensure all dependencies are installed correctly
4. Check TypeScript compilation is successful

## 📄 License

This project is provided as-is for educational and testing purposes.

