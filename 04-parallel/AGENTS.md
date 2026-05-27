# AGENTS.md

## Project shape
Shared utility library for a web platform. Python 3.12.
Each utility module is independent — no imports between them.

## Build and test
pytest tests/ -x --tb=short

## Task workflow
1. Read your task file completely before writing any code.
2. Write a failing test first.
3. Implement the function.
4. Run pytest and confirm all tests pass.

## Done definition
All tests pass. Your function is in the correct module. Diff touches ≤ 2 files.
