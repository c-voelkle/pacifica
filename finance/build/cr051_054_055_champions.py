"""Put the costs and output of CR-051, CR-054 and CR-055 into the financial workbook.

    python3 finance/build/cr051_054_055_champions.py IN.xlsx ENERGY_OUTPUTS.csv OUT.xlsx

IN is the CR-052 workbook (cr052_energy_link.py built on the CR-050 workbook). ENERGY_OUTPUTS.csv
is written by energy/build/export_energy.py from the energy workbook. The script never
recalculates; run LibreOffice (xlsx skill scripts/recalc.py) afterwards.

Authorization: the author, 4 November 2026, after PR #63: "put the costs and output of
CR-051, CR-054 and CR-055 into the financial workbook. Do not change any storyline canon.
Report back to me before merging."

What it does (all amounts MODEL):

CR-051 (sheet "Works", linked into "Atomic"): the magnet halls at a multiple of Y-12's
construction cost (lever halls_y12) on CR-051 M2's timetable, their operation by the energy
workbook's draw, Ralston College's thermal-diffusion feed plant with its oil-fired powerhouse,
the Columbia station at White Bluffs (towns bought out, piles, separation plant, company town,
Roslyn steam, the experimental breeder), the gaseous-diffusion pilot and plant, the Works' dams
on the Pit and the upper Feather and the Rock Island dam with its line (investment, like the
atomic power stations), the White Bluffs fee and the royalties on the Works' dams (CR-051 S8),
Rock Island's sales to Wenatchee and the Basin, and the Mint's silver (memo). The separation
chain is government consumption, as CR-052's account already counts the halls; the dams are
investment. The CR-050 hall rows it replaces (construction 1917-1923, enlargement 1928-1930,
operation and hydro power) come out of Atomic!O; the weapon engineering, the security and the
tests stay. The uranium quantities do not change (the storyline quotes them).

CR-054 and CR-055 (sheet "Electro champions", linked into "Champions"): aluminium at A1's
amounts by destination (the Realm and the Concord at the pool's price; the third beyond the
Concord at the world price, which falls in 1931-32), its first fabrication, and the aircraft
and engines, in Champions!AO; electrolytic and Haber-Bosch nitrogen, electric steel's premium,
magnesium, phosphorus, synthetic rubber and hydrogenation in a new Champions column (BF), added
to the champions' value added at home and the competitive industries' profits. Electrolytic zinc
and copper refining are memos: the metals series (Resources!F) values them at the metal's price. Electric pig iron is a change of process, not new output (memo). The copper
the Great Salt Lake refines is reconciled with the metals series (Resources!F). Arkansas bauxite
and the alumina refinery appear as Gulf trade (memo). Plant investment is counted.

The investment account (sheet "Energy link", new columns): the energy workbook's power
investment becomes the account's first identified component, counted once: the Works' dams and
Rock Island at their CR-051 cost instead of the energy workbook's generic cost, the Columbia's
second units at a lower cost (lever col2_cost), plus the Columbia-Sierra line; then the atomic
stations, the CR-054/055 works and public works, and the rest of investment as a residual that
must not be negative. Financing: the Treasury builds the Works' dams (through Atomic); the
Development Fund's credit (dev_share and df_max as in the energy workbook, CR-052 F12 not
decided here) on the rest; the power estate's bonds for its own dams, the second units and the
line; the Reserve Bank buys part of the estate's issues in 1930-1932 (Gold & money); a market
test for the Treasury's and the estate's bonds together.
"""
from __future__ import annotations

import argparse
import copy
import csv
import sys
from pathlib import Path

import openpyxl
from openpyxl.utils import column_index_from_string as cidx
from openpyxl.utils import get_column_letter as col

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / "energy" / "build"))
import cr041_russian_war as base  # noqa: E402
import cr050_atomic_retiming as c50  # noqa: E402
import energy_inputs as ein  # noqa: E402

AUTHOR = "CR-051/054/055, 4 Nov 2026"
base.AUTHOR = AUTHOR
FIRST, LAST = 1846, 1932
ROW0 = 6
YEARS = range(FIRST, LAST + 1)


def row(y: int) -> int:
    return ROW0 + y - FIRST


def interp(points: dict[int, float], before: float | None = None) -> dict[int, float]:
    """Linear between break-points; constant after the last; `before` (or the first value) before the first."""
    ks = sorted(points)
    out = {}
    for y in YEARS:
        if y < ks[0]:
            out[y] = points[ks[0]] if before is None else before
        elif y >= ks[-1]:
            out[y] = points[ks[-1]]
        else:
            lo = max(k for k in ks if k <= y)
            hi = min(k for k in ks if k > y)
            out[y] = points[lo] + (points[hi] - points[lo]) * (y - lo) / (hi - lo)
    return out


def energy_lever(name: str) -> tuple[float, float]:
    """(Story, Stress) of an energy-workbook lever, as energy_inputs.py finally sets it."""
    for lv in ein.LEVERS:
        if isinstance(lv, tuple) and len(lv) >= 4 and lv[0] == name:
            return lv[2], lv[3]
    raise SystemExit(f"energy lever {name!r} not found")


