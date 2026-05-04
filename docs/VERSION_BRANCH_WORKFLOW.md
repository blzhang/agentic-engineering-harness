# Version Branch Workflow

This workflow is for projects where `main` represents human-accepted stable software and a whole version should be developed, integrated, tested, and accepted before it returns to `main`.

## Branch Roles

- `main`: stable line. Only human-accepted versions, hotfixes, or release metadata land here.
- `version/vNext`: version integration line. PRD, plan, generated Issues, and completed Issue PRs integrate here while the version is under development.
- `codex/vNext-plan`: optional planning branch for PRD, design, and Issue generation work before the version line is ready.
- `codex/vNext-issue-<number>-<topic>`: task branch for one ready Issue or tightly coupled Issue set.
- `hotfix/main-<topic>`: urgent fix branch from `main`; accepted fixes must be backported or cherry-picked to the active version branch when relevant.

Use project-specific names when they are clearer, but preserve the roles.

## Flow

```text
main
  -> version/vNext
      -> codex/vNext-plan
      -> codex/vNext-issue-001-topic
      -> codex/vNext-issue-002-topic
      -> codex/vNext-issue-003-topic
  -> final PR: version/vNext -> main
```

The version branch is an integration branch, not a construction site. Agents do not directly edit it for implementation work. They create isolated task branches and PR back into the version branch.

## Version Start

1. Create `version/vNext` from the current accepted `main`.
2. Create or update the PRD/version plan in a planning branch or isolated worktree.
3. Run the PRD review gate from `docs/PRD_EXECUTION_LOOP.md`: use an isolated PRD reviewer subagent/session when available, revise the PRD from accepted findings, and self-review the revised plan.
4. Get human approval for the reviewed PRD/version plan.
5. Generate structured Issues from the approved plan.
6. Mark generated Issues ready only when they preserve the approved scope and deterministic acceptance criteria.

## Task Execution

For each ready Issue:

1. Create a dedicated worktree or isolated checkout from `version/vNext`.
2. Create `codex/vNext-issue-<number>-<topic>`.
3. Verify the clean baseline or record known pre-existing failures.
4. Follow RED/GREEN/REFACTOR or a deterministic substitute.
5. Open a draft PR targeting `version/vNext`.
6. Run CI and independent review: PR-level review when available, otherwise an isolated reviewer subagent/session when the runtime supports it.
7. Merge into `version/vNext` only after checks, review, and required human acceptance for that task.

Serial execution remains the default: one ready Issue, one task branch, one draft PR. Parallel work is allowed only when the human explicitly asks and the work units are independent.

## Version Integration

The version branch must stay reviewable and recoverable:

- no direct agent implementation commits;
- CI runs on PRs into the version branch and on pushes to the version branch;
- each merged Issue PR keeps its own evidence and closeout;
- the version branch maintains a version-level evidence summary or PR description;
- blockers are tracked as Issues, not hidden in session memory.

## Version Closeout

When all version Issues are complete:

1. Run version-level regression checks.
2. Confirm review findings are fixed or explicitly rejected with evidence.
3. Produce a version evidence summary.
4. Open the final PR from `version/vNext` to `main`.
5. Human accepts or rejects the complete version.
6. Merge to `main` only after human acceptance.
7. Tag or record the release when the project requires it.

The final version PR reviews the integrated version evidence and remaining risk. It should not replace the per-Issue implementation reviews.

## Hotfixes

Urgent fixes that must land on stable software start from `main`.

After the hotfix is accepted, decide whether it must also land in the active `version/vNext` branch. If yes, backport or cherry-pick it with a separate PR and evidence.

## Worktree Safety

Prefer worktrees for version planning and Issue execution so the main workspace and version integration branch stay clean.

Before creating a project-local worktree directory such as `.worktrees/`, verify it is ignored by git. If it is not ignored, add the ignore rule before creating worktrees.
