# Demo 04 — Parallel Agents

## Prompt

> Open **one** Claude Code session in this folder and paste this:
>
> ```
> Implement all three utility functions in parallel. Spawn a subagent for each task
> and run them simultaneously — do not do them one at a time:
>
> - tasks/agent-1.md → format_currency in src/utils/format.py
> - tasks/agent-2.md → validate_email in src/utils/validate.py
> - tasks/agent-3.md → slugify in src/utils/text.py
>
> Each subagent must write a failing test first, then implement the function.
> Once all three finish, run pytest and confirm everything passes.
> ```

---

## Steps

1. `cd` into `04-parallel/`
2. Open **one** Claude Code session: `claude`
3. Paste the prompt above and hit enter
4. Watch Claude spawn three subagents and dispatch them simultaneously
5. Once they finish, Claude runs `pytest tests/ -x --tb=short` to confirm all pass

---

## What this teaches

You don't need to open multiple terminals. A single prompt to a single agent can fan
out to multiple subagents running in parallel — Claude handles the orchestration.

The key requirement for safe parallelism: **the tasks must not touch the same files**.
Each subagent here works in its own module with no imports between them, so there's
no risk of conflicting writes.

This is the orchestrator → subagent pattern:
- You give one instruction to one agent
- The orchestrator identifies which work is parallelizable
- It dispatches subagents and collects results
- You get the combined output without managing multiple sessions

Compare the wall-clock time to running them sequentially — that's the unlock.

---

## Files

```
AGENTS.md             — project conventions and done definition
tasks/agent-1.md      — format_currency spec
tasks/agent-2.md      — validate_email spec
tasks/agent-3.md      — slugify spec
src/utils/format.py
src/utils/validate.py
src/utils/text.py
```
