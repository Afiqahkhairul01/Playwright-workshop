import os

import pytest
from playwright.sync_api import Page

from tests.ui.pages.login_page import LoginPage


@pytest.fixture
def signed_in_page(page: Page) -> Page:
    login = LoginPage(page)
    login.open()
    login.sign_in(os.environ["APP_USERNAME"], os.environ["APP_PASSWORD"])
    # Stop here, with a clear error, if signing in didn't work
    page.wait_for_url("**/users")
    return page
