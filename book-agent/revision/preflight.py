#!/usr/bin/env python3
"""Mechanical checks to run before a review or a push.

    python3 book-agent/revision/preflight.py --draft book-agent/revision/CR-083.md
        Check a CR draft before a fresh-context review. Errors (exit 1):
          1. the machine-read headings are present, spelled exactly;
          2. the fact changes parse, apply to canon_facts.toml and preview cleanly,
             and no event pattern fixes its own year;
          3. the ledger lists under "### New parties", "### Amended commitments" and
             "### New commitments" agree with commitments/data/ledger.toml;
          4. every storyline line the draft cites carries an anchor at least once,
             L1554 ("a phrase from that line"), and the phrase is on that line or
             the line beside it.
        Warnings (exit 0): 'line 1562' written without the checked L form; CR
        numbers with no file and no register entry; forbidden
        patterns that match the draft's own prose; new people missing from the
        registry; commitment IDs mentioned in the text that the ledger does not have.

    python3 book-agent/revision/preflight.py --draft DRAFT.md --skip-approved
        The same, but a CR the register already marks approved is skipped (CI uses
        this: integration edits old CR records that predate CR-TEMPLATE.md).

    python3 book-agent/revision/preflight.py --integration
        Run every canon check CI runs, in one command: storyline sync, canon lint,
        register facts, the commitments ledger, the character documents and the
        unit tests.

The draft format is in book-agent/revision/CR-TEMPLATE.md. Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
STORY = BASE / "master_storyline.md"
REGISTRY = BASE / "character_registry.json"
LEDGER = ROOT / "commitments" / "data" / "ledger.toml"
sys.path.insert(0, str(BASE))
import cr_facts  # noqa: E402

REQUIRED_HEADINGS = ("Canon tensions", "Fact changes", "Decisions", "Sources")
LEDGER_LISTS = ("New parties", "Amended commitments", "New commitments")
ANCHOR_WINDOW = 1   # lines either side of the cited line that may hold the phrase
MIN_ANCHOR = 8      # characters; shorter phrases match almost any line

HEADING = re.compile(r"^(#{2,6})\s+(.*?)\s*$", re.M)
FENCE = re.compile(r"^```.*?^```[^\n]*$", re.M | re.S)
COMMENT = re.compile(r"<!--.*?-->", re.S)
CITATION = re.compile(r"(?<![\w-])L(\d+)(?:\s*[–-]\s*L?(\d+))?(\s*\(\s*[\"“]([^\"”\n]+)[\"”]\s*\))?")
YEAR_GROUP = re.compile(r"\(\?P<year>((?:[^()\\]|\\.|\([^()]*\))*)\)")
BULLET_ID = re.compile(r"^\s*[-*]\s+`([^`]+)`", re.M)
COMMITMENT_ID = re.compile(r"`(C-\d{4}-[A-Z0-9-]+)`")
CR_NUMBER = re.compile(r"\bCR-(\d{3})\b")
LINE_WORD = re.compile(r"\blines?\s+[`*]*(\d{2,4})\b(?!(?:[\s,`*–-]|and|\d+)*\bof\b)", re.I)


def blank(text: str, pattern: re.Pattern) -> str:
    """Replace every match with spaces, keeping newlines so line numbers still hold."""
    return pattern.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)


def prose(text: str) -> str:
    """The draft without fenced blocks and HTML comments, line numbers unchanged."""
    return blank(blank(text, FENCE), COMMENT)


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def sections(text: str, level: int = 2) -> list[tuple[str, int, int]]:
    """(heading text, start of body, end of body) for each heading of this level."""
    heads = [m for m in HEADING.finditer(blank(text, FENCE)) if len(m.group(1)) <= level]
    out = []
    for i, m in enumerate(heads):
        if len(m.group(1)) == level:
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            out.append((m.group(2), m.end(), end))
    return out


def normalise(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("*", "").replace("’", "'")).strip().casefold()


# ---------------------------------------------------------------------------
# 1. Headings
# ---------------------------------------------------------------------------

def check_headings(text: str) -> list[str]:
    errors = []
    found = [h for h, _, _ in sections(text, 2)]
    for want in REQUIRED_HEADINGS:
        if want in found:
            continue
        near = [h for h in found if want.casefold() in h.casefold()]
        hint = f"; found '## {near[0]}', which the tools do not read" if near else ""
        errors.append(f"headings: no '## {want}' section, spelled exactly{hint}")
    return errors


# ---------------------------------------------------------------------------
# 2. Fact changes
# ---------------------------------------------------------------------------

def event_patterns(change: dict) -> list[str]:
    if "add_event" in change:
        return list(change["add_event"].get("patterns", []))
    if "event" in change:
        return list(change.get("set", {}).get("patterns", []))
    return []


def check_fact_changes(path: Path, run_preview: bool = True) -> tuple[list[str], list[str], list[dict]]:
    errors, warnings = [], []
    try:
        changes = cr_facts.draft_changes(path)
    except cr_facts.FactError as e:
        return [f"fact changes: {e}"], warnings, []
    for change in changes:
        for pattern in event_patterns(change):
            try:
                compiled = re.compile(pattern)
            except re.error as e:
                errors.append(f"fact changes: event pattern does not compile ({e}): {pattern}")
                continue
            if "year" not in compiled.groupindex:
                errors.append(f"fact changes: event pattern has no (?P<year>…) group: {pattern}")
                continue
            body = YEAR_GROUP.search(pattern)
            if body and re.fullmatch(r"\d{4}", body.group(1)):
                errors.append(f"fact changes: event pattern fixes its year to {body.group(1)}, so a wrong "
                              f"year can never be caught; use (?P<year>1[89]\\d\\d): {pattern}")
        if "add_forbidden" in change:
            pattern = change["add_forbidden"].get("pattern", "")
            try:
                re.compile(pattern)
            except re.error as e:
                errors.append(f"fact changes: forbidden pattern does not compile ({e}): {pattern}")
    try:
        cr_facts.apply_changes(cr_facts.FACTS.read_text(encoding="utf-8"), changes, path.stem)
    except cr_facts.FactError as e:
        errors.append(f"fact changes: {e}")
    except Exception as e:  # a malformed entry (missing key, wrong type)
        errors.append(f"fact changes: an entry is malformed ({type(e).__name__}: {e})")
    if run_preview and not errors:
        for extra in ([], ["--tensions"]):
            r = subprocess.run([sys.executable, str(BASE / "cr_facts.py"), "preview", *extra, str(path)],
                               capture_output=True, text=True)
            if r.returncode != 0:
                tail = (r.stderr or r.stdout).strip().splitlines()[-1:] or ["no output"]
                errors.append(f"fact changes: cr_facts.py preview {' '.join(extra)} failed: {tail[0]}")
    known = {c["id"] for c in json.loads(REGISTRY.read_text(encoding="utf-8")).get("people", [])}
    for change in changes:
        ident = change.get("add_person", {}).get("id")
        if ident and ident not in known:
            warnings.append(f"registry: {ident} is added under Fact changes and is not yet in "
                            f"character_registry.json; both must land in the same commit")
    return errors, warnings, changes


# ---------------------------------------------------------------------------
# 3. Ledger
# ---------------------------------------------------------------------------

def ledger_ids() -> tuple[set[str], set[str]]:
    data = tomllib.loads(LEDGER.read_text(encoding="utf-8"))
    return ({p["id"] for p in data.get("party", [])}, {c["id"] for c in data.get("commitment", [])})


def ledger_lists(text: str) -> dict[str, list[tuple[str, int]] | None]:
    """IDs under each '### <list>' heading, with line numbers; None if the heading is missing."""
    out: dict[str, list[tuple[str, int]] | None] = {name: None for name in LEDGER_LISTS}
    clean = prose(text)
    for heading, start, end in sections(text, 3):
        if heading in out:
            out[heading] = [(m.group(1), line_of(text, start + m.start())) for m in BULLET_ID.finditer(clean[start:end])]
            if not out[heading] and not re.search(r"\bnone\b", clean[start:end], re.I):
                out[heading] = [("", line_of(text, start))]
    return out


def check_ledger(text: str) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    parties, commitments = ledger_ids()
    lists = ledger_lists(text)
    for name, items in lists.items():
        if items is None:
            errors.append(f"ledger: no '### {name}' list (bullets that start with the ID in backticks, or the word none)")
            continue
        for ident, line in items:
            if not ident:
                errors.append(f"ledger: line {line}: '### {name}' has neither ID bullets nor the word none")
            elif name == "New parties" and ident in parties:
                errors.append(f"ledger: line {line}: new party `{ident}` already exists in ledger.toml; choose another ID")
            elif name == "Amended commitments" and ident not in commitments:
                errors.append(f"ledger: line {line}: amended commitment `{ident}` is not in ledger.toml")
            elif name == "New commitments" and ident in commitments:
                errors.append(f"ledger: line {line}: new commitment `{ident}` already exists in ledger.toml")
    declared = {i for items in lists.values() if items for i, _ in items}
    clean = prose(text)
    seen = set()
    for m in COMMITMENT_ID.finditer(clean):
        ident = m.group(1)
        if ident not in commitments and ident not in declared and ident not in seen:
            seen.add(ident)
            warnings.append(f"ledger: line {line_of(clean, m.start())}: `{ident}` is not in ledger.toml "
                            f"and is not listed as a new commitment")
    return errors, warnings


# ---------------------------------------------------------------------------
# 4. Storyline citations
# ---------------------------------------------------------------------------

def check_citations(text: str, story_lines: list[str] | None = None) -> list[str]:
    """Each cited storyline line carries its anchor phrase at least once in the draft.

    Later mentions of the same line may be bare; a line never anchored is an error.
    """
    errors = []
    if story_lines is None:
        story_lines = STORY.read_text(encoding="utf-8").split("\n")
    clean = prose(text)
    anchored: set[tuple[int, int]] = set()
    bare: dict[tuple[int, int], int] = {}
    for m in CITATION.finditer(clean):
        first = int(m.group(1))
        last = int(m.group(2)) if m.group(2) else first
        where = f"line {line_of(clean, m.start())}"
        label = f"L{first}" + (f"–{last}" if last != first else "")
        if last < first or first < 1 or last > len(story_lines):
            errors.append(f"citations: {where}: {label} is outside master_storyline.md (1–{len(story_lines)})")
            continue
        if not m.group(3):
            bare.setdefault((first, last), line_of(clean, m.start()))
            continue
        anchored.add((first, last))
        phrase = normalise(m.group(4))
        if len(phrase) < MIN_ANCHOR:
            errors.append(f"citations: {where}: the anchor \"{m.group(4)}\" is too short to identify a line")
            continue
        lo, hi = max(1, first - ANCHOR_WINDOW), min(len(story_lines), last + ANCHOR_WINDOW)
        if any(phrase in normalise(story_lines[n - 1]) for n in range(lo, hi + 1)):
            continue
        hits = [n for n, line in enumerate(story_lines, 1) if phrase in normalise(line)]
        hint = (f"; the phrase is on line {', '.join(map(str, hits[:4]))}" if hits
                else "; the phrase is nowhere in the storyline")
        errors.append(f"citations: {where}: \"{m.group(4)}\" is not on {label}{hint}")
    anchored_lines = {n for first, last in anchored for n in (first, last)}
    for (first, last), line in sorted(bare.items()):
        # A bare range is covered when both its ends are anchored somewhere in the draft.
        if (first, last) not in anchored and not {first, last} <= anchored_lines:
            label = f"L{first}" + (f"–{last}" if last != first else "")
            errors.append(f"citations: line {line}: {label} is never given an anchor phrase in this draft; "
                          f"write {label} (\"a phrase from that line\") at least once")
    return errors


# ---------------------------------------------------------------------------
# Warnings
# ---------------------------------------------------------------------------

def warn_future_crs(text: str, own: str) -> list[str]:
    registered = {e["id"] for e in cr_facts.register()["requests"]}
    missing = {}
    clean = prose(text)
    for m in CR_NUMBER.finditer(clean):
        ident = m.group(0)
        if ident == own or ident in registered or ident in missing:
            continue
        if not any(BASE.glob(f"{ident}*.md")):
            missing[ident] = line_of(clean, m.start())
    return [f"standalone merge: {ident} (first cited on line {line}) has no file and no register entry; "
            f"this CR cannot rest on what it will decide" for ident, line in sorted(missing.items())]


def warn_line_words(text: str) -> list[str]:
    """'line 1562' with no file named: probably a storyline citation in the unchecked form."""
    clean = prose(text)
    seen: dict[str, int] = {}
    for m in LINE_WORD.finditer(clean):
        seen.setdefault(m.group(1), line_of(clean, m.start()))
    return [f"citations: line {line}: 'line {n}' is not checked; for the storyline write L{n} "
            f"(\"a phrase from that line\"), for another file 'line {n} of FILE'"
            for n, line in sorted(seen.items(), key=lambda kv: kv[1])]


def warn_self_hits(text: str, changes: list[dict]) -> list[str]:
    """Forbidden patterns that match the draft's own narrative.

    Impact notes, tensions and the fact changes quote the old wording on purpose, so
    those sections are left out, as are fenced blocks and HTML comments.
    """
    clean = prose(text)
    for heading, start, end in sections(text, 2):
        if re.search(r"impact|canon tensions|fact changes|ledger", heading, re.I):
            clean = clean[:start] + re.sub(r"[^\n]", " ", clean[start:end]) + clean[end:]
    warnings = []
    for change in changes:
        pattern = change.get("add_forbidden", {}).get("pattern")
        if not pattern:
            continue
        try:
            compiled = re.compile(pattern)
        except re.error:
            continue
        for m in compiled.finditer(clean):
            warnings.append(f"forbidden pattern matches the draft's own prose on line {line_of(clean, m.start())} "
                            f"(\"{m.group(0)}\"): narrow the pattern or reword the passage")
    return warnings


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def check_draft(path: Path, run_preview: bool = True) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors = check_headings(text)
    fact_errors, warnings, changes = check_fact_changes(path, run_preview)
    errors += fact_errors
    ledger_errors, ledger_warnings = check_ledger(text)
    errors += ledger_errors
    errors += check_citations(text)
    warnings += ledger_warnings
    warnings += warn_line_words(text)
    warnings += warn_future_crs(text, path.stem)
    warnings += warn_self_hits(text, changes)
    return errors, warnings


def cmd_draft(path: Path, skip_approved: bool) -> int:
    if not path.exists():
        print(f"preflight: {path} does not exist")
        return 1
    if skip_approved:
        entry = next((e for e in cr_facts.register()["requests"] if e["id"] == path.stem), None)
        if entry and cr_facts.approved(entry):
            print(f"preflight: {path.name} is approved in the register; draft checks skipped.")
            return 0
    errors, warnings = check_draft(path)
    for w in warnings:
        print(f"warning  {w}")
    for e in errors:
        print(f"ERROR    {e}")
    print(f"\npreflight: {path.name}: {len(errors)} error(s), {len(warnings)} warning(s).")
    if not errors:
        print("Ready for a fresh-context review. For the impact list run: "
              f"python3 book-agent/revision/cr_facts.py preview {path}")
    return 1 if errors else 0


INTEGRATION = [
    ("storyline sync", ["book-agent/revision/sync_master_storyline.py", "--check"]),
    ("canon lint", ["book-agent/revision/lint_canon.py"]),
    ("register facts", ["book-agent/revision/cr_facts.py", "check"]),
    ("commitments ledger", ["commitments/ledger.py", "check"]),
    ("character documents", ["book-agent/revision/validate_character_docs.py"]),
    ("revision tests", ["-m", "unittest", "discover", "-s", "book-agent/revision/tests"]),
    ("ledger tests", ["-m", "unittest", "discover", "-s", "commitments/tests"]),
]


def cmd_integration() -> int:
    failed = []
    for label, args in INTEGRATION:
        r = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True)
        print(f"{'ok  ' if r.returncode == 0 else 'FAIL'}  {label}")
        if r.returncode != 0:
            failed.append(label)
            out = (r.stdout + r.stderr).strip().splitlines()
            for line in out[-15:]:
                print(f"        {line}")
    print(f"\npreflight: {len(INTEGRATION) - len(failed)} of {len(INTEGRATION)} checks pass.")
    return 1 if failed else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--draft", type=Path, metavar="CR.md", help="check a CR draft")
    mode.add_argument("--integration", action="store_true", help="run every canon check")
    ap.add_argument("--skip-approved", action="store_true",
                    help="with --draft: skip a CR the register marks approved")
    args = ap.parse_args(argv)
    return cmd_integration() if args.integration else cmd_draft(args.draft, args.skip_approved)


if __name__ == "__main__":
    sys.exit(main())
