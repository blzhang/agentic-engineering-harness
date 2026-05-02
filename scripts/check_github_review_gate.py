#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REVIEW_REQUEST_MARKERS = ("@codex review", "codex review")
REVIEWER_LOGINS = {"codex"}
REVIEW_SIGNAL_MARKERS = ("codex", "openai")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[Any]:
    items: list[Any] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            items.append(json.loads(line))
    return items


def run_gh_json(args: list[str]) -> Any:
    completed = subprocess.run(args, check=False, text=True, capture_output=True)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip() or f"command failed: {' '.join(args)}")
    return json.loads(completed.stdout or "null")


def fetch_live(repo: str, pr: str) -> tuple[dict[str, Any], list[Any]]:
    pr_json = run_gh_json(
        [
            "gh",
            "pr",
            "view",
            pr,
            "--repo",
            repo,
            "--comments",
            "--json",
            "number,state,isDraft,reviewDecision,comments,reviews,statusCheckRollup,url",
        ]
    )
    timeline = run_gh_json(
        [
            "gh",
            "api",
            f"repos/{repo}/issues/{pr}/timeline",
            "--paginate",
            "--jq",
            "[.[] | {event:.event, actor:(.actor.login // .user.login), created_at:.created_at, state:.state, body:.body}]",
        ]
    )
    return pr_json, timeline


def text_contains_review_request(text: str | None) -> bool:
    if not text:
        return False
    lowered = text.lower()
    return any(marker in lowered for marker in REVIEW_REQUEST_MARKERS)


def comment_author(comment: dict[str, Any]) -> str:
    author = comment.get("author") or comment.get("user") or {}
    if isinstance(author, dict):
        return str(author.get("login") or "")
    return ""


def review_author(review: dict[str, Any]) -> str:
    author = review.get("author") or review.get("user") or {}
    if isinstance(author, dict):
        return str(author.get("login") or "")
    return ""


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def on_or_after(value: str | None, threshold: datetime | None) -> bool:
    if threshold is None:
        return True
    current = parse_time(value)
    if current is None:
        return False
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    return current >= threshold


def check_name(check: dict[str, Any]) -> str:
    parts: list[str] = []
    for key in ("name", "workflowName", "title", "status", "conclusion"):
        value = check.get(key)
        if value:
            parts.append(str(value))
    app = check.get("app")
    if isinstance(app, dict):
        parts.append(str(app.get("slug") or app.get("name") or ""))
    return " ".join(parts).lower()


def check_time(check: dict[str, Any]) -> str | None:
    for key in ("completedAt", "startedAt", "createdAt", "updatedAt", "completed_at", "started_at", "created_at", "updated_at"):
        value = check.get(key)
        if value:
            return str(value)
    return None


