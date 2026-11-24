from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.sign_in_button = page.get_by_role("button", name="Sign in")
        self.error = page.get_by_test_id("login-error")

    def open(self):
        self.page.goto("/login")

    def sign_in(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.sign_in_button.click()
