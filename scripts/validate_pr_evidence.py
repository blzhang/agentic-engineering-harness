#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED = [
    "Tests And Evidence",
    "RED",
    "Preflight Self-Review",
    "Review Gate",
    "Human Acceptance",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a PR body for harness evidence sections.")
    parser.add_argument("path", help="Path to PR markdown/text file")
    args = parser.parse_args()
    text = Path(args.path).read_text(encoding="utf-8")
    missing = [item for item in REQUIRED if item.lower() not in text.lower()]
    if missing:
        for item in missing:
            print(f"FAIL: missing {item}")
        return 1
    print("OK: PR evidence sections present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

