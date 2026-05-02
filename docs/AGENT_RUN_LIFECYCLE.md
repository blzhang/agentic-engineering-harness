# Agent Run Lifecycle

An engineering harness needs more than ready Issues and good PR templates. Each agent session also needs a recoverable lifecycle so a tool, runtime, or context interruption does not leave unowned code behind.

## When A Run Starts

A material agent run starts when the agent:

- edits repository files;
- creates or switches branches for a task;
- opens or updates a pull request;
- runs implementation, test, deployment, runtime, data, or cloud operations for a task.

Direct answers and tiny read-only inspections do not need the full lifecycle gate.

## Terminal States

Every material run must end in one explicit state:

- `completed`: scoped work is implemented, verified, self-reviewed, and the required independent review is complete or an independent-review limitation has been explicitly recorded.
- `checkpoint_completed_continue`: a slice of a larger objective is implemented, verified, self-reviewed, and reviewed when independent review is required; the agent should continue to the next unfinished item.
- `checkpoint_review_waiting_continue`: a slice is implemented, verified, and ready for PR-level review or isolated reviewer subagent/session review while the larger objective still has remaining work.
- `status_answered_continue`: the human asked for status and the agent should continue the active objective.
- `review_waiting`: branch or PR is ready for PR-level review or isolated reviewer subagent/session review, with current evidence attached.
- `blocked_needs_human`: product intent, acceptance criteria, scope, safety, or risk decisions need human clarification.
- `blocked_tooling`: tools, credentials, network, service state, repository state, or CI access prevent completion.
- `test_failed`: a required verification command fails and the failure is unresolved.
- `interrupted_incomplete`: the run stopped before closeout, or left unreconciled local changes, partial tests, a partial PR, or no final status.

## Required Closeout Evidence

Before ending a material run, record:

- current branch and linked Issue, PRD, or plan item;
- target base branch, such as `version/vNext` or `main`;
- changed files and ownership boundaries;
- latest verification commands and outcomes;
- current micro-plan step and next action;
- self-review status and PR-level review or isolated reviewer subagent/session status;
- residual risk, skipped checks, blockers, or reason for an incomplete state.

## Dirty Worktree Sentinel

A dirty worktree with no closeout is not a completed run.

The next agent or engineer must first recover the existing work by inspecting:

- `git status`;
- relevant diffs;
- recent test or command evidence;
- linked Issue, PR, PRD, or plan;
- prior session notes when available.

Do not start a competing implementation, overwrite unfinished changes, or revert them unless the human explicitly asks.

## Long-Running Work

For long-running tasks, keep a small progress trail in the conversation, PR, or run log:

- current micro-plan step;
- last successful command;
- next expected action;
- known blocker or risk.

The goal is not ceremony. The goal is that another agent can resume safely after interruption without guessing what happened.
