#!/usr/bin/env python3
"""Validate Pacifica's canonical character bible against structured identities
and all 250 unmodified legacy profiles.

Usage: python3 book-agent/revision/validate_character_docs.py
No external dependencies and no generation or rewriting of manuscript prose.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
LEGACY = BASE.parent / "character_bible.json"
BIBLE = BASE / "character_bible.md"
REGISTRY = BASE / "character_registry.json"
CROSSWALK = BASE / "legacy_character_crosswalk.json"

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def check() -> list[str]:
    errors: list[str] = []
    legacy = read_json(LEGACY)["characters"]
    registry = read_json(REGISTRY)
    crosswalk = read_json(CROSSWALK)["legacy_profiles"]
    bible = BIBLE.read_text(encoding="utf-8")
    entries = registry["people"]
    ids = [p["id"] for p in entries]
    id_set = set(ids)
    if len(id_set) != len(ids):
        errors.append("Duplicate canonical character IDs")
    if not all(re.fullmatch(r"CT-[A-Z0-9-]+", name) for name in ids):
        errors.append("Malformed canonical character ID")

    headings = re.findall(r"^### (CT-[A-Z0-9-]+) — ", bible, re.M)
    inline = re.findall(r"^\*\*(CT-[A-Z0-9-]+) — ", bible, re.M)
    declared = headings + inline
    if len(set(declared)) != len(declared):
        errors.append("Some IDs are defined multiple times in character_bible.md")
    if set(declared) != id_set:
        errors.append(
            "Registry/bible mismatch — only in registry: "
            + ", ".join(sorted(id_set - set(declared)))
            + "; only in bible: "
            + ", ".join(sorted(set(declared) - id_set))
        )

    # The prose bible is the authored source; registry copies of the profiles
    # must be refreshed whenever a character's narrative dossier is revised.
    starts = []
    for match in re.finditer(
        r"^### (CT-[A-Z0-9-]+) — [^\n]+$|^\*\*(CT-[A-Z0-9-]+) — [^\n]+?\*\*",
        bible, re.M,
    ):
        starts.append((match.start(), match.group(1) or match.group(2),
                       "dossier" if match.group(1) else "short_profile"))
    breaks = sorted(m.start() for m in re.finditer(
        r"^## |^### |^\*\*CT-[A-Z0-9-]+ — ", bible, re.M
    ))
    expected_profiles = {}
    for pos, cid, kind in starts:
        after = next((q for q in breaks if q > pos), len(bible))
        chunk = bible[pos:after].strip()
        if kind == "dossier":
            chunk = chunk.split("\n", 1)[1].strip()
        else:
            chunk = re.sub(r"^\*\*CT-[A-Z0-9-]+ — [^\n]+?\*\*\s*", "", chunk)
        expected_profiles[cid] = chunk
    for person in entries:
        expected_profile = expected_profiles.get(person["id"])
        if expected_profile is not None and person.get("narrative_profile") != expected_profile:
            errors.append(f"Registry profile out of sync with character bible: {person['id']}")

    for person in entries:
        for link in person.get("links", []):
            if link["to"] not in id_set:
                errors.append(
                    f"Unresolved relationship: {person['id']} to {link['to']}"
                )
        for ix in person.get("legacy_profile_indices", []):
            if not 1 <= ix <= len(legacy):
                errors.append(f"Legacy index out of range: {person['id']} #{ix}")

    expected_indices = list(range(1, len(legacy) + 1))
    actual_indices = [p["legacy_profile_index"] for p in crosswalk]
    if len(crosswalk) != len(legacy) or sorted(actual_indices) != expected_indices:
        errors.append("Legacy crosswalk must contain all original profiles once")
    matching = {
        ix: person["id"]
        for person in entries
        for ix in person.get("legacy_profile_indices", [])
    }
    if len(matching) != sum(len(p.get("legacy_profile_indices", [])) for p in entries):
        errors.append("A legacy profile is assigned to more than one canonical ID")

    for profile in crosswalk:
        ix = profile["legacy_profile_index"]
        if not 1 <= ix <= len(legacy):
            continue
        if profile["legacy_name"] != legacy[ix-1]["name"]:
            errors.append(f"Legacy profile name mismatch at #{ix}")
        assigned = matching.get(ix)
        if profile["canonical_id"] != assigned:
            errors.append(f"Canonical mapping mismatch at legacy #{ix}")
        if not assigned and profile["disposition"] != "legacy_secondary_not_yet_assigned":
            errors.append(f"Unmapped legacy profile incorrectly marked canonical #{ix}")

    # Approved revisions must never be mistaken for the original life histories.
    by_id = {p["id"]: p for p in entries}
    expected = [
        "CT-ELIAS","CT-KAIULANI","CT-JULIAN","CT-JULIAN-MOTHER",
        "CT-LOST-SON","CT-MARCUS-I","CT-SOBERANES","CT-MARCUS-III",
        "CT-KALANIMOKU-EMPEROR","CT-CHRONICLER"
    ]
    for k in expected:
        if k not in by_id:
            errors.append(f"Missing essential canonical character {k}")
    if "1931" not in by_id.get("CT-JULIAN", {}).get("narrative_profile", ""):
        errors.append("Julian's revised late chronology is not documented")
    if "1858" not in by_id.get("CT-II", {}).get("narrative_profile", ""):
        errors.append("Japanese character chronology must refer to 1858 Edo")

    return errors

if __name__ == "__main__":
    problems = check()
    if problems:
        print("CHARACTER DOCUMENTATION CHECK FAILED")
        for problem in problems:
            print("- " + problem)
        sys.exit(1)
    print("Character documents valid: all canonical IDs, links and 250 legacy profiles agree.")
