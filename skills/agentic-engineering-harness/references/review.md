# Review Reference

Self-review is preflight only. It cannot satisfy the independent review gate.

After PR creation, trigger automatic independent review. Then verify that review actually started; for GitHub Codex review, use `python3 scripts/check_github_review_gate.py --repo owner/name --pr <number> --wait-seconds 600`. A plain `mentioned` event is not a review signal.

If PR-level review is unavailable, blocked, not configured, mention-only after the checker timeout, or not yet possible because no PR exists for a material checkpoint, open an isolated reviewer subagent/session when the runtime supports it.

Checker status meanings: `review_signal_present` means PR-level review is real; `mentioned_only` means fallback immediately; `no_review_request` means trigger review or fallback; `tooling_error` means tooling is blocked unless local evidence allows fallback.

If no independent reviewer is available, record that limitation as a review-gate blocker or fallback before using a local second-pass review.

Fix P0/P1 findings or reject only with evidence. Human acceptance remains required before merge, deploy, or use.
