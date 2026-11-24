import pytest
from playwright.sync_api import Page, expect

from tests.ui.pages.user_details_page import UserDetailsPage
from tests.ui.pages.user_form_page import UserFormPage
from tests.ui.pages.users_page import UsersPage


@pytest.mark.parametrize("search_text, expected_name", [
    ("Chloe", "Chloe Lim"),
    ("tan", "Ben Tan"),
    ("esther.wong@example.com", "Esther Wong"),
])
def test_search_finds_one_user(signed_in_page: Page, search_text: str, expected_name: str):
    users = UsersPage(signed_in_page)

    users.search(search_text)

    expect(users.result_count).to_have_text("Showing 1 user")
    expect(users.rows).to_have_count(1)
    expect(users.rows).to_contain_text(expected_name)


def test_add_user(signed_in_page: Page):
    users = UsersPage(signed_in_page)

    users.add_user()
    form = UserFormPage(signed_in_page)
    form.fill_in(name="Test Engineer", email="test.engineer@example.com", age="30", city="Kuala Lumpur")
    form.save()

    details = UserDetailsPage(signed_in_page)
    expect(details.flash_message).to_have_text("User Test Engineer created successfully.")
    expect(details.heading).to_have_text("Test Engineer")
    expect(details.email).to_have_text("test.engineer@example.com")
    expect(details.age).to_have_text("30")
    expect(details.city).to_have_text("Kuala Lumpur")
