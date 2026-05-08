# Review Reference

Self-review is preflight only. It cannot satisfy the isolated reviewer budget or the final PR-level review gate.

Intermediate Issue PRs do not trigger PR-level review by default. Inside one PRD/version batch, use at most three isolated reviewer subagent/session passes total for implementation work: one initial review plus up to two re-review passes after fixes. PRD/version-plan review passes do not count against this implementation budget.

Fix P0/P1 findings or reject only with evidence. P2/P3 findings may be fixed or recorded as residual risk/backlog. If the three-pass budget is exhausted while unresolved P0/P1 findings remain, stop as `blocked_needs_human` or record an explicit risk decision.

On the final version PR, trigger PR-level review when available. Then verify that review actually started; for GitHub Codex review, use `python3 scripts/check_github_review_gate.py --repo owner/name --pr <number> --wait-seconds 600`. A plain `mentioned` event is not a review signal. Final review/fix/re-review cycles are not limited by the isolated reviewer budget.

If final PR-level review is unavailable, blocked, not configured, mention-only after the checker timeout, or tooling cannot verify the final review signal, open an isolated reviewer subagent/session when the runtime supports it and record the limitation.

Checker status meanings: `review_signal_present` means PR-level review is real; `mentioned_only` means fallback immediately; `integration_not_configured` means Codex has no private-repository access or Code review is not enabled; `no_review_request` means trigger review or fallback; `tooling_error` means tooling is blocked unless local evidence allows fallback.

If no independent reviewer is available where the applicable policy requires one, record that limitation as a review-gate blocker or fallback before using a local second-pass review.

Human acceptance remains required before merge, deploy, or use.
