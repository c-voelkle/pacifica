# CR-049 — verification and fresh-context review

**Status:** Review of a PROPOSED CR, 2 November 2026. This record does not adopt the fictional changes or certify the accelerated scientific dates.

**Baseline:** `main` at `a267b87103d9f7f11000225b12480c783bf6d821`, including PR #57's canon-revisability policy. The working proposals originated at `7ab6434`; the storyline, character and approval-register bytes are unchanged between those bases. CR-049 contains its own Canon tensions section under the new policy.

## Fresh-context review

One reviewer received only the actual CR, affected author/canon context, current repository AGENTS and shared scope rules. No writer advocacy, prior drafts or prior review findings were supplied. The retired Pacifica specialist skills were not used.

The review covered chronology, identities, authority, approval status, agency, causal development and usefulness as a formal decision record. It found two material payload issues:

- Regex backslashes in seven common fact additions had invalid JSON escaping. Corrected; all payloads now parse.
- A guard fixed neutron confirmation in 1890 although the chronology says “by 1890”. The exact-year guard was removed; the deadline remains.

The reviewer found no further material issues for publication as a proposed CR. Expedition episodes remain outline-level development work. Historical, financial and engineering feasibility were not independently verified by that review.

## Checks

- Current canon lint: clean, four files checked.
- Approved register/facts agreement: passes, 34 approved fact changes.
- Storyline/index synchronization: passes.
- Canonical character validation: passes, including 250 legacy profiles.
- Commitments ledger: 188 commitments checked, zero problems.
- Whitespace check: passes.
- Standard `cr_facts.py preview --tensions` executed with temporary data inside the working directory. Common payload: 14 additions; T2 adds seven scientific point dates. T1 and T3 have empty machine-readable amendments and explicit prose impacts/open decisions.

The **default draft lint reports seven unregistered IDs**, exactly the seven proposed characters. Those IDs remain absent from the canonical registry because the CR is unapproved. This is not reported as a clean default draft lint.

A separate read-only proposal-overlay check used the same linter, the declared proposed facts and **only those seven declared IDs** in addition to the current registry. It checked current canon and the CR for the common case and each tension independently: zero findings in all four cases. No canonical file was changed by either preview. Range-valued proposals remain explicitly subject to human comparison; the exact-year linter does not certify them.

## Publication boundary

The proposed PR adds only `book-agent/revision/CR-049.md` and this review record. It does not amend the approval register, master storyline, canonical facts, character documents, commitments ledger, supplied attachments or financial model. Earlier local working drafts are not included. Adoption and subsequent integration require an explicit author decision on the selected groups and tensions.

## Round 2 — the partly approved decision record (2 November 2026)

**Candidate:** CR-049 revised on the author's decision (N, E, I, T1 Case A and C1 approved; tone fixed; invented cast limited; Babbage and Boole anchors; S1/S2/G1 returned). One fresh-context reviewer received only CR-049.md, AGENTS.md, the affected storyline passages and the new historical-background section; not the drafter's reasoning or the chat.