# ------------------------------------------------------------------ levers
def levers() -> list:
    ch, ch2 = energy_lever("cost_hydro"), energy_lever("cost_td")
    ds, dm = energy_lever("dev_share"), energy_lever("df_max")
    ps, lf = energy_lever("price_strat"), energy_lever("strat_lf")
    return [
        "— CR-051, CR-054 and CR-055: the Works' costs, the energy-intensive champions and the Columbia (4 Nov 2026) —",
        ("halls_y12", "CR-051 M2: the magnet halls' construction, as a multiple of Y-12's", 2.75, 3.0, "× Y-12", "OPEN (author's decision)",
         "CR-051 M2: first-stage halls rising to about two and a half to three times Y-12's electromagnetic plant by 1925-26, "
         "with the second stage and the 1923 rewind in copper. Story takes the middle (2.75), Stress the top (3.0)."),
        ("y12_build", "Y-12's construction cost in 1913 dollars", 110, 110, "1913 $m", "Model estimate (to verify)",
         "Y-12 cost about $0.48bn to the end of 1946 with its operation (Hewlett and Anderson, appendix; to verify), of which "
         "construction about $0.3bn; building costs in 1945 were about 2.8 times those of 1913 (ENR index; to verify): about "
         "$110m in 1913 dollars."),
        ("halls_op", "CR-051: the halls' operation per MW of draw", 35, 45, "1913 $ thousand a MW-year", "Model estimate",
         "Thousands of examined operators, the recovery chemists, the vacuum and magnet shops, and the running cost of the Works' "
         "own dams (their capital is in the Works sheet): about $25m a year (1913 $) at the full plant's 700 MW. Power from "
         "elsewhere is bought at en_price_strat (Works sheet). Replaces CR-050's 'operation and hydro power' ($6-10m)."),
        ("feed_staff", "CR-051 M1: the feed plant's staff and upkeep", 1.5, 2.0, "1913 $m a year", "Model estimate",
         "Its oil is costed from the energy workbook's 0.4-0.75 Mt at the oil price (Resources!L)."),
        ("diff_op", "CR-051 M4: the gaseous-diffusion plant's operation per MW of draw", 20, 25, "1913 $ thousand a MW-year", "Model estimate", ""),
        ("works_kw", "CR-051: the Works' dams and Rock Island, built cost with their lines", 130, 160, "1913 $/kW", "Model estimate",
         "CR-051 M2: about $100m for dams and lines on the Pit and the upper Feather (400-500 MW): about $130/kW in 1913 money "
         "at 1920s prices, below the energy workbook's generic $160/kW plant plus $110/kW of lines and distribution, because "
         "the halls take the power at the dams' busbars. Rock Island adds its 80-mile line to White Bluffs."),
        ("works_price", "Price of Rock Island's power sold to Wenatchee, the orchards and the pumps", 0.4, 0.35, "1913 cents/kWh", "Model estimate",
         "Wholesale hydro to a smelter and to irrigation pumping; the energy workbook values the strategic loads at 0.5."),
        ("silver_t", "CR-051 M3: the Mint's silver lent for the first two halls' windings", 3000, 3000, "tonnes", "Model estimate",
         "'A few thousand tons' (CR-051 M3); Y-12 borrowed 13,300 t. Lent 1918, returned in 1923, every bar weighed: a memo, "
         "no cash flow."),
        ("en_cost_hydro", "Energy workbook's hydro plant cost (mirror, do not change here)", ch[0], ch[1], "1913 $/kW", "Mirror of the energy workbook",
         "energy/build/energy_inputs.py cost_hydro: used only to take the energy workbook's own costing of the Works' dams, "
         "Rock Island and the second units out of its power investment before the finance basis is put in."),
        ("en_cost_td", "Energy workbook's lines and distribution per kW (mirror, do not change here)", ch2[0], ch2[1], "1913 $/kW", "Mirror of the energy workbook",
         "energy/build/energy_inputs.py cost_td."),
        ("en_dev_share", "Share of power investment the Development Fund would lend (mirror)", ds[0], ds[1], "share", "OPEN (CR-052 F12; not decided here)",
         "energy/build/energy_inputs.py dev_share. Applied here to the power investment the Treasury does not build itself."),
        ("en_df_max", "Most of the Fund's yearly investment power can take (mirror)", dm[0], dm[1], "share", "Mirror of the energy workbook",
         "energy/build/energy_inputs.py df_max."),
        ("en_price_strat", "Price of power to the strategic loads (mirror)", ps[0], ps[1], "1913 cents/kWh", "Mirror of the energy workbook",
         "energy/build/energy_inputs.py price_strat: what the halls pay for power that is not the Works' own (the freed arc plants' "
         "power, the Columbia-Sierra line, the grid) and the diffusion plant pays for the river's power. The energy workbook counts "
         "the same kilowatt-hours in its electricity revenue."),
        ("en_strat_lf", "Load factor of the strategic loads (mirror)", lf[0], lf[1], "share", "Mirror of the energy workbook",
         "energy/build/energy_inputs.py strat_lf."),
        ("col2_cost", "CR-055 R9: the Columbia's second units, cost as a share of a new plant's", 0.4, 1.0, "share", "OPEN (author's decision)",
         "CR-055 R9: costed by the energy workbook like a new plant with its lines (about $0.45bn), an overstatement, since units "
         "added to existing powerhouses need no new dam and little new line. Story 0.4 (turbines, generators and the powerhouse "
         "extension); Stress has no second units."),
        ("rb_est", "CR-055 R9: share of the power estate's 1930-1932 bond issues the Reserve Bank buys", 0.5, 0.3, "share", "Model estimate",
         "'Financed as the Fund's cap allows and otherwise by the power estate's bonds and, in the slump, the Reserve Bank.' "
         "The purchases are added to notes and bank reserves (Gold & money!I) and tested against the gold cover."),
        ("est_amort", "Power estate's bonds repaid each year", 0.03, 0.03, "share", "Model estimate", "About a thirty-year amortisation."),
        ("est_coupon", "Coupon on the power estate's bonds", 0.045, 0.05, "share", "Model estimate", "Memo: paid from the estate's sales, not the Budget."),
        ("alu_inp", "CR-054 A1: aluminium's purchased inputs per tonne (alumina, carbon, power, materials)", 210, 230, "1913 $/t", "Model estimate",
         "About two tonnes of Gulf alumina ($70), carbon ($20), 22-27 MWh at about two mills ($50) and materials ($70)."),
        ("alu_fab", "CR-054 A1: first fabrication (conductor, sheet, castings) per tonne sold in the Realm and the Concord", 60, 50, "1913 $/t", "Model estimate", ""),
        ("alu_x31", "CR-054 A4: world price for the third beyond the Concord in 1931, × the pool's", 0.70, 0.60, "×", "Model estimate",
         "'Sterling-priced aluminium undercuts Hilo in September 1931'; outside the European cartel the export third 'loses "
         "price, not volume' (A4, A6). The Concord pool holds its price."),
        ("alu_x32", "CR-054 A4: the same in 1932", 0.65, 0.55, "×", "Model estimate", ""),
        ("alu_alumina", "Alumina per tonne of aluminium", 1.93, 1.93, "t/t", "Model estimate", "Hall-Héroult practice of the 1920s, about 1.9-2 t."),
        ("alumina_px", "CR-054 A1: alumina bought from the Gulf's refinery", 30, 30, "1913 $/t", "Model estimate",
         "Arkansas bauxite refined in the Gulf (site OPEN) and shipped by the canal; the Gulf keeps the refinery and the royalty."),
        ("n_va", "CR-054 A2: nitrogen, value added / sales", 0.45, 0.40, "share", "Model estimate", "Electrolytic ammonia on the Columbia's cells and Haber-Bosch on Valley gas."),
        ("es_prem", "CR-054 A5: electric steel, value added above ordinary steel", 20, 15, "1913 $/t", "Model estimate",
         "Alloy and tool steel for the aircraft and electrical champions; ordinary steel is valued in Champions!S."),
        ("zn_va", "CR-055: electrolytic zinc, value added / sales", 0.40, 0.35, "share", "Model estimate", "The Coeur d'Alene ores are in the metals series."),
        ("mg_va", "CR-055: magnesium, value added / sales", 0.60, 0.50, "share", "Model estimate", ""),
        ("p_va", "CR-055: furnace phosphorus, value added / sales", 0.50, 0.45, "share", "Model estimate", ""),
        ("cu_margin", "CR-055: electrolytic copper refining margin", 20, 18, "1913 $/t", "Model estimate",
         "About 1-1.25 cents a pound; the copper itself is in the metals series (Resources!F)."),
        ("rub_inp", "CR-055: synthetic rubber's purchased inputs per tonne (carbide, power, materials)", 180, 200, "1913 $/t", "Model estimate",
         "Carbide-acetylene-butadiene. Above the world price after the Stevenson scheme ends: the loss is shown, not hidden."),
        ("hyd_cost", "CR-055: hydrogenation's purchased hydrogen and catalyst per barrel of motor fuel gained", 0.9, 1.1, "1913 $/bbl", "Model estimate",
         "About 430 kWh of the river's secondary power and the catalyst per barrel gained (9m bbl of residue give 5m)."),
    ] + [
        (f"inv_{k}", f"Plant cost: {lab}", v, round(v * 1.2, 1), f"1913 $ per {unit} of yearly output", "Model estimate", basis)
        for k, lab, v, unit, basis in (
            ("alu", "aluminium smelters and carbon plants", 300, "t", "Alcoa's 1920s smelters (to verify)."),
            ("n", "ammonia plants", 400, "t N", ""),
            ("zn", "electrolytic zinc", 120, "t", ""),
            ("mg", "magnesium cells", 1500, "t", ""),
            ("p", "phosphorus furnaces", 400, "t P", ""),
            ("cu", "copper refinery", 30, "t", ""),
            ("rub", "the Tacoma rubber works", 1200, "t", ""),
            ("hyd", "the Portland hydrogenation works", 15, "bbl of residue", "Leuna's hydrogenation cost about $35-40 a barrel of yearly product (to verify); about $15 a barrel of residue."),
            ("pig", "electric pig-iron furnaces", 20, "t", ""),
            ("es", "electric steel furnaces", 15, "t", ""),
        )
    ]


# ------------------------------------------------------------------ CR-051 inputs (1913 $m)
HALLS_PROFILE = {1917: 0.02, 1918: 0.06, 1919: 0.12, 1920: 0.14, 1921: 0.14, 1922: 0.16, 1923: 0.14,
                 1924: 0.12, 1925: 0.07, 1926: 0.03}
FEED_BUILD = {1920: 4, 1921: 14, 1922: 6, 1924: 4, 1925: 4}
STATION_BUILD = {1919: 3.5, 1920: 6, 1921: 5, 1922: 7, 1923: 6, 1924: 4, 1925: 3, 1926: 3, 1927: 3}
STATION_OPS = c50.ramp({1921: 1, 1922: 2, 1924: 3, 1927: 4, 1930: 5})
BREEDER = {1930: 2, 1931: 3, 1932: 3}
DIFF_BUILD = {1925: 0.5, 1926: 1.5, 1927: 1, 1930: 12, 1931: 18, 1932: 20}
ROCK_LINE = {1921: 0.8, 1922: 0.8}
FEES = c50.ramp({1920: 0.15})
SILVER_OUT = {y: 1 for y in range(1918, 1923)}  # lent 1918, returned 1923
SILVER_PX = {1917: 0.84, 1918: 0.98, 1919: 1.12, 1920: 1.02, 1921: 0.63, 1922: 0.68, 1923: 0.65}
# CR-050 rows this build replaces (Atomic!O)
REPLACED = ("Separation halls: construction 1917-1923 (first hall 1919, rebuilt), enlargement 1928-1930",
            "Separation halls: operation and hydro power")

