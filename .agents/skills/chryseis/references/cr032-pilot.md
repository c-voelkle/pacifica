# CR-032 pilot: dated source map

This reference captures the repository state inspected on 24 October 2026. Refresh refs and source passages before use; later author instructions and repository revisions take precedence. These are four separate proposals, not canonical integrations.

Repository: https://github.com/c-voelkle/pacifica
Recorded canonical baseline: cc6e017780970433ab63bc95d0e3749510b44d49
Recorded proposal branch: drafts/cr032-alternatives-20261024
Recorded proposal commit: 626ffbb0bd6486c19164f89104569d78321ebd55
Recorded draft PR: https://github.com/c-voelkle/pacifica/pull/6

Paths:
- book-agent/revision/master_storyline.md
- book-agent/revision/change_requests.json
- finance/Pacifica_financial_model_1846-1932.xlsx
- finance/CR-031-review.md
- book-agent/revision/alternatives/CR-032/README.md
- book-agent/revision/alternatives/CR-032/CR-032.md (A)
- book-agent/revision/alternatives/CR-032/CR-032b.md
- book-agent/revision/alternatives/CR-032/CR-032c.md
- book-agent/revision/alternatives/CR-032/CR-032d.md

The recorded CR-031 workbook SHA-256 is 29aaeaafeeef712ff6c276c71495c461a122f111726abdafacd558f9bab30091. Its saved Story case is a reference snapshot, not an independently rerun experiment. The documented Ledger was an older CR-021 snapshot; do not assume it matches later workbooks.

## Shared and branch-specific changes

All four drafts retain a limited Petropavlovsk cruiser campaign and May 1905 victory in place of the canonical Baltic Fleet destruction. Reprice the 1904-1905 campaign, Japanese war finance, the Russian indemnity and surviving-fleet consequences. Do not assume the roughly $300m modelled 1906-1910 indemnity remains fixed under the smaller campaign. Begin the comparison before this change; verify any earlier consequences of the Russian development premise.

A useful additional control contains only the shared 1904-1905 changes. It does not replace comparison with the original canonical baseline.

| Case | Narrative specification | Financial work |
|---|---|---|
| A, CR-032.md | Great War; coalition intervention from May 1918; Ob defence in January 1920; Moscow falls in March; federal Russia replaces independent Siberia | Campaign beyond the Ob, Russian reconstruction and relief, Legion replacement/repatriation/pensions, federal/regional revenue and continuing security. Replace the old Ob operation rather than counting both. Keep Russian production foreign to Pacifican GDP. |
| B | Credit-policy change from summer 1916 and general armistice in August 1917; Russian stabilization is conditional | Preserve incurred contracts and existing claims, limit new exposures, price cancellations and industrial conversion, replace later war flows with actual reconstruction projects. Separate borrower obligations and public/private holders. Do not pro-rate everything by war duration. |
| C | Accession in 1907 and prewar diplomacy; working prevention of war in 1914; immediate crisis resolution and later Russia remain open | Price earlier succession, the Philippine balance at the new date, development and diplomacy. Calculate supported early periods; any 1932 projection requires explicitly named completion assumptions. Do not silently copy D's completed history. |
| D | No general European war through 1932; constitutional Russian monarchy, narrower treaty protection in Transbaikalia, lawful 1927 Japanese partnership | Remove Great War-specific loans, war-derived claims/concessions and Russian campaign. Price civilian investment, armed neutrality, treaty obligations and revised banking. Reassess earthquake FX needs and the peacetime contraction. |

C and D advance the accession and Philippine settlement to 1907. An earlier assumption of debt must use a reconstructed outstanding balance, with interest and service after transfer, rather than moving the $9.5m 1914 amount unchanged.

D preserves the physical 1923 earthquake but not the original financial balance sheets or rescue drawing. Its 1927 treaty does not create the canonical common finance/foreign ministries or bank-rescue Concord. The Union's 1932 commercial accommodation is not the original rescue-driven association.

D's treaty does not create an independent Siberia/Kamchatka, Commander Islands transfer, Arctic leases, or the old Company arrangement. Keep any alternative Russian investment and its income separately justified. No old concession income survives merely because a chart expects it.

## Recorded baseline quantities: reference, not scenario gains

Verify current values and source formulas before reusing these anchors. Currency is period dollars in millions; multi-year totals below are nominal disbursement sums, not constant-price costs.

- Treasury Entente principal, 1914-1918: 1,700, from Events rows 75-79, IDs E70-E74. The aggregate syndicated advance was 8,500, split among Treasury, Pacifican private and foreign lenders.
- Siberian campaign, 1918-1922: about 965.794, from Events rows 81 and 157-160.
- Standing Siberian front, 1923-1932: about 407.545, from Events row 87 and rows 161-169.
- Combined campaign/front: about 1,373.339. These rows are spending, unlike loan principal.
- Japanese public rescue drawing: about 165.620, Japan rescue!D11. Public commitment: 200, Events!H90. Drawings and commitments cannot be added.
- Union rescue principal, 1931-1932: 400, Events rows 94-95. Any peacetime stabilization facility needs new quantities and terms.
- Philippine debt assumption: 9.5 in 1914, Events row 146, ID E145. No 1907 balance has been established by that number.

When removing loans, also remove or reconstruct the corresponding assets, repayments, interest and losses. Reallocate released funding explicitly. Neither avoided spending nor undisbursed principal is an equal GDP gain.

## Pilot comparison design

Use the same 1932 reporting endpoint and common accounting definitions. Also show cumulative public costs, exposure and the path through the intervening years. The matched-shock experiment must distinguish timeline effects from a differently chosen downturn.

C's unresolved continuation is different from a wide cost range. D's no-general-war assumption remains part of its reference scenario; a renewed general war is another branch, not a recession sensitivity.

D retains planning targets of peacetime military-plus-overseas spending at 4% of North American GDP, interest at 15% of revenue and debt at 30% of North American GDP. Verify the applicable period, exceptions and geographic denominator against the current source. Do not silently substitute network GDP or force the output to hit a ceiling.

Useful D sensitivities include weak Russian reform, narrower transit-only rights, weaker Japanese alignment, severe downturn and adverse Union alignment. Model the actual costs and rights in each; do not give D both peace's advantages and the war branches' distress-driven concessions.

If building the engine, baseline-versus-D is a useful initial dependency test. This implementation order does not justify omitting requested A/B comparisons or inventing C's unresolved outcomes.
