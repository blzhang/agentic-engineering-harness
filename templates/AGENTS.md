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
- capped isolated reviewer budget for intermediate Issue work and final PR-level review on the version PR when available;
- human acceptance before merge, deploy, or use.

Every material agent run must end as `completed`, `checkpoint_completed_continue`, `checkpoint_review_waiting_continue`, `status_answered_continue`, `review_waiting`, `blocked_needs_human`, `blocked_tooling`, `test_failed`, or `interrupted_incomplete`. For material code work, `completed` and `checkpoint_completed_continue` require the applicable review policy to be complete, or require an explicitly recorded review limitation. Intermediate Issue work uses the PRD/version batch review budget: at most three isolated reviewer subagent/session passes total, with P0/P1 findings fixed or rejected with evidence. Final version completion requires PR-level review on the final version PR when available, and that final review loop is not limited by the isolated reviewer budget. A dirty worktree, partial PR, unpushed branch, unfinished tests, or prior session without closeout must be recovered before starting competing work.

For whole-PRD or whole-version objectives, a local implementation pass is only a checkpoint. Continue to the next unfinished ready item unless the human explicitly says to pause, stop, only answer, or not continue. Status questions should be answered briefly and then execution should continue.

When drafting or updating a PRD/version plan, record both the final design and the discussion-to-decision logic: original requirement, discussion path, assumptions, rejected alternatives, selected rationale, and the mapping from rationale to acceptance, verification, and Issues. If that logic is unclear, ask the human to clarify before treating the PRD as ready.

Before a PRD/version plan can be marked ready for human approval, run an independent PRD review pass when the runtime supports a separate reviewer subagent/session. The main session drafts or updates the PRD, opens a short-lived isolated PRD reviewer with the draft, discussion context, acceptance expectations, and relevant guardrails, then uses the review findings to revise the PRD itself. The reviewer returns findings only and does not edit the PRD directly unless the main session explicitly delegates a separate repair task. The main session self-reviews the revised PRD after applying accepted findings. If no independent reviewer is available, record that limitation and perform an explicit local second-pass PRD review before asking the human to approve the plan.

For version-scoped work, keep `main` stable and use `version/vNext` as the integration branch. Agents must not implement directly on `main` or the version branch; create a task branch from the version branch and open a PR back to it.

Project-specific product policy and safety guardrails override generic harness defaults.
