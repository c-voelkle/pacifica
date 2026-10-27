"""Pacifica commitments ledger: political obligations kept like a debt register.

Every treaty, compact, lease, loan, guarantee, charter and life office in the
canon, with who owes what to whom, from when, until when, when it renews, what
ends it and who can refuse. Each entry quotes the storyline verbatim, so the
ledger records canon and never invents it.

  python3 commitments/ledger.py check                 # validate against the storyline and canon facts
  python3 commitments/ledger.py at 1928 [--party JP]  # what is in force in a year
  python3 commitments/ledger.py schedule 1887 1932    # starts, expiries, renewals and lapses by year
  python3 commitments/ledger.py if-dies CT-ELIAS      # what lapses or changes hands at a death
  python3 commitments/ledger.py report                # writes commitments/outputs/ledger.md

Data: commitments/data/ledger.toml (format at the top of that file).
"""
from __future__ import annotations

import argparse
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = HERE / "data"
STORY = ROOT / "book-agent" / "revision" / "master_storyline.md"
FACTS = ROOT / "book-agent" / "revision" / "canon_facts.toml"
OUT = HERE / "outputs"

KINDS = {"treaty", "convention", "compact", "lease", "loan", "guarantee", "office", "charter",
         "law", "constitution", "pact", "concession", "settlement", "alliance"}
STATUSES = {"CANON", "APPROVED", "PROPOSED", "OPEN", "MODEL"}
LABEL = re.compile(r"\*\*\[(APPROVED|PROPOSED|OPEN|MODEL)[^\]]*\]\*\*")
HORIZON = 1932


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def norm(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


@dataclass
class Story:
    lines: list[str]

    @classmethod
    def load(cls, path: Path = STORY) -> "Story":
        return cls(path.read_text(encoding="utf-8").splitlines())

    def find(self, quote: str) -> list[int]:
        """1-based line numbers of the paragraphs (lines) that contain the quote."""
        q = norm(quote)
        return [i + 1 for i, line in enumerate(self.lines) if q in norm(line)]

    def section(self, lineno: int) -> int | None:
        for i in range(lineno - 1, -1, -1):
            m = re.match(r"## (\d+)\.", self.lines[i])
            if m:
                return int(m.group(1))
            if self.lines[i].startswith("# Explicitly unresolved"):
                return None
        return None

    def label_at(self, lineno: int, quote: str) -> str:
        """The canon label in force at the quote: the last label before it in the same
        paragraph, or CANON when the paragraph has none before it."""
        line = norm(self.lines[lineno - 1])
        pos = line.find(norm(quote))
        found = "CANON"
        for m in LABEL.finditer(line):
            if m.start() < pos:
                found = m.group(1)
        return found


def load_ledger(path: Path = DATA / "ledger.toml") -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)


def load_people() -> dict[str, dict]:
    with open(FACTS, "rb") as f:
        facts = tomllib.load(f)
    people = {p["id"]: {"name": p["aliases"][0], "died": p.get("died")} for p in facts.get("person", [])}
    return people


