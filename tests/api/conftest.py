import os

import pytest


@pytest.fixture(scope="session")
def api(playwright):
    """A request context that sends your token with every request."""
    context = playwright.request.new_context(
        base_url=os.environ["API_BASE_URL"],
        extra_http_headers={"Authorization": f"Bearer {os.environ['API_TOKEN']}"},
    )
    yield context
    context.dispose()


@pytest.fixture(scope="session")
def anonymous_api(playwright):
    """A request context with no token, for authentication tests."""
    context = playwright.request.new_context(base_url=os.environ["API_BASE_URL"])
    yield context
    context.dispose()


@pytest.fixture(autouse=True)
def reset_data(api):
    """Start every API test with the 5 default users."""
    response = api.post("/api/reset")
    assert response.status == 200, response.text()
