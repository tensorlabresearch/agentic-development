# Demo 03 — TDD Bug Fix

## Prompt

> Paste this into Claude Code after `cd`-ing into this folder:
>
> ```
> The calculate_price function applies tax and discount in the wrong order.
> Fix it using TDD — write the failing test first, then fix the code.
> ```

---

## Steps

1. `cd` into `03-tdd-fix/`
2. Run `pytest tests/ -x --tb=short` to see the current (passing) state
3. Open Claude Code in this directory
4. Paste the prompt above and hit enter
5. Watch Claude write a **failing test first**, then run it to confirm it fails
6. Watch Claude make the **minimal change** to `src/pricing.py` to fix the order
7. Run `pytest tests/ -x --tb=short` — all tests should pass

---

## What this teaches

Test-driven development as a forcing function: writing the test first makes you define
correct behavior precisely before touching any production code.

The `AGENTS.md` task workflow enforces a strict red-green cycle:
1. Write a failing test that encodes the exact behavior rule
2. Run it — confirm it fails for the **right reason**
3. Make the smallest change that passes the test
4. Run the full suite

**The bug:** `src/pricing.py` applies tax first, then discount. The spec says discount
applies to the base price, and tax applies to the discounted price. The test must encode
this as an explicit rule — not just check a number.

If Claude writes the fix before the test, the red-green discipline isn't being followed.

---

## Files

```
AGENTS.md             — enforces TDD workflow (red → green → done)
src/pricing.py        — calculate_price with the bug
tests/test_pricing.py — existing test suite
```
