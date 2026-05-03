# Agentic Engineering Harness Rules

This project uses the Agentic Engineering Harness.

Follow `docs/GITHUB_HARNESS_WORKFLOW.md` for:

- PRD/version-plan to Issue flow;
- structured deterministic Issue contracts;
- version integration branches;
- isolated worktree and task branch execution;
- strict RED/GREEN/REFACTOR implementation;
- explicit agent run lifecycle closeout;
- preflight self-review;
- automatic independent review, with isolated reviewer subagent/session fallback when PR-level review is unavailable and the runtime supports it;
- human acceptance before merge, deploy, or use.

Every material agent run must end as `completed`, `checkpoint_completed_continue`, `checkpoint_review_waiting_continue`, `status_answered_continue`, `review_waiting`, `blocked_needs_human`, `blocked_tooling`, `test_failed`, or `interrupted_incomplete`. For material code work, `completed` and `checkpoint_completed_continue` require independent review to be complete, or require an explicitly recorded independent-review limitation. A dirty worktree, partial PR, unpushed branch, unfinished tests, or prior session without closeout must be recovered before starting competing work.

For whole-PRD or whole-version objectives, a local implementation pass is only a checkpoint. Continue to the next unfinished ready item unless the human explicitly says to pause, stop, only answer, or not continue. Status questions should be answered briefly and then execution should continue.

When drafting or updating a PRD/version plan, record both the final design and the discussion-to-decision logic: original requirement, discussion path, assumptions, rejected alternatives, selected rationale, and the mapping from rationale to acceptance, verification, and Issues. If that logic is unclear, ask the human to clarify before treating the PRD as ready.

For version-scoped work, keep `main` stable and use `version/vNext` as the integration branch. Agents must not implement directly on `main` or the version branch; create a task branch from the version branch and open a PR back to it.

Project-specific product policy and safety guardrails override generic harness defaults.
