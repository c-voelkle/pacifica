# Phase 5: the Civil War levers and the headroom, 1859–1872

13–14 November 2026. Model plan for CR-059–065, 067 and 068, phase 5.

- Build script: `finance/build/cr059_068_levers.py`. Its input is the phase 4 workbook.
- Output: `phase5/Pacifica_financial_model_cr059-068_levers.xlsx`, recalculated in the Story case (SHA-256 eac77da5…).
- The build is deterministic: two runs differ only in `docProps/core.xml`.
- The author's answers of 14 November are built in (see the last section).

## Result

**Every check passes as before: Story 0 failed year-checks, Stress 17.** These are the same 17 year-checks that fail in phase 4.

**All 36 levers move the model** when their cell changes. See `phase5/lever_test.json` and the lever table below.

**Room in Stress is tight in 1862–64, and private saving binds:**

| Year | Room in Stress |
|---|---|
| 1862 | $11.2m |
| 1863 | $6.0m |
| 1864 | $9.0m |

In Story the room in those years is $23–28m, and the bond market binds first. The idle-gold rule (L17, now on) adds $1.3–1.8m a year to the Stress figures.

**The 1867 settlement is lighter than in phase 4.**

- 1867 no longer borrows. In phase 4 it borrowed $4.7m in Story and $7.5m in Stress.
- Two changes do this: the private lending of E14 ($3m, D8) replaces the Treasury's $10m, and the instalment is split under option (b).
- Gold paid out in 1867 is $56.6m in Story. Of that, $16.9m is the settlement and $39.8m is the gold held back in 1861–65 going east (F18).

## What changed at the story minimum (against phase 4)

| | Phase 4 | Phase 5 (Story) | Why |
|---|---|---|---|
| Public debt, end of 1867 | $24.8m | $17.3m | E14 leaves the Treasury's books (L13) |
| Reserve Fund, end of 1870 | $24.7m | $34.8m | the same |
| Monetary gold, end of 1865 | $189m | $269m | F18: no gold to New York |
| Monetary gold, end of 1868 | $192m | $199m | the held gold has gone east; E14 takes $7m less |
| Spending, 1862 | $51.2m | $50.5m | E09 split: the credit is a loan, not a subsidy |

## Headroom, 1859–1872

**Room** is the most new spending (or lost receipts) a year can take before a check fails. It is what is left of the Reserve Fund that year, plus the smaller of two margins:

- the bond-market margin: 6% of GDP, plus $10m abroad, plus the L17 source, less the bonds placed;
- the private-saving margin: Sources & uses L.

Before 1887 only two checks can fail: Bond markets can absorb them, and Private saving capacity. Cash is always brought to target, first from the Reserve Fund and then by borrowing.

| Year | Story: borrowed | Story: Reserve Fund | Story: room | binds | Stress: borrowed | Stress: debt | Stress: room | binds |
|---|---|---|---|---|---|---|---|---|
| 1859 | 0.0 | 3.3 | 21.3 | private saving | 0.0 | 1.3 | **10.4** | private saving |
| 1860 | 0.0 | 3.3 | 23.5 | private saving | 0.0 | 1.1 | **11.6** | private saving |
| 1861 | 0.0 | 2.0 | 32.1 | private saving | 0.0 | 1.1 | **17.6** | private saving |
| 1862 | 6.8 | 0.0 | 25.6 | bond market | 7.7 | 9.0 | **11.2** | private saving |
| 1863 | 11.3 | 0.0 | 23.5 | bond market | 12.3 | 21.6 | **6.0** | private saving |
| 1864 | 11.0 | 0.0 | 27.7 | bond market | 12.2 | 33.7 | **9.0** | private saving |
| 1865 | 0.0 | 0.6 | 41.2 | bond market | 0.0 | 31.7 | **22.9** | private saving |
| 1866 | 0.0 | 2.4 | 34.3 | private saving | 0.0 | 25.2 | **13.7** | private saving |
| 1867 | 0.0 | 3.0 | 39.1 | private saving | 0.0 | 24.0 | **14.4** | private saving |
| 1868 | 0.0 | 6.0 | 48.9 | private saving | 0.0 | 13.8 | **20.0** | private saving |
| 1869 | 0.0 | 20.9 | 55.2 | private saving | 0.0 | 0.5 | **23.7** | private saving |
| 1870 | 0.0 | 34.8 | 77.3 | bond market | 0.0 | 0.0 | **36.9** | private saving |
| 1871 | 0.0 | 45.1 | 94.5 | bond market | 0.0 | 0.0 | **50.9** | private saving |
| 1872 | 0.0 | 62.0 | 100.5 | private saving | 0.0 | 0.0 | **43.8** | private saving |

All figures are $m. The full table, with the margins, gold and cash, is in `phase5/headroom.csv`.

