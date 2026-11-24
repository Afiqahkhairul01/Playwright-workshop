from playwright.sync_api import Page, expect

from tests.ui.pages.user_details_page import UserDetailsPage
from tests.ui.pages.user_form_page import UserFormPage
from tests.ui.pages.users_page import UsersPage


def test_search_by_name(signed_in_page: Page):
    users = UsersPage(signed_in_page)
    users.reset_data()

    users.search("Chloe")

    expect(users.result_count).to_have_text("Showing 1 user")
    expect(users.rows).to_have_count(1)
    expect(users.rows).to_contain_text("Chloe Lim")


def test_add_user(signed_in_page: Page):
    users = UsersPage(signed_in_page)
    users.reset_data()

    users.add_user()
    form = UserFormPage(signed_in_page)
    form.fill_in(name="Test Engineer", email="test.engineer@gmail.com", age="25", city="Kuala Lumpur")
    form.save()

    details = UserDetailsPage(signed_in_page)
    expect(details.flash_message).to_have_text("User Test Engineer created successfully.")
    expect(details.heading).to_have_text("Test Engineer")
    expect(details.email).to_have_text("test.engineer@gmail.com")
    expect(details.age).to_have_text("25")
    expect(details.city).to_have_text("Kuala Lumpur")
