---
name: pacifica-commitments
description: Pacifica's commitments ledger — every treaty, compact, lease, loan, guarantee, charter and life office in canon, with who owes what to whom, terms, renewals, what ends it and who can refuse. Use for "what is Julian/Pacifica/Japan bound by in year X", "what lapses if X dies", maturity and renewal schedules, and checking a CR against existing obligations.
---

# Pacifica commitments

A debt register for political obligations. Companion to [Chryseis](../chryseis/SKILL.md) (what things cost) and [pacifica-population](../pacifica-population/SKILL.md) (who is there to do them): this ledger says what each party is bound to and who can refuse.

Apply the [shared authority and scope rules](../../../docs/authority-and-scope.md) (R1–R7).

## Run

```
python3 commitments/ledger.py check                 # every quote is in the storyline, labels and dates agree
python3 commitments/ledger.py at 1928 --party JP    # in force in a year, optionally for one party
python3 commitments/ledger.py schedule 1887 1932    # starts, renewals, term ends, endings, lapses at a death
python3 commitments/ledger.py if-dies CT-JULIAN --year 1925
python3 commitments/ledger.py report                # commitments/outputs/ledger.md
python3 -m unittest discover -s commitments/tests
```

## Rules

- The ledger records canon; it never adds to it. Every entry quotes the storyline verbatim, and `check` fails when a quote disappears. When an approved CR changes a passage, update the entry in the same PR.
- Status is the storyline's own label at the quote (CANON, APPROVED, PROPOSED, OPEN, MODEL). Report answers with those labels.
- Never fill a gap with a plausible term, renewal or veto. A missing term is a finding: put it in `open` and tell the author.
- No probabilities, scores or moods. Record who can refuse and how; whether they would is the author's judgment.
- To test a CR draft, list the obligations it touches (`at`, `if-dies`) and whether it creates, renews, breaks or ends one. A new instrument in an adopted CR becomes a new entry.
