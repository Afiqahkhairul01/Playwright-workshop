import os

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def api(playwright):
    context = playwright.request.new_context(
        base_url=os.environ["API_BASE_URL"],
        extra_http_headers={"Authorization": f"Bearer {os.environ['API_TOKEN']}"},
    )
    yield context
    context.dispose()


def test_user_created_through_api_appears_in_ui(api, page: Page):
    # Arrange: create the test data through the API (fast and reliable)
    api.post("/api/reset")
    username = api.get("/api/auth/me").json()["username"]
    response = api.post("/api/users", data={
        "name": "Hybrid Tester",
        "email": "hybrid.tester@example.com",
        "age": 40,
        "address": {"city": "Kuching"},
    })
    assert response.status == 201

    # Act: sign in to the website as the same username, then search
    page.goto("/login")
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(os.environ["APP_PASSWORD"])
    page.get_by_role("button", name="Sign in").click()
    page.get_by_label("Search users").fill("Hybrid Tester")
    page.get_by_role("button", name="Search").click()

    # Assert: the user created through the API is shown in the UI
    expect(page.get_by_test_id("result-count")).to_have_text("Showing 1 user")
    row = page.get_by_test_id("user-row")
    expect(row).to_contain_text("hybrid.tester@example.com")
    expect(row).to_contain_text("Kuching")
