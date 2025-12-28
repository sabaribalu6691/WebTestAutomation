# Playwright Testing - Learning Summary
**Date:** Today  
**Topic:** Web Testing with Playwright for Python

---

## What We Learned Today

### 1. Setting Up Playwright

**Installation:**
```bash
pip install playwright
pip install pytest
pip install pytest-playwright
playwright install  # Install browsers
```

**Key Libraries:**
- `playwright` - Main browser automation library
- `pytest` - Test framework/runner
- `pytest-playwright` - Integration between pytest and Playwright

---

### 2. Understanding pytest vs Playwright

**pytest:**
- Test framework + runner
- General-purpose (works with many libraries)
- Discovers and runs test functions
- Flexible with plugins

**Playwright:**
- Browser automation library
- Specifically for browser testing
- Has its own test runner (`playwright test`)
- Can work with pytest via `pytest-playwright`

**Key Difference:** pytest is a framework, Playwright is a library. They work together.

---

### 3. Synchronous vs Asynchronous Testing

**Synchronous (`sync_api`):**
- Code runs step by step
- Automatically waits for each action
- No `await` keywords needed
- Simpler for learning

**Example:**
```python
from playwright.sync_api import Page, expect

def test_example(page: Page):
    page.goto("https://github.com")  # Waits automatically
    page.click("button")  # Waits for click to complete
```

---

### 4. Test Structure

**Basic Test Function:**
```python
from playwright.sync_api import Page, expect

def test_github_signin(page: Page):
    # Navigate to website
    page.goto("https://github.com")
    
    # Find element
    signin_button = page.get_by_role("link", name="Sign in")
    
    # Assert it's visible
    expect(signin_button).to_be_visible()
```

**Key Points:**
- Function name must start with `test_`
- Takes `page: Page` as parameter (provided by pytest-playwright)
- `Page` (capital) = type/class
- `page` (lowercase) = variable name (the actual browser page object)
- No closing braces needed in Python (uses indentation)

---

### 5. Finding Elements

**Methods to Find Elements:**
- `page.get_by_text("Sign in")` - Find by text content
- `page.get_by_role("link", name="Sign in")` - Find by role and name (more reliable)
- `page.locator("text=Sign in")` - Find using CSS/text selector
- `page.locator('a[href="/login"]')` - Find by attribute

**Best Practice:** Use `get_by_role()` for better reliability.

---

### 6. Assertions

**Using `expect()`:**
```python
expect(element).to_be_visible()  # Check if visible
expect(page).to_have_title("Title")  # Check page title
```

**Key Concepts:**
- **Find** = Locate an element on the page
- **Assert** = Verify/check that something is true

---

### 7. Running Tests

**Command:**
```bash
pytest webtest_autoplaywright.py
```

**Options:**
- `--headed` - Show browser window (watch the test run)
- `--slow-mo=1000` - Slow down actions (milliseconds)

**Example:**
```bash
pytest webtest_autoplaywright.py --headed --slow-mo=1000
```

**Headless vs Headed:**
- **Headless (default)**: Runs in background, faster, no visible browser
- **Headed**: Shows browser window so you can watch

---

### 8. Git Commands We Used

**Initialize Repository:**
```bash
git init
```

**Check Status:**
```bash
git status
```

**Add Files:**
```bash
git add webtest_autoplaywright.py
```

**Commit:**
```bash
git commit -m "Add Playwright test for GitHub sign in button"
```

**Connect to GitHub:**
```bash
git remote add origin https://github.com/username/repo-name.git
```

**Check Remote Connection:**
```bash
git remote -v
```

**Push to GitHub:**
```bash
git push -u origin master
```

**Future Pushes (after -u):**
```bash
git push
```

---

### 9. Git Concepts

**Remote:**
- "Remote" = repository not on your computer (like GitHub)
- `origin` = default name for remote repository
- `git remote add origin <url>` = save the GitHub repo address

**Branch:**
- `master` = default branch name (some repos use `main`)
- `origin/master` = master branch on GitHub (via origin)

**Tracking:**
- `-u` flag = sets up tracking between local and remote branch
- After `-u`, you can just use `git push` instead of `git push origin master`

**Key Terms:**
- **Local** = on your computer
- **Remote** = on GitHub (somewhere else)
- **Origin** = nickname for your GitHub repo
- **Master** = branch name

---

### 10. Complete Test Example

```python
from playwright.sync_api import Page, expect

def test_github_signin(page: Page):
    # Navigate to GitHub
    page.goto("https://github.com")
    
    # Find the Sign in button
    signin_button = page.get_by_role("link", name="Sign in")
    
    # Assert it's visible
    expect(signin_button).to_be_visible()
```

---

## Key Takeaways

1. **Playwright** automates browsers for testing
2. **pytest** runs the tests
3. **Synchronous API** is simpler - no await needed
4. **`page: Page`** parameter is provided automatically by pytest-playwright
5. **`expect()`** is used for assertions
6. **Headless mode** runs tests in background (default)
7. **`--headed`** flag shows the browser
8. **Git** tracks your code changes
9. **Remote** connects local repo to GitHub
10. **`-u` flag** sets up tracking for easier future pushes

---

## Common Commands Reference

**Testing:**
```bash
pytest webtest_autoplaywright.py
pytest webtest_autoplaywright.py --headed
```

**Git:**
```bash
git status
git add filename.py
git commit -m "message"
git remote -v
git push
```

---

## What to Remember

- **Page** (capital) = type/class
- **page** (lowercase) = variable/object
- **Find** = locate element
- **Assert** = verify/check
- **Remote** = repository not on your computer
- **Origin** = nickname for GitHub repo
- **Master** = branch name
- **Headless** = no visible browser (default)
- **Synchronous** = waits automatically, simpler

---

## Next Steps for Practice

1. Try testing different websites
2. Test different elements (buttons, forms, links)
3. Try different assertions (text, attributes, visibility)
4. Practice with `--headed` to see what's happening
5. Create more test files
6. Practice git workflow (add, commit, push)

---

**Repository:** https://github.com/sabaribalu6691/WebTestAutomation



