# Task: format_currency

Add a function `format_currency(amount: float, currency: str = "USD") -> str`
to `src/utils/format.py`.

Behavior:
- format_currency(1234.5) returns "$1,234.50"
- format_currency(9.9) returns "$9.90"
- format_currency(1000.0, "EUR") returns "€1,000.00"
- Supported currencies: USD ($), EUR (€), GBP (£). Raise ValueError for others.

Write the test in tests/test_format.py first.
