# Step 1: Store the test data
users = [
    {"id": 1, "name": "Aisha Rahman", "email": "aisha.rahman@example.com", "age": 29},
    {"id": 2, "name": "Ben Tan", "email": "ben.tan@example", "age": 34},
    {"id": 3, "name": "", "email": "chloe.lim@example.com", "age": 41},
    {"id": 4, "name": "Daniel Lee", "email": "daniel.lee@example.com"},
    {"id": 5, "name": "Esther Wong", "email": "esther wong@example.com", "age": -3},
    {"id": 6, "name": "Fiona Ng", "email": "fiona.ng@example.com", "age": 28},
    {"id": 7, "name": "Fiona Ng", "email": "fiona.ng@example.com", "age": 28},
]

print(f"Loaded {len(users)} user records")

for user in users:
    print(user["id"], user["name"])
