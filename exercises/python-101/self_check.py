from user_validator import is_valid_age, is_valid_email, validate_user

# Each assert is a tiny test: if the condition is False, Python stops with AssertionError
assert is_valid_email("aisha.rahman@example.com") is True
assert is_valid_email("ben.tan@example") is False
assert is_valid_age(29) is True
assert is_valid_age(-3) is False
assert validate_user({"id": 9, "name": "Test", "email": "test@example.com", "age": 30}) == []

print("All self-checks passed")
