"""CR-081 and CR-082: China's loans and the provisioning doctrine in the workbook (22 November 2026).

    python3 finance/build/cr081_082_provisioning.py IN.xlsx OUT.xlsx [--off]

IN is the workbook after cr076_drink_coffee.py (the last step of cr057_rebuild_pair.py). The script
never recalculates; run LibreOffice afterwards. With --off the master lever pv_on is saved at 0 in
both cases, which must reproduce IN's values exactly (every row's amount is multiplied by pv_on).

Authorization: the author, 22 November 2026, 14:05 ("I approve all as recommended", CR-082 D19,
item 6: one task after the merge for CR-081's loans, Chile's loan, the nitrogen plants and the
storage works, with the Entente's grain inside the existing advances). Amounts MODEL.

What this adds, as Events rows (Events is read by the Budget, Loans, Debt & cash and Saving):
- CR-082 D: the regency's loan to Chile on the nitrate duty (Loan, 1891-92);
- CR-082 A3 and D19: the storage works of 1900-1920 in basins without salmon, lent to the
  districts on Development Fund credit (Investment, 1900-1920) and repaid from water rates
  (Receipt, 1906-1932), on the pattern of CR-071 C5's rows E243-E244;
- CR-081 C (P-4b, P-5): the banner loan of 1908, the Treasury's part (Loan, 1908-1912);
- CR-082 R-2: Realm credit for the Gulf's rice, feed and drainage under the provisioning
  compact of 1928 (Loan, 1928-1932);
- CR-081 G-10: the wheat credit to China's relief commission (Loan, 1931);
- CR-081 G-14: the Crown's granary, bought by the Patrimony from its own reserves (Commitment, a
  memo: no Treasury cash, no new issue; 1931-32).

The nitrogen plants are re-sized in the energy workbook (energy/build/energy_inputs.py, the CR-082
block: eln_kt and haber_kt), which the Electro champions sheet reads; this script does not touch them.

What is not added, and why:
- the Entente's grain (CR-082 F-16): bought with the Entente advances already in E70-E74;
- the railway bonds of 1896: the Treasury's part is already E53; the rest is San Francisco savers';
- the conservancy of 1891, the Pingxiang credit of 1904 and the Shanghai power bonds of 1929:
  China's or a bank's money, not the Treasury's;
- Chilean buyers' credit for the British houses' fields: Realm banks', not the Treasury's;
- the conversion of Chile's loan to the copper duty in the mid-1920s and New Zealand's crop
  guarantee of 1931: no cash (a change of security; a guarantee never called before 1933);
- the dry-land programme: inside the growth engine's research flow (Growth sheet);
- the Realm's grain sales abroad: the workbook has no commodity trade account.
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402

AUTHOR = "the author, 22 November 2026, 14:05 (CR-082 D19)"
base.AUTHOR = AUTHOR

LEVERS = [
    "— CR-081 and CR-082: China's loans and provisioning (22 Nov 2026) —",
    ("pv_on", "Provisioning and China: 1 = on; 0 = the input workbook exactly", 1, 1, "switch",
     "Author, 22 Nov 2026, 14:05 (CR-082 D19)", "0 reproduces the input workbook exactly. 1 adds the Events rows of CR-081 and CR-082."),
    ("pv_chile", "Chile: the regency's loan on the nitrate duty ($m)", 10, 14, "$m",
     "CR-082 D (MODEL)", "Lent in 1891-92 to the Chilean state after the armistice, secured on the nitrate duty; moved to the copper duty in the mid-1920s (D19)."),
    ("pv_st_acres", "Storage works: acres brought under water by storage, 1900-1920", 4500000, 4500000, "acres",
     "CR-082 A3 (F-1c revised, MODEL)", "13.8 million acres under the works by 1900, 18.3 million by 1920."),
    ("pv_st_cost", "Storage works: cost per acre served ($)", 60, 90, "$ an acre",
     "Story assumption (MODEL)", "Below the Reclamation Service's projects of 1903-20 (to verify), because the districts' canals already exist (CR-071 C5). Stress: half as much again."),
    ("pv_st_loss", "Storage works: share of the districts' loans never repaid", 0.25, 0.4, "share",
     "Story assumption (MODEL)", "As CR-071 C5 (sp_irr_loss)."),
    ("pv_st_years", "Storage works: years over which the water rates repay", 30, 30, "years",
     "Story assumption (MODEL)", "Repayments from 1906 to 1932 inside the book; the rest after it."),
    ("pv_bn_taels", "Banner loan of 1908: principal (Haikwan taels)", 40000000, 50000000, "taels",
     "CR-081 P-4b (MODEL)", "Service of 3-3.5 million taels a year once fully drawn in 1912 (P-5's table)."),
    ("pv_tael_usd", "Dollars per Haikwan tael, 1908-1912", 0.66, 0.66, "$ a tael",
     "Historical (to verify)", "About $0.63-0.74 in 1908-1912."),
    ("pv_bn_pub", "Banner loan: the Treasury's part", 0.5, 0.5, "share",
     "Story assumption (MODEL)", "The rest placed with San Francisco savers, as for the other China loans (E53, E191)."),
    ("pv_gulf", "Gulf provisioning compact: Realm credit for rice, feed and drainage, 1928-32 ($m)", 25, 35, "$m",
     "CR-082 R-2 (MODEL)", "After the flood of 1927, with Hoover's relief."),
    ("pv_wheat_bu", "Wheat credit to China's relief commission (bushels)", 15000000, 15000000, "bushels",
     "CR-081 G-10 (APPROVED)", "Fifteen million bushels of wheat and flour, serviced from the Customs' flood-relief surtax."),
    ("pv_wheat_usd", "Wheat credit: dollars a bushel, 1931", 0.6, 0.6, "$ a bushel",
     "Historical (to verify)", "Our timeline's sale of 1931 was valued at about $9 million."),
    ("pv_gran_t", "The Crown's granary: home wheat and feed bought, 1931-32 (tonnes)", 3000000, 4000000, "tonnes",
     "CR-081 G-14 (MODEL)", "A reserve against a bad year or a closed sea, about a month of the Realm's grain."),
    ("pv_gran_usd", "The Crown's granary: price paid ($ a tonne)", 18, 18, "$ a tonne",
     "Story assumption (MODEL)", "The slump's price for wheat and feed together."),
]

ROWS = [
    # (start, end, label, category, group, party, formula for H, gold, status, section, basis)
    (1891, 1892, "Chile: the regency's loan on the nitrate duty after the armistice (CR-082)", "Loan", "Continental", "Chile",
     "=pv_on*pv_chile/2", "No", "Approved", "§25 (CR-082 D)", "Secured on the nitrate duty; on the copper duty from the mid-1920s (D19)"),
    (1900, 1920, "Storage works in basins without salmon, lent to the districts on Development Fund credit (CR-082)", "Investment",
     None, None, "=pv_on*pv_st_acres*pv_st_cost/21/1000000", "No", "Approved", "§25 (CR-082 A3, D19)",
     "Minidoka, Jackson Lake, the Salt and Yuma, Elephant Butte, the Truckee and Carson, Strawberry Valley; each under its compact"),
    (1906, 1932, "Storage works: the districts' repayments from water rates (CR-082)", "Receipt", None, None,
     "=pv_on*pv_st_acres*pv_st_cost*(1-pv_st_loss)/pv_st_years/1000000", "No", "Approved", "§25 (CR-082)",
     "As CR-071 C5 (E244)"),
    (1908, 1912, "China: the banner loan of 1908, the Treasury's part (CR-081)", "Loan", "Asia", "China",
     "=pv_on*pv_bn_taels*pv_tael_usd*pv_bn_pub/5/1000000", "No", "Approved", "§26 (CR-081 P-4b)",
     "Serviced from the stipend funds, the customs balance second; on the customs from 1912"),
    (1928, 1932, "Gulf: credit for rice, feed and drainage under the provisioning compact (CR-082)", "Loan", "Continental",
     "Gulf Republic", "=pv_on*pv_gulf/5", "No", "Approved", "§25 (CR-082 R-2)", "After the flood of 1927; the admission tests unchanged"),
    (1931, 1931, "China: wheat credit to the relief commission (CR-081)", "Loan", "Asia", "China",
     "=pv_on*pv_wheat_bu*pv_wheat_usd/1000000", "No", "Approved", "§34 (CR-081 G-10)", "Serviced from the Customs' flood-relief surtax"),
    (1931, 1932, "The Crown's granary, bought by the Patrimony from its own reserves (CR-081; memo, no Treasury cash)", "Commitment",
     None, None, "=pv_on*pv_gran_t*pv_gran_usd/2/1000000", "No", "Approved", "§34 (CR-081 G-14)",
     "The Patrimony's board votes it as an investment; no new issue, so the Bank's refusal to print stands"),
]


def add_rows(wb) -> list[str]:
    ids = []
    for a, b, label, cat, grp, party, h, gold, status, sec, basis in ROWS:
        r = base.add_event(wb, [a, b, label, cat, grp, party, h, None, gold, status, sec, basis])
        if r > 400:
            raise SystemExit("Events table full")
        ids.append(wb["Events"].cell(r, 1).value)
    return ids


def log(wb, ids: list[str], off: bool) -> None:
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "22 Nov: CR-081, CR-082"
    Ch.cell(n, 2).value = "China's loans and provisioning"
    Ch.cell(n, 3).value = (f"Master lever pv_on (at 0 the input workbook exactly). Events {ids[0]}-{ids[-1]}: Chile's loan (1891-92); "
                           "the storage works of 1900-1920 and their repayments; the banner loan of 1908; the Gulf's provisioning credit "
                           "(1928-32); the wheat credit to China (1931); the Crown's granary as a memo. The nitrogen plants are re-sized "
                           "in the energy workbook. MODEL.")
    for c_ in range(1, 4):
        Ch.cell(n, c_)._style = copy.copy(Ch.cell(n - 1, c_)._style)
    if off:
        L = wb["Levers"]
        rr = int(wb.defined_names["pv_on"].attr_text.split("$")[-1])
        L.cell(rr, 3).value = 0
        L.cell(rr, 4).value = 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--off", action="store_true")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    if "dc_on" not in wb.defined_names:
        raise SystemExit("needs the workbook after cr076_drink_coffee.py")
    if "pv_on" in wb.defined_names:
        raise SystemExit("CR-081 and CR-082 already added")
    base.add_levers(wb, LEVERS)
    ids = add_rows(wb)
    log(wb, ids, a.off)
    wb.save(a.dst)
    print(f"wrote {a.dst}: {len(LEVERS) - 1} levers, Events {ids[0]}-{ids[-1]}")


if __name__ == "__main__":
    main()
