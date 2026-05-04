# Version Branch Reference

Use this when the project wants `main` to stay stable until a full version is accepted.

Branch roles:

- `main`: human-accepted stable line.
- `version/vNext`: active version integration branch.
- `codex/vNext-plan`: optional planning branch.
- `codex/vNext-issue-<number>-<topic>`: task branch for one ready Issue.
- `hotfix/main-<topic>`: urgent stable fix branch.

Rules:

- Create or select `version/vNext` before executing version-scoped Issues.
- Draft or update the PRD/version plan in a planning branch or isolated worktree.
- Run the PRD review gate before human plan approval: independent PRD reviewer when available, agent revision, and self-review.
- Create task branches from `version/vNext`, ideally in isolated worktrees.
- Open Issue PRs back to `version/vNext`.
- Do not implement directly on `main` or `version/vNext`.
- Run CI on PRs into `version/vNext` and on pushes to `version/vNext`.
- Merge `version/vNext` to `main` only through a final version PR after human acceptance.
- Backport relevant `main` hotfixes into the active version branch with evidence.
