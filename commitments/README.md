# Commitments ledger

Pacifica's political obligations kept like a debt register: 164 treaties, compacts, leases, loans, guarantees, charters and life offices from 1846 to 1932. Each entry records:
- who owes what to whom;
- when it starts, ends or renews;
- what ends it;
- who can refuse.

Every entry quotes the storyline verbatim, so the ledger records canon and never adds to it.

```
python3 commitments/ledger.py check                 # quotes, labels, sections, dates and people
python3 commitments/ledger.py at 1928 --party JP    # in force in a year
python3 commitments/ledger.py schedule 1887 1932    # maturity schedule
python3 commitments/ledger.py if-dies CT-JULIAN --year 1925
python3 commitments/ledger.py report                # outputs/ledger.md
python3 -m unittest discover -s commitments/tests
```

## How it stays honest

- **Quotes:** `check` fails when a quote is no longer in `master_storyline.md`. CI runs it on every storyline change, so an edited passage flags the ledger entries that rest on it.
- **Status:** each entry's status is the storyline's label at the quote: CANON for unlabelled base text, or APPROVED, PROPOSED, OPEN or MODEL. `check` compares the two. Where a label's scope is misleading, the entry says why in `label_note`.
- **Gaps:** these are recorded, not filled. Where canon gives no year, `from_approx` marks the year of the passage that first states the obligation. Missing terms go in `open`.
- **Deaths:** these come from `book-agent/revision/canon_facts.toml`, or from a quoted `[[person]]` in the ledger.

The entries were extracted from the storyline in four parts on 27 October 2026 and checked mechanically: every quote, label, section and date. The descriptions in `owes`, `can_end` and `conditions` paraphrase the quoted passages; they are a reading aid, not canon.

## Findings for the author (27 October 2026)

Gaps and tensions the extraction found in canon. None has been changed.

1. **The Puʻuloa lease expires in 1924.** The fifty-year term from 1874 ends then. The storyline never says whether it is renewed, replaced or lapses, yet the fleet base at Pearl Harbor continues.
2. **The 1887 compact with Tokyo** is renewed in 1897, 1907 and 1917. Its next renewal would fall in 1927, the year of the Concord, but canon doesn't say whether the Concord replaces it.
3. **China's "defense treaty."** China recovers the Inspectorate and customs in 1928–29 "under the defense treaty", which appears nowhere else.
4. **Ka Lōkahi's agreed matters** are "renewed every ten years", with no base year, so the renewal dates are unknown.
5. **The Gulf compact** is dated 1895 (PROPOSED dates), before the Gulf Republic exists (1899–1900). It is unclear which compact sets the admission tests.
6. **The Concord's first executive term** could run from 1927 (provisional application) or from 1928 (consent). The 1932 renewal implies 1927–1932.
7. **The Buchanan–Vallejo Convention (1848)** gives only its commercial articles a twelve-year term. At Carson in 1860, though, the ports and the Sausalito storehouse are among the expired articles. Carson also recognizes US sovereignty over Washoe, which Pacifica retakes in 1863–64, and nothing ends that convention.
8. **Querétaro (1847)** pledges California "never to cede itself or its territory to any power", which is never squared with joining the 1856 Confederation.
9. **The Protectorship** is renewed in 1862 and 1863. Its 1864 renewal and its end are not stated, yet it is still in use for the 1864–65 dissolution.
10. **The tobacco company (1876)** has "the Crown" keeping a quarter decades before the Crown is established (1914).
11. **Silas's death in the winter of 1912** ends his inland command, but it is not in `canon_facts.toml`.
12. **Label scope.** Some labels seem to reach further than meant:
    - the Korea rights at L610 sit under an OPEN marker about the signing place;
    - the 1897 Whitney treaty sits under a PROPOSED label about Governor Waite;
    - the Association treaties sit under a CR-029 label about the quitclaim;
    - the Truce's terms paragraph is unlabelled while its signing is PROPOSED.