def classify(pr_json: dict[str, Any], timeline: list[Any]) -> tuple[str, dict[str, Any]]:
    comments = pr_json.get("comments") or []
    reviews = pr_json.get("reviews") or []
    checks = pr_json.get("statusCheckRollup") or []
    review_decision = str(pr_json.get("reviewDecision") or "")

    request_comments = [
        {
            "author": comment_author(comment),
            "createdAt": comment.get("createdAt"),
            "url": comment.get("url"),
            "body": comment.get("body"),
        }
        for comment in comments
        if isinstance(comment, dict) and text_contains_review_request(comment.get("body"))
    ]
    request_times = [parse_time(item.get("createdAt")) for item in request_comments]
    latest_request_time = max((item for item in request_times if item is not None), default=None)
    codex_mentions = [
        item
        for item in timeline
        if isinstance(item, dict)
        and str(item.get("event") or "").lower() == "mentioned"
        and str(item.get("actor") or "").lower() == "codex"
    ]
    codex_comments = [
        {
            "author": comment_author(comment),
            "createdAt": comment.get("createdAt"),
            "url": comment.get("url"),
            "body": comment.get("body"),
        }
        for comment in comments
        if isinstance(comment, dict)
        and comment_author(comment).lower() == "codex"
        and str(comment.get("body") or "").strip()
        and on_or_after(comment.get("createdAt"), latest_request_time)
    ]
    codex_reviews = [
        {
            "author": review_author(review),
            "submittedAt": review.get("submittedAt") or review.get("createdAt"),
            "state": review.get("state"),
            "body": review.get("body"),
        }
        for review in reviews
        if isinstance(review, dict)
        and review_author(review).lower() in REVIEWER_LOGINS
        and on_or_after(review.get("submittedAt") or review.get("createdAt"), latest_request_time)
    ]
    codex_checks = [
        check
        for check in checks
        if isinstance(check, dict)
        and any(marker in check_name(check) for marker in REVIEW_SIGNAL_MARKERS)
        and on_or_after(check_time(check), latest_request_time)
    ]
    review_timeline_events = [
        item
        for item in timeline
        if isinstance(item, dict)
        and str(item.get("event") or "").lower()
        in {"reviewed", "review_requested", "review_request_removed", "ready_for_review"}
    ]

    evidence = {
        "pr": {
            "number": pr_json.get("number"),
            "state": pr_json.get("state"),
            "isDraft": pr_json.get("isDraft"),
            "url": pr_json.get("url"),
        },
        "request_comments": request_comments,
        "codex_mentions": codex_mentions,
        "reviews_count": len(reviews),
        "codex_reviews": codex_reviews,
        "review_decision": review_decision,
        "codex_comments": codex_comments,
        "codex_checks": codex_checks,
        "review_timeline_events": review_timeline_events,
    }

    has_request = bool(request_comments)
    has_review_signal = has_request and bool(codex_reviews or codex_comments)
    if has_review_signal:
        return "review_signal_present", evidence
    if has_request:
        return "mentioned_only", evidence
    return "no_review_request", evidence


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check whether a GitHub Codex review request produced a real review signal."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--repo", help="GitHub repository, for example owner/name. Requires --pr.")
    source.add_argument("--pr-json", help="Fixture path from gh pr view --json ...")
    parser.add_argument("--pr", help="Pull request number when using --repo.")
    parser.add_argument("--timeline-jsonl", help="Fixture path containing one GitHub timeline JSON object per line.")
    parser.add_argument("--wait-seconds", type=int, default=0, help="Poll live GitHub for up to this many seconds.")
    parser.add_argument("--poll-interval", type=int, default=30, help="Live polling interval in seconds.")
    parser.add_argument("--expect-status", help="Testing helper: exit 0 only when the computed status matches.")
    args = parser.parse_args()

    if args.repo and not args.pr:
        parser.error("--repo requires --pr")
    if args.pr_json and not args.timeline_jsonl:
        parser.error("--pr-json requires --timeline-jsonl")

    deadline = time.time() + max(args.wait_seconds, 0)
    last_status = "unknown"
    last_evidence: dict[str, Any] = {}

    while True:
        try:
            if args.repo:
                pr_json, timeline = fetch_live(args.repo, args.pr)
            else:
                pr_json = load_json(Path(args.pr_json))
                timeline = load_jsonl(Path(args.timeline_jsonl))
        except Exception as exc:
            print(json.dumps({"status": "tooling_error", "error": str(exc)}, ensure_ascii=False, indent=2))
            return 4

        last_status, last_evidence = classify(pr_json, timeline)
        if last_status == "review_signal_present" or time.time() >= deadline or not args.repo:
            break
        time.sleep(max(args.poll_interval, 1))

    print(json.dumps({"status": last_status, "evidence": last_evidence}, ensure_ascii=False, indent=2))
    if args.expect_status:
        return 0 if last_status == args.expect_status else 5
    if last_status == "review_signal_present":
        return 0
    if last_status == "mentioned_only":
        return 2
    if last_status == "no_review_request":
        return 3
    return 4


if __name__ == "__main__":
    raise SystemExit(main())
