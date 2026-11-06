# Design note: where Pacifica's lead comes from (CR-057 follow-up)

**Status:** DESIGN NOTE for the author's approval, 6 November 2026. Nothing in the storyline or the workbooks is changed by this note. Figures are MODEL; anchors marked *to verify* are not yet relied on.

**Authorization:** Author, 6 November 2026:
- "I agree that that's not the right way to calculate. However there must be a believable path to the old 2.4x. I feel like there is something we haven't considered here."
- On the proposal of a growth engine with research, diffusion, learning curves, selection, ordinary capital and income from abroad: "Yes that sounds much more accurate".

**Read with:** `finance/CR-057-workbook.md` (the rebuild of 5 November, and why it fell short); CR-020 B8–B10; CR-056 (the dynamics layer, `claude/CR-056-dynamics-workbook.md` in the claude.ai project, not yet in this repo); `outputs/research/20261105-mises-review/Mises-review.md` (MR-01, MR-07, MR-08, MR-11).

## 1. The finding: what the old model's lead is made of

Four recalculations of the current workbook, run with CR-057 switched off (Story case, 1929; "× US" is Economy R, money output per person against US history):

| Variant | × US | Real GDP ($m, 1913) | Residents (m) | Real GDP per resident ($) |
| --- | --- | --- | --- | --- |
| Base: no Development Fund return, no champions, no migration pull | 1.50 | 16,102 | 19.3 | 836 |
| + the migration pull (B10) | 1.55 | 20,631 | 24.0 | 859 |
| + the national champions (B9) | 1.67 | 25,789 | 27.4 | 943 |
| **+ the Development Fund's return (B8): the old model** | **2.37** | **44,374** | **33.4** | **1,330** |

- **The base is already about 1.5×.** That is `Paths!L`: a growth path at the level of the historical West and California, which CR-020 B2 put at about 1.4 times the United States. It is an input, and it is believable on its own: gold, oil, climate and a selected migrant population.
- **The Development Fund carries most of the rest:** 0.70 of the 0.87 points above the base. It does so through one coefficient: every dollar invested raises yearly output by 30 cents from the next year on, forever, with no depreciation, no diminishing return and no failures. Through the migration and champion loops it adds 41% to real output per resident by 1929.
- **So the old 2.4× was technology hidden inside a capital return.** The Fund's coefficient stood in for everything the storyline says makes Pacifica rich: the Polytechnic, the research institutes, the patents and the frontier industries. When CR-057 removed the Fund's surplus financing, it removed that stand-in, and the lead with it.

## 2. Why capital cannot carry it, and what can

In growth accounting, differences in output per worker this large come mostly from productivity and from the quality of the workforce, not from the amount of capital. That is the standard finding of cross-country studies (Hall and Jones 1999, *to verify*).

A simple Solow comparison shows why. Investing 28% of GDP against the Union's 20%, with Pacifica's faster population growth from immigration, raises output per worker by only a few percent in the long run. Diminishing returns absorb the rest, whoever owns the capital. A believable 2.4× therefore needs an explicit productivity engine, applied to every design in the same way.

## 3. The proposed structure

Every channel applies equally to the old Development Fund design and to CR-057's Patrimony, so that the comparison between them turns only on who pays and how.

