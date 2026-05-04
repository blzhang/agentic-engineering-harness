# Agentic Engineering Harness Protocol

## Purpose

This protocol helps AI coding agents work inside a human-owned engineering process without turning vague intent into unreviewable code.

The protocol separates four concerns:

- planning: what should be built and why;
- execution: the next scoped work unit;
- verification: how correctness is proven;
- acceptance: the human decision to merge, deploy, or use the result.

## Workflow

```text
natural-language requirement
  -> human requirement confirmation
  -> agent drafts PRD or version plan
  -> independent PRD review and agent revision
  -> human approves plan
  -> version integration branch is created or selected
  -> agent generates structured Issues from approved plan
  -> one ready Issue is selected
  -> agent creates isolated worktree and task branch
  -> strict RED/GREEN/REFACTOR implementation
  -> agent preflight self-review
  -> draft PR targeting the version branch
  -> CI and automatic independent review
  -> agent fixes review findings and reruns checks
  -> explicit agent run closeout
  -> human accepts or rejects result
  -> version branch merges to main only after version acceptance
```

## Human Gates

Human approval is required for:

- original requirement or PRD/version plan acceptance;
- standalone Issue readiness when no approved plan exists;
- final result acceptance;
- merge, deploy, production use, irreversible actions, risk increases, or promotion decisions.

Issues generated directly from a reviewed and human-approved PRD/version plan inherit that approval. They do not require another human approval unless they change scope, expose ambiguity, or conflict with the approved plan.

## PRD Authoring

A PRD or version plan must be reviewable as a reasoning artifact, not only as a task list.

When drafting or updating a PRD/version plan, include:

- the original human requirement and product intent;
- the discussion path that shaped the requirement;
- key assumptions, constraints, and non-goals;
- alternatives considered and why they were rejected or deferred;
- the selected design and why it satisfies the requirement better than the alternatives;
- how the design rationale maps to acceptance criteria, guardrails, verification, and generated Issues.

If the discussion-to-decision logic is missing or ambiguous, ask the human to clarify before treating the PRD/version plan as approved or ready for Issue generation.

## PRD Review Gate

A PRD/version plan draft is not ready for human approval until it has passed a PRD-focused review loop.

Required flow:

1. The drafting agent writes or updates the PRD/version plan, including requirements, discussion-to-decision logic, selected design, rejected alternatives, acceptance criteria, verification approach, guardrails, and Issue mapping.
2. The drafting agent opens an isolated PRD reviewer subagent/session when the runtime supports it.
3. The PRD reviewer audits the draft for unclear requirements, missing rationale, unverifiable acceptance criteria, weak regression criteria, unsafe boundaries, inconsistent scope, untracked assumptions, and Issue decomposition gaps.
4. The reviewer returns findings only. It should not directly edit the PRD unless the main agent explicitly delegates a separate repair task.
5. The drafting agent applies accepted findings by revising the PRD, then performs a local self-review of the revised PRD.
6. Only after the revised PRD has no known material PRD-quality findings may the agent ask the human to approve the PRD/version plan.

If an independent PRD reviewer subagent/session is unavailable, record that limitation and perform an explicit local second-pass PRD review before requesting human approval.

## Version Branches

For version-scoped work, `main` is the stable human-accepted line and `version/vNext` is the integration line for the active version.

The version branch can contain code, docs, plans, and completed Issue work, but it is not a direct editing surface for agents. Agents create isolated worktrees and task branches from the version branch, then open PRs back to the version branch.

Default version flow:

```text
main
  -> version/vNext
      -> codex/vNext-plan
      -> codex/vNext-issue-001-topic
      -> codex/vNext-issue-002-topic
  -> final PR: version/vNext -> main
```

See `docs/VERSION_BRANCH_WORKFLOW.md` for the full rule.

## Ready Issue Rule

A ready Issue must be structured, deterministic, and regression-testable. It must include enough detail for another agent or engineer to verify correctness without relying on the implementing agent's interpretation.

Required content:

