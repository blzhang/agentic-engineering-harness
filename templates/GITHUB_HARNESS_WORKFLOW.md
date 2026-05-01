# GitHub Harness Workflow

## Flow

```text
human requirement
  -> PRD or version plan
  -> human plan approval
  -> structured Issues
  -> one ready Issue
  -> branch
  -> RED/GREEN/REFACTOR implementation
  -> draft PR
  -> CI and automatic review
  -> human acceptance
```

## Ready Issues

Issues must be structured, deterministic, and regression-testable. They must include input, output, rules, constraints, acceptance, verification, guardrails, and micro-plan.

If any part is unclear, ask the human before marking ready.

## Execution

Default to serial execution: one Issue, one branch, one PR.

## Review

Self-review is preflight. Independent review should run automatically after PR creation.

Human acceptance is required before merge, deploy, or use.

