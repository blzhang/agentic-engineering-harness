# Structured Issue Contract

Issues are executable specifications. They do not need one fixed template, but they must be structured enough to verify and regress.

## Minimum Contract

```text
Title:

Context:

Input:

Output:

Rules:

Constraints:

Acceptance:

Verification:

Guardrails:

Micro-plan:
```

The wording can vary by project, but the information must exist.

## Ready Checklist

- [ ] The target behavior is observable.
- [ ] Inputs or triggering state are explicit.
- [ ] Outputs or state transitions are explicit.
- [ ] Rules are testable.
- [ ] Constraints are concrete.
- [ ] Acceptance criteria are deterministic.
- [ ] Verification includes commands, fixtures, or reproducible evidence.
- [ ] There are no placeholders such as `TBD`, `TODO`, `handle edge cases`, or `add tests`.
- [ ] Ambiguities are resolved or sent back to the human.

## Not Ready Examples

```text
Improve the backtest system.
```

```text
Add better validation and tests.
```

```text
Make the UI nicer.
```

These might be valid ideas, but they are not ready Issues.