def people_index(ledger: dict) -> dict[str, dict]:
    people = load_people()
    for p in ledger.get("person", []):
        people.setdefault(p["id"], {"name": p["name"], "died": p.get("died")})
    return people


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def check(ledger: dict, story: Story | None = None) -> list[str]:
    story = story or Story.load()
    errors: list[str] = []
    parties = {p["id"] for p in ledger.get("party", [])}
    people = people_index(ledger)

    for p in ledger.get("person", []):
        if "quote" in p and not story.find(p["quote"]):
            errors.append(f"person {p['id']}: quote not found in the storyline: {p['quote'][:70]!r}")

    seen: set[str] = set()
    for c in ledger.get("commitment", []):
        cid = c.get("id", "?")
        where = f"{cid}"
        if cid in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(cid)
        for key in ("id", "name", "kind", "parties", "from", "status", "quote", "section"):
            if key not in c:
                errors.append(f"{where}: missing '{key}'")
        if c.get("kind") not in KINDS:
            errors.append(f"{where}: unknown kind {c.get('kind')!r}")
        if c.get("status") not in STATUSES:
            errors.append(f"{where}: unknown status {c.get('status')!r}")
        for p in c.get("parties", []):
            if p not in parties:
                errors.append(f"{where}: undeclared party {p!r}")
        for o in c.get("owes", []):
            for k in ("by", "to"):
                if o.get(k) not in parties:
                    errors.append(f"{where}: owes.{k} {o.get(k)!r} is not a declared party")
            if "what" not in o:
                errors.append(f"{where}: owes entry without 'what'")
        for e in c.get("can_end", []):
            if e.get("who") not in parties and e.get("who") not in people:
                errors.append(f"{where}: can_end.who {e.get('who')!r} is neither a party nor a person")
        start, until = c.get("from"), c.get("until")
        if until is not None and start is not None and until < start:
            errors.append(f"{where}: until {until} is before from {start}")
        if c.get("term_years") and until is not None and start is not None and until - start != c["term_years"]:
            errors.append(f"{where}: term_years {c['term_years']} ≠ until − from ({until - start})")
        for y in c.get("renewals", []):
            if start is not None and y < start:
                errors.append(f"{where}: renewal {y} before from {start}")
            if until is not None and y > until:
                errors.append(f"{where}: renewal {y} after until {until}")
        for who in c.get("lapses_on_death", []) + ([c["holder"]] if "holder" in c else []):
            if who not in people:
                errors.append(f"{where}: person {who!r} not in canon_facts.toml or the ledger's [[person]] list")
        for who in c.get("lapses_on_death", []):
            d = people.get(who, {}).get("died")
            if d is not None and start is not None and d < start:
                errors.append(f"{where}: lapses on the death of {who}, who died in {d}, before it starts")
        # the quote anchors the entry in canon
        quotes = [c["quote"]] if "quote" in c else []
        quotes += c.get("more_quotes", [])
        for i, q in enumerate(quotes):
            hits = story.find(q)
            if not hits:
                errors.append(f"{where}: quote not found in the storyline: {q[:70]!r}")
                continue
            if i == 0:
                sec = story.section(hits[0])
                if c.get("section") is not None and sec != c["section"]:
                    errors.append(f"{where}: quote is in §{sec}, entry says §{c['section']}")
                label = story.label_at(hits[0], q)
                if label != c.get("status") and not c.get("label_note"):
                    errors.append(f"{where}: storyline label at the quote is {label}, entry says {c.get('status')} "
                                  f"(add label_note if the label's scope is misleading)")
    return errors


# ---------------------------------------------------------------------------
# Queries
# ---------------------------------------------------------------------------

def lapse_year(c: dict, people: dict) -> int | None:
    years = [people[w]["died"] for w in c.get("lapses_on_death", []) if people.get(w, {}).get("died")]
    return min(years) if years else None


def end_year(c: dict, people: dict) -> int | None:
    """Last year in which the commitment is in force, or None if open-ended."""
    cands = [y for y in (c.get("until"), c.get("ended"), lapse_year(c, people)) if y is not None]
    return min(cands) if cands else None


def in_force(c: dict, year: int, people: dict) -> bool:
    e = end_year(c, people)
    return c["from"] <= year and (e is None or year <= e)


def at(ledger: dict, year: int, party: str | None = None) -> list[dict]:
    people = people_index(ledger)
    return [c for c in ledger["commitment"]
            if in_force(c, year, people) and (party is None or party in c["parties"])]


def schedule(ledger: dict, y0: int, y1: int) -> dict[int, list[str]]:
    people = people_index(ledger)
    ev: dict[int, list[str]] = {}

    def add(y: int | None, text: str) -> None:
        if y is not None and y0 <= y <= y1:
            ev.setdefault(y, []).append(text)

    for c in ledger["commitment"]:
        tag = f"{c['name']} [{c['status']}]"
        add(c["from"], f"starts: {tag}")
        for y in c.get("renewals", []):
            add(y, f"renewal or review: {tag}")
        if c.get("until") is not None:
            add(c["until"], f"term ends: {tag}")
        if c.get("ended") is not None:
            add(c["ended"], f"ended: {tag}" + (f" — {c['ended_by']}" if c.get("ended_by") else ""))
        ly = lapse_year(c, people)
        if ly is not None:
            who = ", ".join(people[w]["name"] for w in c["lapses_on_death"])
            add(ly, f"lapses on the death of {who}: {tag}")
    return dict(sorted(ev.items()))


