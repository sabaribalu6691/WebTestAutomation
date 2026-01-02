from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.signin_button = page.get_by_role("link", name="Sign in")
        self.signup_button = page.get_by_role("link", name="Sign up")
        self.github_logo = page.locator('a[aria-label="Homepage"]')
        self.navbar = page.get_by_role("banner")

        
    def open(self):
        self.page.goto("https://github.com", timeout=60000)

    def assert_signin_visible(self):
        self.signin_button.wait_for(state="visible", timeout=10000)
        expect(self.signin_button).to_be_visible()

    def assert_signup_visible(self):
        self.signup_button.wait_for(state="visible", timeout=10000)
        expect(self.signup_button).to_be_visible()

    def assert_github_logo_visible(self):
        self.github_logo.wait_for(state="visible", timeout=10000)
        expect(self.github_logo).to_be_visible()

    def assert_navbar_visible(self):
        self.navbar.wait_for(state="visible", timeout=10000)
        expect(self.navbar).to_be_visible()

