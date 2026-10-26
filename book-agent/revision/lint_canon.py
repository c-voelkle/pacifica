#!/usr/bin/env python3
"""Lint Pacifica prose against canon_facts.toml.

Checks, sentence by sentence:
  * deaths   — a stated death year/season/month for a person matches the facts
  * births   — a stated birth year matches the facts
  * ages     — "twenty-one-year-old X", "X, aged 21", "about forty in 1887"
               agree with the birth year (and the person is alive)
  * events   — key dated events are stated with their canonical year
  * IDs      — every CT-… identifier exists in character_registry.json
  * forbidden statements listed in the facts file

Usage:
  python3 book-agent/revision/lint_canon.py              # current canon files
  python3 book-agent/revision/lint_canon.py draft.md ... # also lint drafts
  python3 book-agent/revision/lint_canon.py --only draft.md

Exit status is 1 when any finding is reported. Standard library only.
A line containing `canon-lint: ignore` is skipped (use sparingly, with a reason).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
FACTS = BASE / "canon_facts.toml"
REGISTRY = BASE / "character_registry.json"
DEFAULT_FILES = [
    ROOT / "AGENTS.md",
    BASE / "master_storyline.md",
    BASE / "character_bible.md",
    REGISTRY,
]

SEASONS = ("spring", "summer", "autumn", "fall", "winter")
MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")
UNITS = ("zero one two three four five six seven eight nine ten eleven twelve "
         "thirteen fourteen fifteen sixteen seventeen eighteen nineteen").split()
TENS = "twenty thirty forty fifty sixty seventy eighty ninety".split()
NUMBER_WORD = r"(?:(?:%s)(?:-(?:%s))?|%s)" % ("|".join(TENS), "|".join(UNITS[1:10]),
                                             "|".join(UNITS))
NUMBER = r"(?:\d{1,3}|%s)" % NUMBER_WORD
YEAR = re.compile(r"(?<![\d–-])(1[789]\d\d)(?![\d])")
PRONOUN = re.compile(r"\b(?:she|he|her|his)\b", re.I)
DEATH_VERB = re.compile(r"\b(?:dies|died|death|dying)\b", re.I)
BIRTH_VERB = re.compile(r"\b(?:is born|was born|born)\b", re.I)
# change-log wording that states an old value on purpose
HISTORY = re.compile(r"\bfrom\b[^.;]{0,30}\b1[789]\d\d\s+to\b|\b(?:originally|previously|formerly|superseded|was once)\b", re.I)


def number_value(text: str) -> int | None:
    text = text.lower()
    if text.isdigit():
        return int(text)
    if text in UNITS:
        return UNITS.index(text)
    if "-" in text:
        tens, unit = text.split("-", 1)
        if tens in TENS and unit in UNITS:
            return (TENS.index(tens) + 2) * 10 + UNITS.index(unit)
    if text in TENS:
        return (TENS.index(text) + 2) * 10
    return None


@dataclass
class Person:
    id: str
    aliases: list[str]
    born: int | None = None
    born_approx: bool = False
    died: int | None = None
    died_season: str | None = None
    died_month: str | None = None
    pattern: re.Pattern = field(init=False)

    def __post_init__(self):
        alts = sorted((re.escape(a) for a in self.aliases), key=len, reverse=True)
        self.pattern = re.compile(r"(?<![\w-])(?:%s)(?![\w-])" % "|".join(alts))

    @property
    def label(self) -> str:
        return self.aliases[0]


@dataclass
class Finding:
    where: str
    check: str
    message: str
    text: str

    def __str__(self) -> str:
        snippet = re.sub(r"\s+", " ", self.text).strip()
        if len(snippet) > 160:
            snippet = snippet[:157] + "…"
        return f"{self.where}: [{self.check}] {self.message}\n    “{snippet}”"


def load_facts(path: Path):
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    people = [Person(**{k: v for k, v in p.items() if k != "source"})
              for p in data.get("person", [])]
    return people, data.get("event", []), data.get("forbidden", [])


def registry_ids() -> set[str]:
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {p["id"] for p in reg["people"]}


TITLES = {"The", "Lady", "Prince", "Princess", "King", "Queen", "Emperor", "Empress",
          "Captain", "Admiral", "General", "Sir", "Rev.", "Dr.", "Count", "Mr.", "Mrs.",
          "Elias's", "Silas’s", "Julian’s", "Victoria's"}


def registry_names() -> set[str]:
    """Personal names from the registry, used only to stop a pronoun or a
    bare noun from being attributed to the wrong configured person."""
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    names: set[str] = set()
    for person in reg["people"]:
        head = person["display_name"].split(",")[0]
        for part in head.split(" / "):
            words = [w for w in re.findall(r"[A-ZĀĒĪŌŪʻ][\wʻ'’.-]+", part) if w not in TITLES]
            if words:
                names.add(words[0].strip("'’."))
                names.add(" ".join(words).strip("'’."))
    return {n for n in names if len(n) > 2}


# ---------------------------------------------------------------------------
# Text units
# ---------------------------------------------------------------------------

def paragraphs(path: Path):
    """Yield (location, paragraph text, line offset) for a file."""
    if path.suffix == ".json":
        reg = json.loads(path.read_text(encoding="utf-8"))
        for person in reg.get("people", []):
            for key in ("narrative_profile", "legacy_conflicts"):
                value = person.get(key)
                values = value if isinstance(value, list) else [value]
                for i, text in enumerate(v for v in values if isinstance(v, str)):
                    for para in text.split("\n\n"):
                        yield f"{path.name}:{person['id']}.{key}", para, None, person["id"]
        return
    lines = path.read_text(encoding="utf-8").splitlines()
    buf: list[str] = []
    start = 0
    in_comment = False
    dossier = None
    for n, line in enumerate(lines + [""], 1):
        head = re.match(r"^(?:### |\*\*)(CT-[A-Z0-9-]+) — ", line)
        if head or line.startswith("#"):
            if buf:
                yield f"{path}", "\n".join(buf), start, dossier
                buf = []
            dossier = head.group(1) if head else (None if line.startswith("## ") or line.startswith("# ") else dossier)
        if "<!--" in line and "-->" not in line:
            in_comment = True
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if line.strip() and not line.lstrip().startswith("#"):
            if not buf:
                start = n
            buf.append(line)
        else:
            if buf:
                yield f"{path}", "\n".join(buf), start, dossier
            buf = []


SENTENCE_SPLIT = re.compile(r"(?<=[.;!?])\s+(?=[A-Z“\"*(\[])")


def sentences(para: str):
    for s in SENTENCE_SPLIT.split(para):
        if "canon-lint: ignore" not in s:
            yield s


def line_of(para: str, offset: int | None, fragment: str) -> int | None:
    if offset is None:
        return None
    idx = para.find(fragment[:40])
    return offset + (para[:idx].count("\n") if idx >= 0 else 0)


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

class Linter:
    def __init__(self, people, events, forbidden, ids, names=()):
        self.people = people
        by_id = {p.id: p for p in people}
        for e in events:
            if "year_from" in e:
                pid, attr = e["year_from"].rsplit(".", 1)
                e["year"] = getattr(by_id[pid], attr)
        self.events = [(e, [re.compile(p) for p in e["patterns"]]) for e in events]
        configured = {a for p in people for a in p.aliases}
        others = sorted((re.escape(n) for n in names if n not in configured), key=len, reverse=True)
        self.others = re.compile(r"(?<![\w-])(?:%s)(?![\w-])" % "|".join(others)) if others else None
        self.forbidden = [(re.compile(f["pattern"], re.I), f["message"]) for f in forbidden]
        self.ids = ids
        self.findings: list[Finding] = []

    def report(self, loc, para, offset, sentence, check, message):
        line = line_of(para, offset, sentence)
        where = f"{loc}:{line}" if line else loc
        self.findings.append(Finding(where, check, message, sentence))

    # --- person resolution -------------------------------------------------
    POSSESSIVE = re.compile(r"^['’]s\b")

    def names_in(self, text: str, end: int, allow_possessive: bool):
        """(position, Person-or-None) for every name before `end`; None marks
        a registry name that is not configured in the facts file."""
        hits = []
        for person in self.people:
            for m in person.pattern.finditer(text, 0, end):
                if not allow_possessive and self.POSSESSIVE.match(text[m.end():m.end() + 2]):
                    continue
                hits.append((m.start(), m.end(), person))
        if self.others:
            for m in self.others.finditer(text, 0, end):
                if not any(s <= m.start() < e for s, e, _ in hits):
                    hits.append((m.start(), m.end(), None))
        return sorted(hits, key=lambda h: h[0])

    def subject_before(self, text: str, pos: int, allow_possessive: bool = False) -> Person | None:
        hits = self.names_in(text, pos, allow_possessive)
        return hits[-1][2] if hits else None

    def subject_of_verb(self, para: str, sent: str, verb: re.Match,
                        prev: str = "", dossier: str | None = None) -> Person | None:
        """The person a birth/death statement is about: a name ending within
        five words before the verb (a possessive counts only for the noun
        'death'), or a pronoun there resolved to the nearest named person."""
        noun = verb.group(0).lower() == "death"
        before = sent[:verb.start()]
        tail_words = before.split()[-5:]
        tail = " ".join(tail_words)
        tail_start = len(before) - len(before.rstrip()) and 0
        tail_pos = before.rfind(tail) if tail else len(before)
        all_hits = self.names_in(sent, verb.start(), allow_possessive=noun)
        hits = [h for h in all_hits if h[1] >= tail_pos]
        # "contested autumn 1888 death": a year right before the noun ties it to
        # the sentence's nearest name, however far back
        pre_year = noun and re.search(r"(1[789]\d\d)\s+(?:\w+\s+)?$", before)
        if not hits and pre_year and all_hits:
            return all_hits[-1][2]
        if not hits and pre_year and dossier:
            return next((p for p in self.people if p.id == dossier), None)
        if hits:
            # a later clause boundary between the name and the verb breaks the link
            s, e, person = hits[-1]
            between = sent[e:verb.start()]
            if re.search(r"[,;:]|\b(?:and|while|after|before|when)\b", between) and not noun:
                return None
            return person
        pron = list(re.finditer(r"\b(?:she|he|her|his)\b", tail, re.I))
        if pron:
            sent_pos = max(para.find(sent), 0)
            hits = self.names_in(para, sent_pos + tail_pos + pron[-1].start(), allow_possessive=False)
            if hits:
                return hits[-1][2]
            if dossier:
                return next((p for p in self.people if p.id == dossier), None)
            prev_hits = self.names_in(prev, len(prev), allow_possessive=False)
            return prev_hits[-1][2] if prev_hits else None
        if noun and dossier and not all_hits:
            # "birth 1886, adoption 1886, death autumn 1888" inside a dossier
            return next((p for p in self.people if p.id == dossier), None)
        return None

    @staticmethod
    def year_near(sent: str, verb: re.Match) -> tuple[int | None, str]:
        """Year stated for the verb: within the five words before it (as in
        'her 1888 death') or the first year after it in the sentence."""
        before = sent[max(0, verb.start() - 30):verb.start()]
        m = list(YEAR.finditer(before))
        if m and len(before[m[-1].end():].split()) <= 3:
            return int(m[-1].group(1)), before[m[-1].start() - 15 if m[-1].start() > 15 else 0:]
        after = sent[verb.end():verb.end() + 60]
        m2 = YEAR.search(after)
        if m2:
            gap = after[:m2.start()]
            if (re.search(r"[,;]|\b(?:and|but|while|after|before|when|which|who)\b", gap)
                    or DEATH_VERB.search(gap) or BIRTH_VERB.search(gap)
                    or re.search(r"\b[A-Z][a-zʻ]+(?:'s|’s)?\b", gap)
                    and not re.search(r"\b(?:%s)\b" % "|".join(MONTHS), gap)):
                return None, ""
            return int(m2.group(1)), after[:m2.end()]
        return None, ""

    def check_life_dates(self, loc, para, offset, prev="", dossier=None):
        for sent in sentences(para):
            if HISTORY.search(sent):
                continue
            for verb in DEATH_VERB.finditer(sent):
                person = self.subject_of_verb(para, sent, verb, prev, dossier)
                if not person or person.died is None:
                    continue
                year, span = self.year_near(sent, verb)
                if year is None:
                    continue
                if year != person.died:
                    self.report(loc, para, offset, sent, "death",
                                f"{person.label} dies in {person.died}, not {year}")
                    continue
                seasons = [s for s in SEASONS if re.search(rf"\b{s}\b", span, re.I)]
                if person.died_season and seasons and person.died_season not in seasons:
                    self.report(loc, para, offset, sent, "death",
                                f"{person.label} dies in {person.died_season} {person.died}, not {seasons[0]}")
                months = [mo for mo in MONTHS if re.search(rf"\b{mo}\b", span)]
                if person.died_month and months and person.died_month not in months:
                    self.report(loc, para, offset, sent, "death",
                                f"{person.label} dies in {person.died_month} {person.died}, not {months[0]}")
            for verb in BIRTH_VERB.finditer(sent):
                person = self.subject_of_verb(para, sent, verb, prev, dossier)
                if not person or person.born is None:
                    continue
                year, _ = self.year_near(sent, verb)
                if year is None:
                    continue
                tol = 2 if person.born_approx else 0
                if abs(year - person.born) > tol:
                    self.report(loc, para, offset, sent, "birth",
                                f"{person.label} is born in {'c.' if person.born_approx else ''}{person.born}, not {year}")

    AGE_PATTERNS = [
        # twenty-one-year-old Jani / the 24-year-old physician
        re.compile(rf"\b(?P<age>{NUMBER})-year-old\b", re.I),
        # Julian, aged twenty-one / at the age of 21
        re.compile(rf"\b(?:aged|at the age of|age)\s+(?P<age>{NUMBER})\b", re.I),
        # about forty in 1887
        re.compile(rf"\b(?:about|around|nearly|almost)\s+(?P<age>{NUMBER})\s+in\s+(?P<year>1[789]\d\d)\b", re.I),
    ]

    def check_ages(self, loc, para, offset, dossier=None):
        sent_start = 0
        for sent in sentences(para):
            sent_start = para.find(sent, sent_start)
            for pattern in self.AGE_PATTERNS:
                for m in pattern.finditer(sent):
                    age = number_value(m.group("age"))
                    if age is None or age > 110:
                        continue
                    # person: name right after "N-year-old", else nearest before
                    after = sent[m.end():m.end() + 40]
                    person = None
                    for p in self.people:
                        pm = p.pattern.match(after.lstrip())
                        if pm:
                            person = p
                            break
                    if person is None:
                        if re.match(r"\s*[A-Z]", after) and not re.match(r"\s*(?:physician|man|woman)", after):
                            continue  # names someone not in the facts file
                        prev_start = para.rfind(".", 0, max(sent_start - 2, 0)) + 1
                        hits = self.names_in(para, sent_start + m.start(), allow_possessive=False)
                        hits = [h for h in hits if h[0] >= prev_start]
                        if dossier and not any(h[0] >= sent_start for h in hits):
                            # unnamed age inside a dossier belongs to that dossier's person
                            person = next((p for p in self.people if p.id == dossier), None)
                            if person is None:
                                continue
                        else:
                            person = hits[-1][2] if hits else None
                    if not person or person.born is None:
                        continue
                    # year: explicit, else in the sentence, else earlier in the paragraph
                    year = int(m.group("year")) if "year" in m.groupdict() and m.group("year") else None
                    if year is None:
                        ys = [int(y.group(1)) for y in YEAR.finditer(sent)]
                        if ys:
                            year = min(ys, key=lambda y: abs(sent.find(str(y)) - m.start()))
                    if year is None:
                        earlier = list(YEAR.finditer(para[:sent_start]))
                        if earlier:
                            year = int(earlier[-1].group(1))
                    if year is None:
                        continue
                    if person.died is not None and year > person.died:
                        continue  # retrospective or a different person; not an age claim
                    expected = year - person.born
                    tol = 3 if person.born_approx else 1
                    if not (expected - tol <= age <= expected + (1 if person.born_approx else 0)):
                        lo = expected - tol
                        self.report(loc, para, offset, sent, "age",
                                    f"{person.label} (born {'c.' if person.born_approx else ''}{person.born}) "
                                    f"is about {lo}–{expected} in {year}, not {age}")

    def check_events(self, loc, para, offset):
        for sent in sentences(para):
            if HISTORY.search(sent):
                continue
            for ev, patterns in self.events:
                for pattern in patterns:
                    for m in pattern.finditer(sent):
                        year = int(m.group("year"))
                        if year != ev["year"]:
                            self.report(loc, para, offset, sent, "event",
                                        f"{ev['id']}: canon year is {ev['year']}, not {year}")

    def check_structured(self, path: Path):
        """**Born:** / **Died:** lines in each dossier, checked against the
        dossier's own ID rather than by name resolution."""
        by_id = {p.id: p for p in self.people}
        if path.suffix == ".json":
            reg = json.loads(path.read_text(encoding="utf-8"))
            units = [(f"{path.name}:{p['id']}.narrative_profile", p["id"], p.get("narrative_profile") or "", None)
                     for p in reg["people"]]
        else:
            text = path.read_text(encoding="utf-8")
            heads = list(re.finditer(r"^(?:### |\*\*)(CT-[A-Z0-9-]+) — ", text, re.M))
            units = []
            for i, h in enumerate(heads):
                end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
                units.append((str(path), h.group(1), text[h.start():end], text[:h.start()].count("\n") + 1))
        for loc, cid, body, line0 in units:
            person = by_id.get(cid)
            if not person:
                continue
            for field_name, value in (("Born", person.born), ("Died", person.died)):
                m = re.search(r"\*\*%s:\*\*\s*([^\n]*)" % field_name, body)
                if not m or value is None:
                    continue
                stated = m.group(1)
                years = [int(y) for y in YEAR.findall(stated.split(";")[0])]
                if not years:
                    continue
                tol = 2 if field_name == "Born" and person.born_approx else 0
                where = f"{loc}:{line0 + body[:m.start()].count(chr(10))}" if line0 else loc
                if all(abs(y - value) > tol for y in years):
                    self.findings.append(Finding(where, field_name.lower(),
                                                 f"{person.label}: facts say {value}, dossier says {years[0]}", m.group(0)))
                elif field_name == "Died" and person.died_season:
                    seasons = [s for s in SEASONS if re.search(rf"\b{s}\b", stated, re.I)]
                    if seasons and person.died_season not in seasons:
                        self.findings.append(Finding(where, "died",
                                                     f"{person.label}: facts say {person.died_season}, dossier says {seasons[0]}", m.group(0)))

    def check_ids(self, loc, para, offset):
        for m in re.finditer(r"\bCT-[A-Z0-9]+(?:-[A-Z0-9]+)*\b", para):
            if m.group(0) not in self.ids:
                self.report(loc, para, offset, para[max(0, m.start() - 40):m.end() + 40],
                            "id", f"unknown character ID {m.group(0)} (not in character_registry.json)")

    def check_forbidden(self, loc, para, offset):
        for sent in sentences(para):
            for pattern, message in self.forbidden:
                if pattern.search(sent):
                    self.report(loc, para, offset, sent, "forbidden", message)

    def lint(self, path: Path):
        if path.name in ("character_bible.md", "character_registry.json"):
            self.check_structured(path)
        prev = ""
        for loc, para, offset, dossier in paragraphs(path):
            self.check_life_dates(loc, para, offset, prev, dossier)
            if not loc.endswith(".legacy_conflicts"):  # these quote superseded sources on purpose
                self.check_ages(loc, para, offset, dossier)
            self.check_events(loc, para, offset)
            self.check_ids(loc, para, offset)
            self.check_forbidden(loc, para, offset)
            prev = para


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="*", type=Path, help="extra files (drafts) to lint")
    ap.add_argument("--only", action="store_true", help="lint only the given files, not current canon")
    ap.add_argument("--facts", type=Path, default=FACTS)
    args = ap.parse_args(argv)

    people, events, forbidden = load_facts(args.facts)
    linter = Linter(people, events, forbidden, registry_ids(), registry_names())
    targets = list(args.files) if args.only else DEFAULT_FILES + list(args.files)
    for path in targets:
        if not path.exists():
            print(f"{path}: file not found", file=sys.stderr)
            return 2
        linter.lint(path)

    try:
        rel = lambda w: w.replace(str(ROOT) + "/", "")
    except Exception:  # pragma: no cover
        rel = lambda w: w
    for f in linter.findings:
        f.where = rel(f.where)
        print(f)
    n = len(linter.findings)
    print(f"\n{n} finding{'s' if n != 1 else ''} in {len(targets)} file{'s' if len(targets) != 1 else ''}."
          if n else f"Canon lint clean: {len(targets)} file{'s' if len(targets) != 1 else ''} checked.")
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
