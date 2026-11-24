from playwright.sync_api import Page


class UserDetailsPage:
    def __init__(self, page: Page):
        self.page = page
        self.flash_message = page.get_by_test_id("flash-message")
        self.heading = page.get_by_role("heading", level=1)
        self.email = page.get_by_test_id("user-email")
        self.age = page.get_by_test_id("user-age")
        self.city = page.get_by_test_id("user-city")
