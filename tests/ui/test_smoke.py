import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_sign_in_page_opens(page: Page):
    page.goto("/login")

    expect(page).to_have_title("Sign in | Practice App")
    expect(page.get_by_role("heading", name="Sign in")).to_be_visible()