def if_dies(ledger: dict, person: str, year: int | None = None) -> dict[str, list[dict]]:
    people = people_index(ledger)
    year = year or people.get(person, {}).get("died")
    out: dict[str, list[dict]] = {"lapse": [], "holds": []}
    for c in ledger["commitment"]:
        if year is not None and not in_force(c, year, people):
            continue
        if person in c.get("lapses_on_death", []):
            out["lapse"].append(c)
        elif c.get("holder") == person:
            out["holds"].append(c)
    return out


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def describe(c: dict) -> str:
    owes = "; ".join(f"{o['by']} → {o['to']}: {o['what']}" for o in c.get("owes", []))
    ends = "; ".join(f"{e['who']}: {e['how']}" for e in c.get("can_end", []))
    span = f"{'c.' if c.get('from_approx') else ''}{c['from']}–{c.get('until') or c.get('ended') or ''}"
    parts = [f"**{c['name']}** ({c['kind']}, {span}, §{c['section']}, {c['status']}"
             + (f", {c['cr']}" if c.get("cr") else "") + ")"]
    if owes:
        parts.append(f"owes: {owes}")
    if c.get("secured_on"):
        parts.append(f"secured on: {c['secured_on']}")
    if c.get("renewals"):
        parts.append("renewals: " + ", ".join(map(str, c["renewals"])))
    if ends:
        parts.append(f"can end or refuse: {ends}")
    return " — ".join(parts)


def report(ledger: dict) -> str:
    people = people_index(ledger)
    parties = {p["id"]: p["name"] for p in ledger["party"]}
    cs = ledger["commitment"]
    L = ["# Pacifica commitments ledger", "",
         f"Generated by `commitments/ledger.py report` from `data/ledger.toml`: {len(cs)} commitments, "
         f"{len(parties)} parties. Each entry quotes the storyline; `ledger.py check` confirms every quote and its label. "
         "Status is the storyline's own label at the quote (CANON = unlabelled base text).", "",
         "## Maturity schedule", "",
         "Starts, scheduled renewals and reviews, term ends, endings and lapses at a death.", ""]
    for y, items in schedule(ledger, 1840, HORIZON + 10).items():
        L.append(f"- **{y}:** " + "; ".join(items))
    L += ["", "## In force at key dates", ""]
    for y in (1856, 1867, 1874, 1887, 1895, 1907, 1915, 1922, 1928, 1932):
        names = [f"{c['name']} [{c['status']}]" for c in at(ledger, y)]
        L.append(f"- **{y}** ({len(names)}): " + "; ".join(names))
    L += ["", "## Who can refuse or end what", ""]
    holders: dict[str, list[str]] = {}
    for c in cs:
        for e in c.get("can_end", []):
            holders.setdefault(e["who"], []).append(f"{c['name']} ({e['how']})")
    for who in sorted(holders):
        label = parties.get(who) or people.get(who, {}).get("name", who)
        L.append(f"- **{label}:** " + "; ".join(holders[who]))
    L += ["", "## By party", ""]
    for pid, pname in parties.items():
        mine = [c for c in cs if pid in c["parties"]]
        if mine:
            L.append(f"### {pname}")
            L.append("")
            for c in sorted(mine, key=lambda c: c["from"]):
                L.append(f"- {describe(c)}")
            L.append("")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    a = sub.add_parser("at"); a.add_argument("year", type=int); a.add_argument("--party")
    s = sub.add_parser("schedule"); s.add_argument("y0", type=int); s.add_argument("y1", type=int)
    d = sub.add_parser("if-dies"); d.add_argument("person"); d.add_argument("--year", type=int)
    sub.add_parser("report")
    p = sub.add_parser("check-file"); p.add_argument("path")
    args = ap.parse_args(argv)

    if args.cmd in ("check", "check-file"):
        ledger = load_ledger()
        if args.cmd == "check-file":       # a part file, checked with the main ledger's parties and people
            part = load_ledger(Path(args.path))
            for key in ("party", "person"):
                ledger[key] = ledger.get(key, []) + part.get(key, [])
            ledger["commitment"] = part.get("commitment", [])
        errs = check(ledger)
        for e in errs:
            print(e)
        print(f"{len(ledger.get('commitment', []))} commitments checked, {len(errs)} problem(s).")
        return 1 if errs else 0
    ledger = load_ledger()
    if args.cmd == "at":
        for c in at(ledger, args.year, args.party):
            print("- " + describe(c))
    elif args.cmd == "schedule":
        for y, items in schedule(ledger, args.y0, args.y1).items():
            print(f"{y}: " + "; ".join(items))
    elif args.cmd == "if-dies":
        r = if_dies(ledger, args.person, args.year)
        print("Lapses:")
        for c in r["lapse"]:
            print("- " + describe(c))
        print("Held by this person (passes on by its own rules):")
        for c in r["holds"]:
            print("- " + describe(c))
    elif args.cmd == "report":
        OUT.mkdir(exist_ok=True)
        text = report(ledger)
        (OUT / "ledger.md").write_text(text, encoding="utf-8")
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
