# Test-First Rules

## Iron Rule

No material production behavior change without a failing or reproducible verification step first.

## Standard Cycle

1. RED: write or adjust the smallest test, fixture, replay, or deterministic command that proves the missing behavior.
2. Verify RED: run it and confirm it fails for the expected reason.
3. GREEN: implement the smallest code change.
4. Verify GREEN: run the focused check and nearby regression checks.
5. REFACTOR: clean up while checks stay green.

## Valid Substitutes

When traditional unit-test red phase is not practical, use the strongest deterministic substitute:

- reproduce the original bug;
- replay a fixture;
- run an evidence reconciliation command;
- compare generated artifact output before and after;
- run a dry-run/backtest fixture;
- assert a schema rejection or safety gate.

The PR must say which substitute was used and why.

## Stop Conditions

Stop and ask the human when:

- no meaningful test or deterministic substitute can be written;
- expected behavior is ambiguous;
- acceptance criteria cannot be checked;
- repeated failures suggest the plan is wrong.

