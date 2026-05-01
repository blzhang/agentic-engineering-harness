---
name: agentic-engineering-harness
description: Use when turning human requirements into PRDs, deterministic GitHub Issues, serial AI coding tasks, strict test-first implementation, draft PRs, automatic review loops, and human-gated acceptance across software projects.
---

# Agentic Engineering Harness

Use this skill when a user wants agentic coding governed by a reusable workflow.

## Core Workflow

1. Clarify the human requirement.
2. For large or product-level work, draft a PRD or version plan and wait for human approval.
3. Convert approved plan items into structured Issues.
4. For standalone Issues, get human confirmation before marking ready.
5. Ensure every ready Issue has deterministic input, output, rules, constraints, acceptance, verification, guardrails, and micro-plan.
6. Execute serially by default: one ready Issue, one branch, one draft PR.
7. Use RED/GREEN/REFACTOR for material behavior changes.
8. Treat self-review as preflight only.
9. Trigger independent review automatically after PR creation.
10. Keep human acceptance as the final gate before merge, deploy, or use.

## When To Stop

Stop and ask the human when:

- requirement intent is unclear;
- the Issue cannot be made deterministic;
- acceptance criteria are not testable;
- a meaningful red test or deterministic substitute cannot be written;
- implementation would exceed the approved plan scope;
- review reveals a product decision rather than an engineering fix.

## References

Read only what is needed:

- `references/protocol.md` for the end-to-end flow.
- `references/issue-contract.md` for ready Issue requirements.
- `references/tdd.md` for strict test-first rules.
- `references/review.md` for review loop and human acceptance.

