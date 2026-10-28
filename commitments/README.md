# Commitments ledger

Pacifica's political obligations kept like a debt register: 165 treaties, compacts, leases, loans, guarantees, charters and life offices from 1846 to 1932. Each entry records:
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

Gaps and tensions the extraction found in canon. The author answered them on 28 October 2026; [CR-039](../book-agent/revision/CR-039.md) records the answers.

Resolved by CR-039:
- **1.** The Puʻuloa lease lapses in 1924; the fleet stays as the Hawaiian crown's tenant at the Mōʻī's pleasure.
- **2.** The Pacific Concord replaces the 1887 compact with Tokyo when its fourth renewal falls due in 1927.
- **3.** China recovers its customs under the Treaty of Nanjing (1928).
- **5.** The Gulf Republic is founded in 1900, the year the canal opens; the Gulf compact is signed at its founding and sets the admission tests. There is no 1895 compact.
- **6.** The Concord's first executive term runs 1927–1932.
- **7.** The 1848 naval articles share the twelve-year term; the 1865 peace ends the 1848 and 1860 conventions.
- **8.** Querétaro's pledge is narrowed to joining the United States or ceding territory.
- **9.** The Protectorship is renewed in 1862, 1863 and 1864.
- **10.** The state, not the Crown, keeps a quarter of the 1876 tobacco company.
- **11.** Silas's death in the winter of 1912 is in `canon_facts.toml`.
- **12.** Waite and Whitney's 1897 treaty, the Association treaties and the Truce's signing are approved; Korea's post-1905 rights no longer sit under the OPEN marker; the 1905 peace is signed at Urajio.

Still open:
- **4.** **Ka Lōkahi** names both the 1914 council of the crowns and, in Hawaiian, the Concord: on hold for a larger change the author is planning.
- The Gulf Republic's part in the Cuban guarantee, now that it is founded in 1900.
