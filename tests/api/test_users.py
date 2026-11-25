from tests.api.helpers import build_user

def test_create_user(api):
    new_user = build_user()

    response = api.post("/api/users", data=new_user)

    assert response.status == 201
    created = response.json()
    assert created["name"] == new_user["name"]
    assert created["email"] == new_user["email"]
    assert created["age"] == new_user["age"]
    assert created["address"]["city"] == "Melaka"
    assert response.headers["location"] == f"/api/users/{created['id']}"

    # Read it back to prove it was really saved
    saved = api.get(f"/api/users/{created['id']}")
    assert saved.status == 200
    assert saved.json() == created

def test_list_users_returns_five_default_users(api):
    response = api.get("/api/users")

    assert response.status == 200
    body = response.json()
    assert body["count"] == 5
    assert len(body["users"]) == 5
    assert body["users"][0]["name"] == "Aisha Rahman"

def test_search_finds_matching_user(api):
    response = api.get("/api/users", params={"search": "wong"})

    assert response.status == 200
    body = response.json()
    assert body["count"] == 1
    assert body["users"][0]["email"] == "esther.wong@example.com"


def test_get_one_user(api):
    response = api.get("/api/users/2")

    assert response.status == 200
    user = response.json()
    assert user["id"] == 2
    assert user["name"] == "Ben Tan"
    assert user["address"]["city"] == "George Town"


def test_get_unknown_user_returns_404(api):
    response = api.get("/api/users/999")

    assert response.status == 404
    assert response.json()["error"] == "User 999 not found"