# ------------------------------------------------------------------ CR-054/055 prices, current $ (historical; to verify)
PX = {
    "alu": interp({1890: 60, 1900: 33, 1905: 35, 1907: 45, 1908: 28, 1910: 22, 1912: 21, 1913: 23, 1914: 18.6, 1915: 34,
                   1916: 38, 1917: 40, 1918: 33, 1919: 32, 1920: 32, 1921: 22, 1922: 18, 1923: 25, 1924: 27, 1927: 25,
                   1928: 24, 1929: 24, 1930: 23.8, 1931: 23.3}),
    "cu": interp({1880: 21, 1890: 15.8, 1895: 10.7, 1900: 16.2, 1905: 15.6, 1906: 19.3, 1907: 20, 1908: 13.2, 1909: 13,
                  1910: 12.7, 1911: 12.4, 1912: 16.3, 1913: 15.3, 1914: 13.3, 1915: 17.3, 1916: 27.2, 1917: 27.2,
                  1918: 24.6, 1919: 18.7, 1920: 17.5, 1921: 12.5, 1922: 13.4, 1923: 14.4, 1924: 13.0, 1925: 14.0,
                  1926: 13.8, 1927: 12.9, 1928: 14.6, 1929: 18.1, 1930: 13.0, 1931: 8.1, 1932: 5.6}),
    "zn": interp({1900: 4.4, 1905: 5.9, 1907: 5.9, 1908: 4.6, 1910: 5.4, 1912: 6.9, 1913: 5.6, 1914: 5.1, 1915: 14.2,
                  1916: 12.6, 1917: 8.8, 1918: 8.1, 1919: 7.0, 1920: 7.7, 1921: 4.7, 1922: 5.7, 1923: 6.6, 1924: 6.3,
                  1925: 7.6, 1926: 7.3, 1927: 6.2, 1928: 6.0, 1929: 6.5, 1930: 4.6, 1931: 3.6, 1932: 2.9}),
    "mg": interp({1909: 1.5, 1914: 1.5, 1915: 5.0, 1916: 4.0, 1917: 2.5, 1918: 2.0, 1919: 1.75, 1920: 1.75, 1922: 1.0,
                  1925: 0.80, 1927: 0.65, 1929: 0.57, 1931: 0.40, 1932: 0.30}),
    "n": interp({1913: 290, 1915: 320, 1916: 360, 1917: 420, 1918: 450, 1919: 400, 1920: 380, 1921: 300, 1922: 280,
                 1923: 280, 1924: 270, 1925: 260, 1926: 250, 1927: 240, 1928: 230, 1929: 220, 1930: 190, 1931: 160, 1932: 140}),
    "p": interp({1913: 300, 1915: 300, 1918: 400, 1920: 350, 1925: 300, 1929: 280, 1931: 230, 1932: 220}),
    "rub": interp({1913: 82, 1915: 66, 1918: 60, 1920: 36, 1921: 16, 1922: 17, 1923: 29.4, 1924: 26.2, 1925: 72.5,
                   1926: 48.5, 1927: 37.7, 1928: 22.4, 1929: 20.6, 1930: 11.9, 1931: 6.2, 1932: 3.5}),
    "gas": interp({1918: 4.0, 1920: 3.5, 1921: 2.5, 1923: 2.0, 1925: 2.2, 1927: 1.6, 1929: 1.7, 1930: 1.3, 1931: 0.8, 1932: 0.9}),
}
PX_NOTE = {
    "alu": "Aluminium ingot, cents a pound (Alcoa's list and the New York market; to verify). The Concord pool's price.",
    "cu": "Electrolytic copper, New York, cents a pound (to verify).",
    "zn": "Prime western zinc, St Louis, cents a pound (to verify).",
    "mg": "Magnesium ingot, dollars a pound (US, to verify).",
    "n": "Fixed nitrogen in ammonia and ammonium sulphate, dollars a tonne of N (to verify).",
    "p": "Phosphorus, dollars a tonne of P (to verify).",
    "rub": "Plantation smoked sheet, New York, cents a pound (to verify); the Stevenson scheme 1922-28.",
    "gas": "Gasoline over fuel oil at the Pacific refineries, dollars a barrel (to verify).",
}
AIRCRAFT = interp({1909: 0, 1910: 0.2, 1913: 1, 1914: 2, 1915: 5, 1916: 12, 1917: 30, 1918: 50, 1919: 20, 1920: 12,
                   1921: 12, 1922: 18, 1923: 22, 1924: 28, 1925: 38, 1926: 50, 1927: 62, 1928: 78, 1929: 95, 1930: 100,
                   1931: 110, 1932: 125}, before=0)
LINE = {1920: 6, 1921: 12, 1922: 15, 1923: 15, 1924: 12}  # the Columbia-Sierra line, $m current (CR-055 R9: about $60m)


# ------------------------------------------------------------------ sheet builder
class Sheet:
    def __init__(self, wb, name: str, after: str, title: str, purpose: str):
        B, P = wb["Budget"], wb["Paths"]
        self.ws = wb.create_sheet(name, index=wb.sheetnames.index(after) + 1)
        self.ws["A1"].value = title
        self.ws["A2"].value = purpose
        self.ws["A3"].value = ("Years run down the page. Blue = input you can change · black = formula. "
                               "Built by finance/build/cr051_054_055_champions.py; all amounts MODEL.")
        for c, src in (("A1", B["A1"]), ("A2", B["A2"]), ("A3", B["A3"])):
            self.ws[c]._style = copy.copy(src._style)
        self.grp, self.head = B["B4"]._style, B["B5"]._style
        self.year, self.f, self.inp = B["A6"]._style, B["B6"]._style, P["B6"]._style
        self.ws.cell(5, 1).value = "Year"
        self.ws.cell(5, 1)._style = copy.copy(B["A5"]._style)
        for y in YEARS:
            self.ws.cell(row(y), 1).value = y
            self.ws.cell(row(y), 1)._style = copy.copy(self.year)
        self.ws.column_dimensions["A"].width = 8
        self.ws.freeze_panes = "B6"
        self.n = 1
        self.cols: dict[str, str] = {}

    def add(self, key: str, header: str, fn, *, group: str | None = None, note: str = "", is_input: bool = False,
            fmt: str | None = None) -> str:
        self.n += 1
        L_ = col(self.n)
        self.cols[key] = L_
        c = self.ws.cell(4, self.n)
        if group:
            c.value = group
        c._style = copy.copy(self.grp)
        h = self.ws.cell(5, self.n)
        h.value = header
        h._style = copy.copy(self.head)
        if note:
            base.note(h, note, 120)
        self.ws.column_dimensions[L_].width = 13
        for y in YEARS:
            v = fn(y, row(y))
            cell = self.ws.cell(row(y), self.n)
            cell.value = v
            cell._style = copy.copy(self.inp if is_input else self.f)
            if fmt:
                cell.number_format = fmt
        return L_

    def __getitem__(self, key: str) -> str:
        return self.cols[key]


def energy_series(sh: Sheet, data: dict, key: str, header: str, *, group: str | None = None, note: str = "") -> str:
    """One input column if Story = Stress, else Story, Stress and the active one."""
    s, t = data[f"{key}__story"], data[f"{key}__stress"]
    if all(abs(a - b) < 1e-9 for a, b in zip(s, t)):
        return sh.add(key, header, lambda y, r: round(s[y - FIRST], 6), group=group, is_input=True,
                      note=(note + " " if note else "") + "Energy workbook (same in Story and Stress).")
    a = sh.add(f"{key}_s", header + ", Story", lambda y, r: round(s[y - FIRST], 6), group=group, is_input=True,
               note=(note + " " if note else "") + "Energy workbook, Story.")
    b = sh.add(f"{key}_t", header + ", Stress", lambda y, r: round(t[y - FIRST], 6), is_input=True, note="Energy workbook, Stress.")
    return sh.add(key, header, lambda y, r: f"=IF(case_sel=1,{a}{r},{b}{r})")


def spread(L_: str, r: int, y: int, lead: int = 2) -> str:
    """Capacity added this year and in the next `lead` years, averaged: the building cost falls before first power."""
    terms = []
    for k in range(lead + 1):
        yy = y + k
        if yy > LAST:
            break
        rr = row(yy)
        terms.append(f"MAX(0,{L_}{rr}-{L_}{rr - 1})" if yy > FIRST else f"{L_}{rr}")
    return "(" + "+".join(terms) + f")/{lead + 1}"


