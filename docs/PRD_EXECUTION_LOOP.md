# PRD Execution Loop

This rule applies when a human assigns a whole PRD, version plan, milestone, or large requirement as the active objective.

## Objective Versus Checkpoint

Do not treat a coherent local implementation pass as completion of the whole objective.

- Objective completion means the assigned PRD/version scope is implemented, verified, independently reviewed when required, and ready for the required human gate.
- Checkpoint completion means one Issue, slice, or local pass has reached `checkpoint_completed_continue`; material code checkpoints require independent review to be complete or an independent-review limitation to be recorded.

`completed` is a terminal state only for the active objective. If the whole PRD/version is still incomplete, use a checkpoint state and continue.

## Non-Terminal Checkpoint States

Use these states inside a large objective:

- `checkpoint_completed_continue`: a coherent slice is implemented, verified, self-reviewed, and reviewed when independent review is required; select the next unfinished ready item.
- `checkpoint_review_waiting_continue`: a slice is implemented, verified, and ready for PR-level review or isolated reviewer subagent/session review while the remaining objective still has work; continue only when serial review policy allows it.
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

For material code checkpoints, self-review is preflight only. Use PR-level review when a PR exists and review is available. If PR-level review is unavailable or no PR exists yet for that checkpoint, open an isolated reviewer subagent/session when the runtime supports it.

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
