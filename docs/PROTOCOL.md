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
  -> human approves plan
  -> agent generates structured Issues from approved plan
  -> one ready Issue is selected
  -> agent creates branch
  -> strict RED/GREEN/REFACTOR implementation
  -> agent preflight self-review
  -> draft PR
  -> CI and automatic independent review
  -> agent fixes review findings and reruns checks
  -> human accepts or rejects result
  -> merge/deploy/use decision
```

## Human Gates

Human approval is required for:

- original requirement or PRD/version plan acceptance;
- standalone Issue readiness when no approved plan exists;
- final result acceptance;
- merge, deploy, production use, irreversible actions, risk increases, or promotion decisions.

Issues generated directly from an approved PRD/version plan inherit that approval. They do not require another human approval unless they change scope, expose ambiguity, or conflict with the approved plan.

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
one ready Issue -> one branch -> one draft PR -> review -> human acceptance
```

Parallel coding is not the default. Use it only when the human explicitly asks for it and the work units are genuinely independent.

## Test-First Rule

Features, bug fixes, refactors, and material behavior changes follow:

```text
RED: write or adjust a failing test, fixture, replay, or deterministic check
GREEN: implement the smallest change that makes it pass
REFACTOR: clean up while checks stay green
```

If a true red phase is impossible, the Issue or PR must state why and provide the strongest deterministic substitute.

## Review Rule

Agent self-review is preflight only. It catches low-level gaps before PR publication.

Independent review should start automatically after PR creation. The implementing agent fixes accepted findings and reruns checks.

Human acceptance remains separate from review approval.

