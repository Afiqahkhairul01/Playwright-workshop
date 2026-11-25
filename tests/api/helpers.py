def build_user(**overrides):
    """Return a valid user body. Pass keyword arguments to change any field."""
    user = {
        "name": "Farah Ali",
        "email": "farah.ali@example.com",
        "age": 30,
        "address": {"street": "1 Jalan Satu", "city": "Melaka", "postcode": "75000"},
    }
    user.update(overrides)
    return user
