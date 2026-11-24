from playwright.sync_api import Page, expect


class UsersPage:
    def __init__(self, page: Page):
        self.page = page
        self.flash_message = page.get_by_test_id("flash-message")
        self.current_user = page.get_by_test_id("current-user")
        self.search_box = page.get_by_label("Search users")
        self.search_button = page.get_by_role("button", name="Search")
        self.result_count = page.get_by_test_id("result-count")
        self.rows = page.get_by_test_id("user-row")
        self.add_user_link = page.get_by_role("link", name="Add user")
        self.reset_button = page.get_by_role("button", name="Reset data")

    def open(self):
        self.page.goto("/users")

    def search(self, text: str):
        self.search_box.fill(text)
        self.search_button.click()

    def reset_data(self):
        self.reset_button.click()
        # Wait for the reloaded page, so the next step sees the 5 default users
        expect(self.flash_message).to_have_text("Your data has been reset to the 5 default users.")

    def add_user(self):
        self.add_user_link.click()
