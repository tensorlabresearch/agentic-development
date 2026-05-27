# Agentic Development — Workshop Demos

Hands-on demos for the Tensor Lab Agentic Development workshop.
Each folder is a self-contained exercise. Open the `README.md` inside each one for the prompt and steps.

---

## Demos

| # | Folder | Concept |
|---|--------|---------|
| 01 | [`01-ask-first/`](01-ask-first/) | Agents should ask clarifying questions before assuming |
| 02 | [`02-draft-agents/`](02-draft-agents/) | Bootstrap an AGENTS.md from existing documentation |
| 03 | [`03-tdd-fix/`](03-tdd-fix/) | Write the failing test first, then fix the code |
| 04 | [`04-parallel/`](04-parallel/) | Run independent tasks across multiple agents simultaneously |
| 05 | [`05-context/`](05-context/) | AGENTS.md keeps agents focused and scoped |

---

## Setup

```bash
git clone https://github.com/tensorlabresearch/agentic-development.git
cd agentic-development
pip install pytest
```

Each demo runs with `pytest tests/ -x --tb=short` from inside its folder.
No other dependencies required.

---

## How to use

1. Pick a demo folder
2. Read its `README.md` — the prompt is at the top
3. `cd` into the folder
4. Open Claude Code (`claude` in your terminal)
5. Paste the prompt and watch what happens