| ID | Finding | Disposition |
| --- | --- | --- |
| F1 | P1 was recorded as approved, but the author set a limit (“one or two”), not a choice of people. | P1 now PROPOSED within the limit; Liang's and Mele's scenes labelled PROPOSED; register, AGENTS.md and storyline note corrected. |
| F2 | O4's “one fellow must not come back” went beyond the author's “real danger”. | Marked as a suggestion. |
| F3 | Hollerith read as joining the Calculation Office; in canon he tabulates Noe's registers at the Office of Public Measures. | Corrected; the Calculation Office borrows the method, and Liang's relays lose that work to the cards (PROPOSED). |
| F4 | Mele as an Oahu College “graduate” before 1859 sits awkwardly with women's admission from 1862. | “Educated at Oahu College”. |
| F5 | Hedging and memo sentences remained in the narrative; Peirce, Shannon and Jevons comparisons sat in the chronology. | Rewritten as events or cut; comparisons kept in the anchors table and historical_background.md only. |
| F6 | An 1856 commission precedes the 1857 Albany and London purchases, so Carquinez is the first buyer, not the third; “Pacifica” is anachronistic in 1856. | Corrected. |
| F7 | Jevons's logic piano is a logic machine, not a rival calculator. | Labelled a comparison only. |
| F8 | Flat or unopposed beats: the wartime protection, the Japanese hosts, Mele's motive, nothing after 1879. | The navy's claim on the laboratory's people and the cost in gunboats (PROPOSED); hosts who test Liang and keep his better methods; Mele's own readings among those discarded; Liang against Hollerith's cards in 1888 (PROPOSED). |
| F9 | Two pattern false positives (an 1866 sentence; London's 1857 order) and four misses (bold years, year-after-verb phrasing). | Patterns rewritten and tested against the CR's sentences and the two false-positive sentences. |

Checked and confirmed by the reviewer: Babbage (1826), Menabrea (1842) and Lovelace (1843), Boole (1847, 1854), Donkin and Farr (1859, 1864), Peirce (1886), Shannon (1937/38), Niépce de Saint-Victor (1857–61). The Bodleian source gives Lovelace's Notes as 41 of 66 pages. No other invented named person appears.

**Checks after repair:** canon lint clean; register and facts agree (CR-049 facts deferred to integration); storyline synchronised; character documents valid; commitments 0 problems; `cr_facts.py preview --tensions` parses every payload, with only the two expected unregistered-ID findings.

## Round 3 — the reworked atomic branch (2 November 2026)

**Candidate:** S1/S2 reworked against requirements 1–5 after the author kept Liang and Mele. One fresh-context reviewer received only CR-049.md, AGENTS.md, the two CR-049 sections of historical_background.md and the affected storyline passages.

| ID | Finding | Disposition |
| --- | --- | --- |
| F10 | No single-particle detector before the neutron, fission pulses and neutron counting. | A counter at Yerba Buena, 1885–1887, read on a quadrant electrometer with photographic records (the Rutherford–Geiger principle, 1908), with Tesla's high voltage; neutron numbers by foil activation. |
| F11 | Helium's 0.7% deficit was below the 1880s uncertainty in the oxygen–hydrogen ratio. | Morley's ratio (historically 1895) brought forward to 1884–1885 as the stated mechanism; litres of helium from pitchblende. |
| F12 | “Alpha is helium” rested only on helium in sealed tubes. | Charge-to-mass ratio measured with strong magnets and plates on the 1876 sources. |
| F13 | Energy “atom for atom” in 1877, and mass–energy “fits” in 1886 and 1892, broke requirement 5. | 1877 gram for gram; per-atom energy after counting in 1883; the mass link stays a conjecture with no conversion until 1905. |
| F14 | Goldstein was 26 and without a doctorate in 1876. | Assistant under Genth from 1876, doctorate and mastership 1881. |
| F15 | Hillebrand's 1879 gas came from ore found only in 1881 (and poor in helium). | Joachimsthal pitchblende; he corrects his own claim in 1881. |
| F16 | Talbert's 1881 find lies in Uncompahgre Ute country. | Mining on a lease through the Republic with the fee to the Ute, under CR-033 (PROPOSED; terms OPEN). |
| F17 | Mele sidelined after 1867; Morley overloaded. | Transformation credit becomes an open quarrel, restored by a correction entry in 1872; helium and radiogenic lead go to Hillebrand. |
| F18 | Tesla as furnace chemist. | Tesla supplies the power; Hillebrand's group runs the furnaces. |
| F19 | One tension bundled S1, S2 and G1; a stale background line; the thorium identification labelled approved; “goldbeater's leaf”. | T2 (S1) and T4 (S2, G1) split; background updated; identification marked PROPOSED; “beaten gold leaf”. |

No safety finding: the text stays at a history-of-science level. Canon consistency (Western Slope and Leadville, Michelson from 1878, Yerba Buena 1866, Morley 1868, Genth) confirmed.

**Checks after repair:** canon lint clean; register and facts agree; storyline synchronised; character documents valid; commitments 0 problems; all tension payloads parse and each S1/S2 pattern matches its own milestone sentence in the CR.

## Round 4 — Peirce, P2 and the atomic estate (2 November 2026)

A fresh-context reviewer read the participants, chronology, P2, F1, T5–T6, the register, the people anchors and the storyline passages on the Five, the Polytechnic, the women's examinations and the retirement rule.

| ID | Finding | Disposition |
| --- | --- | --- |
| F20 | Hillebrand was twenty-nine in 1883, not thirty. | Corrected. |
| F21 | Wet collodion plates cannot be stored for a month. | The laboratory's experimental dry plates (Taupenot, 1855). |
| F22 | Peirce's 1886 letter missing from his anchor. | Added. |
| F23 | Peirce in Japan at seventeen in 1856 needs a timeline. | Arrives spring 1856, sails in the autumn after his seventeenth birthday; the Dutch-run Nagasaki naval school (1855–1859) as the real setting. |
| F24 | Kate Curran's 1866 marriage and medicine unresolved. | She marries Curran (historical), keeps her post and never studies medicine. |
| F25 | “The first test” of the Five's bargain contradicts canon (Donner, 1887). | “Another test”. |
| F26 | The Crown does not touch the estates' charters (CR-027). | Soberanes uses the Polytechnic's powers at the Regent's request; the Regent acts as holder of the Crown's shares in the champion. |
| F27 | The Office of Public Measures is an independent estate (1888) reporting to the Senate, not “Victoria's own”. | Corrected; noted that it has no seat among the Five. |
| F28 | Labels: Peirce's mechanics shown as approved; participants headcount; G1 status; Hearst's label; P2 count. | Peirce's mechanics marked PROPOSED; “one historical person and one invented person”; G1 “PENDING”; Hearst stays PROPOSED; “two Californians and a Hawaiian”. |
| F29 | “Liang's rule” left in Mele's row; “Robert Vance” beside canon's Vances. | Corrected; “a San Francisco daguerreotype studio”. |

**Checks after repair:** canon lint clean; storyline synchronised; all tension payloads parse.