**The estimate holds when tested.** These tests ran before L17 was switched on, when the estimates were $4.6m, $20.4m and $14.4m. In each test I added a single spend in one year and recalculated:

| Case and year | Passes | Fails |
|---|---|---|
| Stress 1863 | $4.0m | $5.0m (private saving) |
| Story 1863 | $19.5m | $21.5m |
| Stress 1867 | $13.5m | $15.5m |

**The Stress ceiling stays at 17** (author, 14 Nov). A spend that adds an 18th failed year-check is over the limit.

**What this means for phase 6:**

- The free items with a cost in the war years must fit into Stress's $6.0m in 1863 and $9.0m in 1864. That room also has to carry what a war-year cost adds later in interest and repayment.
  - The items: the Honolulu batteries and turret-ship slip, the 1865–67 garrisons, the annuities, and the Richmond credit above its floor.
- Receipts in the same years lift the war years:
  - the regional receipts (D4);
  - Washoe's net-proceeds tax (L11);
  - the refugee stream (L12). Twenty thousand a year in 1863–65 adds $45m to receipts and $19m to spending over 1859–85.
- Costs placed after 1866 take little room: the Oregon works on Development Fund credit (D9), and the scrip set-off.

## F18: no treasure steamers to New York, 1861–65

**Before the war most exported Pacific treasure went to New York.** The Custom House statement for the first quarter of 1860 gives $8.66m to New York, out of about $10.2m in all: 85% (`cw_ny_share`).

**That share was already falling by 1863.** New York took $11.3m in the first half of 1862 and $5.65m in the first half of 1863. In January 1863 one steamer carried $1.34m for England and $0.35m for New York.

**In the model, the New York-bound gold of 1861–65 is split two ways** (`cw_ny_home`). In Story half stays at home, in Stress a quarter; the rest goes direct to London.

**The gold held back goes east when the steamers return** (`cw_ny_return` = 1, author 14 Nov). Half goes in 1866 and half in 1867, counted in Gold & money E. In Story the held gold is $79.6m.

- *Two Houses* (CR-068 G6b) supports this: at peace, "the coast's gold goes to New York again".
- From 1868 the gold stock is back where phase 4 had it.

F18 changes monetary gold only, not the Treasury's cash. No check before 1900 reads monetary gold.

## L17: war bonds subscribed in coin from idle gold (approved 14 Nov)

**The rule.** In each year 1861–65, war bonds may draw coin up to a share (`cw_idle_ratio`) of notes and bank reserves (Gold & money I), never more than the gold above cover (Gold & money K).

- The share is 0.12 in Story and 0.06 in Stress.
- The rule counts as a private source in Sources & uses (column R, added into E). It also counts as home-market capacity in the bond-market check (Checks L).
- It adds $2.6–3.8m a year in Story and $1.3–1.8m in Stress.

**The bound comes from the Union's own bank loan of 1861.**

- On 15 August 1861 the banks of New York, Boston and Philadelphia contracted to take $150m of government securities, in three instalments of $50m.
- In the six weeks to 30 September, the New York banks' specie fell from $48m to $37m. Over the same weeks the sub-treasury's gold rose by $13m: the coin was paid out at home and largely came back.
- The New York banks' specie was 50% of their deposits and notes in August. A net drain of 23% of specie is therefore about 12% of deposits and notes.
- From 7 to 28 December a run, after the Trent affair and Chase's report, took another third of their reserves, and they suspended. Stress keeps half.

**The model's gold above cover does not give a usable bound.** In the model, monetary gold piles up and never leaves, until 1866–67. It reaches about half of GDP by 1865. A fifth of it would allow $30–50m a year, which the 1861 evidence does not support.

## The levers (Levers rows 408–446; named `cw_*`; Story = Stress unless shown)