- problem or requirement;
- target observable behavior;
- input, state, fixture, command, event, or API surface;
- output, state transition, artifact, or visible result;
- rules and constraints;
- acceptance criteria;
- verification commands or deterministic evidence;
- risk class;
- guardrails and forbidden behavior;
- dependencies and blockers;
- micro-plan.

If any of these cannot be made clear, the agent must stop and ask the human to clarify.

## Serial Execution

The default execution model is serial:

```text
one ready Issue -> one worktree -> one task branch -> one draft PR -> review -> human acceptance
```

Parallel coding is not the default. Use it only when the human explicitly asks for it and the work units are genuinely independent.

## Large PRD Execution

When the active objective is a whole PRD, version plan, milestone, or large requirement, a local implementation pass is only a checkpoint. It is not terminal completion unless the whole assigned objective is implemented, verified, independently reviewed when required, and ready for the required human gate.

Use checkpoint states inside a large objective:

- `checkpoint_completed_continue`: one slice is implemented, verified, self-reviewed, and reviewed when independent review is required; choose the next unfinished ready item.
- `checkpoint_review_waiting_continue`: one slice is implemented, verified, and ready for PR-level review or isolated reviewer subagent/session review while more objective work remains.
- `status_answered_continue`: the human asked for status; answer briefly and continue unless they explicitly said to pause, stop, only answer, or not continue.

During a large objective, the agent may stop only for full objective completion, a required human gate, a real blocker, unresolved test failure, explicit human pause/stop, or runtime interruption. Questions like "is it done?" or "what remains?" are status requests, not stop commands.

See `docs/PRD_EXECUTION_LOOP.md` for the full rule.

## Agent Run Lifecycle

A material agent run starts when the agent edits files, creates or switches branches, opens or updates a PR, runs implementation tests, or performs runtime, deployment, cloud, or data operations for a task.

Every material run must end in one explicit state:

- `completed`;
- `checkpoint_completed_continue`;
- `checkpoint_review_waiting_continue`;
- `status_answered_continue`;
- `review_waiting`;
- `blocked_needs_human`;
- `blocked_tooling`;
- `test_failed`;
- `interrupted_incomplete`.

For material code work, `completed` and `checkpoint_completed_continue` require independent review to be complete, or require an explicitly recorded independent-review limitation. If review is pending, use `review_waiting` or `checkpoint_review_waiting_continue`.

Before ending, the agent must record the current branch, target base branch, linked Issue or plan, changed files, latest verification commands and outcomes, current micro-plan step, next action, review status, and residual risk.

A dirty worktree, partial PR, unpushed branch, unfinished test run, or prior session with no closeout must be treated as `interrupted_incomplete`. The next agent must recover by reading status, diffs, evidence, and the linked Issue or plan before continuing. It must not restart, overwrite, or revert unfinished work unless the human explicitly asks.

See `docs/AGENT_RUN_LIFECYCLE.md` for the full lifecycle rule.

## Test-First Rule

Features, bug fixes, refactors, and material behavior changes follow:

```text
RED: write or adjust a failing test, fixture, replay, or deterministic check
GREEN: implement the smallest change that makes it pass
REFACTOR: clean up while checks stay green
```

If a true red phase is impossible, the Issue or PR must state why and provide the strongest deterministic substitute.

## Review Rule

Agent self-review is preflight only. It catches low-level gaps before PR publication and cannot satisfy the independent review gate.

Independent review should start automatically after PR creation. The implementing agent must verify that PR-level review actually started; a plain mention event is not sufficient evidence. For GitHub Codex review, use `python3 scripts/check_github_review_gate.py --repo owner/name --pr <number> --wait-seconds 600`.

If PR-level review is unavailable, blocked, not configured, mention-only after the checker timeout, `integration_not_configured`, or not yet possible because no PR exists for a material checkpoint, the implementing agent opens an isolated reviewer subagent/session when the runtime supports it.

If neither PR-level review nor an isolated reviewer subagent/session is available, the agent records that limitation as a review-gate blocker or fallback before using a local second-pass review. The implementing agent fixes accepted findings and reruns checks.

Human acceptance remains separate from review approval.
