REQUIRED_FIELDS = ["id", "name", "email", "age"]

users = [
    {"id": 1, "name": "Aisha Rahman", "email": "aisha.rahman@example.com", "age": 29},
    {"id": 2, "name": "Ben Tan", "email": "ben.tan@example", "age": 34},
    {"id": 3, "name": "", "email": "chloe.lim@example.com", "age": 41},
    {"id": 4, "name": "Daniel Lee", "email": "daniel.lee@example.com"},
    {"id": 5, "name": "Esther Wong", "email": "esther wong@example.com", "age": -3},
    {"id": 6, },
]


def find_missing_fields(user):
    """Return a list of required fields that are missing or empty."""
    missing = []
    for field in REQUIRED_FIELDS:
        value = user.get(field)
        if value is None or value == "":
            missing.append(field)
    return missing


for user in users:
    missing = find_missing_fields(user)
    print(f"User {user['id']}: missing fields = {missing}")