# ------------------------------------------------------------------ the Works (CR-051)
def build_works(wb, data: dict) -> Sheet:
    W = Sheet(wb, "Works", "Atomic", "The Works: what CR-051 costs (1913 $m unless stated)",
              "CR-051 (integrated 4 Nov 2026): the magnet halls at a multiple of Y-12, the feed plant, the Columbia station at "
              "White Bluffs, gaseous diffusion, the Works' dams and Rock Island, the compacts, Rock Island's sales and the Mint's "
              "silver. Linked into Atomic (AD-AG), whose costs reach Budget 'Technical programmes' and returns 'State enterprises'.")
    g = "From the energy workbook"
    halls = energy_series(W, data, "halls_mw", "Halls' draw (MW)", group=g, note="CR-051 M2 range, positioned by halls_pos.")
    feed = energy_series(W, data, "feed_mt", "Feed plant oil (Mt)", note="CR-051 M1, M2: 0.4-0.75 Mt a year from 1921.")
    diff = energy_series(W, data, "diff_mw", "Gaseous-diffusion plant's draw (MW)")
    works = energy_series(W, data, "cap_works", "The Works' dams, Pit and upper Feather (MW)")
    wavg = energy_series(W, data, "works_avg", "The Works' dams, average output (MW)")
    rock = energy_series(W, data, "cap_rock", "Rock Island (MW)")
    wen = energy_series(W, data, "wen_mw", "Wenatchee smelter on Rock Island (MW avg)")
    spare = energy_series(W, data, "rock_spare", "Rock Island left for orchards and pumps (MW avg)")

    g = "The separation chain (government consumption)"
    prof = W.add("prof", "Halls' construction, share in the year", lambda y, r: HALLS_PROFILE.get(y, 0), group=g, is_input=True,
                 fmt="0%", note="CR-051 M2's timetable: decided 1917, first halls 1919 (one rewound over the winter), first stage on "
                 "natural feed 1920, more halls 1921, the second stage from mid-1922, about twice Y-12 in 1923 with the copper "
                 "rewind of the first two halls, two and a half times in 1924, the full plant in 1925-26.")
    hb = W.add("halls_build", "Halls: construction", lambda y, r: f"={prof}{r}*halls_y12*y12_build",
               note="Share × halls_y12 × y12_build. Replaces CR-050's $130m in 1917-1923 and its $60m enlargement of 1928-1930 "
               "(after 1927 the output rises through gaseous diffusion as feed, M4).")
    ho = W.add("halls_op", "Halls: operation", lambda y, r: f"={halls}{r}*halls_op/1000",
               note="Draw × halls_op: staff, shops and the Works' dams' running cost. Replaces CR-050's operation and hydro power.")
    hp = W.add("halls_pw", "Halls: power bought beyond the Works' dams",
               lambda y, r: f"=MAX(0,{halls}{r}*en_strat_lf-{wavg}{r})*8.76*en_price_strat/100",
               note="The halls' use (draw × en_strat_lf) less the Works' dams' average output: the freed arc plants' power (1919 on), the "
               "Columbia-Sierra line (1924 on) and any grid power, bought at en_price_strat. In the energy workbook's electricity revenue.")
    fb = W.add("feed_build", "Feed plant and its oil-fired powerhouse: construction", lambda y, r: FEED_BUILD.get(y, 0), is_input=True,
               note="CR-051 M1: Ralston College's columns put in front of the halls in 1921, several times S-50 (about $6m in 1913 $), "
               "with a powerhouse of their own; larger feed 1924-25.")
    fo = W.add("feed_op", "Feed plant: oil, staff and upkeep",
               lambda y, r: f"=IF({feed}{r}>0,{feed}{r}*7*Resources!L{r}/Paths!B{r}+feed_staff,0)",
               note="Oil at seven barrels a tonne and the oil price (Resources!L, current $) deflated by Paths!B, plus feed_staff.")
    sb = W.add("station_build", "Columbia station: construction", lambda y, r: STATION_BUILD.get(y, 0), is_input=True,
               note="CR-051 S7: White Bluffs and Hanford bought out in 1919-1920 above appraisers' prices; pile buildings, the "
               "separation plant on the plateau, the company town, Roslyn steam on standby. Hanford's construction was about "
               "$90m in 1913 $; the 1920s piles are smaller. The 1921 research installation of CR-049/050 (Atomic N, $3m) is "
               "taken as the station's first pile and is not counted again here.")
    so = W.add("station_op", "Columbia station: operation", lambda y, r: STATION_OPS.get(y, 0), is_input=True,
               note="Pumps, chemists, wardens' pay, the clinic, the river measurements the Office publishes.")
    br = W.add("breeder", "Experimental breeder at the station", lambda y, r: BREEDER.get(y, 0), is_input=True,
               note="CR-050 X2 and CR-051 S7: the breeder lit about 1930-1932, at the Columbia.")
    db = W.add("diff_build", "Gaseous diffusion: pilot and plant", lambda y, r: DIFF_BUILD.get(y, 0), is_input=True,
               note="CR-051 M4: a pilot in the inner circle about 1926, a plant 1930-32 at the Columbia station (site PROPOSED, CR-055 R3). "
               "K-25 cost about $140m in 1913 $; the first plant draws 150 MW in 1932.")
    do = W.add("diff_op", "Gaseous diffusion: operation, with its power",
               lambda y, r: f"={diff}{r}*diff_op/1000+{diff}{r}*en_strat_lf*8.76*en_price_strat/100",
               note="Draw × diff_op, plus the river's power at en_price_strat (the plant stands at the Columbia station on the estate's dams).")
    sep = W.add("sep", "Separation chain: total", lambda y, r: f"={hb}{r}+{ho}{r}+{hp}{r}+{fb}{r}+{fo}{r}+{sb}{r}+{so}{r}+{br}{r}+{db}{r}+{do}{r}",
                note="To Atomic AD (× atom_scale there), counted with the halls and weapons as government consumption.")

    g = "The Works' dams (investment)"
    wd = W.add("works_dams", "The Works' dams on the Pit and the upper Feather", lambda y, r: f"={spread(works, r, y)}*works_kw/1000",
               group=g, note="CR-051 M2: 1920-1926, about 400-500 MW (energy workbook). Capacity added this year and in the next two, "
               "averaged, × works_kw. Consent of the Pit River peoples and the Maidu OPEN (CR-051 item 9).")
    rl = W.add("rock_line", "Rock Island's line to White Bluffs", lambda y, r: ROCK_LINE.get(y, 0), is_input=True,
               note="About eighty miles down the river (CR-051 S7).")
    rd = W.add("rock_dam", "Rock Island dam with its line", lambda y, r: f"={spread(rock, r, y)}*works_kw/1000+{rl}{r}",
               note="CR-051 S7: a hydro company of the Works builds it in 1920-1923; ladders (S8 C4).")
    dams = W.add("dams", "Dams: total", lambda y, r: f"={wd}{r}+{rd}{r}",
                 note="To Atomic AF: investment, like the atomic power stations (excluded from government consumption on Energy link). "
                 "The energy workbook's power investment also contains these dams at its generic cost; Energy link swaps that cost "
                 "for this one, so they are counted once.")

    g = "The compacts"
    fee = W.add("fee", "White Bluffs fee and the river accord's share", lambda y, r: FEES.get(y, 0), group=g, is_input=True,
                note="CR-051 S8 A1, B3: a fee every year to the Wanapum, a share to the Yakama, Umatilla and Nez Perce councils. "
                "Me-Wuk's lease is $0.05m (Atomic M).")
    roy = W.add("roy", "Royalty on Rock Island's and the Works' dams' kilowatt-hours", lambda y, r: f"='Energy link'!Q{r}/Paths!B{r}",
                note="CR-051 S8 C2: the energy workbook's royalty (roy_mill, size OPEN under CR-052 F12), paid by the Works' hydro "
                "company, so a Treasury cost. The Columbia's five dams' royalties are the power estate's, outside the Budget.")
    comp = W.add("comp", "Compacts: total", lambda y, r: f"={fee}{r}+{roy}{r}", note="To Atomic AE (contracts and leases).")

    g = "Returns"
    gwh = W.add("rock_gwh", "Rock Island power sold (GWh)", lambda y, r: f"=(MAX(0,{wen}{r})+MAX(0,{spare}{r}))*8.76", group=g,
                note="To the Wenatchee smelter, the orchards and the Basin's pumps; the station's own draw is not sold.")
    ret = W.add("rock_ret", "Rock Island's sales", lambda y, r: f"={gwh}{r}*works_price/100", note="To Atomic AG (direct returns).")

    g = "The Mint's silver (memo, no cash flow)"
    st = W.add("silver_t", "Silver in the first halls' windings (t)", lambda y, r: f"=silver_t*{SILVER_OUT.get(y, 0)}", group=g,
               note="CR-051 M3: the Mint lends it in 1918 for the first two halls; the later halls are wound in copper bought "
               "cheaply in the postwar slump; the first halls are rewound in copper in 1923 (inside the 1923 construction) and "
               "the silver goes back, every bar weighed.")
    sp = W.add("silver_px", "Silver, New York ($ an ounce)", lambda y, r: SILVER_PX.get(y), is_input=True, note="To verify.")
    W.add("silver_v", "Value of the silver lent ($m current)", lambda y, r: f'=IF(ISNUMBER({sp}{r}),{st}{r}*32150.7*{sp}{r}/1000000,0)')

    g = "Against the CR-050 build"
    rep = W.add("replaced", "CR-050 hall rows replaced", lambda y, r: round(sum(c50.COSTS[("weapons", n)].get(y, 0) for n in REPLACED), 4),
                group=g, is_input=True, note="Construction 1917-1923, enlargement 1928-1930, operation and hydro power: taken out of Atomic!O.")
    W.add("net", "Added by CR-051, net of what it replaces", lambda y, r: f"={sep}{r}+{dams}{r}+{comp}{r}-{ret}{r}-{rep}{r}",
          note="1913 $m, before atom_scale.")
    return W


