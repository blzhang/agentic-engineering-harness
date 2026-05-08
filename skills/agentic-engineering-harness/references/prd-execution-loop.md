# PRD Execution Loop Reference

Use when the active objective is a whole PRD, version plan, milestone, or large requirement.

Rules:

- A local implementation pass is a checkpoint, not final completion.
- `completed` means the entire assigned objective is implemented, verified, reviewed under the applicable final review gate, and ready for the human gate.
- Use `checkpoint_completed_continue` after a verified slice covered by the current batch review policy when more work remains; use `checkpoint_review_waiting_continue` when an isolated reviewer pass is pending and the batch still has review budget.
- Use `status_answered_continue` after answering status questions such as "is it done?" or "what remains?".
- Continue to the next unfinished ready item unless the human explicitly says pause, stop, only answer, or do not continue.
- Stop only for objective completion, human gate, real blocker, unresolved verification failure, explicit pause/stop, or runtime interruption.
- Keep a concise external trail of completed slices, latest verification, next item, and blockers.
- Intermediate Issue work uses at most three isolated reviewer subagent/session passes per PRD/version batch; fix or evidentially reject P0/P1 findings after each pass.
- Final version PR-level review is not limited by the isolated reviewer budget.
- PRD/version plan drafts are not ready for human approval until an independent PRD reviewer subagent/session audits the draft when available.
- The PRD reviewer returns findings only; the main agent revises the PRD from accepted findings and self-reviews the revised plan.
- If no independent PRD reviewer is available, record the limitation and perform a local second-pass PRD review before requesting human approval.
