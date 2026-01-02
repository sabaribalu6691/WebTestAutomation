# Import Page and expect from Playwright's synchronous API
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_signin_button_visible(page: Page):
    home = HomePage(page) 
    home.open() 
    home.assert_signin_visible()

def test_signup_button_visible(page: Page):
    home = HomePage(page) 
    home.open() 
    home.assert_signup_visible()

def test_github_logo_visible(page: Page):
    home = HomePage(page)
    home.open()
    home.assert_github_logo_visible()

def test_navbar_visible(page: Page):
    home = HomePage(page)
    home.open()
    home.assert_navbar_visible()
