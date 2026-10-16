#!/usr/bin/env python3
"""Sync the approved-change ledger in master_storyline.md.

No LLM or external dependencies. The authored story remains outside the
generated region. --write updates that region; --check enforces both exact
sync and presence of every approved CR in the hand-written story.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "change_requests.json"
STORYLINE = ROOT / "master_storyline.md"
BEGIN = "<!-- BEGIN AUTO-APPROVAL-LEDGER -->"
END = "<!-- END AUTO-APPROVAL-LEDGER -->"


def approved(change: dict) -> bool:
    return change.get("status", "").startswith("approved")


def normalized_digest(data: dict) -> str:
    canonical = json.dumps(
        data, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()[:20]


def one_line(value: str) -> str:
    return " ".join(str(value).split())


def approval_ledger(data: dict) -> str:
    changes = [c for c in data.get("requests", []) if approved(c)]
    digest = normalized_digest(data)
    lines = [
        BEGIN,
        "<!-- GENERATED: do not edit; run python sync_master_storyline.py --write -->",
        f"<!-- change_register_digest: {digest} -->",
        "",
        "## Automatically synchronized approval ledger",
        "",
        f"**Change register fingerprint:** `{digest}` · "
        f"**Approved requests:** {len(changes)} · "
        "**Authority:** [change_requests.json](change_requests.json).",
        "",
        "This ledger reflects approved requirements, outstanding qualifications, "
        "and the provisional timeline verbatim from the register. The "
        "chronological narrative above must separately integrate each approval.",
        "",
    ]
    for change in changes:
        code = change["id"]
        lines.extend(
            [
                f"### {code} — {one_line(change['title'])}",
                "",
                f"**Register status:** `{change['status']}`",
                "",
            ]
        )
        for requirement in change.get("requirements", []):
            lines.append(f"- {one_line(requirement)}")
        if change.get("open"):
            lines.extend(["", "**Still open:**"])
            for detail in change["open"]:
                lines.append(f"- {one_line(detail)}")
        lines.append("")

    lines.extend(["### Author-approved editorial safeguards", ""])
    for caution in data.get("explicit_cautions", []):
        lines.append(f"- {one_line(caution)}")
    lines.extend(
        [
            "",
            "### Provisional canonical timeline",
            "",
            "| Period | Event or direction |",
            "|---|---|",
        ]
    )
    for entry in data.get("provisional_timeline", []):
        period = one_line(entry.get("range", "")).replace("|", "\\|")
        event = one_line(entry.get("event", "")).replace("|", "\\|")
        lines.append(f"| {period} | {event} |")
    lines.extend(["", END])
    return "\n".join(lines)


def render(text: str, data: dict) -> str:
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError("Exactly one start marker and end marker are required.")
    start = text.index(BEGIN)
    end = text.index(END, start) + len(END)
    return text[:start] + approval_ledger(data) + text[end:]


def missing_narrative_integrations(text: str, data: dict) -> list[str]:
    narrative = text.split(BEGIN, 1)[0]
    # Require a reference in authored prose, not just the generated appendix.
    return [
        change["id"] for change in data.get("requests", [])
        if approved(change) and not re.search(
            r"(?<![A-Za-z0-9])" + re.escape(change["id"]) + r"(?![0-9])",
            narrative,
        )
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Regenerate ledger")
    mode.add_argument("--check", action="store_true", help="Verify exact sync and narrative reconciliation")
    args = parser.parse_args()

    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    text = STORYLINE.read_text(encoding="utf-8")
    expected = render(text, data)

    if args.write:
        if text != expected:
            STORYLINE.write_text(expected, encoding="utf-8")
            print("Updated master_storyline.md approval ledger.")
        else:
            print("master_storyline.md is already synchronized.")
        pending = missing_narrative_integrations(expected, data)
        if pending:
            print("WARNING: Narrative integration still required for " + ", ".join(pending))
        return 0

    problems: list[str] = []
    if text != expected:
        problems.append(
            "Generated ledger is stale: python book-agent/revision/sync_master_storyline.py --write"
        )
    missing = missing_narrative_integrations(text, data)
    if missing:
        problems.append(
            "Approved changes missing from authored narrative: " + ", ".join(missing)
            + ". Integrate each into its chronological story section, not only the generated appendix."
        )
    if problems:
        print("MASTER STORYLINE VALIDATION FAILED:")
        for problem in problems:
            print("- " + problem)
        return 1
    print("Master storyline ledger synchronized; all approved IDs present in authored narrative.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