def link_atomic(wb, W: Sheet) -> None:
    A = wb["Atomic"]
    heads = {A.cell(5, c).value: c for c in range(2, A.max_column + 1)}
    assert A.max_column == 29 and heads["Reserve not negative"] == 29, A.max_column
    assert heads["Separation halls, weapons, tests"] == 15
    kept = {y: sum(d.get(y, 0) for (cat, n), d in c50.COSTS.items() if cat == "weapons" and n not in REPLACED) for y in YEARS}
    for y in range(1864, LAST + 1):
        r = row(y)
        old = A.cell(r, 15).value
        assert isinstance(old, (int, float)), (y, old)
        rep = sum(c50.COSTS[("weapons", n)].get(y, 0) for n in REPLACED)
        assert abs(old - rep - kept[y]) < 1e-6, (y, old, rep, kept[y])
        A.cell(r, 15).value = round(kept[y], 4)
    base.note(A.cell(5, 15), "CR-051 build (4 Nov 2026): weapon engineering, the wall's security and the test site, the desert test "
              "(May 1924) and the sea demonstration (1927). The halls, the feed plant, the station and gaseous diffusion are now "
              "in AD from the Works sheet (input; CR-050, CR-051).", 110)
    new = [("AD", "CR-051: the separation chain", "sep", "Works sheet: the halls (construction and operation), the feed plant, the Columbia station, "
            "the breeder and gaseous diffusion (1913 $m). Government consumption."),
           ("AE", "CR-051: compacts' fees and royalties", "comp", "Works sheet: the White Bluffs fee, the river accord's share, the royalty on "
            "Rock Island's and the Works' dams' kilowatt-hours (1913 $m)."),
           ("AF", "CR-051: the Works' dams and Rock Island", "dams", "Works sheet (1913 $m). Investment, like the power stations (P)."),
           ("AG", "CR-051: Rock Island's sales", "rock_ret", "Works sheet (1913 $m): a direct return.")]
    gstyle, hstyle = A.cell(4, 20)._style, A.cell(5, 20)._style
    lstyle = A.cell(row(1925), 18)._style  # Atomic R: a link to Paths
    for i, (L_, head, key, txt) in enumerate(new):
        c = cidx(L_)
        A.cell(4, c).value = "CR-051 (Works sheet)" if i == 0 else None
        A.cell(4, c)._style = copy.copy(gstyle)
        A.cell(5, c).value = head
        A.cell(5, c)._style = copy.copy(hstyle)
        base.note(A.cell(5, c), txt, 110)
        A.column_dimensions[L_].width = 13
        for y in YEARS:
            r = row(y)
            A.cell(r, c).value = f"=Works!{W[key]}{r}"
            A.cell(r, c)._style = copy.copy(lstyle)
            A.cell(r, c).number_format = A.cell(r, 15).number_format
        A.cell(94, c).value = f"=SUM({L_}6:{L_}92)"
        A.cell(94, c)._style = copy.copy(A.cell(94, 15)._style)
    for y in YEARS:
        r = row(y)
        q = A.cell(r, 17).value
        assert q == f"=L{r}+(M{r}+N{r}+O{r}+P{r})*atom_scale", q
        A.cell(r, 17).value = f"=L{r}+(M{r}+N{r}+O{r}+P{r}+AD{r}+AF{r})*atom_scale+AE{r}"
        x = A.cell(r, 24).value
        assert x == f"=T{r}+U{r}+W{r}", x
        A.cell(r, 24).value = f"=T{r}+U{r}+W{r}+AG{r}"
    base.note(A.cell(5, 17), (A.cell(5, 17).comment.text + "\n\n" if A.cell(5, 17).comment else "")
              + "CR-051 build: plus the separation chain and the Works' dams (AD, AF) × atom_scale, and the compacts' fees and "
              "royalties (AE), which are not a cost overrun and are not scaled.", 120)
    base.note(A.cell(5, 24), (A.cell(5, 24).comment.text + "\n\n" if A.cell(5, 24).comment else "")
              + "CR-051 build: plus Rock Island's sales (AG).", 120)
    A["A2"].value = (A["A2"].value or "") + (" CR-051 (4 Nov 2026): the halls at a multiple of Y-12, the feed plant, the Columbia station, "
                                             "gaseous diffusion, the Works' dams and Rock Island, the compacts and Rock Island's sales "
                                             "from the Works sheet (AD-AG).")


