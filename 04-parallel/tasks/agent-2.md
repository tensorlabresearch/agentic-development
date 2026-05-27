# Task: validate_email

Add a function `validate_email(email: str) -> bool`
to `src/utils/validate.py`.

Behavior:
- validate_email("user@example.com") returns True
- validate_email("user@sub.example.co.uk") returns True
- validate_email("notanemail") returns False
- validate_email("missing@tld") returns False
- validate_email("") returns False

No external libraries. Use only the standard library.
Write the test in tests/test_validate.py first.
