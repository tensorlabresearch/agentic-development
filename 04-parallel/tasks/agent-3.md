# Task: slugify

Add a function `slugify(text: str) -> str`
to `src/utils/text.py`.

Behavior:
- slugify("Hello World") returns "hello-world"
- slugify("  Spaces  Around  ") returns "spaces-around"
- slugify("Special! @#$ Characters") returns "special-characters"
- slugify("Already-a-slug") returns "already-a-slug"
- Multiple consecutive spaces or hyphens collapse to a single hyphen.

No external libraries. Use only the standard library.
Write the test in tests/test_text.py first.
