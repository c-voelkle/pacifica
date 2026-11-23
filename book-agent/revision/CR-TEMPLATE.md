# CR-NNN — Title: what changes (years)

<!--
Copy this file to CR-NNN.md and fill it in. Before asking for a fresh-context review, run

    python3 book-agent/revision/preflight.py --draft book-agent/revision/CR-NNN.md

and fix every error. The script reads the four headings marked (machine-read) below and the
three lists under "Ledger and registry"; keep their spelling exactly. Everything else is free.

Citing the storyline. Give the line and a short phrase copied from that line or from the
HTML comment directly above it, in this form (the script checks that the phrase is there):

    L1554 ("a compact gives British Columbia half")
    L1695 ("the refusal to print")
    L1746–1752 ("Thalassia Conference")

Anchor each line once; later mentions of the same line may be a bare L1554. A line that is
never anchored is an error: line numbers shift, and a wrong number that still points at a
real line is otherwise invisible. Lines of other files are written "line 36 of CR-082.md"
and are not checked.

Ledger IDs. Before naming a new party or commitment, look it up:

    grep -n 'id = "CAL"' commitments/data/ledger.toml

Standalone merge. If this CR needs a fact, a price or an instrument from a CR that is not
yet written, say so under Status and either define it here or mark the dependent passage
OPEN. The script warns on every CR number that has no file and no register entry.
-->

**Status:** DRAFT, revision 1 (date). Not integrated; nothing in `master_storyline.md` is changed by this file.
- Approved so far: none.
- Details added by the drafter are marked PROPOSED and listed under `## Decisions`.
- **Standalone merge check:** this CR can merge without any unwritten CR (or: it waits on CR-NNN for …).
- **Next:** the author's answers, then a fresh-context review.

Figures are MODEL unless marked otherwise. Historical claims are marked *Hist.* and sourced under `## Sources`.

**Depends on:**
- CR-0xx: what this CR takes from it.

## The author's request

> The author's words, verbatim, with date and time.

## A. The change

**A1.** What happens, who decides it and from what interest, and what it costs them.

## B. Impact notes

Storyline passages to revise on integration. Start from `cr_facts.py preview` and add the passages no pattern tracks.

- none yet

## C. Set pieces (candidates, not drafted)

- none yet

## D. Model and workbook tasks

- none

## E. Ledger and registry

One bullet per ID, the ID first and in backticks, or the single word "none" under a heading.

### New parties

none

### Amended commitments

none

### New commitments

none

### Registry

- Existing people who gain a note: none.
- New people (each needs an `add_person` under `## Fact changes` and an entry in `character_registry.json` in the same commit): none.

## Canon tensions

<!-- (machine-read) For each conflict with canon: both cases, the fact changes of the
amending case in a json block under that tension, and a recommendation. Or the word "none". -->

none

## Fact changes

<!-- (machine-read) One json list in the format at the top of cr_facts.py, or the word "none".
Event patterns keep a general year group, (?P<year>1[89]\\d\\d), never a fixed year. -->

none

## Decisions

<!-- (machine-read) -->

| # | Decision | Status |
|---|---|---|
| D-1 | … | PROPOSED |

**PROPOSED by the drafter:** none yet.

**OPEN:** none yet.

## Sources

<!-- (machine-read) Each historical claim with a URL or a full publication. Say which claims
are not yet verified. -->

- none yet
