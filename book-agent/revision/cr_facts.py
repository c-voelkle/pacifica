#!/usr/bin/env python3
"""Carry fact changes from change requests into canon_facts.toml.

A CR that changes a date, age, identity or protected fact lists the change
once, in the same format, in two places:

* a CR draft: a "## Fact changes" section with one ```json block;
* the approved register entry in change_requests.json: a "facts" list.

Entry forms (use "was" whenever a value already exists, so a stale CR is caught):

    {"person": "CT-JULIAN-MOTHER", "set": {"died": 1889, "died_season": "spring"},
     "was": {"died": 1888, "died_season": "autumn"}}
    {"event": "hollerith-tabulation", "set": {"year": 1889}, "was": {"year": 1888}}
    {"add_person": {"id": "CT-…", "aliases": ["…"], "born": 1890}}
    {"add_event": {"id": "…", "year": 1900, "patterns": ["… (?P<year>1[89]\\\\d\\\\d)"]}}
    {"add_forbidden": {"pattern": "…", "message": "…"}}

Commands:

    python3 book-agent/revision/cr_facts.py preview DRAFT.md
        Lint current canon as if the draft's fact changes were approved and list
        every passage that would still state the old value (the impact list).
    python3 book-agent/revision/cr_facts.py apply CR-033
        For an approved register entry: update canon_facts.toml, then list the
        passages to revise. Refuses unapproved CRs and stale "was" values.
    python3 book-agent/revision/cr_facts.py check
        CI: every approved CR's fact changes are reflected in canon_facts.toml
        (a later approved CR may supersede an earlier one's value).

Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
import tomllib
from pathlib import Path

BASE = Path(__file__).resolve().parent
FACTS = BASE / "canon_facts.toml"
REGISTER = BASE / "change_requests.json"
sys.path.insert(0, str(BASE))
import lint_canon  # noqa: E402


class FactError(Exception):
    pass


# ---------------------------------------------------------------------------
# Reading fact changes
# ---------------------------------------------------------------------------

def register() -> dict:
    return json.loads(REGISTER.read_text(encoding="utf-8"))


def approved(entry: dict) -> bool:
    return entry.get("status", "").startswith("approved")


def draft_changes(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    section = re.search(r"^##+\s*Fact changes\s*$(.*?)(?=^##?\s|\Z)", text, re.M | re.S)
    if not section:
        raise FactError(f"{path.name}: no '## Fact changes' section")
    block = re.search(r"```json\s*\n(.*?)```", section.group(1), re.S)
    if not block:
        if re.search(r"\bnone\b", section.group(1), re.I):
            return []
        raise FactError(f"{path.name}: 'Fact changes' needs a ```json block (or the word 'none')")
    try:
        changes = json.loads(block.group(1))
    except json.JSONDecodeError as e:
        raise FactError(f"{path.name}: Fact changes JSON is invalid: {e}") from e
    if not isinstance(changes, list):
        raise FactError(f"{path.name}: Fact changes must be a JSON list")
    return changes


def current_facts(text: str) -> dict:
    data = tomllib.loads(text)
    return {
        "person": {p["id"]: p for p in data.get("person", [])},
        "event": {e["id"]: e for e in data.get("event", [])},
        "forbidden": [f["pattern"] for f in data.get("forbidden", [])],
    }


# ---------------------------------------------------------------------------
# Editing the TOML text (keeps comments and layout)
# ---------------------------------------------------------------------------

def toml_value(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        if "\\" in value or '"' in value:
            if "'''" in value:
                raise FactError(f"cannot write value containing ''' : {value!r}")
            return f"'''{value}'''"
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, list):
        return "[" + ", ".join(toml_value(v) for v in value) + "]"
    raise FactError(f"unsupported value {value!r}")


def block_span(lines: list[str], table: str, ident: str) -> tuple[int, int]:
    for i, line in enumerate(lines):
        if line.strip() == f"[[{table}]]":
            j = i + 1
            while j < len(lines) and not lines[j].startswith("[["):
                j += 1
            if any(re.match(rf'^id\s*=\s*"{re.escape(ident)}"', l) for l in lines[i:j]):
                # stop before trailing comment/blank lines that belong to the next section
                while j > i + 1 and (not lines[j - 1].strip() or lines[j - 1].lstrip().startswith("#")):
                    j -= 1
                return i, j
    raise FactError(f"no [[{table}]] with id = \"{ident}\" in canon_facts.toml")


def set_fields(text: str, table: str, ident: str, fields: dict, cr: str) -> str:
    lines = text.splitlines()
    start, end = block_span(lines, table, ident)
    for key, value in fields.items():
        rendered = f"{key} = {toml_value(value)}"
        for k in range(start, end):
            if re.match(rf"^{re.escape(key)}\s*=", lines[k]):
                comment = re.search(r"\s+#.*$", lines[k])
                lines[k] = rendered + (comment.group(0) if comment else "")
                break
        else:
            insert = next((k for k in range(start, end) if lines[k].startswith("source")), end)
            lines.insert(insert, rendered)
            end += 1
    for k in range(start, end):
        if lines[k].startswith("source") and cr not in lines[k]:
            m = re.match(r'^source\s*=\s*"(.*)"\s*$', lines[k])
            if m:
                lines[k] = f'source = "{m.group(1)}; {cr}"'
            break
    else:
        lines.insert(end, f'source = "{cr}"')
    return "\n".join(lines) + "\n"


def add_block(text: str, table: str, fields: dict, cr: str) -> str:
    body = [f"[[{table}]]"]
    for key, value in fields.items():
        if key != "source":
            body.append(f"{key} = {toml_value(value)}")
    body.append(f'source = "{fields.get("source", cr)}"' if "source" in fields else f'source = "{cr}"')
    return text.rstrip("\n") + "\n\n" + "\n".join(body) + "\n"


def apply_changes(text: str, changes: list[dict], cr: str, verify_was: bool = True) -> str:
    facts = current_facts(text)
    for change in changes:
        if "person" in change or "event" in change:
            table = "person" if "person" in change else "event"
            ident = change[table]
            if ident not in facts[table]:
                raise FactError(f"{cr}: {table} {ident} is not in canon_facts.toml (use add_{table})")
            if verify_was:
                for key, old in change.get("was", {}).items():
                    now = facts[table][ident].get(key)
                    if now != old:
                        raise FactError(f"{cr}: {ident}.{key} is {now!r} in canon_facts.toml, "
                                        f"but the CR says it was {old!r} — reconcile before applying")
            text = set_fields(text, table, ident, change["set"], cr)
        elif "add_person" in change or "add_event" in change:
            table = "person" if "add_person" in change else "event"
            fields = change[f"add_{table}"]
            if fields.get("id") in facts[table]:
                raise FactError(f"{cr}: {table} {fields['id']} already exists (use set)")
            text = add_block(text, table, fields, cr)
        elif "add_forbidden" in change:
            if change["add_forbidden"]["pattern"] not in facts["forbidden"]:
                text = add_block(text, "forbidden", change["add_forbidden"], cr)
        else:
            raise FactError(f"{cr}: unrecognised fact change {change}")
        facts = current_facts(text)  # fails loudly if the edit broke the TOML
    return text


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def temp_facts(text: str) -> tuple[tempfile.TemporaryDirectory, Path]:
    d = tempfile.TemporaryDirectory()
    path = Path(d.name) / "canon_facts.toml"
    path.write_text(text, encoding="utf-8")
    return d, path


def cmd_preview(args) -> int:
    draft = Path(args.draft)
    changes = draft_changes(draft)
    if not changes:
        print(f"{draft.name}: no fact changes declared.")
        return 0
    text = apply_changes(FACTS.read_text(encoding="utf-8"), changes, draft.stem)
    d, facts = temp_facts(text)
    with d:
        print(f"Impact of {len(changes)} fact change(s) in {draft.name}.")
        print("Passages in current canon that would still state the old value:\n")
        lint_canon.main(["--facts", str(facts)])
        print(f"\n{draft.name} itself, against the changed facts:\n")
        lint_canon.main(["--only", "--facts", str(facts), str(draft)])
    return 0


def cmd_apply(args) -> int:
    reg = register()
    entry = next((e for e in reg["requests"] if e["id"] == args.cr), None)
    if entry is None:
        raise FactError(f"{args.cr} is not in change_requests.json")
    if not approved(entry):
        raise FactError(f"{args.cr} has status {entry.get('status')!r}; only approved CRs are applied")
    changes = entry.get("facts", [])
    if not changes:
        print(f"{args.cr}: no fact changes in the register entry.")
        return 0
    text = apply_changes(FACTS.read_text(encoding="utf-8"), changes, args.cr)
    FACTS.write_text(text, encoding="utf-8")
    print(f"Updated canon_facts.toml with {len(changes)} fact change(s) from {args.cr}.")
    print("Passages that still state the old value (revise these, then rerun lint_canon.py):\n")
    lint_canon.main(["--facts", str(FACTS)])
    return 0


def cmd_check(args) -> int:
    facts = current_facts(FACTS.read_text(encoding="utf-8"))
    expected: dict[tuple[str, str, str], tuple[object, str]] = {}
    problems = []
    for entry in register()["requests"]:
        if not approved(entry):
            continue
        for change in entry.get("facts", []):
            for table in ("person", "event"):
                if table in change:
                    for key, value in change["set"].items():
                        expected[(table, change[table], key)] = (value, entry["id"])  # later CRs win
                if f"add_{table}" in change:
                    ident = change[f"add_{table}"]["id"]
                    if ident not in facts[table]:
                        problems.append(f"{entry['id']} adds {table} {ident}, missing from canon_facts.toml")
            if "add_forbidden" in change and change["add_forbidden"]["pattern"] not in facts["forbidden"]:
                problems.append(f"{entry['id']} adds a forbidden statement missing from canon_facts.toml")
    for (table, ident, key), (value, cr) in expected.items():
        now = facts[table].get(ident, {}).get(key)
        if now != value:
            problems.append(f"{cr} sets {ident}.{key} = {value!r}; canon_facts.toml has {now!r} "
                            f"(run: python3 book-agent/revision/cr_facts.py apply {cr})")
    for p in problems:
        print(p)
    if problems:
        print(f"\n{len(problems)} register fact change(s) not reflected in canon_facts.toml.")
        return 1
    n = sum(len(e.get("facts", [])) for e in register()["requests"] if approved(e))
    print(f"Register and facts file agree ({n} approved fact change(s)).")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Carry CR fact changes into canon_facts.toml")
    sub = ap.add_subparsers(dest="command", required=True)
    p = sub.add_parser("preview", help="impact list for a CR draft")
    p.add_argument("draft")
    a = sub.add_parser("apply", help="apply an approved CR's fact changes")
    a.add_argument("cr")
    sub.add_parser("check", help="CI: register and facts file agree")
    args = ap.parse_args(argv)
    try:
        return {"preview": cmd_preview, "apply": cmd_apply, "check": cmd_check}[args.command](args)
    except FactError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
