import os

from playwright.sync_api import Page, expect


def test_search_by_name(page: Page):
    page.goto("/login")
    page.get_by_label("Username").fill(os.environ["APP_USERNAME"])
    page.get_by_label("Password").fill(os.environ["APP_PASSWORD"])
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Reset data").click()

    page.get_by_label("Search users").fill("Chloe")
    page.get_by_role("button", name="Search").click()

    expect(page.get_by_test_id("result-count")).to_have_text("Showing 1 user")
    expect(page.get_by_test_id("user-row")).to_have_count(1)
    expect(page.get_by_test_id("user-row")).to_contain_text("Chloe Lim")


def test_add_user(page: Page):
    page.goto("/login")
    page.get_by_label("Username").fill(os.environ["APP_USERNAME"])
    page.get_by_label("Password").fill(os.environ["APP_PASSWORD"])
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Reset data").click()

    page.get_by_role("link", name="Add user").click()
    page.get_by_label("Name").fill("Test Engineer")
    page.get_by_label("Email").fill("test.engineer@gmail.com")
    page.get_by_label("Age").fill("25")
    page.get_by_label("City").fill("Kuala Lumpur")
    page.get_by_role("button", name="Save user").click()

    expect(page.get_by_test_id("flash-message")).to_have_text("User Test Engineer created successfully.")
    expect(page.get_by_role("heading", level=1)).to_have_text("Test Engineer")
    expect(page.get_by_test_id("user-email")).to_have_text("test.engineer@gmail.com")
    expect(page.get_by_test_id("user-age")).to_have_text("25")
    expect(page.get_by_test_id("user-city")).to_have_text("Kuala Lumpur")
