# Demo 04 — Parallel Agents

## Prompt

> Open **three separate Claude Code sessions** in the `04-parallel/` folder.
> Paste one prompt per session, then start all three at the same time:
>
> **Session 1:**
> ```
> Read tasks/agent-1.md and complete the task.
> ```
>
> **Session 2:**
> ```
> Read tasks/agent-2.md and complete the task.
> ```
>
> **Session 3:**
> ```
> Read tasks/agent-3.md and complete the task.
> ```

---

## Steps

1. `cd` into `04-parallel/`
2. Open **three** Claude Code terminal windows in this directory
3. Paste one prompt into each session (don't hit enter yet)
4. Hit enter on all three at roughly the same time
5. Watch them work simultaneously without conflicting
6. Once all three finish, run `pytest tests/ -x --tb=short`
7. All tests from all three agents should pass together

---

## What this teaches

The biggest speed multiplier in agentic development is parallelism. When tasks don't
share state and modules don't import each other, multiple agents can run simultaneously —
compressing wall-clock time dramatically.

Each agent implements one independent utility function with TDD:
- Agent 1 → `format_currency` in `src/utils/format.py`
- Agent 2 → `validate_email` in `src/utils/validate.py`
- Agent 3 → `slugify` in `src/utils/text.py`

Because the three modules have **no imports between them**, there's zero risk of agents
stepping on each other. The combined `pytest` run at the end is the proof.

---

## Files

```
AGENTS.md             — shared workflow (TDD, done definition)
tasks/agent-1.md      — format_currency spec
tasks/agent-2.md      — validate_email spec
tasks/agent-3.md      — slugify spec
src/utils/format.py
src/utils/validate.py
src/utils/text.py
```