# ------------------------------------------------------------------ the champions (CR-054, CR-055)
def build_electro(wb, data: dict) -> Sheet:
    E = Sheet(wb, "Electro champions", "Champions", "The energy-intensive champions (CR-054, CR-055), $m current unless stated",
              "Aluminium at CR-054 A1's amounts by destination, the aircraft, nitrogen, electric steel and the Columbia's "
              "electrochemistry (CR-055 R0), valued at historical prices. Aluminium and aircraft feed Champions!AO; the rest "
              "Champions!BF. Quantities from the energy workbook.")
    g = "Quantities (energy workbook)"
    alu = energy_series(E, data, "alu_kt", "Aluminium, all smelters (kt)", group=g)
    grid = energy_series(E, data, "alu_grid", "… the grid's conductor (kt)")
    air = energy_series(E, data, "alu_air", "… the Concord fleet's aircraft (kt)")
    pool = energy_series(E, data, "alu_pool", "… the Concord pool, to Japan (kt)")
    energy_series(E, data, "alu_civil", "… civil uses at home (kt)")
    exp = energy_series(E, data, "alu_export", "… beyond the Concord (kt)", note="The part exposed in 1931 (CR-054 A4).")
    energy_series(E, data, "alu_hilo", "… of it at Hilo (kt)", note="The showcase Keawe built; sterling undercuts it in September 1931.")
    eln = energy_series(E, data, "eln_kt", "Ammonia on electrolytic hydrogen (kt N)")
    hab = energy_series(E, data, "haber_kt", "Haber–Bosch on Valley gas (kt N)")
    es = energy_series(E, data, "esteel", "Electric steel / steel output")
    zn = energy_series(E, data, "zinc_kt", "Electrolytic zinc (kt)")
    mg = energy_series(E, data, "mg_kt", "Magnesium (kt)")
    ph = energy_series(E, data, "phos_kt", "Furnace phosphorus (kt P)")
    cu = energy_series(E, data, "cu_kt", "Electrolytic copper refined (kt)")
    rub = energy_series(E, data, "rubber_kt", "Synthetic rubber (kt)")
    pig = energy_series(E, data, "pig_kt", "Electric pig iron (kt)")
    hyd = energy_series(E, data, "hyd_bbl", "Residue hydrogenated (m bbl)")
    mf = energy_series(E, data, "hyd_mf", "Motor fuel gained by hydrogenation (m bbl)")

    g = "Prices (historical, current $)"
    px = {}
    for k in ("alu", "cu", "zn", "mg", "n", "p", "rub", "gas"):
        px[k] = E.add(f"px_{k}", PX_NOTE[k].split(",")[0].split(" (")[0], lambda y, r, k=k: round(PX[k][y], 4),
                      group=g if k == "alu" else None, is_input=True, note=PX_NOTE[k])

    g = "Aluminium (CR-054 A1, A4)"
    p_t = E.add("alu_pt", "Pool price ($/t)", lambda y, r: f"={px['alu']}{r}*22.046", group=g)
    p_x = E.add("alu_px", "Price beyond the Concord ($/t)", lambda y, r: f"={p_t}{r}*IF($A{r}=1931,alu_x31,IF($A{r}=1932,alu_x32,1))",
                note="The world price; the European cartel's quotas and the sterling undercut of 1931-32 (alu_x31, alu_x32).")
    c_t = E.add("alu_ct", "Purchased inputs ($/t)", lambda y, r: f"=alu_inp*Paths!B{r}")
    va_in = E.add("alu_va_in", "Smelting, the Realm and the Concord", lambda y, r: f"=({alu}{r}-{exp}{r})*({p_t}{r}-{c_t}{r})/1000")
    va_x = E.add("alu_va_x", "Smelting, beyond the Concord", lambda y, r: f"={exp}{r}*({p_x}{r}-{c_t}{r})/1000",
                 note="Price, not volume, in 1931-32: a champion's bad year, not the Realm's.")
    fab = E.add("alu_fab", "First fabrication", lambda y, r: f"=({alu}{r}-{exp}{r})*alu_fab*Paths!B{r}/1000",
                note="Steel-cored conductor, sheet for the air arm, castings.")
    alu_va = E.add("alu_va", "Aluminium: value added", lambda y, r: f"={va_in}{r}+{va_x}{r}+{fab}{r}")
    craft = E.add("aircraft", "Aircraft and engines: value added", lambda y, r: round(AIRCRAFT[y], 3), is_input=True,
                  note="The earlier workbook's note on Champions!AO has Douglas, Lockheed and Boeing as Pacifican (not storyline canon); the Concord's carrier and shore air arm all-metal from the mid-1920s, "
                  "built in Los Angeles and (PROPOSED) under licence in Japan; the naval and air programme of 1931-32 is the order book. "
                  "US aircraft and parts were about $70m of output in 1929 (to verify).")
    E.add("ao", "Aluminium and aircraft (to Champions!AO)", lambda y, r: f"={alu_va}{r}+{craft}{r}")
    E.add("ao_old", "Aluminium and aircraft before this build", lambda y, r: wb["Champions"][f"AO{r}"].value, is_input=True,
          note="Champions!AO as built to CR-052 (an input path); kept for comparison only.")
    E.add("pool_v", "Concord pool sales to Japan (memo)", lambda y, r: f"={pool}{r}*{p_t}{r}/1000",
          note="CR-054 A3: Japan's navy's aircraft and its electrical industry; an export inside the Concord.")
    E.add("x_loss", "Price lost beyond the Concord (memo)", lambda y, r: f"={exp}{r}*({p_t}{r}-{p_x}{r})/1000")
    E.add("alumina_kt", "Alumina from the Gulf (kt, memo)", lambda y, r: f"={alu}{r}*alu_alumina",
          note="CR-054 A1: Arkansas bauxite through the Gulf compact, refined in the Gulf (site OPEN), shipped by the canal. Guiana is not used.")
    E.add("alumina_v", "Alumina bought from the Gulf (memo)", lambda y, r: f"={alu}{r}*alu_alumina*alumina_px*Paths!B{r}/1000",
          note="Gulf trade: inside aluminium's purchased inputs; the refinery and the bauxite royalty are the Gulf's.")

    g = "Electrochemistry and metals (value added)"
    vn = E.add("va_n", "Nitrogen", lambda y, r: f"=({eln}{r}+{hab}{r})*{px['n']}{r}*n_va/1000", group=g,
               note="CR-054 A2: the Valley, the Imperial Valley, the Columbia Basin, Hawaii's and the Philippines' sugar and rice, Korea "
               "and the China trade; not Japan's market. The Concord joins the 1930 convention as one party. The arc plants' war "
               "nitric acid to 1919 is not counted here.")
    ves = E.add("va_es", "Electric steel above ordinary steel",
                lambda y, r: f"=Champions!R{r}*Champions!B{r}*{es}{r}*es_prem*Paths!B{r}",
                note="CR-054 A5: an eighth of steel by 1929. Steel output × scale × share × premium.")
    vzn = E.add("va_zn", "Electrolytic zinc (memo: inside Resources!F)", lambda y, r: f"={zn}{r}*{px['zn']}{r}*22.046*zn_va/1000",
                note="Resources!F carries historical values at the metal's price, and Resources!O takes mining's value added from it, so "
                "the smelting step is already in GDP. Memo only; not in BF.")
    vmg = E.add("va_mg", "Magnesium", lambda y, r: f"={mg}{r}*{px['mg']}{r}*2204.6*mg_va/1000")
    vp = E.add("va_p", "Furnace phosphorus", lambda y, r: f"={ph}{r}*{px['p']}{r}*p_va/1000")
    vcu = E.add("va_cu", "Copper refining (memo: inside Resources!F)", lambda y, r: f"={cu}{r}*cu_margin*Paths!B{r}/1000",
                note="As zinc: refined copper is valued at the refined price inside Resources!F. Memo only; not in BF.")
    rub_m = f"({px['rub']}{{r}}*22.046-rub_inp*Paths!B{{r}})"
    vr = E.add("va_rub", "Synthetic rubber", lambda y, r: f"={rub}{r}*MAX(0,{rub_m.format(r=r)})/1000",
               note="CR-055 purpose 3: against the Stevenson scheme (1922-28). Value added at the world price, never below zero.")
    lr = E.add("loss_rub", "… loss at the world price (memo)", lambda y, r: f"={rub}{r}*MAX(0,-{rub_m.format(r=r)})/1000",
               note="Once the scheme ends the world price falls below the acetylene route's cost; who bears it (the fleet's contracts, "
               "the champion, a subsidy) is OPEN.")
    hyd_m = f"({px['gas']}{{r}}-hyd_cost*Paths!B{{r}})"
    vh = E.add("va_hyd", "Hydrogenation", lambda y, r: f"={mf}{r}*MAX(0,{hyd_m.format(r=r)})",
               note="CR-055 purpose 2: about 5m bbl of motor fuel from 9m bbl of California's residue in 1929, for the fuel gap; "
               "never more than barely commercial.")
    lh = E.add("loss_hyd", "… loss at market prices (memo)", lambda y, r: f"={mf}{r}*MAX(0,-{hyd_m.format(r=r)})")
    E.add("pig_memo", "Electric pig iron (kt, memo: no new value added)", lambda y, r: f"={pig}{r}",
          note="CR-055 purpose 4: the yards' own iron on Philippine and Chilean ore; a change of process inside steel (Champions!T).")
    bf = E.add("bf", "Electrochemistry and metals (to Champions!BF)",
               lambda y, r: f"={vn}{r}+{ves}{r}+{vmg}{r}+{vp}{r}+{vr}{r}+{vh}{r}",
               note="Nitrogen, electric steel's premium, magnesium, phosphorus, rubber and hydrogenation (CR-054, CR-055). Zinc and copper "
               "refining are inside the metals series (memos). Champions!Z (chemicals and drugs) is the fine and organic chemistry of "
               "the licence trade and is not reduced.")
    E.add("losses", "Losses at world prices (memo)", lambda y, r: f"={lr}{r}+{lh}{r}")
    E.add("cuzn_share", "Copper and zinc refined / copper and other metals", lambda y, r: f"=IF(Resources!F{r}>0,({cu}{r}*{px['cu']}{r}+{zn}{r}*{px['zn']}{r})*22.046/1000/Resources!F{r},0)",
          group="Copper against the metals series", fmt="0%")

    cv = E.add("cu_v", "Copper refined, value ($m)", lambda y, r: f"={cu}{r}*{px['cu']}{r}*22.046/1000")
    E.add("cu_share", "… share of copper and other metals (Resources!F)", lambda y, r: f"=IF(Resources!F{r}>0,{cv}{r}/Resources!F{r},0)",
          fmt="0%", note="CR-055: Bingham and Arizona copper for the grid and the cable industry. The refined copper is mined inside the "
          "Realm, so it must fit inside the metals series with the zinc; the rest is lead, silver ores and the rest. 8-83% (1921, "
          "when the series falls to $70m in the slump while the copper path is smooth): below 100% in every year, no change to "
          "Resources!F; 1921 is tight.")

    g = "Plant investment ($m)"
    lines = [("alu", alu, 1), ("n", None, 1), ("zn", zn, 1), ("mg", mg, 1), ("p", ph, 1), ("cu", cu, 1), ("rub", rub, 1),
             ("hyd", hyd, 1000), ("pig", pig, 1), ("es", None, 1)]
    terms = []
    for i, (k, L_, mult) in enumerate(lines):
        if k == "n":
            q = lambda rr: f"({eln}{rr}+{hab}{rr})"  # noqa: E731
        elif k == "es":
            q = lambda rr: f"(Champions!R{rr}*1000*{es}{rr})"  # noqa: E731
        else:
            q = lambda rr, L_=L_: f"{L_}{rr}"  # noqa: E731

        def f(y, r, q=q, k=k, mult=mult):
            if y == FIRST:
                return f"=MAX(0,{q(r)})*{mult}*inv_{k}*Paths!B{r}/1000"
            prev = ",".join(q(row(yy)) for yy in range(max(FIRST, y - 10), y))
            return f"=MAX(0,{q(r)}-MAX({prev}))*{mult}*inv_{k}*Paths!B{r}/1000"
        L2 = E.add(f"inv_{k}", f"Plant: {k}", f, group=g if i == 0 else None,
                   note="New output above the best of the last ten years × the plant cost lever (inv_*) × the price level.")
        terms.append(L2)
    E.add("inv", "CR-054/055 works' plant (to Energy link)", lambda y, r: "=" + "+".join(f"{t}{r}" for t in terms),
          note="Investment inside gross domestic investment (the account's identified components).")
    return E


