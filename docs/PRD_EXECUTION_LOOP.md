# PRD Execution Loop

This rule applies when a human assigns a whole PRD, version plan, milestone, or large requirement as the active objective.

## Objective Versus Checkpoint

Do not treat a coherent local implementation pass as completion of the whole objective.

- Objective completion means the assigned PRD/version scope is implemented, verified, reviewed under the applicable final review gate, and ready for the required human gate.
- Checkpoint completion means one Issue, slice, or local pass has reached `checkpoint_completed_continue`; material code checkpoints must satisfy the current PRD/version batch review budget or record a review limitation.

`completed` is a terminal state only for the active objective. If the whole PRD/version is still incomplete, use a checkpoint state and continue.

## Non-Terminal Checkpoint States

Use these states inside a large objective:

- `checkpoint_completed_continue`: a coherent slice is implemented, verified, self-reviewed, and covered by the current PRD/version batch review policy; select the next unfinished ready item.
- `checkpoint_review_waiting_continue`: a slice is implemented, verified, and ready for the next isolated reviewer subagent/session pass while the remaining objective still has work and the batch still has review budget.
- `status_answered_continue`: the human asked for status; answer briefly and continue the active objective.

## Allowed Stops

During a large PRD/version objective, the agent may stop only when:

- the entire assigned objective is `completed`;
- a required human decision or acceptance gate is reached;
- tooling, credentials, repository state, or services block progress;
- a verification failure cannot be fixed in the current run;
- the human explicitly says to pause, stop, only answer, or not continue;
- the runtime interrupts unexpectedly, in which case the state is `interrupted_incomplete`.

Questions such as "is it done?", "what is the status?", or "what remains?" are not pause commands by themselves. Answer them, update the run state, and continue unless the human explicitly asks to pause or only answer.

## Checkpoint Review

For material code checkpoints, self-review is preflight only. Intermediate Issue/task checkpoints do not trigger PR-level review by default. Instead, use the PRD/version batch's isolated reviewer budget when the runtime supports it.

One PRD/version batch may use at most three isolated reviewer subagent/session passes total for implementation work: one initial review plus up to two re-review passes after fixes. PRD/version-plan review passes do not count against this implementation budget. P0/P1 findings must be fixed or explicitly rejected with evidence before continuing; P2/P3 findings may be fixed or recorded as residual risk/backlog.

If the three-pass isolated reviewer budget is exhausted while unresolved P0/P1 findings remain, stop as `blocked_needs_human` or record an explicit risk decision. Do not continue the objective as clean.

The final version PR must run PR-level review when available. Final review/fix/re-review cycles do not count against the isolated reviewer budget and continue until no blocking P0/P1 findings remain, or until a finding is explicitly rejected with evidence.

If no independent reviewer is available, record that limitation as a review-gate blocker or fallback before using a local second-pass review. Do not mark a material checkpoint as fully reviewed with local self-review alone.

## Next-Item Selection

After each checkpoint:

1. Re-read the active PRD/version plan or Issue list.
2. Mark completed slices and known blockers.
3. Choose the next unfinished ready item by dependency and risk order.
4. State the next target, expected files, and verification command.
5. Continue implementation.

If the next item is not deterministic or violates the approved plan, stop as `blocked_needs_human`.

## Context Protection

Large objectives should keep a concise external trail:

- current objective;
- completed slices;
- active branch and target base branch;
- latest verification commands and outcomes;
- next unfinished item;
- blockers and residual risk.

Use a PR description, Issue comment, or run ledger when available. This lets a future session recover without rereading the whole conversation.

## PRD Logic Preservation

Before implementing or generating Issues from a PRD/version plan, verify that the plan records both:

- the final requirements and design;
- the discussion-to-decision logic explaining why those requirements and design choices were selected.

If a PRD only states what to build but omits why the team chose that design, what alternatives were rejected, or how the rationale maps to acceptance and verification, treat the PRD as not yet review-ready and ask the human to clarify.

## PRD Review Gate

A PRD/version plan draft is not ready for human approval until it has passed a PRD-focused review loop.

Required flow:

1. The main agent drafts or updates the PRD/version plan, including requirements, discussion-to-decision logic, accepted design, rejected alternatives, acceptance criteria, verification approach, and Issue mapping.
2. The main agent opens an isolated PRD reviewer subagent/session when the runtime supports it.
3. The PRD reviewer audits the draft for unclear requirements, missing rationale, unverifiable acceptance criteria, weak regression criteria, unsafe boundaries, inconsistent scope, untracked assumptions, and Issue decomposition gaps.
4. The reviewer returns findings only. It should not directly edit the PRD unless the main agent explicitly delegates a separate repair task.
5. The main agent applies accepted findings by revising the PRD, then performs a local self-review of the revised PRD.
6. Only after the revised PRD has no known material PRD-quality findings may the agent ask the human to approve the PRD/version plan.

If an independent PRD reviewer subagent/session is unavailable or forbidden by higher-priority runtime policy, the agent must disclose that limitation in the PRD evidence and perform an explicit local second-pass PRD review before requesting human approval.
