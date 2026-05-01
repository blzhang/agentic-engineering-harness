# Agentic Engineering Harness

A reusable, human-gated engineering workflow for AI coding agents.

This project packages a development methodology for turning human intent into verifiable software changes:

```text
human requirement
  -> PRD or version plan
  -> human plan approval
  -> structured GitHub Issues
  -> one ready Issue, one branch, serial execution
  -> strict RED/GREEN/REFACTOR
  -> draft PR
  -> automatic review
  -> human acceptance before merge, deploy, or use
```

The harness is designed for projects where AI coding agents are useful but should not be allowed to blur product intent, skip tests, self-approve work, or merge/deploy without human acceptance.

## What It Provides

- A protocol for PRD-first, human-approved planning.
- GitHub Issue contracts that are structured, deterministic, and regression-testable.
- A strict test-first implementation rule for material behavior changes.
- PR evidence templates for tests, review status, and residual risk.
- A Codex skill that can apply the workflow across projects.
- Scripts for validating Issue and PR text for common harness failures.

## Core Rules

1. Human approval of a PRD or version plan is the planning gate.
2. Issues generated from an approved plan do not need a second human approval unless scope changes or ambiguity appears.
3. Standalone Issues require human confirmation before they can be marked ready.
4. Every ready Issue must have deterministic input, output, rules, constraints, acceptance criteria, verification, and a micro-plan.
5. If the agent cannot make the Issue deterministic, it must ask the human to clarify.
6. Default execution is serial: one ready Issue, one branch, one draft PR.
7. Material behavior changes use strict RED/GREEN/REFACTOR.
8. Agent self-review is only preflight, never the independent review gate.
9. Review should run automatically after PR creation.
10. Human acceptance is required before merge, deploy, production use, irreversible actions, or risk increases.

## Repository Layout

```text
docs/                         Protocol and reference docs
templates/                    Files copied into target projects
skills/agentic-engineering-harness/
                              Codex skill
scripts/                      Deterministic validators and installers
examples/                     Example adapted project snippets
```

## Quick Start

Copy the templates into a target project:

```bash
python scripts/install_templates.py --target /path/to/project
```

Then use the skill instructions in `skills/agentic-engineering-harness/SKILL.md` when working with Codex.

## Status

This is an early harness extracted from real project work. It is intentionally conservative: serial execution first, deterministic contracts first, human gates preserved.

