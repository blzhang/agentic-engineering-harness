# PRD Execution Loop Reference

Use when the active objective is a whole PRD, version plan, milestone, or large requirement.

Rules:

- A local implementation pass is a checkpoint, not final completion.
- `completed` means the entire assigned objective is implemented, verified, independently reviewed when required, and ready for the human gate.
- Use `checkpoint_completed_continue` after a verified and reviewed slice when more work remains; use `checkpoint_review_waiting_continue` when independent review is still pending.
- Use `status_answered_continue` after answering status questions such as "is it done?" or "what remains?".
- Continue to the next unfinished ready item unless the human explicitly says pause, stop, only answer, or do not continue.
- Stop only for objective completion, human gate, real blocker, unresolved verification failure, explicit pause/stop, or runtime interruption.
- Keep a concise external trail of completed slices, latest verification, next item, and blockers.
