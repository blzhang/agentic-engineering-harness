# Review Loop

## Preflight

Before opening a PR, the implementing agent checks:

- Issue acceptance criteria;
- guardrails;
- changed files and scope;
- tests and deterministic evidence;
- residual risk;
- documentation updates.

Preflight self-review is not independent review.

## Batch Review Budget

Intermediate Issue PRs do not trigger PR-level review by default. They use a capped isolated reviewer budget for implementation work inside one PRD/version batch.

One PRD/version batch may use at most three isolated reviewer subagent/session passes total:

- one initial implementation review;
- up to two re-review passes after fixes;
- PRD/version-plan review passes do not count against this implementation budget;
- final PR-level review passes do not count against this implementation budget.

The reviewer returns findings only; the implementing agent owns fixes, rerun checks, and final judgment. P0/P1 findings are blocking until fixed or rejected with specific evidence. P2/P3 findings may be fixed immediately or recorded as residual risk/backlog.

If the three-pass isolated reviewer budget is exhausted while unresolved P0/P1 findings remain, stop as `blocked_needs_human` or record an explicit risk decision. Do not continue the batch as clean.

If no isolated reviewer is available for an intermediate checkpoint, record that limitation as a review-gate blocker or fallback before using a local second-pass review.

## Final PR-Level Review

The final version PR, such as `version/vNext -> main`, is the default PR-level review gate. Prefer GitHub Code Review when it is available for the project. A configured AI reviewer may be used when the project defines it as the PR-level review tool.

Triggering a review request is not enough. The implementing agent must verify that the request produced a real review signal by using the project checker, such as `python3 scripts/check_github_review_gate.py --repo owner/name --pr <number> --wait-seconds 600`. A plain `mentioned` event is not a review signal.

If final PR-level review is unavailable, blocked, not configured, mention-only after the checker timeout, `integration_not_configured`, or tooling cannot verify the final review signal, open an isolated reviewer subagent/session when the runtime supports it. The limitation must be recorded in the final evidence.

The GitHub review checker emits:

- `review_signal_present`: PR-level review produced a Codex review or Codex bot comment after the latest review request.
- `mentioned_only`: a review request was mentioned, but no review signal exists. Treat this as PR-level review unavailable and use reviewer fallback.
- `integration_not_configured`: the PR is in a private repository and GitHub reports `codex` has no repository access. Treat this as PR-level review unavailable until Codex cloud is set up for the repository and Code review is enabled in Codex settings.
- `no_review_request`: no review request was found. Trigger review or use fallback if PR-level review is not possible.
- `tooling_error`: GitHub tooling or API access failed. Treat as tooling blocked unless fallback can proceed from local evidence.

If no independent reviewer is available for the final PR, record that limitation as a review-gate blocker or fallback before using a local second-pass review.

Review should check:

- requirements compliance;
- safety and permission boundaries;
- test quality;
- deterministic evidence;
- data/schema compatibility;
- code quality;
- missing docs or migration notes.

Final PR-level P0/P1 findings are blocking until fixed or rejected with specific evidence. Final review/fix/re-review cycles are not limited by the isolated reviewer budget.

## Human Acceptance

Review approval is not human acceptance. Human acceptance decides whether the result satisfies the original need and can be merged, deployed, or used.