| Register | Lever | Value now | Wired to | Moves |
|---|---|---|---|---|
| F18 | `cw_ny_share`, `cw_ny_home`, `cw_ny_return` | 0.85; 0.5 / 0.25; 1 | Resources R 1861–65; Gold & money E 1866–67 | gold |
| L17 | `cw_idle_ratio` | 0.12 / 0.06 | Sources & uses R, E; Checks L | idle-gold source |
| L01 | `cw_rich_early`, `cw_rich_late` | $0.3m / yr 1862–63; $0.9m / yr 1864–65 | E09, E198 (Loan, Continental, in goods) | net lending, debt |
| L01 | `cw_mission` | $0.1m / yr 1862–65 | E199 | spending |
| L02 | `cw_hon_batt`, `cw_hon_frig`, `cw_hon_turret` | 0 | E203; Navy plan C22 (ships); E204 | spending; navy running costs |
| L03 | `cw_war61`, `cw_occ6264`, `cw_occ6567` | $6m; $5m / yr; 0 | E07, E08, E200 | spending |
| L04 | `cw_sitka_gar`, `cw_sitka_mail` | 0 | E195, E196 | spending |
| L05 | `cw_inst_opt` | 2, option (b) (D8) | E11 (1867), E197 (1868–72) | gold paid out, debt |
| L06 | `cw_scrip_face`, `cw_scrip_price` | 0; 0.6 | E205 (1865–66); the set-off in E11 | spending, gold |
| L07 | `cw_setoff_nc`, `cw_nb_credit` | 0; 1 | the E11 set-off; E206 (N-C paid on to the nations) | gold paid out |
| F13, F14 | `cw_union_prop`, `cw_keep64`, `cw_keep67` | 0 | E11; E201, E202 and the E11 set-off | spending, gold |
| L08 | `cw_ann_nw`, `cw_ann_gb`, `cw_ann_sw` | 0 | E207–E209 (to 1881–82) | spending |
| D4, L11 | `cw_rc_or`, `cw_washoe`, `cw_rc_sw`, `cw_rc_gb` | 0 | E210–E213 (receipts, to 1866 or 1872) | receipts |
| L09 | `cw_juarez` | 0 | E214 (Loan, Continental, Mexico) | net lending |
| L10 | `cw_or_works` | 0 | E215 (Investment, 1868–75) | spending, development stock |
| L12 | `cw_refugees` | 0 | Paths E 1863–65 | residents, receipts |
| L13 | `cw_priv1867` | $3m (D8; private) | E14, under the new category "Private lending", feeding Gold & money E and Sources & uses K | gold, private uses |
| L16 | `cw_legion_on`, `cw_legion_pay` | off; $0.15m / yr | E216 | spending |
| | `cw_setoffs`, `cw_ny_held` (computed) | 0; $79.6m in Story | E11; Gold & money E | |

**The set-offs against the 1867 instalment** are:
- the scrip at face;
- the Northwest annuities of 1862–66;
- N-C;
- the garrisons' keep.

Union property at valuation (F13) is added to the instalment instead.

## The author's answers (14 Nov 2026)

1. **L17's bound is approved:** 0.12 of notes and bank reserves in Story and 0.06 in Stress, capped by the gold above cover. It is now on.
2. **The held gold goes east when the steamers return,** half in 1866 and half in 1867 (`cw_ny_return` = 1). Stress is back at 17: the 1932 gold-cover check fails again, as it did in phase 4.
3. **The Stress ceiling stays at 17** for the packages.
4. **Victoria's frigates are the Navy plan's two steam cruisers of 1861,** built for the war, and she gets them after the war. `cw_hon_frig` stays 0. The Navy sheet keeps their running costs. A charge to Hawaii's budget from 1866 under the Enabling Law would be a later refinement.
5. **The technical mission's pay of $0.1m a year stands.**
6. **E14 is private money,** as built.

**L15 is still to build.** It is approved: the Land Fund takes in the ceded public domain from 1867. It needs Land Fund formulas, and it adds receipts only after 1867.

**Next, phase 6:**
- a ceiling per lever, by bisection;
- the four packages: creditor first; fleet and garrisons first; balanced; self-financing (D4–D10);
- the price of each $1m, the instalment split against 1867, the refugee sizing, and sensitivity.

## Sources (for L17 and F18)

- [Give Lincoln Credit: How Paying for the Civil War Transformed the United States Financial System](https://www.albanygovernmentlawreview.org/article/23834-give-lincoln-credit-how-paying-for-the-civil-war-transformed-the-united-states-financial-system.pdf) (Albany Government Law Review): New York bank specie fell from $48m to $37m in the six weeks to 30 Sept 1861, while the sub-treasury's gold rose $13m; another third went from 7 to 28 Dec; the Northern state banks held $101m of specie in June 1861.
- [A History of Banking in the United States, ch. 16](https://en.wikisource.org/wiki/A_History_of_Banking_in_the_United_States/Chapter_16) (Wikisource): the contract of 15 August 1861 for $150m, in three instalments of $50m.
- [Banks of New York, suspension of 28 Dec 1861](https://www.finhist.com/bank-runs/episodes/15445.html) (New York Herald, 31 Dec 1861): the New York banks alone had advanced $80m to the government.
- [A History of the Greenbacks, notes on Mitchell (1903)](https://danallosso.substack.com/p/greenbacks-and-wealth-transfer): the New York associated banks' specie ratio was 50% in August 1861.
- [San Francisco directory, 1860](https://library.sfgenealogy.org/directory/san-francisco-county-directory/1860/1860_62.pdf): treasure exported in the first quarter of 1860, $8,663,875 of it to New York.
- [Imports and exports of treasure, 1862 and 1863](https://maritimeheritage.org/news/goods.htm) and [the shipment of 10 January 1863](https://www.maritimeheritage.org/passengers/SS-Golden-Age-21January1863.html) (Daily Alta California): $11.3m to New York in the first half of 1862 and $5.65m in the first half of 1863; England $1.34m and New York $0.35m on one steamer.
