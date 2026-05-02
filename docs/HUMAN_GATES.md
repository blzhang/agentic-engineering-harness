# Human Gates

The harness preserves human authority over intent and final use.

## Required Human Gates

1. Requirement or PRD/version-plan approval.
2. Standalone Issue confirmation when no approved plan exists.
3. Final result acceptance.
4. Final version acceptance before `version/vNext` merges to `main`.
5. Merge, deploy, production use, irreversible action, risk increase, or promotion decision.

## Not Human Gates

These can be automated:

- generating Issues from an approved plan;
- creating branches;
- filling PR templates;
- running CI;
- triggering independent review;
- applying accepted review fixes;
- rerunning focused checks.

## Clarification Gate

When the agent cannot make an Issue deterministic, it must ask the human to clarify before implementation.
