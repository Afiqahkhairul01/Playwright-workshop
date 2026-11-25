def test_request_without_token_returns_401(anonymous_api):
    response = anonymous_api.get("/api/users")

    assert response.status == 401
    assert response.headers["www-authenticate"] == "Bearer"


def test_request_with_invalid_token_returns_401(anonymous_api):
    response = anonymous_api.get(
        "/api/users", headers={"Authorization": "Bearer not-a-real-token"}
    )

    assert response.status == 401


def test_login_with_wrong_password_returns_401(anonymous_api):
    response = anonymous_api.post(
        "/api/auth/login", data={"username": "trainee99", "password": "wrong-password"}
    )

    assert response.status == 401
    assert response.json()["error"] == "Invalid username or password"
