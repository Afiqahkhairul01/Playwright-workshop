import os

import pytest
from playwright.sync_api import Page

from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.users_page import UsersPage


@pytest.fixture
def signed_in_page(page: Page):
    # Setup: sign in, then start from the 5 default users
    login = LoginPage(page)
    login.open()
    login.sign_in(os.environ["APP_USERNAME"], os.environ["APP_PASSWORD"])
    page.wait_for_url("**/users")
    users = UsersPage(page)
    users.reset_data()

    yield page

    # Teardown: put the 5 default users back, even if the test failed
    users.open()
    users.reset_data()
