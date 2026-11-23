import re

EMAIL_PATTERN = r"[^@\s]+@[^@\s]+\.[^@\s]+"


def is_valid_email(email):
    """Return True if the email looks like name@domain.tld (simplified check)."""
    if not isinstance(email, str):
        return False
    return re.fullmatch(EMAIL_PATTERN, email) is not None


test_emails = [
    "aisha.rahman@example.com",
    "ben.tan@example",
    "esther wong@example.com",
    "no-at-sign.example.com",
    None,
]

for email in test_emails:
    print(email, "->", is_valid_email(email))
