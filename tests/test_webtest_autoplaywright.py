# Import Page and expect from Playwright's synchronous API
from playwright.sync_api import Page, expect

# Define test function for GitHub Sign in button
# page: Page parameter is automatically provided by pytest-playwright
def test_github_signin(page: Page):
    # Navigate to GitHub homepage with 60 second timeout
    page.goto("https://github.com", timeout=60000)
    # Find the Sign in link by its role (link) and name (Sign in)
    signin_button = page.get_by_role("link", name="Sign in")
    # Wait for the button to become visible (up to 10 seconds)
    signin_button.wait_for(state="visible", timeout=10000)
    # Assert/verify that the Sign in button is visible on the page
    expect(signin_button).to_be_visible()

# Define test function for GitHub Sign up button
# page: Page parameter is automatically provided by pytest-playwright
def test_github_signup(page: Page):
    # Navigate to GitHub homepage with 60 second timeout
    page.goto("https://github.com", timeout=60000)
    # Find the Sign up link by its role (link) and name (Sign up)
    signup_button = page.get_by_role("link", name="Sign up")
    # Wait for the button to become visible (up to 10 seconds)
    signup_button.wait_for(state="visible", timeout=10000)
    # Assert/verify that the Sign up button is visible on the page
    expect(signup_button).to_be_visible()