def link_champions(wb, E: Sheet) -> None:
    C = wb["Champions"]
    assert C.max_column == 57 and C["BE5"].value == "Crown share, average across the champions", C["BE5"].value
    gst, hst = C["AO4"]._style, C["AO5"]._style
    C["BF4"].value = "CR-054, CR-055"
    C["BF4"]._style = copy.copy(gst)
    C["BF5"].value = "Electrochemistry and metals ($m)"
    C["BF5"]._style = copy.copy(hst)
    base.note(C["BF5"], "Electro champions sheet: nitrogen, electric steel's premium, zinc, magnesium, phosphorus, copper refining, "
              "synthetic rubber and hydrogenation (CR-054 A2, A5; CR-055 R0). MODEL.", 120)
    C.column_dimensions["BF"].width = 13
    link_style = wb["Atomic"].cell(row(1925), 18)._style
    for y in YEARS:
        r = row(y)
        C[f"AO{r}"].value = f"='Electro champions'!{E['ao']}{r}"
        C[f"AO{r}"]._style = copy.copy(link_style)
        C[f"BF{r}"].value = f"='Electro champions'!{E['bf']}{r}"
        C[f"BF{r}"]._style = copy.copy(link_style)
        ap = C[f"AP{r}"].value
        assert ap == f"=K{r}+T{r}+W{r}+Z{r}+AF{r}+AI{r}+AK{r}+AM{r}+AN{r}+AO{r}", ap
        C[f"AP{r}"].value = ap + f"+BF{r}"
        bc = C[f"BC{r}"].value
        assert bc.startswith(f"=(T{r}+W{r}+Z{r}+AF{r}+AN{r}+AO{r})*champ_profit"), bc
        C[f"BC{r}"].value = bc.replace(f"+AO{r})*champ_profit", f"+AO{r}+BF{r})*champ_profit", 1)
    base.note(C["AO5"], "CR-054 build (4 Nov 2026): from the Electro champions sheet: aluminium at A1's amounts by destination, "
              "its first fabrication, and the aircraft and engines. Was an input path (kept there for comparison).", 120)
    base.note(C["AP5"], (C["AP5"].comment.text + "\n\n" if C["AP5"].comment else "") + "CR-054/055 build: plus BF.", 120)
    base.note(C["BC5"], (C["BC5"].comment.text + "\n\n" if C["BC5"].comment else "") + "CR-054/055 build: BF among the competitive industries.", 120)


# ------------------------------------------------------------------ the investment account and its financing
ACCOUNT = [
    # (letter, group, header, note)
    ("AL", "Investment, counted once (CR-051, CR-055)", "Energy workbook's own cost of the Works' dams and Rock Island ($m)",
     "New Works and Rock Island capacity × (en_cost_hydro + en_cost_td) × the price level: what the energy workbook's power investment (H) charges for them."),
    ("AM", None, "The Works' dams and Rock Island, finance basis ($m)", "Works sheet (works_kw, the line) × atom_scale × price: built by the Treasury through Atomic AF."),
    ("AN", None, "Second units: cost taken out ($m)", "New second-unit capacity × the energy workbook's cost × (1 − col2_cost): CR-055 R9's overstatement removed."),
    ("AO", None, "The Columbia–Sierra line ($m)", "CR-055 purpose 1 and R9: about $60m, decided 1919, energised 1924 at 287 kV (input, current $). "
     "Not in the energy workbook's power investment, which costs lines per kW of new capacity."),
    ("AP", None, "Power investment, counted once ($m)", "H − AL + AM − AN + AO. The energy workbook's memo becomes the account's first identified component."),
    ("AQ", None, "… of which the Columbia's five dams ($m)", "Bonneville, Rocky Reach, Wells, McNary, Chief Joseph: new capacity × the energy workbook's cost. "
     "Inside H already; shown so they are not added again."),
    ("AR", None, "… of which the second units ($m)", "At col2_cost of a new plant's cost."),
    ("AS", None, "Atomic power stations ($m)", "Atomic P × atom_scale × price (Tokyo and the Pacifican stations)."),
    ("AT", None, "CR-054/055 works' plant ($m)", "Electro champions: smelters, ammonia, zinc, magnesium, phosphorus, refinery, rubber, hydrogenation, furnaces."),
    ("AU", None, "Public works ($m)", "Budget R."),
    ("AV", None, "Other investment ($m)", "Gross domestic investment (AA) less the identified components: housing, railways, private industry, "
     "farms, the Fund's other lending. Must not be negative (Checks)."),
    ("AW", None, "… share of gross domestic investment", ""),
    ("AX", "Financing power (CR-055 R9)", "Built by the Treasury: the Works' dams and Rock Island ($m)", "Through Atomic AF and Budget 'Technical programmes'."),
    ("AY", None, "The power estate's investment ($m)", "The Columbia's five dams, the second units and the Columbia–Sierra line (AQ + AR + AO)."),
    ("AZ", None, "Development Fund's power credit, finance basis ($m)", "en_dev_share × the power investment the Treasury does not build, capped at "
     "en_df_max × what the Fund invests ('Debt & cash'!I): inside the Fund's investment, not additional. Column K is the energy workbook's "
     "own memo on its full power investment."),
    ("BA", None, "… of it to the power estate ($m)", "Pro rata to the estate's share of the non-Treasury power investment."),
    ("BB", None, "Power estate's bonds issued ($m)", "The estate's investment less the Fund's credit to it. The estate's, not the Treasury's: outside public debt."),
    ("BC", None, "Reserve Bank buys the estate's bonds ($m)", "1930-1932, rb_est of each year's issue: the slump. Added to notes and bank reserves (Gold & money I)."),
    ("BD", None, "Power estate's bonds outstanding ($m)", "Less est_amort a year."),
    ("BE", None, "Reserve Bank's holdings of the estate's bonds ($m)", "Running off with the bonds."),
    ("BF", None, "Estate bonds placed in the market ($m)", "Issued less the Reserve Bank's purchases."),
    ("BG", None, "Estate's bond interest (memo, $m)", "est_coupon on last year's bonds; paid from its sales, outside the Budget."),
    ("BH", None, "Other private financing of power ($m)", "County and private utilities' bonds and shares, the champions' retained earnings."),
    ("BI", "Tests", "Treasury and estate bonds within the market", "Treasury bonds placed × issue_price + estate bonds placed ≤ mkt_capacity × GDP + foreign_capacity."),
    ("BJ", None, "Identified investment within the total", "Other investment (AV) not negative."),
]


def build_account(wb, W: Sheet, E: Sheet, line: dict) -> None:
    """Energy link AL-BJ; reads the capacities written by add_capacity_inputs (BK-BP)."""
    X = wb["Energy link"]
    assert X["AK5"].value == "Pacifica / US, consumption per person" and X["AL5"].value is None, X["AL5"].value
    gst, hst = X["Y4"]._style, X["Y5"]._style
    f_style, in_style = X["AA6"]._style, X["V6"]._style
    for L_, grp, head, text in ACCOUNT:
        c = cidx(L_)
        if grp:
            X.cell(4, c).value = grp
        X.cell(4, c)._style = copy.copy(gst)
        X.cell(5, c).value = head
        X.cell(5, c)._style = copy.copy(hst)
        if text:
            base.note(X.cell(5, c), text, 120)
        X.column_dimensions[L_].width = 13
    cost = "(en_cost_hydro+en_cost_td)"

    def d(sheet_col: str, r: int, y: int) -> str:
        return f"MAX(0,{sheet_col}{r}-{sheet_col}{r - 1})" if y > FIRST else f"{sheet_col}{r}"

    for y in YEARS:
        r = row(y)

        def put(L_, v, is_input=False, fmt=None):
            cell = X[f"{L_}{r}"]
            cell.value = v
            cell._style = copy.copy(in_style if is_input else f_style)
            if fmt:
                cell.number_format = fmt
        wk, rk = f"Works!{W['cap_works']}", f"Works!{W['cap_rock']}"
        put("AL", f"=({d(wk, r, y)}+{d(rk, r, y)})*{cost}/1000*Economy!H{r}")
        put("AM", f"=(Works!{W['dams']}{r})*atom_scale*Atomic!R{r}")  # as in Atomic Q and S
        put("AN", f"={d('BK', r, y)}*{cost}*(1-col2_cost)/1000*Economy!H{r}")
        put("AO", line.get(y, 0), True)
        put("AP", f"=H{r}-AL{r}+AM{r}-AN{r}+AO{r}")
        five = "+".join(d(L_, r, y) for L_ in ("BL", "BM", "BN", "BO", "BP"))
        put("AQ", f"=({five})*{cost}/1000*Economy!H{r}")
        put("AR", f"={d('BK', r, y)}*{cost}*col2_cost/1000*Economy!H{r}")
        put("AS", f"=Atomic!P{r}*atom_scale*Atomic!R{r}")
        put("AT", f"='Electro champions'!{E['inv']}{r}")
        put("AU", f"=Budget!R{r}")
        put("AV", f"=AA{r}-AP{r}-AS{r}-AT{r}-AU{r}")
        put("AW", f"=IF(AA{r}>0,AV{r}/AA{r},0)", fmt="0.0%")
        put("AX", f"=AM{r}")
        put("AY", f"=AQ{r}+AR{r}+AO{r}")
        put("AZ", f"=MIN(MAX(0,AP{r}-AX{r})*en_dev_share,en_df_max*MAX(0,'Debt & cash'!I{r}))")
        put("BA", f"=IF(AP{r}-AX{r}>0,AZ{r}*MIN(1,AY{r}/(AP{r}-AX{r})),0)")
        put("BB", f"=MAX(0,AY{r}-BA{r})")
        put("BC", f"=IF(AND($A{r}>=1930,$A{r}<=1932),BB{r}*rb_est,0)")
        put("BD", f"=BB{r}" if y == FIRST else f"=BD{r - 1}*(1-est_amort)+BB{r}")
        put("BE", f"=BC{r}" if y == FIRST else f"=BE{r - 1}*(1-est_amort)+BC{r}")
        put("BF", f"=BB{r}-BC{r}")
        put("BG", "=0" if y == FIRST else f"=BD{r - 1}*est_coupon")
        put("BH", f"=MAX(0,AP{r}-AX{r}-AZ{r}-BB{r})")
        put("BI", f"=IF('Debt & cash'!Y{r}*issue_price+BF{r}<=mkt_capacity*Economy!O{r}+foreign_capacity,\"OK\",\"Check\")")
        put("BJ", f"=IF(AV{r}>=-0.001,\"OK\",\"Check\")")


