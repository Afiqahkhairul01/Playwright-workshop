import os

from playwright.sync_api import Page, expect


def test_sign_in_shows_welcome_message(page: Page):
    username = os.environ["APP_USERNAME"]

    page.goto("/login")
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(os.environ["APP_PASSWORD"])
    page.get_by_role("button", name="Sign in").click()

    expect(page).to_have_title("Users | Practice App")
    expect(page.get_by_test_id("flash-message")).to_have_text(f"Welcome, {username}!")
    expect(page.get_by_test_id("current-user")).to_have_text(f"Signed in as {username}")
