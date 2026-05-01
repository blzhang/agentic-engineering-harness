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

After PR creation, trigger an independent review automatically when available. This may be a GitHub Code Review tool, a configured AI reviewer, or an isolated reviewer session.

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