def add_capacity_inputs(wb, data: dict) -> None:
    X = wb["Energy link"]
    assert X.max_column == 37, X.max_column  # the CR-052 sheet ends at AK
    in_style, gst, hst = X["V6"]._style, X["Y4"]._style, X["Y5"]._style
    keys = [("BK", "cap_col2", "Columbia second units (MW)"), ("BL", "cap_bonn", "Bonneville (MW)"),
            ("BM", "cap_rreach", "Rocky Reach (MW)"), ("BN", "cap_wells", "Wells (MW)"),
            ("BO", "cap_mcnary", "McNary (MW)"), ("BP", "cap_cjoe", "Chief Joseph (MW)")]
    for i, (L_, k, head) in enumerate(keys):
        c = cidx(L_)
        if i == 0:
            X.cell(4, c).value = "Capacity (energy workbook)"
        X.cell(4, c)._style = copy.copy(gst)
        X.cell(5, c).value = head
        X.cell(5, c)._style = copy.copy(hst)
        s, t = data[f"{k}__story"], data[f"{k}__stress"]
        base.note(X.cell(5, c), "Energy workbook, Hydro sheet" + (" (the same in Story and Stress)." if s == t else
                                  ": Story and Stress values in one cell, =IF(case_sel=1,Story,Stress)."), 100)
        X.column_dimensions[L_].width = 11
        for y in YEARS:
            r = row(y)
            a, b = round(s[y - FIRST], 4), round(t[y - FIRST], 4)
            X[f"{L_}{r}"].value = a if a == b else f"=IF(case_sel=1,{a},{b})"
            X[f"{L_}{r}"]._style = copy.copy(in_style)


def patch_links(wb) -> None:
    X, G, K = wb["Energy link"], wb["Gold & money"], wb["Checks"]
    for y in YEARS:
        r = row(y)
        ae = X[f"AE{r}"].value
        old = f"-Atomic!P{r}*atom_scale*Atomic!R{r}"
        assert old in ae, ae
        X[f"AE{r}"].value = ae.replace(old, f"-(Atomic!P{r}+Atomic!AF{r})*atom_scale*Atomic!R{r}")
        i = G[f"I{r}"].value
        assert i.startswith(f"=Economy!O{r}*money_ratio+H{r}"), i
        G[f"I{r}"].value = i + f"+'Energy link'!BE{r}"
    base.note(X["AE5"], X["AE5"].comment.text + "\n\nCR-051 build: the Works' dams and Rock Island (Atomic AF) are investment too.", 140)
    base.note(G["I5"], (G["I5"].comment.text + "\n\n" if G["I5"].comment else "")
              + "CR-055 build: plus the Reserve Bank's holdings of the power estate's bonds (Energy link BE).", 120)
    # checks
    assert K.max_column == 38 and K["AL5"].value == "Uranium reserve not negative (CR-049)", K.max_column
    for L_, head, src in (("AM", "Treasury and power-estate bonds within the market (CR-055)", "BI"),
                          ("AN", "Identified investment within the total (CR-051-055)", "BJ")):
        K[f"{L_}5"].value = head
        K[f"{L_}5"]._style = copy.copy(K["AL5"]._style)
        K[f"{L_}4"]._style = copy.copy(K["AL4"]._style)
        K.column_dimensions[L_].width = K.column_dimensions["AL"].width or 13
        for y in YEARS:
            r = row(y)
            K[f"{L_}{r}"].value = f"='Energy link'!{src}{r}"
            K[f"{L_}{r}"]._style = copy.copy(K[f"AL{r}"]._style)
    for y in YEARS:
        r = row(y)
        s = K[f"S{r}"].value
        assert s.endswith(f"+COUNTIF(AL{r},\"Check\")"), s
        K[f"S{r}"].value = s + f"+COUNTIF(AM{r}:AN{r},\"Check\")"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("energy_csv")
    ap.add_argument("dst")
    a = ap.parse_args()
    lines = Path(a.energy_csv).read_text().splitlines()
    sha = lines[0].split()[-1]
    rdr = list(csv.reader(lines[1:]))
    hdr = rdr[0]
    data = {k: [float(r[j]) for r in rdr[1:]] for j, k in enumerate(hdr) if k != "year"}
    assert [int(r[0]) for r in rdr[1:]] == list(YEARS)
    need = ["halls_mw", "cap_works", "alu_kt", "cu_kt", "hyd_mf", "cap_col2"]
    for k in need:
        if f"{k}__story" not in data:
            raise SystemExit(f"{a.energy_csv} lacks {k}: re-run energy/build/export_energy.py")

    wb = openpyxl.load_workbook(a.src)
    if "Energy link" not in wb.sheetnames:
        raise SystemExit("needs the CR-052 workbook (Energy link sheet)")
    if "Works" in wb.sheetnames:
        raise SystemExit("Works sheet already exists: build from the CR-052 workbook")
    base.add_levers(wb, levers())
    W = build_works(wb, data)
    link_atomic(wb, W)
    E = build_electro(wb, data)
    link_champions(wb, E)
    add_capacity_inputs(wb, data)
    build_account(wb, W, E, LINE)
    patch_links(wb)
    X = wb["Energy link"]
    X["A2"].value = X["A2"].value + (f" CR-051/054/055 build (energy outputs {sha[:16]}…): the investment account's identified components "
                                     "and the financing of power (AL-BJ), with the capacities it reads (BK-BP).")
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "4 Nov: CR-051/054/055"
    Ch.cell(n, 2).value = "The Works' costs and the champions"
    Ch.cell(n, 3).value = (
        "CR-051 (Works sheet, into Atomic AD-AG): the halls at halls_y12 × Y-12 (Story 2.75) on M2's timetable and their "
        "operation by the energy workbook's draw (replacing CR-050's hall rows), the feed plant and powerhouse, the Columbia "
        "station with the breeder, gaseous diffusion, the Works' dams and Rock Island (investment), the White Bluffs fee and "
        "the royalty, Rock Island's sales, the Mint's silver (memo). CR-054/055 (Electro champions, into Champions AO and BF): "
        "aluminium by destination with the 1931-32 export price, aircraft, nitrogen, electric steel, zinc, magnesium, "
        "phosphorus, copper refining (reconciled with Resources F), rubber and hydrogenation (losses shown), alumina from the "
        "Gulf, plant investment. Energy link AL-BJ: power investment counted once (second units at col2_cost, the Columbia-Sierra "
        "line added), the identified components and the residual; the Fund's credit, the power estate's bonds and the Reserve "
        "Bank's purchases in 1930-32 (Gold & money I); two new checks. Energy outputs SHA-256 " + sha[:16] + "…. MODEL.")
    for c in range(1, 4):
        Ch.cell(n, c)._style = copy.copy(Ch.cell(n - 1, c)._style)
    S = wb["Start"]
    r0 = S.max_row + 1
    for i, (nm, txt) in enumerate((("Works", "CR-051: what the halls, the feed plant, the Columbia station, gaseous diffusion and the Works' dams cost (into Atomic)."),
                                   ("Electro champions", "CR-054 and CR-055: aluminium, aircraft and the electrochemistry, valued (into Champions)."),
                                   ("Energy link", "CR-052 and CR-055: the energy workbook's paths, the investment and consumption account, and how power is financed."))):
        S.cell(r0 + i, 1).value = nm
        S.cell(r0 + i, 2).value = txt
        for c in (1, 2):
            S.cell(r0 + i, c)._style = copy.copy(S.cell(81, c)._style)
    wb.save(a.dst)
    print(f"saved {a.dst}")


if __name__ == "__main__":
    main()
