---
name: agentic-engineering-harness
description: Use when turning human requirements into PRDs, deterministic GitHub Issues, version integration branches, isolated worktree/task-branch execution, strict test-first implementation, draft PRs, automatic review loops, and human-gated acceptance across software projects.
---

# Agentic Engineering Harness

Use this skill when a user wants agentic coding governed by a reusable workflow.

## Core Workflow

1. Clarify the human requirement.
2. For large or product-level work, draft a PRD or version plan.
3. PRDs/version plans must record discussion-to-decision logic: original requirement, discussion path, assumptions, rejected alternatives, selected rationale, and the mapping from rationale to acceptance, verification, and Issues.
4. Before asking for human approval, open an isolated PRD reviewer subagent/session when the runtime supports it; revise the PRD from accepted findings and self-review the revised PRD.
5. Wait for human approval of the reviewed PRD/version plan.
6. For version-scoped work, create or select the `version/vNext` integration branch while keeping `main` stable.
7. Convert approved plan items into structured Issues.
8. For standalone Issues, get human confirmation before marking ready.
9. Ensure every ready Issue has deterministic input, output, rules, constraints, acceptance, verification, guardrails, and micro-plan.
10. Execute serially by default: one ready Issue, one isolated worktree, one task branch, one draft PR.
11. Open task PRs back to the version branch; merge the version branch to `main` only after version-level human acceptance.
12. Use RED/GREEN/REFACTOR for material behavior changes.
13. For whole-PRD or whole-version objectives, treat each local pass as a checkpoint and continue to the next unfinished item.
14. Answer status questions briefly, then continue the active objective unless the human explicitly pauses, stops, or asks for answer-only.
15. End every material agent run with an explicit lifecycle state and closeout evidence.
16. Treat self-review as preflight only.
17. Trigger independent review automatically after PR creation, then verify that it actually produced a review signal. For GitHub Codex review, use `scripts/check_github_review_gate.py`. If PR-level review is unavailable, mention-only, or no PR exists yet for a material checkpoint, open an isolated reviewer subagent/session when the runtime supports it.
18. Keep human acceptance as the final gate before merge, deploy, or use.

## When To Stop

Stop and ask the human when:

- requirement intent is unclear;
- the PRD discussion-to-decision logic is missing or ambiguous;
- the PRD review gate cannot be completed and no limitation has been recorded;
- the Issue cannot be made deterministic;
- acceptance criteria are not testable;
- a meaningful red test or deterministic substitute cannot be written;
- implementation would exceed the approved plan scope;
- review reveals a product decision rather than an engineering fix.

Do not stop silently after material edits, tests, branch work, PR work, or runtime operations. If closeout cannot be completed, mark the run `interrupted_incomplete`, `test_failed`, `blocked_tooling`, or `blocked_needs_human` with the next action.

## References

Read only what is needed:

- `references/protocol.md` for the end-to-end flow.
- `references/issue-contract.md` for ready Issue requirements.
- `references/version-branches.md` for version integration and task branch rules.
- `references/prd-execution-loop.md` for whole-PRD continuation rules.
- `references/tdd.md` for strict test-first rules.
- `references/run-lifecycle.md` for closeout states and interruption recovery.
- `references/review.md` for review loop and human acceptance.
