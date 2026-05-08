# Run Lifecycle Reference

A material run starts when the agent edits files, creates or switches branches, opens or updates a PR, runs implementation tests, or performs runtime, deployment, cloud, or data operations.

Allowed terminal states:

- `completed`
- `checkpoint_completed_continue`
- `checkpoint_review_waiting_continue`
- `status_answered_continue`
- `review_waiting`
- `blocked_needs_human`
- `blocked_tooling`
- `test_failed`
- `interrupted_incomplete`

For material code work, `completed` and `checkpoint_completed_continue` require the applicable review policy to be complete, or require an explicitly recorded review limitation. Intermediate Issue work uses the PRD/version batch review budget. Final version completion requires PR-level review on the final version PR when available. If review is pending, use `review_waiting` or `checkpoint_review_waiting_continue`.

Before ending, record branch, target base branch, linked Issue or plan, changed files, latest verification, current micro-plan step, next action, isolated reviewer budget status, final PR-level review status when applicable, and residual risk.

If the prior run left a dirty worktree, partial PR, unpushed branch, unfinished tests, or no final status, treat it as `interrupted_incomplete`. Recover by reading status, diffs, evidence, and the linked Issue or plan. Do not restart, overwrite, or revert unfinished work unless the human asks.
