from playwright.sync_api import Page, expect

def test_github_signin(page: Page):
    # Navigate to GitHub
    page.goto("https://github.com")
    
    # Your test code here - find and assert the Sign in button
    signin_button = page.get_by_role("link", name="Sign in")
    expect(signin_button).to_be_visible()
