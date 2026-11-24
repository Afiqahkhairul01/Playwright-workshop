import os

from playwright.sync_api import Page, expect

from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.users_page import UsersPage


def test_sign_in_shows_welcome_message(page: Page):
    username = os.environ["APP_USERNAME"]

    login = LoginPage(page)
    login.open()
    login.sign_in(username, os.environ["APP_PASSWORD"])

    users = UsersPage(page)
    expect(page).to_have_title("Users | Practice App")
    expect(users.flash_message).to_have_text(f"Welcome, {username}!")
    expect(users.current_user).to_have_text(f"Signed in as {username}")
