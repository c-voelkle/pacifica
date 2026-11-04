# CR-052 — fresh-context review (3 November 2026)

Independent reviewer, given CR-052, the workbook note, the README, the workbook and its build scripts, the handoff, AGENTS.md, the financial workbook and the master storyline; no access to the drafting conversation. Reviewed the first build (energy workbook SHA-256 `5aca0d32…`). The dispositions at the end record what the second build (`f474cb9f…`) changed.

## Verdict (reviewer)

The workbook is carefully built, reproducible and dimensionally sound, and it does what the handoff mainly asked: the multiplier becomes an output. Most quoted numbers match the saved values. Before approval: fix the mismatches (F5's year, the 1924–27 gap, "none after 1926", the F1 and F4 ranges); F1 and F2 rest on a factory-motor intensity calibrated to the US being applied to a GDP the fuel side treats as far less industrial (with a consistent intensity the multiplier is nearer two to two and a half, and CT1 becomes unnecessary); F4's coal gap is mostly the result of the `coal_mult` lever and its import share counts coal that cannot be shipped; the "importer" finding needs a canon tension against Pacifica's oil-exporter passages. W1 can be approved now.

## MUST FIX (reviewer) and disposition

| # | Finding | Disposition |
| --- | --- | --- |
| 1 | F5 says first power 1925; the formula gives 1924. Check 2 tests lead times only for the Works' dams and Rock Island. | Text now says 1924. Check 2 also tests the mid-Columbia chain and Boulder (both formula-gated, so they pass by construction; stated). The chain is now an option, off by default. |
| 2 | F4's "7 Mt in 1924–27" is wrong (7.3, 10.8, 13.7, 6.7). | Superseded by the second build: 0, 1.5, 4.6, 0. Quoted annually. |
| 3 | Note's "none after 1926" for all Gulf crude home is wrong. | Corrected; the run is re-done on the second build (75 Mt in all, worst 14.7 Mt in 1917). |
| 4 | F1 and F4 ranges cover benchmark years only. | Annual ranges given throughout, with the war-boom peaks named. |
| 5 | Factory motors on total GDP at a US-calibrated intensity contradict the fuel side's lighter industry. | **Fixed:** one industrial weight `ind_w` = 0.5 scales factory motors, consistent with `ind_mj`. The multiplier falls to 1.86–2.30 (1920–32); the halls' share of electricity becomes 6–13%, inside CR-051's range; the coal gap falls from 271 to 130 Mt. Sensitivity at 0.7 and 1.0 shown. CT1 reduced to the capacity share. |

## SHOULD FIX (reviewer) and disposition

| # | Finding | Disposition |
| --- | --- | --- |
| 1 | F1's "about three" is not like-for-like with the power check's capacity yardstick. | Both yardsticks reported; "about two" only for the all-producers comparison; capacity against US utilities 2.2–3.6 (1920–32). |
| 2 | The mainland is one pool, so Columbia hydro displaces Californian steam. | Stated as a limit in the note and the CR; the mid-Columbia chain is no longer a proposal, only an option. A two-system grid is a next step. |
| 3 | Import share counts coal that cannot be shipped. | Two columns: "would have to import" and "can actually be imported". |
| 4 | The coal gap mostly reflects `coal_mult`; home oil sold in Asia first. | Both named in F4 and CT3, with runs (4× coal: 3 Mt in all; no Asian sales from home crude: 101 Mt). |
| 5 | Missing canon tension: Pacifica as an oil supplier (Germany's ships under Ballin's contracts, the Entente's oil, Japan's dependence). | Added as CT4 with both cases. |
| 6 | Smaller mismatches (gap years, freed arc power, Stress grid range, 1882–88 failures are oil, 1919 freed power below R1). | Corrected; the early oil imports from elsewhere were raised so 1882–88 no longer fail; 1919 stated. |
| 7 | Boulder's first power in 1932 is four years ahead of history. | Lead time set to 6 years (Story): no Boulder power before 1932. |
| 8 | Fact changes "none"; CT5 lacks a canon-adapted case; F13's status label. | Fact changes stay "none" (no dated canon event is added: the chain is off, Boulder is historical); CT for Hilo now has both cases; F13 labelled PROPOSED (context). |
| 9 | The 1930 anchor's "utility-provided" label conflicts with the all-producers series. | Anchor relabelled; status "VERIFIED (label to check)". |

## NOTE (reviewer), kept

Formulas checked by hand were dimensionally right; row convention holds; no double counting; supply equals use to 1e-11. Checks 1 and 8 are largely identities; check 4's lower band sits just below the model's own range; the Works' dams path does not shift with the Stress lead time; revenue overstates self-generation. Handoff fidelity: §4–§7 met except a partners' trade block; finance link by script and named ranges, but the financial workbook not re-run (disclosed); anchors mostly TO VERIFY (disclosed). Hilo on oil and Hetch Hetchy fit canon.