| ID | Channel | Mechanism | Calibration (MODEL) | Anchors |
| --- | --- | --- | --- | --- |
| G1 | **Base** | `Paths!L` as now: a frontier pace that already holds the Union's own technology, including its electrification (CR-056 Q1) | unchanged | CR-020 B2 |
| G2 | **Research stock** | Research spending, public and private, accumulates into a knowledge stock that depreciates at 15% a year (as in CR-056 C3). Productivity rises with Pacifica's stock relative to the Union's, with a diminishing (logarithmic) effect. | Research intensity is a path for the author: about 0.3% of GDP in 1880, 1.5% in 1900, 2.5% in 1913 and 3% in 1929. The Union's is about 0.1–0.4% (*to verify*; US manufacturing research was under 0.5% of sales in the 1930s). The social return at Pacifica's intensity is set at 30–40%. | Hall, Mairesse and Mohnen (2010): private returns to R&D "somewhat higher than those for ordinary capital", social returns "even higher, although variable and imprecisely measured"; Jones and Williams (1998, *to verify*) |
| G3 | **Diffusion (MR-11)** | Open patents raise the share of the knowledge stock that every firm can use | about 0.9 of the stock usable under open licensing, against about 0.6 under exclusive licences (lever) | MR-11; CR-057 E |
| G4 | **Learning curves (MR-01: cheap inputs)** | In power, aluminium, steel, cars, chemicals and aircraft, unit cost falls a fixed share with every doubling of cumulative output. Pacifica produces far more per head, so it moves down the curves faster than the Union. Cheaper inputs lower downstream costs in proportion to their share of costs. | 15–25% per doubling (lever by sector) | Wright (1936): about 20% per doubling for aircraft; the Model T from about $850 to $260 in 1908–25 (*to verify*); CR-056's aircraft curve |
| G5 | **Selection** | Kept as now: the skilled-entry and talent channel (B10), "Output raised by the extra talent". The examination state's effect on residents' skills is optional and must not double-count G2. | as now | CR-020 B10, CR-034 |
| G6 | **Capital at ordinary returns** | Public and private investment both enter a capital stock that depreciates (4%), with the ordinary return (capital's share 0.3, so about 0.10–0.12 gross on the margin). Network infrastructure (grids, ports, rail) may carry a small premium for network effects that diminishes as the network fills. No 30% return on capital anywhere. | k_alpha 0.3, k_dep 4% (as in CR-056 mode 2); network premium 0–0.05 (lever) | CR-056 mode 2; MR-07 |
| G7 | **Income from abroad and resources** | As now (Abroad, Resources) | unchanged | CR-020 B4, B9 |
| G8 | **The champions, driven, not added** | The champions' world shares and costs respond to G2 and G4, as CR-056 C3 already does for electrical and chemical shares, rather than being an independent add-on. That avoids counting the same technology twice, once as productivity and once as champions' value added. | the champions' scale set by G2 and G4 | CR-056 C3 |

## 4. Does it reach about 2.4×? Illustrative arithmetic

Against the 1.5× base, the engine has to supply about ×1.6. The multiples below are the note's estimates, not workbook runs:

| Source | Rough multiple on the base by 1929 |
| --- | --- |
| G2 and G3: research and diffusion. Half a point to nine-tenths of a point of extra productivity growth a year from the mid-1880s compounds to ×1.25–1.5 by 1929. | ×1.25–1.5 |
| G4: learning curves in the energy-intensive and mechanical sectors | ×1.05–1.10 |
| G5: selection (the migration pull gives about ×1.03 in the decomposition) | ×1.03–1.05 |
| G6: capital deepening at ordinary returns | ×1.02–1.05 |
| G7 and G8: income from abroad, the champions' share (about ×1.08 in the decomposition) | ×1.05–1.08 |
| **Combined, on the 1.5× base** | **about 2.2–2.9× (middle about 2.5×)** |

**Cross-check on G2.** Pacifica's research intensity is above the Union's by about 1.5% of GDP on average over 1885–1929, and by about 2.5% at the end. At a 35% social return, that gives about half a point of extra growth a year on average, rising to about 0.9 points by the 1920s. That is the range in the table.

The 2.4× sits just below the middle of that range. It does not need a 30% return on capital. Each piece has a historical parallel:
- Swiss and Swedish research intensity in the 20th century;
- Singapore's selection of its workforce;
- Wright's learning curves;
- Britain's income from abroad before 1914.

## 5. What it means for CR-057 and the Patrimony

- **The question becomes who pays for research and public goods**, not who owns the capital. Pacifica's public share of research (the Polytechnic, the institutes, the Works' civilian research) is perhaps 1–1.5% of GDP by 1929. The Patrimony's 3% spending rule (about 0.6% of GDP in 1929) plus an ordinary research line in the budget can pay for it, with moderate taxes and no quarter-of-receipts surplus.
- **The champions' own laboratories** pay for the private share. Open patents (MR-11) spread what both produce.
- **Under G6, money left with citizens earns the same ordinary return as public capital.** The old and new designs then differ only in the network premium and in what the research budget is.
- **Falling prices (MR-01)** are judged in real terms, at the Union's prices, not by money income.

## 6. Coordination with CR-056

The dynamics layer (CR-056) already has:
- C1, unit electric drive;
- C3, research spillovers on the champions' world shares;
- C5, women's work;
- mode 2, capital accumulation with k_alpha 0.3 and 4% depreciation.

G2, G6 and G8 extend those channels rather than duplicating them. CR-056 is in the claude.ai project but not in this repository, so it should be merged first. The growth engine is then built as its next layer, with the old and CR-057 designs run on it side by side.

One caution from CR-056's known limits applies to G2: the Works' halls and diffusion plant are production spending, not research. Only the Works' civilian research counts in the research stock.

## 7. Decisions for the author

1. **The research-intensity path** (G2): about 0.3% → 1.5% → 2.5% → 3% of GDP, or another. It is the main driver, and the story can show it (the Polytechnic, the institutes, the champions' laboratories).
2. **The social return to research** at that intensity: 30% (cautious) or 40%.
3. **Diffusion under open patents** (G3): 0.9 against 0.6 for exclusive licences.
4. **The learning rates** (G4), by sector.
5. **A network premium** for grids, ports and rail (G6): none, or small and diminishing.
6. **The champions driven by G2 and G4** (G8), replacing the add-on.
7. **Order of work:**
   - merge CR-056 into the repository;
   - build the engine;
   - run the old design and CR-057 on it with falling prices;
   - report the same old-against-new table as the 5 November rebuild, and the storyline's MODEL figures.

## Anchors to verify

- Hall and Jones (1999), "Why do some countries produce so much more output per worker than others?"
- Hall, Mairesse and Mohnen (2010), "Measuring the returns to R&D" (NBER w15622): quoted above.
- Jones and Williams (1998) on social returns and the optimal level of research.
- US research and development as a share of GNP in the 1920s and 1930s (the NBER chapter c2121 gives manufacturing research at under 0.5% of sales in the 1930s).
- Wright (1936), "Factors affecting the cost of airplanes".
- Model T prices, 1908–25.
- Aluminium prices after 1890.
- Historical Swiss and Swedish research intensity.
