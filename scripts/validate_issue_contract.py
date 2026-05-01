#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_PATTERNS = {
    "input": r"\bInput\b|\bInputs\b|输入",
    "output": r"\bOutput\b|\bOutputs\b|输出",
    "rules": r"\bRules\b|\bRule\b|规则",
    "constraints": r"\bConstraints\b|\bConstraint\b|约束",
    "acceptance": r"\bAcceptance\b|验收",
    "verification": r"\bVerification\b|\bTest\b|\bTests\b|验证|测试",
    "micro_plan": r"\bMicro-?plan\b|\bPlan\b|计划",
}
PLACEHOLDERS = ["TBD", "TODO", "handle edge cases", "add tests", "similar to previous"]


def validate(text: str) -> list[str]:
    failures: list[str] = []
    for name, pattern in REQUIRED_PATTERNS.items():
        if not re.search(pattern, text, flags=re.IGNORECASE):
            failures.append(f"missing section: {name}")
    lowered = text.lower()
    for placeholder in PLACEHOLDERS:
        if placeholder.lower() in lowered:
            failures.append(f"placeholder found: {placeholder}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a markdown Issue body for deterministic harness contract sections.")
    parser.add_argument("path", help="Path to issue markdown/text file")
    args = parser.parse_args()
    path = Path(args.path)
    failures = validate(path.read_text(encoding="utf-8"))
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("OK: issue contract looks structured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

