# Demo 05 — AGENTS.md Context

## Prompt

> Paste this into Claude Code after `cd`-ing into this folder:
>
> ```
> The Slack and webhook notification channels are broken. Fix them so all tests pass.
> ```

---

## Steps

1. `cd` into `05-context/`
2. Run `pytest tests/ -x --tb=short` — see Slack and webhook tests fail
3. Open Claude Code in this directory
4. Paste the prompt above and hit enter
5. Watch Claude read `src/notify.py` and `tests/test_notify.py` before making changes
6. The fix should touch **at most 2 files** (enforced by the done definition in `AGENTS.md`)
7. Run `pytest tests/ -x --tb=short` — all three channel tests should pass

**Bonus:** Rename `AGENTS.md` to `AGENTS.md.bak`, run the same prompt in a fresh session,
and compare how the agent behaves without the context.

---

## What this teaches

`AGENTS.md` doesn't just describe a project — it shapes agent behavior. This demo shows
how a tight done definition prevents agents from over-engineering a contained bug fix.

The key constraint in `AGENTS.md`:
> *Diff touches ≤ 2 files.*

Without this, agents tend to refactor surrounding code, rename things, or add abstractions
while fixing a two-line bug. The constraint is a forcing function: it keeps the diff minimal
and the scope honest.

---

## Files

```
AGENTS.md            — project context + ≤ 2 files constraint
src/notify.py        — email (working), Slack (broken), webhook (broken)
tests/test_notify.py
```
