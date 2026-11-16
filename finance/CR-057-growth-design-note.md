# Design note: where Pacifica's lead comes from (CR-057 follow-up)

**Status:** DESIGN NOTE, fourth draft, 6 November 2026; every decision taken (10:06), ready to build. The third draft records the author's 09:48 decisions and checks the anchors the author supplied then: Irwin and Klenow, Lieberman, Blank and Stigler, ETH Zurich and Sweden, and a table on steel. Nothing in the storyline or the workbooks is changed by this note. Figures are MODEL. The multiples in §5 are the note's estimates, not workbook runs. This draft checks the first against the sources the author supplied (§3) and revises the construction (§4).

**Authorization:** Author, 6 November 2026:
- "I agree that that's not the right way to calculate. However there must be a believable path to the old 2.4x. I feel like there is something we haven't considered here."
- On the proposal of a growth engine with research, diffusion, learning curves, selection, ordinary capital and income from abroad: "Yes that sounds much more accurate".
- 09:18, preliminary answers to the first draft's §7: "1. start at 0.6% otherwise ok. 2. 35% (very significant research being done) 3. 0.9 4. please make a suggestion 5. please make a suggestion 6. approved". Then: "Please use the attached texts, which you requested, to verify the numbers and critique the construction of the model once more, then report back to me before building." With the NYC price of primary aluminium ingot, 1895–1940.
- 10:06: steel's learning rate "about 24% seems defensible" (Ohashi 2004); "For 1a, I agree that 2% is the more defensible figure." CR-056 lives in the financial workbook on branch `finance/dynamics-layer` (PR #65).
- 09:48, with the anchors: "I would say we should aim high as the story is supposed to present an impressive but believable alternative history. For the 35% I would therefore say research directed at industrial goals and close to industry."

**Read with:**
- `finance/CR-057-workbook.md` (the rebuild of 5 November, and why it fell short);
- CR-020 B8–B10;
- CR-056 (the dynamics layer, `claude/CR-056-dynamics-workbook.md` in the claude.ai project, not yet in this repo);
- `outputs/research/20261105-mises-review/Mises-review.md` (MR-01, MR-07, MR-08, MR-11).

