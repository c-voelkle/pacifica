"""Apply CR-050 and CR-050-R1 to the financial workbook: re-time the atomic programme.

    python3 finance/build/cr050_atomic_retiming.py IN.xlsx OUT.xlsx

IN is the CR-049 workbook (cr049_atomic_programme.py). The script never recalculates;
run LibreOffice (xlsx skill scripts/recalc.py) afterwards.

The author asked on 3 November 2026 to "update the workbook" after approving CR-050 and
CR-050-R1. Only the Atomic sheet's yearly inputs and notes change; every formula, lever,
Budget link and check stays as CR-049 built it. All amounts are MODEL.

What moves (CR-049 -> CR-050):
- separation halls: decided 1917, first hall 1919 (fails, rebuilt), production from the
  early 1920s, instead of construction from 1912; weapons feed 1920-1927 instead of 1911-1927;
- the desert test: May 1924 instead of about 1920; the sea demonstration of 1927 adds a
  closed zone, fisheries warnings and the scuttling of the target ships;
- the walled college at Hetch Hetchy (spur, tunnel, buildings, 1909-1911), the Tuolumne
  Station, the Me-Wuk and Kootzaduka'a leases, and Ralston College's share under the
  Compact of the Tuolumne (1910);
- the Tokyo station: built 1928-1931, first power 1931 (was 1925-1927, first load 1926-27);
  the four Pacifican stations are built 1929-1932 and follow Tokyo, two loaded in 1932;
- the barium-borne salt: from 1908 the Works buys whole ores and markets Austria's salt
  abroad (more margin), but gives grams as gifts of state from about 1910 (less).
Weapons quantities stay a coarse resource bucket, never per device.
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402
import cr049_atomic_estimate as est  # noqa: E402
import cr049_atomic_programme as prog  # noqa: E402

AUTHOR = "CR-050, 3 Nov 2026"
base.AUTHOR = AUTHOR
ramp = est.ramp

# ------------------------------------------------------------------ uses (t U)
USES = {
    "Research installations (1913, 1916, 1921)": {1913: 50, 1916: 50, 1921: 50},
    "Weapons: separation-hall feed 1920-1927 (test May 1924, three devices 1927)":
        {1920: 10, 1921: 25, **{y: 215 / 6 for y in range(1922, 1928)}},
    "Weapons: separation-hall feed 1928-1932 (small arsenal; count OPEN)": {y: 60 for y in range(1928, 1933)},
    "Energy: Tokyo station (two units, first load 1930-31, first power 1931, refuelling 1932)":
        {1930: 110, 1931: 110, 1932: 45},
    "Energy: Pacifican stations (built 1929-1932; two loaded in 1932, two after)": {1932: 220},
}

# ------------------------------------------------------------------ costs (1913 $m)
COSTS = {
    ("acquisition", "Joachimsthal contract premium and royalties"): est.COSTS[("acquisition", "Joachimsthal contract premium and royalties")],
    ("acquisition", "Shinkolobwe: option, Tanganyika Concessions shares, royalties"):
        est.COSTS[("acquisition", "Shinkolobwe: option, Tanganyika Concessions shares, royalties")],
    ("acquisition", "Fergana concession and Ute lease fees"): est.COSTS[("acquisition", "Fergana concession and Ute lease fees")],
    ("acquisition", "Hetch Hetchy: Me-Wuk lease and Kootzaduka'a share (CR-050-R1)"): ramp({1910: 0.05}),
    ("research", "The Works' atomic laboratories (staff, instruments, recruits)"):
        est.COSTS[("research", "The Works' atomic laboratories (staff, instruments, recruits)")],
    ("research", "Research installations (graphite, metal, buildings)"): {1913: 3, 1916: 3, 1921: 3},
    ("research", "The walled college at Hetch Hetchy: spur, tunnel, buildings, tram (CR-050-R1)"):
        {1909: 1.5, 1910: 2.5, 1911: 2.0},
    ("research", "Ralston College's share under the Compact of the Tuolumne (CR-050-R1)"): ramp({1910: 0.5, 1920: 1.0}),
    ("weapons", "Separation halls: construction 1917-1923 (first hall 1919, rebuilt), enlargement 1928-1930"): {
        1917: 10, 1918: 20, 1919: 25, 1920: 25, 1921: 25, 1922: 15, 1923: 10, **{y: 20 for y in range(1928, 1931)}},
    ("weapons", "Separation halls: operation and hydro power"): ramp({1919: 6, 1922: 8, 1928: 10}),
    ("weapons", "Weapon engineering, the wall's security, test site"): ramp({1909: 1, 1917: 2, 1928: 3}),
    ("weapons", "Desert test (May 1924) and sea demonstration (1927, closed zone)"): {1924: 3, 1927: 7},
    ("energy", "Tokyo station (80 MWe, 1928-1931; financing OPEN)"): {1928: 8, 1929: 10, 1930: 10, 1931: 4},
    ("energy", "Pacifican stations (4 x 40 MWe, 1929-1932; two finished after 1932)"):
        {1929: 10, 1930: 16, 1931: 18, 1932: 20},
}

# ------------------------------------------------------------------ returns (1913 $m)
RADIUM_MARGIN = ramp({1876: 0.5, 1908: 2.4, 1910: 2.1, 1919: 1.7, 1922: 1.4})
STATION_MWE = ramp({1931: 40, 1932: 80})  # Tokyo: first power in 1931 (half a year), full in 1932

NOTES = {
    "Weapons (separation feed)": "A coarse resource bucket, never per device: 1920-1927 for the test of May 1924 and the "
                                 "three devices of 1927 (halls decided 1917, first hall 1919), then a small arsenal whose "
                                 "count is OPEN (input; CR-050).",
    "Energy": "Tokyo station first load 1930-31 and refuelling 1932; two Pacifican stations loaded in 1932 (input; CR-050).",
    "Contracts, concessions, shares": "Joachimsthal premium and royalties, the Shinkolobwe option and Tanganyika "
                                      "Concessions shares, Ute lease and Fergana fees, the Hetch Hetchy lease and the "
                                      "Kootzaduka'a share (input; CR-050-R1).",
    "Laboratories and installations": "The Works' atomic laboratories, the research installations, the walled college at "
                                      "Hetch Hetchy (1909-1911) and Ralston College's share under the Compact of the "
                                      "Tuolumne (input; CR-050-R1).",
    "Separation halls, weapons, tests": "Halls decided 1917, first hall 1919 (fails, rebuilt), enlarged 1928-1930; their "
                                        "operation and power; weapon engineering and the wall's security; the desert test "
                                        "(May 1924) and the sea demonstration (1927) (input; CR-050).",
    "Power stations": "Tokyo (80 MWe, 1928-1931; financing OPEN, entered as Pacifica's) and four Pacifican stations of "
                      "40 MWe, 1929-1932, two finished after 1932 (input; CR-050).",
    "Radium and source trade": "Net margin of the source trade and the barium-borne salt: whole ores bought and Austria's "
                               "salt marketed abroad from 1908, less the grams given as gifts of state (input; CR-050 R1).",
    "Atomic stations in service (MWe)": "Input: Tokyo from 1931 (first power; half a year), 80 MWe in 1932 (CR-050).",
}


def inputs_for(y: int) -> dict:
    sup = [est.SUPPLY[s].get(y, 0.0) for s in prog.SOURCES]
    uses = {"research": 0.0, "weapons": 0.0, "energy": 0.0}
    for name, d in USES.items():
        uses[name.split(":")[0].split(" ")[0].lower()] += d.get(y, 0.0)
    costs = {"acquisition": 0.0, "research": 0.0, "weapons": 0.0, "energy": 0.0}
    for (cat, _), d in COSTS.items():
        costs[cat] += d.get(y, 0.0)
    return {"sup": sup, "use": uses, "cost": costs, "radium": RADIUM_MARGIN.get(y, 0.0),
            "mwe": STATION_MWE.get(y, 0.0), "navy": est.NAVY_SAVING.get(y, 0.0)}


def retime(wb) -> None:
    A = wb["Atomic"]
    heads = {A.cell(5, c).value: c for c in range(2, A.max_column + 1)}
    assert heads["Weapons (separation feed)"] == 9 and heads["Power stations"] == 16 and heads["Atomic stations in service (MWe)"] == 22
    for y in range(1864, prog.LAST + 1):
        r = prog.row(y)
        assert A.cell(r, 1).value == y
        v = inputs_for(y)
        for k in range(5):
            assert not str(A.cell(r, 2 + k).value).startswith("=")
            A.cell(r, 2 + k).value = round(v["sup"][k], 4)
        for c, val in ((8, v["use"]["research"]), (9, v["use"]["weapons"]), (10, v["use"]["energy"]),
                       (13, v["cost"]["acquisition"]), (14, v["cost"]["research"]), (15, v["cost"]["weapons"]),
                       (16, v["cost"]["energy"]), (20, v["radium"]), (22, v["mwe"]), (27, v["navy"])):
            assert not str(A.cell(r, c).value).startswith("="), (y, c)
            A.cell(r, c).value = round(val, 4)
    for head, text in NOTES.items():
        base.note(A.cell(5, heads[head]), text, 110)
    A["A2"].value = ("CR-049, re-timed by CR-050 and CR-050-R1 (MODEL): uranium mined by source and its use for research, "
                     "weapons and energy, the reserve, the programme's cost and its direct returns. Halls decided 1917, "
                     "test May 1924, demonstration 1927, Tokyo station 1928-1931 with first power in 1931.")
    L = wb["Levers"]
    for r in range(1, L.max_row + 1):
        if L.cell(r, 1).value == "atom_cf":
            for c in range(2, L.max_column + 1):
                if isinstance(L.cell(r, c).value, str) and "Tokyo station from 1928" in L.cell(r, c).value:
                    L.cell(r, c).value = L.cell(r, c).value.replace(
                        "Tokyo station from 1928, Pacifican stations 1929-1931.",
                        "Tokyo station from 1931 (CR-050); Pacifican stations loaded in 1932.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    if "Atomic" not in wb.sheetnames:
        raise SystemExit("needs the CR-049 workbook (Atomic sheet)")
    retime(wb)
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "3 Nov: CR-050"
    Ch.cell(n, 2).value = "Atomic programme re-timed"
    Ch.cell(n, 3).value = ("CR-050 and CR-050-R1: halls decided 1917 (first hall 1919, rebuilt), weapons feed 1920-1927, "
                           "test May 1924, demonstration 1927 with a closed zone; the walled college at Hetch Hetchy, the "
                           "Me-Wuk and Kootzaduka'a leases and Ralston College's share; Tokyo station 1928-1931 (first "
                           "power 1931), Pacifican stations after it; salt margin with whole ores, Austrian marketing and "
                           "gifts of state. Inputs and notes only; formulas, levers and links unchanged. MODEL.")
    for c in range(1, 4):
        Ch.cell(n, c)._style = copy.copy(Ch.cell(n - 1, c)._style)
    wb.save(a.dst)
    print(f"saved {a.dst}")


if __name__ == "__main__":
    main()
