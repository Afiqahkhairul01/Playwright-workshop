from playwright.sync_api import Page


class UserFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.name = page.get_by_label("Name")
        self.email = page.get_by_label("Email")
        self.age = page.get_by_label("Age")
        self.city = page.get_by_label("City")
        self.save_button = page.get_by_role("button", name="Save user")

    def fill_in(self, name: str, email: str, age: str, city: str):
        self.name.fill(name)
        self.email.fill(email)
        self.age.fill(age)
        self.city.fill(city)

    def save(self):
        self.save_button.click()
