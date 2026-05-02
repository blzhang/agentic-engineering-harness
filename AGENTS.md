# Agentic Engineering Harness Rules

This repository defines reusable workflow rules for AI-assisted software development.

When changing this repository:

1. Preserve human-gated planning and acceptance.
2. Do not weaken deterministic Issue contracts.
3. Do not weaken RED/GREEN/REFACTOR rules.
4. Do not present agent self-review as a substitute for independent review; use an isolated reviewer subagent/session when PR-level review is unavailable and the runtime supports it.
5. Do not weaken the version branch, isolated worktree, or task branch model.
6. Do not weaken the agent run lifecycle gate or allow silent stops after material edits.
7. Keep templates generic and project-portable.
8. Verify scripts before claiming they work.
