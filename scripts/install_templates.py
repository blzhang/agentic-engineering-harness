#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"


def copy_file(src: Path, dst: Path, overwrite: bool) -> None:
    if dst.exists() and not overwrite:
        print(f"skip existing {dst}")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"wrote {dst}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Install Agentic Engineering Harness templates into a project.")
    parser.add_argument("--target", required=True, help="Target project directory")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    if not target.exists():
        raise SystemExit(f"target does not exist: {target}")

    mapping = {
        TEMPLATES / "AGENTS.md": target / "AGENTS.md",
        TEMPLATES / "GITHUB_HARNESS_WORKFLOW.md": target / "docs" / "GITHUB_HARNESS_WORKFLOW.md",
        ROOT / "docs" / "AGENT_RUN_LIFECYCLE.md": target / "docs" / "AGENT_RUN_LIFECYCLE.md",
        ROOT / "docs" / "PRD_EXECUTION_LOOP.md": target / "docs" / "PRD_EXECUTION_LOOP.md",
        ROOT / "docs" / "VERSION_BRANCH_WORKFLOW.md": target / "docs" / "VERSION_BRANCH_WORKFLOW.md",
        TEMPLATES / "pull_request_template.md": target / ".github" / "pull_request_template.md",
        TEMPLATES / "ISSUE_TEMPLATE" / "change-request.yml": target / ".github" / "ISSUE_TEMPLATE" / "change-request.yml",
        TEMPLATES / "ISSUE_TEMPLATE" / "bug-report.yml": target / ".github" / "ISSUE_TEMPLATE" / "bug-report.yml",
        TEMPLATES / "workflows" / "ci.yml": target / ".github" / "workflows" / "ci.yml",
        ROOT / "scripts" / "check_github_review_gate.py": target / "scripts" / "check_github_review_gate.py",
    }
    for src, dst in mapping.items():
        copy_file(src, dst, args.overwrite)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
