# PRD To Issues

## Rule

Reviewed and human-approved PRDs and version plans are the source of truth for product intent. Issues are execution units derived from them.

## Process

1. Read the reviewed and approved PRD or version plan.
2. Confirm the plan records the requirement and design logic: original requirement, discussion path, assumptions, rejected alternatives, selected design rationale, and acceptance/verification mapping.
3. Confirm the PRD review gate was completed or that an independent-review limitation and local second-pass PRD review were recorded before human approval.
4. Identify coherent work items.
5. Preserve dependencies and priority order.
6. Create one Issue per smallest coherent deliverable.
7. Copy relevant acceptance criteria, guardrails, and rationale into each Issue.
8. Add a deterministic verification plan.
9. Add a micro-plan.
10. Assign the target base branch, usually the active `version/vNext` branch.
11. Mark generated Issues ready only when they do not change scope or introduce ambiguity.

## When To Ask Human

Ask the human before marking ready when:

- the plan has conflicting requirements;
- the plan omits the discussion-to-decision logic needed to review why this design was chosen;
- the plan lacks evidence that the PRD review gate was completed or explicitly limited;
- the Issue needs a product decision not present in the plan;
- the Issue narrows or expands the plan materially;
- deterministic verification cannot be specified;
- risk boundaries are unclear.
