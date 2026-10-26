#!/usr/bin/env python3
"""Pacifica session start and end checks.

    python3 tools/session.py start [--topic WORD]   # at the beginning of a session
    python3 tools/session.py end                     # before finishing

`start` confirms the work begins from current canon: branch and sync state,
unmerged or stale branches, the canonical checks, and where the last session
left off. It saves a snapshot to `.session/start.json` (not committed).

`end` compares against that snapshot and lists anything left behind: canon
changed without a CR, facts or synchronization;
failing checks; uncommitted or unpushed work; a session record without its
"Resume here" lines.

Both commands only report. They never edit, commit, push or delete. Each runs
in a few seconds with the standard library and git. Exit status is 0 unless
`--strict` is given and something needs attention.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REV = ROOT / "book-agent" / "revision"
STATE = ROOT / ".session" / "start.json"
CANON = [
    "AGENTS.md",
    "book-agent/revision/master_storyline.md",
    "book-agent/revision/change_requests.json",
    "book-agent/revision/character_bible.md",
    "book-agent/revision/character_registry.json",
    "book-agent/revision/historical_background.md",
    "book-agent/revision/canon_facts.toml",
]
CHECKS = [
    ("canon lint", [sys.executable, "book-agent/revision/lint_canon.py"]),
    ("CR facts in register", [sys.executable, "book-agent/revision/cr_facts.py", "check"]),
    ("storyline sync", [sys.executable, "book-agent/revision/sync_master_storyline.py", "--check"]),
    ("character docs", [sys.executable, "book-agent/revision/validate_character_docs.py"]),
]

attention: list[str] = []


def git(*args: str, check: bool = False) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError(r.stderr.strip())
    return r.stdout.rstrip("\n") if r.returncode == 0 else ""


def sha_lf(rel: str, basis: str = "LFNormalizedText") -> str | None:
    path = ROOT / rel
    if not path.exists():
        return None
    data = path.read_bytes()
    if basis != "ExactBytes":
        data = data.replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def say(symbol: str, text: str, needs_attention: bool = False) -> None:
    print(f"  {symbol} {text}")
    if needs_attention:
        attention.append(text)


def head(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------

def branch_state(fetch: bool) -> dict:
    if fetch:
        subprocess.run(["git", "fetch", "-q", "--prune", "origin"], cwd=ROOT,
                       capture_output=True, text=True, timeout=120)
    branch = git("branch", "--show-current") or "(detached)"
    sha = git("rev-parse", "HEAD")
    head("Branch")
    say("·", f"on {branch} at {sha[:7]}")
    behind = git("rev-list", "--count", "HEAD..origin/main")
    ahead_main = git("rev-list", "--count", "origin/main..HEAD")
    if behind and int(behind):
        say("!", f"{behind} commit(s) behind origin/main — rebase or merge main before editing canon", True)
    else:
        say("✓", "up to date with origin/main")
    if branch == "main" and ahead_main and int(ahead_main):
        say("!", f"{ahead_main} local commit(s) on main — canon work belongs on a review branch", True)
    dirty = [l for l in git("status", "--porcelain").splitlines() if not l.endswith(".session/")]
    if dirty:
        say("!", f"{len(dirty)} uncommitted change(s): " + ", ".join(l[3:] for l in dirty[:5])
            + (" …" if len(dirty) > 5 else ""), True)
    return {"branch": branch, "sha": sha}


def other_branches() -> None:
    head("Other branches on origin")
    refs = [r for r in git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin").splitlines()
            if r not in ("origin", "origin/HEAD", "origin/main")]
    merged, open_ = [], []
    for ref in refs:
        is_merged = subprocess.run(["git", "merge-base", "--is-ancestor", ref, "origin/main"],
                                   cwd=ROOT).returncode == 0
        (merged if is_merged else open_).append(ref.removeprefix("origin/"))
    if open_:
        for name in open_:
            touched = git("diff", "--name-only", f"origin/main...origin/{name}").splitlines()
            canon = [t for t in touched if t in CANON]
            note = f"touches canon: {', '.join(Path(c).name for c in canon)}" if canon else f"{len(touched)} file(s), no canon"
            say("•", f"unmerged: {name} ({note})")
    else:
        say("✓", "no unmerged branches")
    if merged:
        say("·", f"{len(merged)} merged branch(es) can be deleted on GitHub: " + ", ".join(merged[:4])
            + (" …" if len(merged) > 4 else ""))


def run_checks() -> dict:
    head("Canon checks")
    results = {}
    for name, cmd in CHECKS:
        if not (ROOT / cmd[1]).exists():
            say("·", f"{name}: not present on this branch")
            continue
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        results[name] = r.returncode == 0
        if r.returncode == 0:
            say("✓", name)
        else:
            out = (r.stdout + r.stderr).strip().splitlines()
            say("✗", f"{name} failed: {out[-1] if out else 'no output'}", True)
            for line in [l for l in out if l and not l.startswith(" ")][:5]:
                print(f"      {line}")
    return results


def latest_session() -> None:
    head("Last session")
    records = sorted((ROOT / "outputs" / "sessions").glob("*/session.md"))
    if not records:
        say("·", "no session records yet (outputs/sessions/<YYYYMMDD>-<slug>/session.md)")
        return
    rec = records[-1]
    text = rec.read_text(encoding="utf-8")
    status = re.search(r"^status:\s*(\S+)", text, re.M)
    mode = re.search(r"^mode:\s*(\S+)", text, re.M)
    say("·", f"{rec.parent.name}: status {status.group(1) if status else '?'}, mode {mode.group(1) if mode else '?'}")
    resume = re.search(r"^## Resume here\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if resume and resume.group(1).strip():
        for line in resume.group(1).strip().splitlines()[:6]:
            print(f"      {line}")
    else:
        say("!", "that record has no 'Resume here' lines", True)


def open_items(topic: str) -> None:
    head(f"OPEN items mentioning “{topic}”")
    master = REV / "master_storyline.md"
    hits = [(n, l) for n, l in enumerate(master.read_text(encoding="utf-8").splitlines(), 1)
            if "OPEN" in l and topic.lower() in l.lower()]
    for n, line in hits[:10]:
        snippet = re.sub(r"\s+", " ", line).strip()
        print(f"      master_storyline.md:{n}: {snippet[:150]}{'…' if len(snippet) > 150 else ''}")
    if not hits:
        say("·", "none in master_storyline.md")


def cr_ids() -> set[str]:
    path = REV / "change_requests.json"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    return set(re.findall(r'"id"\s*:\s*"(CR-\d+(?:-R\d+)?)"', text))


# ---------------------------------------------------------------------------

def cmd_start(args) -> int:
    print(f"Pacifica session start — {datetime.now():%Y-%m-%d %H:%M}")
    state = branch_state(fetch=not args.no_fetch)
    other_branches()
    checks = run_checks()
    latest_session()
    if args.topic:
        open_items(args.topic)
    STATE.parent.mkdir(exist_ok=True)
    (STATE.parent / ".gitignore").write_text("*\n", encoding="utf-8")
    STATE.write_text(json.dumps({
        "started": datetime.now().isoformat(timespec="seconds"),
        **state,
        "canon": {rel: sha_lf(rel) for rel in CANON},
        "cr_ids": sorted(cr_ids()),
        "checks": checks,
    }, indent=1), encoding="utf-8")
    return summary("start", args.strict)


def cmd_end(args) -> int:
    print(f"Pacifica session end — {datetime.now():%Y-%m-%d %H:%M}")
    if not STATE.exists():
        print("  ! no start snapshot (.session/start.json); comparing with origin/main instead")
        start = {"sha": git("rev-parse", "origin/main"), "canon": {}, "cr_ids": [], "started": None}
        for rel in CANON:
            blob = subprocess.run(["git", "show", f"origin/main:{rel}"], cwd=ROOT, capture_output=True).stdout
            start["canon"][rel] = hashlib.sha256(blob.replace(b"\r\n", b"\n")).hexdigest() if blob else None
    else:
        start = json.loads(STATE.read_text(encoding="utf-8"))
        print(f"  · since {start['started']} at {start['sha'][:7]}")

    head("Canon changed this session")
    changed = [rel for rel in CANON if sha_lf(rel) != start["canon"].get(rel)]
    for rel in changed:
        say("•", rel)
    if not changed:
        say("✓", "no canon files changed")
    else:
        prose = {"book-agent/revision/master_storyline.md", "book-agent/revision/character_bible.md",
                 "book-agent/revision/character_registry.json"} & set(changed)
        new_crs = cr_ids() - set(start["cr_ids"])
        if prose and "book-agent/revision/change_requests.json" not in changed:
            say("!", "canon prose changed but change_requests.json did not — add or update the CR", True)
        elif new_crs:
            say("✓", f"new CR(s) in the register: {', '.join(sorted(new_crs))}")
            master = (REV / "master_storyline.md").read_text(encoding="utf-8")
            for cr in sorted(new_crs):
                if cr not in master:
                    say("!", f"{cr} has no coverage marker in master_storyline.md", True)
        if prose and "book-agent/revision/canon_facts.toml" not in changed:
            say("?", "facts file unchanged — if a date, age or identity changed, add the CR's \"facts\" list "
                "and run cr_facts.py apply", True)
        if "book-agent/revision/character_bible.md" in changed and "book-agent/revision/character_registry.json" not in changed:
            say("!", "character bible changed without the registry — update both together", True)

    run_checks()

    head("Work in progress")
    dirty = [l for l in git("status", "--porcelain").splitlines() if ".session" not in l]
    if dirty:
        say("!", f"{len(dirty)} uncommitted change(s): " + ", ".join(l[3:] for l in dirty[:6])
            + (" …" if len(dirty) > 6 else ""), True)
    before = len(attention)
    branch = git("branch", "--show-current")
    upstream = git("rev-parse", "--abbrev-ref", "@{upstream}")
    if upstream and branch and upstream != f"origin/{branch}":
        upstream = ""  # tracking main is not the same as having pushed this branch
    if branch and branch != "main" and not upstream and git("rev-list", "--count", "origin/main..HEAD") not in ("", "0"):
        say("!", f"branch {branch} has commits but was never pushed", True)
    elif upstream:
        unpushed = git("rev-list", "--count", f"{upstream}..HEAD")
        if unpushed and int(unpushed):
            say("!", f"{unpushed} commit(s) not pushed to {upstream}", True)
    if not dirty and len(attention) == before:
        say("✓", "everything committed and pushed")

    head("Session record")
    today = datetime.now().strftime("%Y%m%d")
    records = sorted((ROOT / "outputs" / "sessions").glob(f"{today}-*/session.md"))
    if not records:
        say("·", "no session record today (needed only for substantial or resumable work)")
    for rec in records:
        text = rec.read_text(encoding="utf-8")
        resume = re.search(r"^## Resume here\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        status = re.search(r"^status:\s*(\S+)", text, re.M)
        if not resume or not resume.group(1).strip() or "Two to four lines" in resume.group(1):
            say("!", f"{rec.parent.name}: fill in 'Resume here'", True)
        elif status and status.group(1) == "active":
            say("?", f"{rec.parent.name}: status still 'active' — set paused-for-author or stopped", True)
        else:
            say("✓", f"{rec.parent.name}: status {status.group(1) if status else '?'}, resume lines present")
    if not attention:
        STATE.unlink(missing_ok=True)
    return summary("end", args.strict)


def summary(which: str, strict: bool) -> int:
    print()
    if attention:
        print(f"{len(attention)} item(s) need attention before {'starting work' if which == 'start' else 'finishing'}:")
        for item in attention:
            print(f"  - {item}")
        return 1 if strict else 0
    print("Ready." if which == "start" else "Nothing left behind.")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Pacifica session start/end checks")
    sub = ap.add_subparsers(dest="command", required=True)
    s = sub.add_parser("start")
    s.add_argument("--topic", help="also list OPEN items mentioning this word")
    s.add_argument("--no-fetch", action="store_true", help="skip git fetch (offline)")
    e = sub.add_parser("end")
    for p in (s, e):
        p.add_argument("--strict", action="store_true", help="exit 1 if anything needs attention")
    args = ap.parse_args(argv)
    return cmd_start(args) if args.command == "start" else cmd_end(args)


if __name__ == "__main__":
    sys.exit(main())
