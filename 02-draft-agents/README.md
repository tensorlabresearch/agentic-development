# Demo 02 — Draft AGENTS.md from Docs

## Prompt

> Paste this into Claude Code after `cd`-ing into this folder:
>
> ```
> Read the docs/ folder and write an AGENTS.md for this project.
> ```

---

## Steps

1. `cd` into `02-draft-agents/`
2. Open Claude Code in this directory
3. Paste the prompt above and hit enter
4. Watch Claude read all three docs before writing anything
5. Review the generated `AGENTS.md` — does it include project shape, build commands, conventions, and a done definition?
6. **Bonus:** delete the docs and run the same prompt in a fresh session — compare the quality

---

## What this teaches

An agent is only as good as the context it's given. This demo shows how to bootstrap
an `AGENTS.md` by pointing Claude at existing documentation instead of writing the file from scratch.

A good agent will read all three docs before producing anything:
- `docs/architecture.md` — system overview (Ingester, Transformer, Writer, DLQ)
- `docs/domain-glossary.md` — key terms and invariants
- `docs/testing-style.md` — how tests are structured

The output should be a compact, actionable guide that a new agent (or engineer) could open and act on immediately — not a summary of the docs.

---

## Files

```
docs/architecture.md    — system overview
docs/domain-glossary.md — key terms, invariants, naming conventions
docs/testing-style.md   — test structure and coverage expectations
```