**Sources read** (the author's copies, not in the repo; page numbers are printed pages). The third draft adds Irwin and Klenow (1994), Lieberman (1984), Blank and Stigler (1957), Gugerli, Kupper and Speich (2010), the Riksdag statement of 1928 and Kaiserfeld (2013). The second draft read:
- Hall and Jones (1999), *QJE* 114: 83–116;
- Jones and Williams (1998), *QJE* 113: 1119–1135;
- Hall, Mairesse and Mohnen (2010), "Measuring the returns to R&D" (the CIRANO 2010s-02 version of NBER w15622);
- Wright (1936), *Journal of the Aeronautical Sciences* 3: 122–128;
- Moser (2013), "Patents and innovation: evidence from economic history", *JEP* 27(1);
- Mowery and Rosenberg (1998), *Paths of Innovation*;
- McCalley (1994), *Model T Ford*;
- USGS Data Series 140, aluminium statistics (production, and unit values in 1998 dollars).

Separate agents read the books and papers. Their quotations are kept in the session folder (`outputs/sessions/20261105-cr057-economic-order/growth-sources.md`).

## 1. The finding: what the old model's lead is made of

Four recalculations of the current workbook, run with CR-057 switched off (Story case, 1929; "× US" is Economy R, money output per person against US history):

| Variant | × US | Real GDP ($m, 1913) | Residents (m) | Real GDP per resident ($) |
| --- | --- | --- | --- | --- |
| Base: no Development Fund return, no champions, no migration pull | 1.50 | 16,102 | 19.3 | 836 |
| + the migration pull (B10) | 1.55 | 20,631 | 24.0 | 859 |
| + the national champions (B9) | 1.67 | 25,789 | 27.4 | 943 |
| **+ the Development Fund's return (B8): the old model** | **2.37** | **44,374** | **33.4** | **1,330** |

- **The base is already about 1.5×.** That is `Paths!L`: a growth path at the level of the historical West and California, which CR-020 B2 put at about 1.4 times the United States. It is an input.
- **The Development Fund carries most of the rest:** 0.70 of the 0.87 points above the base. It does so through one coefficient: every dollar invested raises yearly output by 30 cents from the next year on, forever, with no depreciation, no diminishing return and no failures.
- **So the old 2.4× was technology hidden inside a capital return.** When CR-057 removed the Fund's surplus financing, it removed that stand-in, and the lead with it.

**What the storyline actually needs.** The storyline's MODEL figure is "about 2.24 times the Union's in 1929" (master storyline, the CR-021 I/H paragraph, held within 10% by CR-056's tests). The same paragraph says "The prosperity comes from champions, talent, oil and partner growth", and that "The Union remains the larger power in real output". So the target is about 2.24× (2.0–2.46× within the 10% band), not 2.4×. Nothing in canon names the Fund's return as the source.

## 2. Why capital cannot carry it

Corrected against Hall and Jones (1999):

> In cross-country levels accounting (127 countries, 1988), physical capital and years of schooling explain only part of the 31.7-fold gap in output per worker between the richest and poorest five countries. Capital intensity contributes a factor of 1.8, schooling 2.2 and the productivity residual 8.3 (p. 92). The authors trace all three to "social infrastructure", "the institutions and government policies that determine the economic environment" (p. 84).

Two corrections to the first draft:
- **Hall and Jones measure years of schooling, not workforce quality.** Their cause is institutions, which raise capital, schooling and productivity together. That suits Pacifica, but it does not by itself support a research channel; G2 rests on Jones and Williams and Hall, Mairesse and Mohnen instead.
- **The Solow arithmetic gives about 7–8%, not "a few percent".** With K/Y = s/(n + g + δ): the Union is 0.20/(0.02 + 0.015 + 0.04) = 2.67, and Pacifica 0.28/(0.035 + 0.015 + 0.04) = 3.11. The ratio is 1.167, so output per worker rises by 1.167^0.5 = 1.08 with Hall and Jones's α = ⅓, or 1.167^0.43 = 1.07 with α = 0.3. Faster population growth from immigration cancels more than half the gain from investing more (without it the gain would be 18%).

## 3. The first draft checked against the sources

| First draft | Source | Verdict |
| --- | --- | --- |
| HMM: private returns "somewhat higher than those for ordinary capital", social returns "even higher, although variable and imprecisely measured" | HMM abstract: "In general, the private returns to R&D are strongly positive and somewhat higher than those for ordinary capital, while the social returns are even higher, although variable and imprecisely measured in many cases." | Quote fair; full wording adopted |
| Social return 30–40% | JW: "a conservative estimate of the social return of 30 percent" (p. 1121); their regression gives 0.35–0.37 (p. 1131); broad estimates "nearly 100 percent" (p. 1129). HMM case studies: median social 56%, private 25% (p. 25). | Supported, **but only as a marginal return at US post-war intensities** |
| A constant 35% applied to a gap of 5–10 times the Union's intensity | JW's own model: the return is λ·g/s, inversely proportional to research intensity s (eq. 14, p. 1130). At the optimum (2–4 times actual US research) it falls to the interest rate, about 7% (p. 1133). "Stepping on toes" and "fishing out" are the reasons (p. 1125). | **Not defensible.** The first draft's ×1.25–1.5 for research was too high (see G2) |
| 15% depreciation of the research stock | HMM: "most researchers use the 15 per cent that Griliches had settled on"; estimates run from 10% to 36% (electrical firms) (p. 15). | Supported as a convention; test 10–25% |
| Research intensity of the Union 0.1–0.4% of GDP | Mowery and Rosenberg: 2,775 research scientists and engineers in manufacturing labs in 1921, 6,274 in 1927, 27,777 in 1940 (Table 1, pp. 21–22). Federal research was 12–20% of the US total in the 1930s, and $74.1m in 1940 (p. 27). That puts the US total near 0.4–0.6% of GNP in 1940 (inferred), and lower in the 1920s. | Supported. The 1920s were nearer 0.1–0.3%; the Union path is set at 0.05% (1880) → 0.1% (1900) → 0.15% (1913) → 0.25% (1929) |
| Wright: "about 20% per doubling for aircraft" | Wright's 80% curve is **cumulative-average labour cost of one design in one plant**, observed up to about 200 units (pp. 122–125). Raw material falls 5% per doubling, purchased material 12% and overhead 30%; the whole airplane falls 17% per doubling at first, flattening to 10% (p. 126). | **Corrected**: 20% is labour only; the whole product falls 10–17% |
| Model T from about $850 to $260 in 1908–25 | McCalley: the Touring went from $850 (1909 model year, "without top, windshield and gas lamps") to $290; the Runabout from $825 to $260 (from 2 December 1923, p. 309). War inflation took the Touring from $360 (1917) to $575 (March 1920). Cumulative output was about 15.1 million. | **Corrected**: two body styles mixed. Price per doubling falls about 10% in money and 15% after deflation (fit 1909–25, R² 0.92 real) |
| Open patents: usable share 0.9 against 0.6 | Moser: no number exists; most knowledge is never patented (p. 40); open licensing raised US chemical patenting about 20% with an 8–9 year lag (p. 38) | **Construction revised**: lag and patented share (G3) |

## 4. The revised construction

Every channel applies equally to the old Development Fund design and to CR-057's Patrimony, so the comparison turns only on who pays and how.

### G1. Base

`Paths!L` as now: a frontier pace that already holds the Union's own technology, including its electrification (CR-056 Q1). Unchanged.

### G2. Research stock: an elasticity, not a constant return

- **Stock.** Research spending (public and private) accumulates into a stock that depreciates at 15% a year (lever, test 10–25%). It enters with a lag: a mean of 3–5 years for applied and private research, and 10–20 years for the Polytechnic, the institutes and basic science (HMM p. 16: "a mean lag from 4 to 6 years"; Adams: 20 years for own R&D, 10 to 30 for basic research).
- **Effect on productivity.** ln(Pacifica's TFP / the Union's TFP) = γ × ln(Pacifica's effective stock per unit of output / the Union's).
  - **Effective stock:** own stock plus the foreign stock it can absorb. Absorption rises with own research, because firms need their own laboratories to use outside knowledge (Mowery and Rosenberg p. 69: the aircraft industry's own R&D "has been essential to the absorption and application of technologies developed outside its boundaries"; HMM p. 31).
  - **Leakage:** about a quarter of Pacifica's stock adds to the Union's effective stock (Coe and Helpman, in HMM p. 30: "roughly a quarter of the benefits from R&D in G-7 countries accrues to their trading partners").
  - **Returns diminish automatically.** With γ constant, the marginal return is γ × output / stock. It falls as the stock grows, as JW's model requires.
- **The author's 35% (decided 09:48)** is the return on research "directed at industrial goals and close to industry". It is held at the lower intensity of the 1900s, and returns diminish from there. That gives **γ = 0.12**, between HMM's firm-level centre ("0.01 to 0.25 but centered on 0.08", p. 21) and the G7 country-level estimates of 0.20–0.22, which are biased upward. At 3% intensity in 1929 the net return at the margin is then about 68%, still within the range of HMM's case-study social returns (median 56%) and JW's broad estimates ("nearly 100 percent"). The narrower reading (35% at the margin in 1929, γ ≈ 0.07) is kept as the cautious variant.
- **What it gives.** On the author's path (0.6% → 1.5% → 2.5% → 3%) against the Union's path, Pacifica's effective stock per unit of output is about 4–6 times the Union's in 1929. The research channel then raises productivity by:

| γ | Net return at the margin, 1929 | × TFP by 1929 |
| --- | --- | --- |
| 0.07 (the author's 35%) | 35% | ×1.11–1.14 |
| 0.08 (HMM firm-level centre) | 40% | ×1.12–1.16 |
| 0.12 | 68% | ×1.19–1.25 |
| 0.20 (G7 country-level, biased upward, HMM p. 28) | 120% | ×1.33–1.43 |

- **Public research** gets a weight of 0.5–0.7 against private research (HMM p. 19 and p. 32: lower returns to publicly funded R&D), unless the story shows it is mission-directed and close to industry. Pacifica's Polytechnic and institutes are drawn that way, so a weight of 0.8 is defensible.
- **Only research counts.** The Works' halls and diffusion plant are production spending (CR-056's known limits). Development ("roughly two thirds of U.S. R&D investment constitutes 'D'", Mowery and Rosenberg p. 173) belongs here. Learning from production belongs in G4.

**What 3% of GDP means on the page.** At about three times average earnings per research worker (salary, technicians, equipment), 3% of Pacifica's 1929 output pays for roughly 250,000 research workers. About 100,000 of them would be scientists and engineers, or about 3 per 1,000 residents. That is two-thirds of today's US level, against the Union's 0.1–0.2 per 1,000 (6,274 in industrial laboratories in 1927).

The supply of graduates is the binding limit:
- **Blank and Stigler**, *The Demand and Supply of Scientific Personnel* (NBER 1957), "The Supply of Engineers":
  - US first degrees in engineering averaged 7,420 a year in 1921–25 and 7,760 in 1926–30 (Table 30, p. 75);
  - engineers trained without a degree added "perhaps two-thirds to the number of engineering graduates" (p. 86);
  - only about 15% of bachelors worked in "development and applied research" (p. 91; a 1946 figure).
- **ETH Zurich** (Gugerli, Kupper and Speich 2010): "between 100 and 300 students a year" graduated in the 19th century (p. 65), about 335 in 1929 from about 1,600 students (Figures 1 and 6, read from the charts). Until 1900 about half the students were foreign, and about half the graduates worked abroad.
- **Sweden.** The Riksdag's Statsutskottet granted 75,000 kronor in 1928 for IVA's research on power and fuel (utlåtande nr 10, 24 April 1928). Kaiserfeld (*Minerva* 51, 2013) gives the Royal Institute of Technology's public allocation as SEK 360,000 in 1919. Public research was in the hundreds of thousands of kronor, far below 0.1% of GDP.
- **Swiss research spending.** Ruzicka put Swiss chemical industry research at about 10 million francs a year around 1942 (Gugerli et al. p. 175), about 0.1% of GDP. The first national figure is 2.1% of GNP in 1969.

| New scientists and engineers a year, per 100,000 residents | Rate |
| --- | --- |
| US engineering degrees, 1920s | about 6.5 |
| US, including engineers without a degree | about 10.5 |
| ETH graduates, 1900–1929 (half of them foreign) | about 8–10 (16 at the 1920 peak) |
| **Pacifica at 3% (9,000–10,000 a year on 33m)** | **27–30** |
| Pacifica at 2% (about 6,000–6,500 a year) | 18–20 |

**No country before 1940 spent 1–3% of GDP on research** (none is found in these sources; Switzerland and Sweden were near 0.1%). Pacifica at 3% needs about 45,000–50,000 science and engineering students by the 1920s. That means 8–12 polytechnics the size of a large modern one, or about thirty ETHs, plus the secondary schools to feed them and a stream of several thousand émigré scientists after 1918.

That is impressive, but it strains "believable". Two ways through (decision 1a):
- **Keep 3%**, and make it a story commitment: the examination state's polytechnics, émigrés from Russia and Central Europe after 1918, and most of the "D" in R&D done by engineers trained on the job (Blank and Stigler's two-fifths without a degree).
- **Lower the path to 0.6% → 1.2% → 1.8% → 2% (1929).** This still has no precedent, at about ten times the Union. Because returns diminish, it gives up only about 3 points of the research channel at γ = 0.12 (×1.20–1.21 against ×1.24–1.25). The pipeline is then about twice ETH's rate per head.

### G3. Diffusion under open patents (MR-11): a faster lag on the patented part

Moser has no number for "the share of the knowledge stock usable by every firm". What her evidence supports:
- **Patents change the direction of invention more than its rate.** Countries without patent laws innovated at similar rates, "focused on a narrow set of industries in which secrecy was effective" (p. 30). Patent laws "may influence the direction of technological change and help to encourage the diffusion of knowledge, even though patent laws do not appear to be a necessary or sufficient condition for higher rates of innovation" (p. 33).
- **Most knowledge is never patented.** "In countries with patent laws, the majority of innovations occur outside of the patent system" (p. 40). About 19–20% of US chemical innovations were patented in 1893 and 1915, and 44–49% in machinery (p. 31). Open licensing can act only on that part.
- **Open licensing works with a lag.** Under the Chemical Foundation's nonexclusive licences of German patents from 1919, domestic patenting rose about 20%, "with a lag of eight to nine years" (p. 38).
- **Licences do not carry know-how.** Licensees "typically cannot access the uncodified knowledge that is embodied in skilled workers and scientists" (p. 39). Mowery and Rosenberg make the same point: "U.S. experts could not replicate the Haber-Bosch process" despite the seized patents (p. 75).
- **There is an incentive cost.** Patents are an effective protection only "for pharmaceuticals and chemical inventions" (p. 31). Compulsory licensing may discourage domestic invention "if it displaces domestic research and development" (p. 37).
- **Fixed, equal royalties are the right form.** The sewing-machine pool's unequal fees "diverted the research investments of outside firms towards technologically inferior substitutes" (p. 37).

**Revised construction.** The author's 0.9 against 0.6 is kept as the usable share of *patented* knowledge (decision 3), applied to the patented share by sector (about 20% in chemicals, about 45% in machinery and electrical). Three further changes:
- **Adoption lag:** 3–5 years under open licensing against 6–10 under exclusive licences.
- **Absorption:** the usable share is reached only by firms with their own laboratories (G2's absorption term).
- **Incentive loss:** a small cut in the private research share in chemicals and drugs, partly made good by the royalty.

The net effect is about ×1.01–1.03 by 1929, more as a story of speed than of level.

### G4. Learning curves, counted once

Construction, corrected against Wright and Mowery and Rosenberg:
- **The rate applies to the whole product, not to labour.** Use Wright's whole-airplane curve, or industry price series, not his 80% labour curve.
- **Experience: own output counts more, the world's counts too (Irwin and Klenow 1994).** Learning rates in semiconductors "average 20 percent", and firms "learn three times more from an additional unit of their own cumulative production than from an additional unit of another firm's cumulative production". Spillovers are as strong between countries as within them: "learning spills over just as much between firms in different countries as between firms within a given country" (abstract, p. 1200; α and γ "average .28 and .32", p. 1217). So experience is
  - Pacifica: E = Q_Pacifica + 0.3 × (Q_world − Q_Pacifica);
  - Union: E = Q_Union + 0.3 × (Q_world − Q_Union).
  
  The fixed one-third share is dropped. Pacifica's advantage then grows with its share of world output: about 77% of its experience is its own at half of world output, under 30% at a tenth. Wright's supplier, who "is constantly manufacturing in greater quantities" (p. 125), is the same idea.
- **Count each sector's gain once.** It enters at the sector's gross output relative to GDP (Hulten weights). It is not passed downstream again. Most of the price fall goes to buyers, many of them abroad, under MR-01's tight margins. What Pacifica keeps shows up as the champions' larger world shares (G8), not as a separate addition.
- **No overlap with G2 or G6.** Tooling is capital (G6), and design and process improvement is development (G2). G4 is pure learning by doing.

**The aluminium curve from the author's series.** The author's NYC ingot prices match USGS's unit values. Deflated (USGS's 1998-dollar series) against world cumulative primary output (USGS; the stock to 1899 estimated at about 28,000 t), leaving out the war years 1907 and 1915–20:

| Fit | Learning rate per doubling | Doublings |
| --- | --- | --- |
| 1900–1929 | 16–20% (starting stock halved or doubled) | 5.5–7.0 |
| 1909–1929 | 14–15% | about 4 |
| 1900–1913 | 15–22% | 3–4 |

- The curve flattens as the industry matures: 1909–29 gives about 14–15%.
- **The price is Alcoa's, not a cost.** After the Hall patent expired in 1909 the nominal price held near 22–24 cents for twenty years, so the real fall from 1909 to 1929 is entirely general inflation. A competitive Pacifican industry with cheap Columbia power could fall faster.

**Suggested learning rates (author's decision 4).** Per doubling of world cumulative output, on the whole product:

| Sector | Rate | Basis |
| --- | --- | --- |
| Aluminium | 15% | The author's series: 14–18% (1900–29), 14–15% (1909–29) |
| Electric power (equipment and fuel rate; none on hydro civil works, which are site-specific) | 10% | Coal per kWh from almost 7 lb in 1900 to under 0.9 lb by the 1960s; household power 7.45 → 6.03 cents a kWh, 1920–30 (Mowery and Rosenberg pp. 105, 117) |
| Steel | **24% to 1900, fading to 15% by 1929** (author, 10:06: "about 24% seems defensible") | **Ohashi (2004)**, "Learning by doing, export subsidies, and industry growth: Japanese steel in the 1950s and 1960s" (CIRJE-F-280; *J. Int. Econ.*), six integrated firms, 1955–65: "The learning rate obtained is 24 percent", with input prices (iron ore, labour) controlled (p. 19). It also finds "little knowledge spilled over from one steel firm to another", which he attributes to permanent employment (p. 20). The later fade follows Ghemawat (1985), cited there: "79 of 97 examined" products fall in 11–21%. **Head (1994)**, *J. Int. Econ.* 37: 141–165: "despite strong learning effects, the steel rail tariff hurt rail users in both the short and long runs"; "The tariff's overall effect on welfare was positive but fairly small." The paper is real, but no numeric learning rate was found in accessible text, so 20% is a judgement. **There is no source for any rate after 1900.** The table supplied with the anchors is partly wrong (see below) |
| Motor vehicles | 15% | The Model T, 1909–25: about 10% in money and 15% after deflation per doubling, over about ten doublings (McCalley's prices and production). The price is Ford's volume strategy ("With the product's cost reduced, its sales price could be lowered", p. 144), not quality-adjusted, and it mixes in the moving line (chassis assembly from 12½ hours to 2 hours 57 minutes in 1913, p. 148), which is partly G2 |
| Chemicals | 15% (band 15–19%) | **Lieberman (1984)**, 37 products, late 1950s–1972: price falls 28% per doubling of cumulated industry output (coefficient −.471); 23.5% with plant scale controlled (−.387); and 19% with cumulated capacity also included (−.303) (Table 3, p. 219). "More than half … between 70% and 80%" (p. 221). About 15% of the decline is scale and 85% cumulated output (p. 221). R&D and capital intensity "steepen the learning curve" (p. 227), and the improvements are "embodied in plant and equipment". Price is not cost: it shifts with "profit margins" (p. 215). The gross 24–28% includes scale, embodied capital and margins, which belong to G6 and G2, so pure learning is at most 19%. Also Mowery and Rosenberg p. 80: organic chemicals not made from coal tar fell from 43 to 13 cents a lb, 1921–39 |
| Aircraft | 15% at first, 10% later | Wright's whole airplane, 17% → 10% (p. 126); cost per seat-mile 2.63 cents (Ford Trimotor, 1928) → 1.27 (DC-3, 1936) (Mowery and Rosenberg p. 63) |

These rates fade as each industry matures (the aluminium fit shows it). Pacifica's net gain over the Union is about ×1.02–1.04 by 1929.

**The steel table supplied with the anchors (09:48)**, checked:

| Row | Finding |
| --- | --- |
| Head (1994), US steel rails, 1867–1895, "~20–25%" | The citation and the "strong learning effects" are verified. The 20–25% rate, the window and "costs below British imports" are not found in accessible text |
| Pig iron, "elasticity about −0.37 (1 − 2^−0.37 ≈ 23–29%)" | **The arithmetic is wrong**: 1 − 2^−0.37 = 22.6%. No study giving −0.37 was found. The nearest are unpublished drafts by Naknoi, with US coefficients of −0.22 to −0.44 |
| Allen (1977, 1979), "collective invention, Cleveland and Pittsburgh, 1870–1900" | The papers are real (*JEH* 37: 605–633; *JEH* 39: 911–937), but neither abstract gives a learning rate. "Collective invention" is Allen (1983), *JEBO* 4: 1–24, and concerns England's **Cleveland district, 1850s–1870s**, not Pittsburgh |
| "Post-1900 steel <5%" | No source found; not used |

### G5. Selection

Kept as now: the skilled-entry and talent channel (B10), "Output raised by the extra talent". The migration pull gives about ×1.03 in the decomposition. Schooling under the examination state is optional and must not double-count G2.

### G6. Capital at ordinary returns, with a network premium

- **Ordinary capital.** Public and private investment both enter a capital stock that depreciates at 4%, with capital's share 0.3 (as in CR-056 mode 2). The gross marginal return is then about 0.10–0.12. Hall and Jones and the Solow arithmetic give about ×1.07–1.08 by the late 1920s for 28% investment against the Union's 20%.
- **Suggested network premium (author's decision 5).** Core network capital only: the grid, trunk rail, the ports and the canal. Not halls, buildings or plant.
  - **Size:** a premium of 0.08 on the margin while the network is being built, so about 0.18–0.20 gross at first. It falls to zero as the network reaches its planned extent: premium = 0.08 × (1 − coverage). Coverage for the grid is homes wired (the energy workbook: 44% in 1913, 86% in 1924, 96% in 1929). Coverage for rail and ports is route-miles and berths against the plan.
  - **Anchors:** Bom and Ligthart (2014), a meta-analysis: "a short-run output elasticity of public capital supplied at the central government level of 0.083, which increases to 0.122 in the long run", and "almost doubled" for core regional infrastructure. Fernald (1999): "the interstate system was highly productive, but a second one would not be." That is the shape of the premium: high while the first network is built, gone once it is complete.
  - **Size of the effect:** about ×1.01–1.03 by 1929, on top of the ordinary return.

### G7 and G8. Income from abroad and resources; the champions driven, not added

- G7 as now (Abroad, Resources).
- G8 (approved): the champions' world shares and costs respond to G2 and G4, as CR-056 C3 already does for the electrical and chemical shares, rather than being an independent add-on. Together about ×1.05–1.08, the champions' ×1.08 in the decomposition.

## 5. Does it reach the storyline's 2.24×? Revised arithmetic

| Source | Cautious (the author's 35%) | Central | Upper |
| --- | --- | --- | --- |
| G1 base | 1.50 | 1.50 | 1.50 |
| G2 research (γ 0.07 · 0.08 · 0.12) | ×1.11 | ×1.13 | ×1.22 |
| G3 diffusion | ×1.01 | ×1.02 | ×1.03 |
| G4 learning curves | ×1.02 | ×1.03 | ×1.04 |
| G5 selection | ×1.03 | ×1.03 | ×1.04 |
| G6 capital and network premium | ×1.07 | ×1.075 | ×1.09 |
| G7 and G8 abroad, resources, champions | ×1.05 | ×1.065 | ×1.08 |
| **Combined, 1929** | **about 2.0×** | **about 2.1×** | **about 2.4×** |

- **The author chose the upper column (09:48): "aim high"**, on the 2% research path (10:06). With γ = 0.12 and the network premium, the engine gives about 2.35× in 1929 (about 2.4× on the 3% path). The storyline's MODEL figure (2.24×) is then re-synced from the workbook after the build.
- **The storyline's 2.24× is also reached** at the central-to-upper values, and the cautious case sits at the bottom of its 10% band.
- **The old 2.4× needs the upper column:**
  - research elasticity 0.12 (a 68% net return at the margin, between HMM's median case-study social return of 56% and JW's broad estimates);
  - strong absorption and diffusion;
  - the network premium.
  - The story can support that: mission-directed applied research close to industry, open patents and in-house laboratories everywhere. But it is the top of what the evidence allows, not the middle.
- **The first draft overstated research** by applying a constant 35% to a gap far outside the measured range. Diminishing returns take most of it back. That is the main revision.

## 6. What it means for CR-057 and the Patrimony

- **The question becomes who pays for research and public goods**, not who owns the capital. The public share of research (the Polytechnic, the institutes, the Works' civilian research) is perhaps 1–1.5% of GDP by 1929. The Patrimony's 3% spending rule (about 0.6% of GDP in 1929) plus an ordinary research line in the budget can pay for it, with moderate taxes and no quarter-of-receipts surplus.
- **The champions' own laboratories** pay for the private share. Open patents (MR-11) spread what both produce.
- **Under G6, money left with citizens earns the same ordinary return as public capital.** The old and new designs then differ only in the network premium and in the research budget.
- **Falling prices (MR-01)** are judged in real terms, at the Union's prices, not by money income. CR-056 already reports both: Pacifica's GDP prices are about 1.17 times the Union's in 1929.

## 7. Coordination with CR-056

The dynamics layer (CR-056) already has:
- C1, unit electric drive;
- C3, research spillovers on the champions' world shares;
- C5, women's work;
- mode 2, capital accumulation with k_alpha 0.3 and 4% depreciation.

G2, G6 and G8 extend those channels rather than duplicating them. CR-056 is in the claude.ai project but not in this repository, so it should be merged first. The growth engine is then built as its next layer, with the old and CR-057 designs run on it side by side.

## 8. Decisions for the author

| # | Decision | Status |
| --- | --- | --- |
| 1 | Research path: 0.6% (1880) → 1.5% (1900) → 2.5% (1913) → 3% (1929) | Decided (09:18); superseded by 1a |
| 1a | Keep 3%, or lower the path? | **Decided (10:06): 0.6% (1880) → 1.2% (1900) → 1.8% (1913) → 2% (1929)**, "2% is the more defensible figure" (G2) |
| 2 | Social return 35% | Decided (09:48): research directed at industrial goals and close to industry, so γ = 0.12 (G2) |
| 3 | Diffusion 0.9 against 0.6 | Decided (09:18). Kept as the usable share of *patented* knowledge, with a faster adoption lag and an incentive loss in chemicals (G3) |
| 4 | Learning rates by sector | Suggested in G4: aluminium 15%, power 10%, steel 24% → 15% (author, 10:06), motor vehicles 15%, chemicals 15%, aircraft 15% → 10%. Experience E = own output + 0.3 × the rest of the world's (Irwin and Klenow), with no national premium |
| 5 | Network premium | Suggested in G6: 0.08 × (1 − coverage), core network only. "Aim high" (09:48) is read as adopting it |
| 6 | Champions driven by G2 and G4 | Approved (09:18) |
| 7 | Target | Decided (09:48): "aim high". The upper column, about 2.4×; the storyline's figure is re-synced after the build |
| 8 | Order of work | Merge CR-056; build the engine; run the old design and CR-057 on it with falling prices; report the old-against-new table and the storyline's MODEL figures. CR-056 is in the financial workbook on branch `finance/dynamics-layer` (PR #65, open; author, 10:06). The engine is built on that branch's workbook: it keeps C1 unit drive and C5 women's work, extends mode 2's capital stock (G6), and supersedes C3 (G2 and G8) |

## Anchors

**Verified in the sources the author supplied** (pages as above):
- Hall and Jones;
- Jones and Williams;
- Hall, Mairesse and Mohnen;
- Wright;
- Mowery and Rosenberg;
- Moser;
- McCalley;
- Irwin and Klenow (1994), *JPE* 102: 1200–1227;
- Lieberman (1984), *RAND J.* 15: 213–228;
- Blank and Stigler (1957), "The Supply of Engineers";
- Ohashi (2004), CIRJE-F-280;
- Gugerli, Kupper and Speich (2010);
- Riksdagen, Statsutskottets utlåtande nr 10 (1928);
- Kaiserfeld (2013), *Minerva* 51 (quotes from the publisher's page; to check against the PDF).

**Verified online:**
- USGS DS140 aluminium statistics;
- the abstracts of Bom and Ligthart (2014), Fernald (1999), Head (1994) and Allen (1977, 1979, 1983).

**To verify:**
- a numeric learning rate for steel before 1914 (Head's estimate is not in accessible text; Ohashi's 24% is for 1955–65);
- US census counts of engineers, 1900–1930;
- the US research share of GNP in the 1920s, inferred from research staff and the 1930s federal share.
