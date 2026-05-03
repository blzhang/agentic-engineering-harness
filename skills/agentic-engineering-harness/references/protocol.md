# Protocol Reference

Flow:

```text
human requirement
  -> PRD/version plan
  -> documented discussion-to-decision logic
  -> human approval
  -> version integration branch
  -> structured Issues
  -> serial worktree/task branch execution
  -> RED/GREEN/REFACTOR
  -> draft PR into version branch
  -> automatic independent review or isolated reviewer fallback
  -> explicit agent run closeout
  -> human acceptance
```

Approved PRD-generated Issues inherit plan approval. Standalone Issues need human confirmation.

PRDs and version plans must explain how the final design was reached: original requirement, discussion path, assumptions, rejected alternatives, chosen rationale, and mapping to acceptance, verification, guardrails, and Issues. If this logic is unclear, ask the human before treating the plan as ready.

For version-scoped work, keep `main` stable, use `version/vNext` as the integration branch, and create task branches from it. Do not implement directly on `main` or the version branch.

For whole-PRD or whole-version objectives, local passes are checkpoints. Answer status questions and continue unless the human explicitly pauses, stops, or asks for answer-only.

Every material run must end with an explicit lifecycle state. A dirty worktree, partial PR, unpushed branch, unfinished tests, or missing final status is `interrupted_incomplete` and must be recovered before starting competing work.
