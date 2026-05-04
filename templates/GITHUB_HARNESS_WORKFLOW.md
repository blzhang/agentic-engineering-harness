# GitHub Harness Workflow

## Flow

```text
human requirement
  -> PRD or version plan
  -> PRD records discussion-to-decision logic
  -> independent PRD review and revision
  -> human plan approval
  -> version integration branch
  -> structured Issues
  -> one ready Issue
  -> isolated worktree and task branch
  -> RED/GREEN/REFACTOR implementation
  -> draft PR into version branch
  -> CI and automatic review or isolated reviewer fallback
  -> explicit agent run closeout
  -> human acceptance
```

## Ready Issues

Issues must be structured, deterministic, and regression-testable. They must include input, output, rules, constraints, acceptance, verification, guardrails, and micro-plan.

If any part is unclear, ask the human before marking ready.

## PRD Rationale

PRDs and version plans must preserve how the team reached the final design. Include the original requirement, discussion path, assumptions, rejected alternatives, selected rationale, and how that rationale maps to acceptance, verification, guardrails, and generated Issues.

If this logic is missing, the PRD is not ready for Issue generation.

## PRD Review Gate

Before a PRD/version plan is ready for human approval, run a PRD-focused independent review pass when the runtime supports a separate reviewer subagent/session. The drafting agent gives the reviewer the PRD draft, discussion context, acceptance expectations, and guardrails. The reviewer returns findings only. The drafting agent revises the PRD from accepted findings, self-reviews the revised PRD, and only then asks the human for approval.

If an independent PRD reviewer is unavailable, record the limitation and perform an explicit local second-pass PRD review before requesting human approval.

## Execution

For version-scoped work, keep `main` stable and use `version/vNext` as the integration branch.

Default to serial execution: one Issue, one worktree, one task branch, one PR.

Agents do not implement directly on `main` or `version/vNext`. Create `codex/vNext-issue-<number>-<topic>` from the version branch and open the PR back to the version branch. The version branch merges to `main` only after version-level human acceptance.

For whole-PRD or whole-version objectives, each local pass is a checkpoint. Continue to the next unfinished ready item until the objective is complete, a human gate is reached, a real blocker appears, or the human explicitly pauses. Status questions do not stop execution by themselves.

## Agent Run Lifecycle

Every material agent run must end in one explicit state:

- `completed`;
- `checkpoint_completed_continue`;
- `checkpoint_review_waiting_continue`;
- `status_answered_continue`;
- `review_waiting`;
- `blocked_needs_human`;
- `blocked_tooling`;
- `test_failed`;
- `interrupted_incomplete`.

Before ending, record the branch, target base branch, linked Issue or plan, changed files, latest verification commands and outcomes, current micro-plan step, next action, review status, and residual risk.

For material code work, `completed` and `checkpoint_completed_continue` require independent review to be complete, or require an explicitly recorded independent-review limitation. If review is pending, use `review_waiting` or `checkpoint_review_waiting_continue`.

A dirty worktree, partial PR, unpushed branch, unfinished tests, or prior agent session without closeout is `interrupted_incomplete`. Recover it before starting competing work.

## Review

Self-review is preflight. Independent review should run automatically after PR creation.

After requesting PR-level review, verify that it actually started. For GitHub Codex review, use `python3 scripts/check_github_review_gate.py --repo owner/name --pr <number> --wait-seconds 600`. A plain `mentioned` event is not a review signal.

If PR-level review is unavailable, blocked, not configured, mention-only after the checker timeout, `integration_not_configured`, or not yet possible because no PR exists for a material checkpoint, open an isolated reviewer subagent/session when the runtime supports it. Local self-review alone cannot satisfy the independent review gate.

If no independent reviewer is available, record that limitation as a review-gate blocker or fallback before using a local second-pass review.

Human acceptance is required before merge, deploy, or use.
