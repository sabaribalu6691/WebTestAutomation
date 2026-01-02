# Playwright Testing - Complete Learning Summary
**Date:** Today's Session  
**Project:** WebTestAutomation

---

## Table of Contents
1. [What We Learned Today](#what-we-learned-today)
2. [Playwright Setup](#playwright-setup)
3. [Test Structure](#test-structure)
4. [Key Concepts](#key-concepts)
5. [Finding Elements](#finding-elements)
6. [Writing Tests](#writing-tests)
7. [Running Tests](#running-tests)
8. [Git Commands](#git-commands)
9. [Project Structure](#project-structure)
10. [Code Examples](#code-examples)

---

## What We Learned Today

### Goals Achieved:
- ✅ Installed Playwright for Python
- ✅ Created first test (GitHub Sign in button)
- ✅ Created second test (GitHub Sign up button)
- ✅ Learned test structure and syntax
- ✅ Learned Git workflow (commit, push)
- ✅ Set up GitHub repository

---

## Playwright Setup

### Installation Commands:
```bash
pip install playwright
pip install pytest
pip install pytest-playwright
playwright install  # Install browsers
```

### Key Libraries:
- **`playwright`** - Browser automation library
- **`pytest`** - Test framework/runner
- **`pytest-playwright`** - Integration plugin

### Understanding pytest vs Playwright:
- **pytest**: Test framework + runner (general purpose)
- **Playwright**: Browser automation library (for web testing)
- They work together: pytest runs tests, Playwright controls browsers

---

## Test Structure

### Basic Test Function:
```python
from playwright.sync_api import Page, expect

def test_name(page: Page):
    # Test code here
    pass
```

### Key Components:
1. **Import statement**: `from playwright.sync_api import Page, expect`
2. **Function name**: Must start with `test_`
3. **Parameter**: `page: Page` (automatically provided by pytest-playwright)
4. **Test code**: Navigate, find elements, assert

### Understanding Parameters:
- **`Page`** (capital P) = Type/class from Playwright
- **`page`** (lowercase p) = Variable name (the actual browser page object)
- Playwright provides the `page` object automatically

---

## Key Concepts

### Synchronous vs Asynchronous:
- **Synchronous (`sync_api`)**: Code runs step-by-step, waits automatically
- **No `await` keywords needed**
- Simpler for learning
- Example: `page.goto()` waits for page to load automatically

### Test Execution:
- **Headless mode (default)**: Runs in background, no visible browser
- **Headed mode**: Shows browser window (`--headed` flag)
- **Timeouts**: Maximum wait time (60 seconds = 60000 milliseconds)

### Finding vs Asserting:
- **Find**: Locate an element on the page (`page.get_by_role()`)
- **Assert**: Verify something is true (`expect(element).to_be_visible()`)

---

## Finding Elements

### Methods to Find Elements:

1. **`page.get_by_role()`** - By role and name (most reliable)
   ```python
   page.get_by_role("link", name="Sign in")
   ```

2. **`page.get_by_text()`** - By visible text
   ```python
   page.get_by_text("Sign up")
   ```

3. **`page.locator()`** - By CSS selector or text
   ```python
   page.locator("text=Sign in")
   page.locator('a[href="/login"]')
   ```

### Understanding Roles:
- **Role** = What the element is/does (link, button, heading, textbox)
- **Name** = Accessible text (what screen readers see)
- Example: `get_by_role("link", name="Sign in")` = Find link with text "Sign in"

---

## Writing Tests

### Complete Test Example:
```python
from playwright.sync_api import Page, expect

def test_github_signin(page: Page):
    # Navigate to GitHub with timeout
    page.goto("https://github.com", timeout=60000)
    
    # Find the Sign in button
    signin_button = page.get_by_role("link", name="Sign in")
    
    # Wait for button to appear (up to 10 seconds)
    signin_button.wait_for(state="visible", timeout=10000)
    
    # Assert it's visible
    expect(signin_button).to_be_visible()
```

### Key Points:
- **Navigation**: `page.goto(url, timeout=60000)`
- **Finding**: `page.get_by_role("link", name="Sign in")`
- **Waiting**: `element.wait_for(state="visible", timeout=10000)`
- **Asserting**: `expect(element).to_be_visible()`

### Understanding Timeouts:
- **`page.goto()` timeout (60s)**: Waits for page to navigate/load
- **`wait_for()` timeout (10s)**: Waits for specific element to appear
- **Why both?**: Page might load, but element takes time to appear

---

## Running Tests

### Basic Commands:
```bash
# Run all tests
pytest tests/test_webtest_autoplaywright.py

# Run specific test
pytest tests/test_webtest_autoplaywright.py::test_github_signin

# Run with visible browser
pytest tests/test_webtest_autoplaywright.py --headed

# Run with slow motion (watch actions)
pytest tests/test_webtest_autoplaywright.py --headed --slow-mo=1000
```

### Expected Output (Success):
```
============================= test session starts =============================
collected 2 items

test_webtest_autoplaywright.py::test_github_signin[chromium] PASSED
test_webtest_autoplaywright.py::test_github_signup[chromium] PASSED

============================== 2 passed in XX.XXs ==============================
```

---

## Git Commands

### Basic Workflow:

```bash
# Check status
git status

# Add files
git add filename.py

# Commit
git commit -m "Your commit message"

# Push to GitHub
git push
```

### Git Concepts:

**Local vs Remote:**
- **Local**: Repository on your computer
- **Remote**: Repository on GitHub (somewhere else)

**Key Terms:**
- **`origin`**: Nickname for your GitHub repository
- **`master`**: Branch name (default branch)
- **`origin/master`**: Master branch on GitHub

**Setting up Remote:**
```bash
# Add remote repository
git remote add origin https://github.com/username/repo-name.git

# Check remote connection
git remote -v

# Push with tracking setup
git push -u origin master

# Future pushes (after -u)
git push
```

**Understanding `-u` flag:**
- Sets up tracking between local and remote branch
- After using `-u`, you can just use `git push` (no need for `git push origin master`)

---

## Project Structure

### Current Structure:
```
playwrighttesting/
  ├── pages/
  │   └── home_page.py      # Page Object Model (to be implemented)
  ├── tests/
  │   └── test_webtest_autoplaywright.py  # Test files
  ├── playwright_learning_notes.md        # Learning notes
  └── README.md                           # Project documentation
```

### Understanding Page Object Model (POM):
- **`pages/`**: Contains page interaction code
- **`tests/`**: Contains test cases
- **Separation**: "What to test" (tests) vs "How to interact" (page objects)

---

## Code Examples

### Test 1: Sign In Button Visibility
```python
from playwright.sync_api import Page, expect

def test_github_signin(page: Page):
    # Navigate to GitHub homepage with 60 second timeout
    page.goto("https://github.com", timeout=60000)
    
    # Find the Sign in link by its role (link) and name (Sign in)
    signin_button = page.get_by_role("link", name="Sign in")
    
    # Wait for the button to become visible (up to 10 seconds)
    signin_button.wait_for(state="visible", timeout=10000)
    
    # Assert/verify that the Sign in button is visible on the page
    expect(signin_button).to_be_visible()
```

### Test 2: Sign Up Button Visibility
```python
def test_github_signup(page: Page):
    # Navigate to GitHub homepage with 60 second timeout
    page.goto("https://github.com", timeout=60000)
    
    # Find the Sign up link by its role (link) and name (Sign up)
    signup_button = page.get_by_role("link", name="Sign up")
    
    # Wait for the button to become visible (up to 10 seconds)
    signup_button.wait_for(state="visible", timeout=10000)
    
    # Assert/verify that the Sign up button is visible on the page
    expect(signup_button).to_be_visible()
```

---

## Common Patterns

### Navigation:
```python
page.goto("https://example.com")
page.goto("https://example.com", timeout=60000)
page.goto("https://example.com", wait_until="domcontentloaded")
```

### Finding Elements:
```python
# By role (recommended)
element = page.get_by_role("link", name="Text")

# By text
element = page.get_by_text("Text")

# By locator
element = page.locator("text=Text")
```

### Assertions:
```python
# Check visibility
expect(element).to_be_visible()

# Check URL
expect(page).to_have_url("https://example.com/page")

# Check title
expect(page).to_have_title("Page Title")
```

### Waiting:
```python
# Wait for element to appear
element.wait_for(state="visible", timeout=10000)

# Wait for navigation
page.wait_for_url("https://example.com/page")
```

---

## Troubleshooting

### Common Issues:

**1. Timeout Errors:**
- **Problem**: Test times out waiting for page/element
- **Solution**: Increase timeout or use `wait_for()` on specific elements

**2. Element Not Found:**
- **Problem**: Can't find element on page
- **Solution**: Check selector, use `--headed` to see what's happening

**3. Tests Pass Individually but Fail Together:**
- **Problem**: State from previous test affects next test
- **Solution**: Each test should be independent (Playwright handles this automatically)

---

## Key Takeaways

### Remember:
1. **Import**: `from playwright.sync_api import Page, expect`
2. **Test function**: `def test_name(page: Page):`
3. **Navigate**: `page.goto(url, timeout=60000)`
4. **Find**: `page.get_by_role("link", name="Text")`
5. **Wait**: `element.wait_for(state="visible")`
6. **Assert**: `expect(element).to_be_visible()`

### Best Practices:
- Use `get_by_role()` for reliability
- Add timeouts for stability
- Use `wait_for()` before assertions
- Keep tests simple and focused
- One assertion per test (when possible)

---

## Next Steps

### To Continue Learning:
1. Learn Page Object Model (POM) pattern
2. Try different assertions (URL, title, text content)
3. Practice with different websites
4. Learn about fixtures and setup/teardown
5. Explore more Playwright features (screenshots, videos, etc.)

### Repository:
- GitHub: https://github.com/sabaribalu6691/WebTestAutomation

---

## Quick Reference

### Commands:
```bash
# Install
pip install playwright pytest pytest-playwright
playwright install

# Run tests
pytest tests/test_file.py
pytest tests/test_file.py --headed

# Git
git add filename.py
git commit -m "message"
git push
```

### Import Statement:
```python
from playwright.sync_api import Page, expect
```

### Test Template:
```python
def test_example(page: Page):
    page.goto("https://example.com", timeout=60000)
    element = page.get_by_role("link", name="Text")
    element.wait_for(state="visible", timeout=10000)
    expect(element).to_be_visible()
```

---

**End of Summary**

