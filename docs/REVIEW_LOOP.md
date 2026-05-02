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

## Automatic Review

After PR creation, trigger independent review automatically. Prefer GitHub Code Review when it is available for the project. A configured AI reviewer may be used when the project defines it as the PR-level review tool.

Triggering a review request is not enough. The implementing agent must verify that the request produced a real review signal by using the project checker, such as `python3 scripts/check_github_review_gate.py --repo owner/name --pr <number> --wait-seconds 600`. A plain `mentioned` event is not a review signal.

If PR-level review is unavailable, blocked, not configured, mention-only after the checker timeout, or not yet possible because no PR exists for a material checkpoint, open an isolated reviewer subagent/session when the runtime supports it. The reviewer returns findings only; the implementing agent owns fixes, rerun checks, and final judgment.

The GitHub review checker emits:

- `review_signal_present`: PR-level review produced a Codex review or Codex bot comment after the latest review request.
- `mentioned_only`: a review request was mentioned, but no review signal exists. Treat this as PR-level review unavailable and use reviewer fallback.
- `no_review_request`: no review request was found. Trigger review or use fallback if PR-level review is not possible.
- `tooling_error`: GitHub tooling or API access failed. Treat as tooling blocked unless fallback can proceed from local evidence.

If no independent reviewer is available, record that limitation as a review-gate blocker or fallback before using a local second-pass review.

Review should check:

- requirements compliance;
- safety and permission boundaries;
- test quality;
- deterministic evidence;
- data/schema compatibility;
- code quality;
- missing docs or migration notes.

P0/P1 findings are blocking until fixed or rejected with specific evidence.

## Human Acceptance

Review approval is not human acceptance. Human acceptance decides whether the result satisfies the original need and can be merged, deployed, or used.
