"""
User record validator - Python hands-on lab.

Checks a list of user records against simple rules and prints
a PASS/FAIL result for each record, followed by a summary.
"""

import re
import sys

# ---------------------------------------------------------------
# Configuration: the rules our "test" checks against
# ---------------------------------------------------------------
REQUIRED_FIELDS = ["id", "name", "email", "age"]
EMAIL_PATTERN = r"[^@\s]+@[^@\s]+\.[^@\s]+"
MIN_AGE = 18
MAX_AGE = 120

# ---------------------------------------------------------------
# Test data: some records are valid, some are deliberately broken
# ---------------------------------------------------------------
users = [
    {"id": 1, "name": "Aisha Rahman", "email": "aisha.rahman@example.com", "age": 29},
    {"id": 2, "name": "Ben Tan", "email": "ben.tan@example", "age": 34},
    {"id": 3, "name": "", "email": "chloe.lim@example.com", "age": 41},
    {"id": 4, "name": "Daniel Lee", "email": "daniel.lee@example.com"},
    {"id": 5, "name": "Esther Wong", "email": "esther wong@example.com", "age": -3},
]


# ---------------------------------------------------------------
# Check functions: each one checks a single rule
# ---------------------------------------------------------------
def find_missing_fields(user):
    """Return a list of required fields that are missing or empty."""
    missing = []
    for field in REQUIRED_FIELDS:
        value = user.get(field)
        if value is None or value == "":
            missing.append(field)
    return missing


def is_valid_email(email):
    """Return True if the email looks like name@domain.tld (simplified check)."""
    if not isinstance(email, str):
        return False
    return re.fullmatch(EMAIL_PATTERN, email) is not None


def is_valid_age(age):
    """Return True if age is a whole number between MIN_AGE and MAX_AGE."""
    if not isinstance(age, int):
        return False
    return MIN_AGE <= age <= MAX_AGE


def validate_user(user):
    """Run every check on one user and return a list of error messages."""
    errors = []

    missing = find_missing_fields(user)
    for field in missing:
        errors.append(f"missing field '{field}'")

    if "email" not in missing and not is_valid_email(user["email"]):
        errors.append(f"invalid email '{user['email']}'")

    if "age" not in missing and not is_valid_age(user["age"]):
        errors.append(f"invalid age {user['age']} (must be {MIN_AGE}-{MAX_AGE})")

    return errors


# ---------------------------------------------------------------
# Main program: run the checks and report results
# ---------------------------------------------------------------
def main():
    passed = 0
    failed = 0

    print("=" * 50)
    print("USER RECORD VALIDATION")
    print("=" * 50)

    for user in users:
        errors = validate_user(user)
        if errors:
            failed += 1
            print(f"[FAIL] User {user.get('id')}")
            for error in errors:
                print(f"       - {error}")
        else:
            passed += 1
            print(f"[PASS] User {user.get('id')}")

    total = passed + failed
    pass_rate = (passed / total) * 100 if total > 0 else 0

    print("=" * 50)
    print(f"Total: {total} | Passed: {passed} | Failed: {failed} | Pass rate: {pass_rate:.0f}%")
    print("=" * 50)

    # Exit code 1 tells other tools (like a CI pipeline) that something failed
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
