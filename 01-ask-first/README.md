# Demo 01 — Ask First

## Prompt

> Paste this into Claude Code after `cd`-ing into this folder:
>
> ```
> The find_orders function is returning results for customers that don't exist.
> Add an edge case test and fix it.
> ```

---

## Steps

1. `cd` into `01-ask-first/`
2. Run `pytest tests/ -x --tb=short` to confirm the baseline passes
3. Open Claude Code in this directory
4. Paste the prompt above and hit enter
5. **Do not answer Claude's questions immediately** — let it ask first
6. Answer the clarifying questions, then let it proceed
7. Run `pytest tests/ -x --tb=short` to confirm all tests still pass

---

## What this teaches

Ambiguous tasks produce bad code. The `AGENTS.md` in this repo contains one rule:

> *Before starting any task, ask any questions needed to avoid wrong assumptions. Do not guess.*

A well-behaved agent will stop and ask 2–3 clarifying questions before writing a single line:
- What does "doesn't exist" mean — a typo, a missing customer, or an empty result set?
- Should it raise an exception or return an empty list?
- Are there existing tests I should follow for style?

If Claude jumps straight to code, the protocol isn't being followed. That's the failure mode this demo illustrates — and why the task protocol section of `AGENTS.md` exists.

---

## Files

```
AGENTS.md            — task protocol with the ask-first rule
src/orders.py        — find_orders, count_by_status, seed
tests/test_orders.py
```
