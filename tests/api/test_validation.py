import pytest

from tests.api.helpers import build_user


def test_missing_fields_are_all_reported(api):
    response = api.post("/api/users", data={})

    assert response.status == 400
    body = response.json()
    assert body["error"] == "Validation failed"
    assert body["details"] == {
        "name": "Name is required",
        "email": "Email is required",
        "age": "Age is required",
    }


@pytest.mark.parametrize("age, expected_status", [
    (17, 400),
    (18, 201),
    (120, 201),
    (121, 400),
])
def test_age_boundaries(api, age, expected_status):
    response = api.post("/api/users", data=build_user(age=age))

    assert response.status == expected_status


def test_duplicate_email_returns_409(api):
    response = api.post("/api/users", data=build_user(email="AISHA.RAHMAN@example.com"))

    assert response.status == 409
    assert response.json()["error"] == "A user with this email already exists"


def test_unknown_field_is_rejected(api):
    response = api.post("/api/users", data=build_user(phone="0123456789"))

    assert response.status == 400
    assert response.json()["details"]["phone"] == "Unknown field"
