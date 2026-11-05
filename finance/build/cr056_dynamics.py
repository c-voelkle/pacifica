"""The dynamic layer: second- and third-order effects of Pacifica's investments (CR-056).

    python3 finance/build/cr056_dynamics.py IN.xlsx ENERGY_OUTPUTS.csv OUT.xlsx

IN is the CR-051/054/055 workbook (SHA-256 cba70b31...). ENERGY_OUTPUTS.csv is written by
energy/build/export_energy.py (it must carry the dynamic layer's series: fact_elec, homes_wired,
homes, pump_acres, el_price, veh_pp, kwh_home). The script never recalculates; run LibreOffice
(xlsx skill scripts/recalc.py) afterwards, then finance/build/cr056_layers.py.

Authorization: the author, 5 November 2026: "Can you please build the model described here?"
(the handoff of 5 November), then, on the design note: "either replace Paths!L after about 1900
with growth derived from capital, power and spillovers, or keep it as the frontier baseline and
add the new channels on top. Then compare the result against Pacifica's own story, not against
US history." Both are built, on one switch:

  dyn_mode 0  the accounting model, unchanged to the cell;
  dyn_mode 1  Paths!L kept as the frontier; the channels added on top (each measured from
              Pacifica's own 1900 position, not against the Union);
  dyn_mode 2  from dyn_start (1900) Paths!L is replaced by growth derived from capital per
              resident, power per person and a base rate of technical progress; the Fund keeps
              only its premium over the ordinary return on capital; the same channels on top.

Channels (all MODEL): C1 unit electric drive (manufacturing TFP above a threshold share, David
1990), net of the Fund's share of power investment; C3 induced R&D from the Works' bottleneck
technologies into the electrical and chemical champions' world shares (Moretti, Steinwender and
Van Reenen); C4 electrically pumped acres and Valley nitrogen on farms; C5 women's paid work from
wired homes (Vidart 2024). Reported, not driving: C2 prices and a consumer deflator with a
services (Balassa-Samuelson) term; C6 the aircraft learning curve (Wright 1936); C7 a
decomposition of the slump; C8 wages, hours, the Japan memo. Touches on the existing model:
Economy C (mode 2), Economy D (mode 2), Economy J (modes 1-2), Champions Z and AF (modes 1-2);
each reduces exactly to the old formula at dyn_mode 0.
"""
from __future__ import annotations

import argparse
import copy
import csv
import sys
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / "energy" / "build"))
import cr041_russian_war as base  # noqa: E402
import cr051_054_055_champions as c51  # noqa: E402

AUTHOR = "CR-056 dynamic layer, 5 Nov 2026"
base.AUTHOR = AUTHOR
FIRST, LAST, YEARS, row, interp = c51.FIRST, c51.LAST, c51.YEARS, c51.row, c51.interp
BENCH = (1900, 1913, 1920, 1924, 1929, 1932)
NEED = ["fact_elec", "homes_wired", "homes", "pump_acres", "el_price", "veh_pp", "kwh_pp", "kwh_home"]


# ------------------------------------------------------------------ levers
LEVERS = [
    "— CR-056: the dynamic layer, second- and third-order effects of the investments (5 Nov 2026) —",
    ("dyn_mode", "Dynamic layer: 0 = accounting model; 1 = channels on top of Paths!L; 2 = growth from capital, power and spillovers", 0, 0,
     "switch", "Author's choice (5 Nov 2026)",
     "0 reproduces the CR-051/054/055 workbook (cba70b31...) exactly. 1 keeps Paths!L as the frontier and adds the channels "
     "(Dynamics T into Economy J; Dynamics AC and AD into Champions AF and Z). 2 replaces Paths!L from dyn_start by "
     "Dynamics AI (capital per resident, power per person, tfp_base) and the Fund's return by its premium over the ordinary "
     "return on capital (Dynamics AK), with the same channels. Saved at 0."),
    ("dyn_start", "Dynamic layer: first year", 1900, 1900, "year", "Model estimate",
     "Channels count from Pacifica's own 1900 position; mode 2 replaces Paths!L from this year."),
    ("el_kappa", "C1: manufacturing TFP per unit of drive share above the threshold", 0.8, 0.5, "×", "Model estimate (anchored)",
     "David (1990, AER P&P): about half of the 5-point acceleration of US manufacturing TFP growth in 1919-29 (against "
     "1909-19) is accounted for by secondary electric motors (verified). With drive share rising about 25 points that decade, "
     "about 1.0-1.1 at the top. Range 0.5-1.1."),
    ("el_thresh", "C1: drive share at which unit drive starts to pay", 0.45, 0.45, "share", "Model estimate (anchored)",
     "David's paradox: little TFP gain while the US share rose from 5% (1899) to 53% (1919, Devine 1983 Table 3, verified); "
     "the gain came once unit drive dominated. Pacifica crosses 0.45 about 1915 (Story)."),
    ("el_lag", "C1: years for factories to be rebuilt around unit drive", 2, 3, "years", "Model estimate", ""),
    ("rd_eps", "C3: private R&D per public R&D (elasticity)", 0.5, 0.3, "elasticity", "Model estimate (anchored)",
     "Moretti, Steinwender and Van Reenen, 'The intellectual spoils of war': a 10% rise in government-funded R&D brings a "
     "5-6% rise in privately funded R&D in the same industry (verified). Range 0.3-0.6."),
    ("rd_gamma", "C3: rise in a champion's world share per log-unit of R&D stock", 0.1, 0.05, "elasticity", "Model estimate",
     "Output elasticity of R&D capital about 0.05-0.15 (Griliches's surveys, to verify)."),
    ("rd_int", "C3: R&D intensity of the electrical and chemical champions", 0.02, 0.02, "share of sales", "Model estimate (to verify)",
     "GE, Westinghouse, du Pont in the 1920s: about 1-3% of sales (to verify)."),
    ("rd_dep", "C3: knowledge depreciation", 0.15, 0.15, "a year", "Model estimate", "The conventional 15% (Hall 2005, to verify)."),
    ("rd_cap_el", "C3: largest electrical world production share", 0.30, 0.28, "share", "Model estimate", "Story path is 0.24 in 1929."),
    ("rd_cap_ch", "C3: largest chemical world share", 0.20, 0.18, "share", "Model estimate", "Story path is 0.15 in 1929."),
    ("ag_va_acre", "C4: extra value added of an electrically pumped acre", 15, 10, "1913 $/acre", "Model estimate (to verify)",
     "California irrigated against dry farming, net of what gravity irrigation and oil engines would have watered anyway "
     "(Census of Agriculture and of Irrigation 1930, to verify)."),
    ("ag_n_share", "C4: share of Valley and Columbia nitrogen used on the Realm's farms", 0.5, 0.4, "share", "Model estimate",
     "CR-054 A2: nitrogen goes to the Valley's and the Concord's farms; the rest to industry and Japan."),
    ("ag_n_yield", "C4: grain per tonne of nitrogen", 25, 20, "t/t", "Model estimate (to verify)", "Early response, about 20-30 kg of grain per kg of N."),
    ("ag_grain_px", "C4: grain price", 33, 33, "1913 $/t", "Model estimate (to verify)", "Wheat about 90 cents a bushel in 1913."),
    ("ag_va_share", "C4: value added in the extra crop", 0.7, 0.7, "share", "Model estimate", ""),
    ("w_lambda", "C5: points of women's paid work per point of homes wired", 0.035, 0.02, "×", "Model estimate (anchored)",
     "Vidart (RES 2024): electrification explains a quarter of the 1880-1940 rise in US women's participation (verified), "
     "about 2.7 of roughly 11 points while wiring went from nothing to about 80%. Range 0.02-0.08 (Greenwood, Seshadri and "
     "Yorukoglu 2005 at the top, to verify)."),
    ("w_lag", "C5: years from wiring to paid work", 1, 2, "years", "Model estimate", ""),
    ("w_adult", "C5: women of working age / residents", 0.33, 0.33, "share", "Model estimate", ""),
    ("w_rel", "C5: output of the extra women workers vs the average worker", 0.58, 0.55, "×", "Model estimate (to verify)",
     "Women's earnings relative to men's about 0.55-0.6 in the 1920s (Goldin, to verify)."),
    ("hrs_eps", "C5: hours worked per unit of real income (elasticity, minus)", 0.15, 0.10, "elasticity", "Model estimate (to verify)",
     "US manufacturing hours fell from 59.6 to 50.6 (15%) while real income per person rose about 70%, 1900-29: about 0.3 over time (hours verified, income to verify); cross-section smaller. Range 0.1-0.25."),
    ("hrs_slump", "C5: short time per point of output below trend", 0.75, 0.75, "×", "Model estimate (to verify)",
     "US 1932: actual manufacturing hours about 38 (to verify; 34.4 in 1934, Census of Manufactures) against a standard of about "
     "50 at an output gap of about 31%: about 0.75-0.8."),
    ("hw_elec", "C5: housework saved in a wired home", 0.25, 0.15, "share of hours", "Model estimate (to verify)",
     "Lebergott's series as used by Greenwood, Seshadri and Yorukoglu (to verify)."),
    ("bs_theta", "C2: services' productivity lead, as a share of the income lead", 0.5, 0.4, "share", "Model estimate",
     "Balassa-Samuelson: services and rent cost (income ratio)^(1 - theta) of the Union's. Range 0.3-0.7."),
    ("res_mult", "C2: household power price over the average price", 2.0, 2.2, "×", "Model estimate",
     "US 1929: residential about 6.3 cents against an average of about 2.7 (to verify); electric cooking on cheap hydro "
     "lowers the ratio."),
    ("car_rel", "C2: a Pacifican car's price against the Union's", 1.0, 1.05, "×", "Model estimate (no anchor)",
     "2.2m cars a year against the Union's 5.3m argues for dearer; cheap aluminium and power for cheaper. Range 0.9-1.1."),
    ("fuel_rel", "C2: motor fuel's price against the Union's", 0.9, 0.95, "×", "Model estimate", "Home oil, the royalty and the trust's refineries."),
    ("app_rel", "C2: electrical appliances' price against the Union's", 0.9, 0.95, "×", "Model estimate", "The AC-standard champion at home."),
    ("food_pass", "C2: share of the farm gain passed to food prices", 0.75, 0.5, "share", "Model estimate", ""),
    ("slump_mult", "C7: multiplier on countercyclical spending", 0.7, 0.5, "×", "Model estimate (to verify)",
     "Barro and Redlick's defence-spending multipliers (about 0.6-0.7); Fishback and Kachanovskaya (JEH 2015). Range 0.4-1.0."),
    ("lab_share", "C8: labour's share of output", 0.6, 0.6, "share", "Model estimate (to verify)", "US compensation about 0.58-0.6 of national income, 1929."),
    ("air_lr", "C6: aircraft cost per doubling of cumulative output", 0.8, 0.85, "×", "Model estimate (anchored)",
     "T. P. Wright (1936), 'Factors affecting the cost of airplanes': 80% per doubling."),
    ("k_alpha", "Mode 2: capital's share of output", 0.3, 0.3, "share", "Model estimate (to verify)", "Kendrick's weights, about 0.3."),
    ("e_alpha", "Mode 2: electricity's share of output", 0.03, 0.03, "share", "Model estimate", "Its cost share, about 0.02-0.04."),
    ("k_dep", "Mode 2: depreciation of the capital stock", 0.04, 0.045, "a year", "Model estimate (to verify)", "Structures and equipment together."),
    ("ky_0", "Mode 2: capital / real GDP in the year before dyn_start", 3.0, 3.0, "×", "Model estimate (to verify)",
     "US reproducible tangible wealth about three times output about 1900 (Goldsmith, to verify)."),
    ("tfp_base", "Mode 2: base technical progress a year (before electric drive and spillovers)", 0.010, 0.010, "a year", "Model estimate (to verify)",
     "US private-economy TFP about 1.0-1.3% a year 1889-1919 (Kendrick, to verify), before the electric-drive surge counted "
     "in C1. Scaled by prod_factor after 1896, so Stress is 0.75%."),
]


# ------------------------------------------------------------------ US anchors (benchmark years; interpolated between)
# Every one TO VERIFY unless marked; sources as given. Current dollars.
US = {
    "cpi": ({1900: 0.85, 1913: 1.0, 1920: 2.02, 1924: 1.73, 1929: 1.73, 1932: 1.38}, "US consumer prices, 1913 = 1",
            "BLS CPI (1913 = 9.9), 1900 from Rees/Officer; to verify."),
    "earn": ({1900: 438, 1913: 621, 1920: 1342, 1924: 1303, 1929: 1405, 1932: 1120}, "US average annual earnings, all employees ($)",
             "Lebergott, HSUS series D; to verify."),
    "kwh_res": ({1900: 15, 1913: 8.5, 1920: 7.5, 1924: 7.3, 1929: 6.3, 1932: 5.6}, "US household power price (cents/kWh)",
                "EEI average residential revenue; to verify."),
    "car": ({1900: 650, 1913: 550, 1920: 525, 1924: 295, 1929: 450, 1932: 460}, "US basic car ($)",
            "Curved-dash Oldsmobile 1901, Ford Model T touring 1913-24, Model A 1929, Model B 1932 list prices; to verify."),
    "gas": ({1900: 15, 1913: 17, 1920: 30, 1924: 21, 1929: 21, 1932: 18}, "US motor fuel (cents/gallon)", "Retail; to verify."),
    "bread": ({1900: 4.5, 1913: 5.6, 1920: 11.5, 1924: 8.8, 1929: 8.8, 1932: 7.0}, "US bread (cents/lb)", "BLS retail prices; 1900 estimated; to verify."),
    "milk": ({1900: 6.0, 1913: 8.9, 1920: 16.7, 1924: 13.6, 1929: 14.4, 1932: 10.7}, "US milk (cents/quart)", "BLS retail prices; to verify."),
    "haircut": ({1900: 15, 1913: 25, 1920: 50, 1924: 50, 1929: 50, 1932: 40}, "US haircut (cents)", "To verify."),
    "cinema": ({1900: 5, 1913: 10, 1920: 25, 1924: 25, 1929: 35, 1932: 25}, "US cinema ticket (cents)", "Average admission; to verify."),
    "radio": ({1920: 0, 1924: 100, 1929: 120, 1932: 50}, "US radio set ($)", "Typical set; to verify."),
    "hours": ({1900: 59.6, 1910: 57.3, 1920: 51.2, 1929: 50.6, 1932: 50.0}, "US manufacturing standard hours a week",
              "Census of Manufactures as tabled by Whaples, EH.net 'Hours of work in U.S. history': 59.6 (1900), 57.3 (1910), "
              "51.2 (1920), 50.6 (1929/30), verified; 1932 the full-time standard before short time (assumed)."),
    "housework": ({1900: 58, 1913: 53.5, 1920: 51, 1924: 49.6, 1929: 47.9, 1932: 46.8}, "US housework hours a week",
                  "Lebergott (58 in 1900) as used by Greenwood, Seshadri and Yorukoglu (2005), linear to about 44 in 1940; to verify."),
    "women": ({1900: 0.206, 1913: 0.22, 1920: 0.237, 1924: 0.24, 1929: 0.247, 1932: 0.25}, "US women in paid work (share)",
              "Goldin (1990), women 16+; to verify."),
    "married": ({1900: 0.056, 1913: 0.075, 1920: 0.09, 1924: 0.10, 1929: 0.115, 1932: 0.12}, "US married women in paid work (share)",
                "Goldin (1990); to verify."),
    "wired": ({1900: 0.05, 1913: 0.17, 1920: 0.35, 1924: 0.5, 1929: 0.68, 1932: 0.70}, "US homes wired (share)",
              "1930: 68% (Construction Physics, verified); earlier to verify."),
    "radio_own": ({1920: 0, 1924: 0.05, 1929: 0.35, 1932: 0.55}, "US homes with a radio", "To verify (1930 census: about 40%)."),
    "washer": ({1913: 0, 1920: 0.05, 1924: 0.10, 1929: 0.24, 1932: 0.25}, "US homes with an electric washer", "To verify."),
    "fridge": ({1920: 0, 1924: 0.005, 1929: 0.05, 1932: 0.13}, "US homes with a refrigerator", "To verify (1930 about 8%)."),
    "veh": ({1900: 0, 1913: 0.013, 1920: 0.087, 1924: 0.155, 1929: 0.22, 1932: 0.195}, "US motor vehicles per person",
            "Registrations over population; to verify (canon: one for every four and a half in 1929)."),
    "hh": ({1900: 4.8, 1913: 4.5, 1920: 4.3, 1924: 4.2, 1929: 4.1, 1932: 4.1}, "US persons per home", "Census; to verify."),
    "gap": ({1929: 0, 1930: 0.11, 1931: 0.19, 1932: 0.31}, "US output below its 1929 path (share)",
            "BEA real GDP 1930-32 at 91.5%, 85.6% and 74.6% of 1929 against a 2.5% trend; to verify."),
}
MFG = {1846: 0.05, 1880: 0.12, 1900: 0.22, 1913: 0.25, 1920: 0.28, 1929: 0.27, 1932: 0.25}
FARM = {1846: 0.5, 1880: 0.25, 1900: 0.16, 1913: 0.12, 1920: 0.11, 1929: 0.08, 1932: 0.07}
WEIGHTS = [("food", 0.35), ("rent", 0.17), ("clothing", 0.15), ("power", 0.02), ("other_fuel", 0.03),
           ("appliances", 0.05), ("car", 0.03), ("motor_fuel", 0.03), ("services", 0.17)]


def us_col(sh, key: str) -> str:
    pts, head, src = US[key]
    vals = interp(pts, before=0 if key in ("radio", "radio_own", "washer", "fridge", "veh", "gap") else None)
    if key == "gap":
        vals = {y: (pts.get(y, 0) if y >= 1930 else 0) for y in YEARS}
    return sh.add(f"us_{key}", head, lambda y, r: round(vals[y], 4), is_input=True, note=src + " Interpolated between benchmarks.")


def new_sheet(wb, name, after, title, purpose):
    sh = c51.Sheet(wb, name, after, title, purpose)
    sh.ws["A3"].value = ("Years run down the page. Blue = input you can change · black = formula. "
                         "Built by finance/build/cr056_dynamics.py; all amounts MODEL.")
    return sh


# ------------------------------------------------------------------ the Dynamics sheet
def build_dynamics(wb, data):
    D = new_sheet(wb, "Dynamics", "Energy link", "Dynamics: second- and third-order effects of the investments (CR-056)",
                  "dyn_mode (Levers): 0 = the accounting model; 1 = these channels on top of Paths!L; 2 = growth from capital, "
                  "power and base progress in place of Paths!L from dyn_start, with the same channels. The level factor (T) "
                  "multiplies Economy J; the share factors (AC, AD) multiply Champions AF and Z. Columns AM-BG are reported only.")
    es = c51.energy_series
    g = "From the energy workbook"
    drive = es(D, data, "fact_elec", "Factory horsepower on electric drive", group=g)
    hw = es(D, data, "homes_wired", "Homes wired (thousand)")
    hm = es(D, data, "homes", "Homes (thousand)")
    wired = D.add("wired", "Homes wired (share)", lambda y, r: f"=IF({hm}{r}>0,{hw}{r}/{hm}{r},0)", fmt="0%")
    pump = es(D, data, "pump_acres", "Electrically pumped acres (m)")
    kwh = es(D, data, "kwh_pp", "Electricity per person (kWh)")
    elp = es(D, data, "el_price", "Average power price (1913 cents/kWh)")
    veh = es(D, data, "veh_pp", "Vehicles per person")
    kwhh = es(D, data, "kwh_home", "Electricity per wired home (kWh)")
    mv, fv = interp(MFG), interp(FARM)
    mfg = D.add("mfg", "Manufacturing's share of output", lambda y, r: round(mv[y], 4), group="Paths", is_input=True,
                note="MODEL; the US share of national income about 0.25 in the 1920s (to verify).")
    farm = D.add("farm", "Agriculture's share of output", lambda y, r: round(fv[y], 4), is_input=True,
                 note="MODEL; the US share about a fifth in 1900 and a tenth in 1929 (to verify); Pacifica's lower.")

    g = "C1 Unit electric drive"
    dl = D.add("drive_lag", "Drive share, el_lag years before", lambda y, r: f"=INDEX(${drive}$6:${drive}$92,MAX(1,A{r}-1845-el_lag))", group=g)
    fs = D.add("fund_share", "Fund's share of power investment, last year",
               lambda y, r: 0 if y == FIRST else f"=IF('Energy link'!AP{r-1}>0,MIN(1,'Energy link'!AZ{r-1}/'Energy link'!AP{r-1}),0)",
               note="Energy link AZ / AP: the part of power investment the Fund finances, which Economy D already pays at dev_return. "
               "C1 is netted by it so the same kilowatts are not credited twice.")
    c1 = D.add("c1", "C1: output per resident raised by unit drive",
               lambda y, r: f"=IF(AND(dyn_mode>0,A{r}>=dyn_start),{mfg}{r}*el_kappa*MAX(0,{dl}{r}-el_thresh)*(1-{fs}{r}),0)",
               fmt="0.0%", note="mfg share × el_kappa × (drive share lagged − el_thresh) × (1 − the Fund's share).")

    g = "C4 Farms"
    nfarm = D.add("n_farm", "Nitrogen on the Realm's farms (kt N)",
                  lambda y, r: f"=('Electro champions'!I{r}+'Electro champions'!J{r})*ag_n_share", group=g)
    fva = D.add("farm_va", "Extra farm value added (1913 $m)",
                lambda y, r: f"=IF(AND(dyn_mode>0,A{r}>=dyn_start),{pump}{r}*ag_va_acre+{nfarm}{r}*ag_n_yield*ag_grain_px*ag_va_share/1000,0)")
    c4 = D.add("c4", "C4: output per resident raised on the farms",
               lambda y, r: 0 if y == FIRST else f"=IF(Economy!J{r-1}>0,{fva}{r}/(Economy!J{r-1}/Economy!H{r-1}),0)", fmt="0.0%",
               note="Extra farm value added / last year's real non-mining output.")

    g = "C5 Wired homes and women's work"
    wl = D.add("wired_lag", "Homes wired, w_lag years before", lambda y, r: f"=INDEX(${wired}$6:${wired}$92,MAX(1,A{r}-1845-w_lag))", group=g)
    wpts = D.add("women_pts", "Extra women in paid work (share of women)",
                 lambda y, r: f"=IF(AND(dyn_mode>0,A{r}>=dyn_start),w_lambda*MAX(0,{wl}{r}-INDEX(${wired}$6:${wired}$92,dyn_start-1845)),0)", fmt="0.0%")
    c5 = D.add("c5", "C5: output per resident raised by women's work", lambda y, r: f"={wpts}{r}*w_adult*w_rel/lf_rate", fmt="0.0%")
    lev = D.add("level", "Level factor into Economy J", lambda y, r: f"={c1}{r}+{c4}{r}+{c5}{r}", fmt="0.0%",
                note="Economy J × (1 + this) when dyn_mode is 1 or 2.")

    g = "C3 Spillovers from the Works (1913 $m)"
    sel = D.add("sp_el", "Works' spending on magnets, vacuum, high voltage", lambda y, r: f"=Works!S{r}+Works!T{r}+(Works!AA{r}+Works!AB{r})/2", group=g,
                note="The halls' construction and operation and half of gaseous diffusion (Works S, T, AA, AB).")
    sch = D.add("sp_ch", "Works' spending on fluorine chemistry", lambda y, r: f"=Works!V{r}+(Works!AA{r}+Works!AB{r})/2",
                note="The feed plant's construction and half of gaseous diffusion (Works V, AA, AB).")
    bel = D.add("rb_el", "Electrical champion's own R&D", lambda y, r: f"=rd_int*Champions!AC{r}*Champions!AD{r}/Paths!B{r}")
    bch = D.add("rb_ch", "Chemical champion's own R&D", lambda y, r: f"=rd_int*Champions!X{r}*Champions!Y{r}/Paths!B{r}")
    iel = D.add("ri_el", "Induced private R&D, electrical", lambda y, r: f"=IF({bel}{r}>0,{bel}{r}*((1+{sel}{r}/{bel}{r})^rd_eps-1),0)")
    ich = D.add("ri_ch", "Induced private R&D, chemical", lambda y, r: f"=IF({bch}{r}>0,{bch}{r}*((1+{sch}{r}/{bch}{r})^rd_eps-1),0)")
    kel = D.add("k_el", "Induced knowledge stock, electrical", lambda y, r: (f"={iel}{r}" if y == FIRST else f"={c51.col(D.n)}{r-1}*(1-rd_dep)+{iel}{r}"))
    kch = D.add("k_ch", "Induced knowledge stock, chemical", lambda y, r: (f"={ich}{r}" if y == FIRST else f"={c51.col(D.n)}{r-1}*(1-rd_dep)+{ich}{r}"))
    fel = D.add("f_el", "Electrical world share raised by (into Champions AF)",
                lambda y, r: 0 if y == FIRST else (f"=IF(AND(dyn_mode>0,A{r}>=dyn_start,{bel}{r-1}>0),MIN(rd_cap_el/Champions!AD{r}-1,"
                                                   f"rd_gamma*LN(1+{kel}{r-1}/({bel}{r-1}/rd_dep))),0)"), fmt="0.0%")
    fch = D.add("f_ch", "Chemical world share raised by (into Champions Z)",
                lambda y, r: 0 if y == FIRST else (f"=IF(AND(dyn_mode>0,A{r}>=dyn_start,{bch}{r-1}>0),MIN(rd_cap_ch/Champions!Y{r}-1,"
                                                   f"rd_gamma*LN(1+{kch}{r-1}/({bch}{r-1}/rd_dep))),0)"), fmt="0.0%")
    pat = D.add("patents", "Patents granted, with the spillovers (memo)",
                lambda y, r: f"=Champions!F{r}*(1+IF(dyn_mode=0,0,0.25*({fel}{r}+{fch}{r})/rd_gamma*rd_eps))",
                note="Memo: a quarter of patents electrical and chemical, patents rising with their R&D stock (to verify).")

    g = "Mode 2: growth from capital, power and base progress"
    kst = D.add("k", "Capital stock (1913 $m)",
                lambda y, r: 0 if y == FIRST else (f"=IF(A{r}=dyn_start-1,ky_0*Economy!S{r},IF(A{r}>=dyn_start,"
                                                   f"{c51.col(D.n)}{r-1}*(1-k_dep)+'Energy link'!AA{r-1}/Economy!H{r-1},0))"), group=g,
                note="Gross domestic investment (Energy link AA, the inv_share path × GDP) at last year's prices, less k_dep. "
                "In mode 2 the investment share becomes a driver.")
    gk = D.add("gk", "Growth of capital per resident",
               lambda y, r: 0 if y == FIRST else f"=IF(AND(A{r}>=dyn_start,{kst}{r-1}>0),({kst}{r}/{kst}{r-1})/(Economy!B{r}/Economy!B{r-1})-1,0)",
               fmt="0.0%")
    ge = D.add("ge", "Growth of electricity per person",
               lambda y, r: 0 if y == FIRST else f"=IF({kwh}{r-1}>0,{kwh}{r}/{kwh}{r-1}-1,0)", fmt="0.0%")
    gro = D.add("growth", "Trend growth per resident, derived (into Economy C)",
                lambda y, r: f"=k_alpha*{gk}{r}+e_alpha*{ge}{r}+tfp_base*IF(A{r}>=1896,prod_factor,1)", fmt="0.00%")
    yk = D.add("yk", "Real GDP / capital, last year",
               lambda y, r: 0 if y == FIRST else f"=IF({kst}{r-1}>0,Economy!S{r-1}/{kst}{r-1},0)")
    prem = D.add("prem", "Fund's return above the ordinary return on capital (into Economy D)",
                 lambda y, r: f"=MAX(0,dev_return-k_alpha*{yk}{r})",
                 note="Mode 2 counts the Fund's investment in the capital stock, so D keeps only its premium (public-good spillover).")
    paths_g = D.add("paths_l", "Paths!L × prod_factor, for comparison", lambda y, r: f"=Paths!L{r}*IF(A{r}>=1896,prod_factor,1)", fmt="0.00%")

    g = "C6 The air arm (reported)"
    air = D.add("air", "Aircraft and engines (1913 $m)", lambda y, r: f"='Electro champions'!AI{r}/Paths!B{r}", group=g)
    cum = D.add("air_cum", "Cumulative aircraft output (1913 $m)", lambda y, r: (f"={air}{r}" if y == FIRST else f"={c51.col(D.n)}{r-1}+{air}{r}"))
    D.air_px = D.add("air_px", "Aircraft price, Wright's curve (1924 = 1)",
          lambda y, r: f"=IF(AND({cum}{r}>0,${cum}${row(1924)}>0),({cum}{r}/${cum}${row(1924)})^LOG(air_lr,2),\"\")", fmt="0.00")

    g = "C7 The slump, decomposed (reported, 1930-32)"
    ab = D.add("gap_p", "Pacifica's output below trend", lambda y, r: f"=1-Economy!G{r}", group=g, fmt="0.0%")
    ug = us_col(D, "gap")
    cc = D.add("cc", "Power investment, navy and aircraft ($m)", lambda y, r: f"='Energy link'!AP{r}+Budget!O{r}+'Electro champions'!AI{r}")
    r29 = row(1929)
    ccx = D.add("cc_x", "… above their 1929 share of GDP ($m)", lambda y, r: f"=IF(A{r}>=1930,{cc}{r}-${cc}${r29}/Economy!$O${r29}*Economy!O{r},0)")
    dem = D.add("dem", "Points of the gap closed by that demand",
                lambda y, r: f"=IF(A{r}>=1930,slump_mult*{ccx}{r}/(Economy!O{r}/Economy!G{r}),0)", fmt="0.0%")
    D.add("money", "Points left to prices, money and banks", lambda y, r: f"=IF(A{r}>=1930,{ug}{r}-{ab}{r}-{dem}{r},0)", fmt="0.0%",
          note="The Union's gap less Pacifica's, less what demand explains: the residual the Reserve Bank's policy must carry.")

    g = "C8 Wages, hours, partners (reported)"
    earn = D.add("earn", "Average earnings per worker ($)", lambda y, r: f"=lab_share*Labour!C{r}", group=g)
    usx = us_col(D, "earn")
    une = D.add("earn_u", "Union average earnings ($)", lambda y, r: f"={usx}{r}*Labour!BE{r}",
                note="US historical × the Union's productivity against history (Labour BE): what Pacifica's pull leaves the Union.")
    D.add("earn_x", "Pacifica / Union earnings, money", lambda y, r: f"=IF({une}{r}>0,{earn}{r}/{une}{r},\"\")", fmt="0.00")
    ush = us_col(D, "hours")
    D.add("women_us", "US women in paid work (memo)", lambda y, r: round(interp(US["women"][0])[y], 4), is_input=True, fmt="0.0%")
    D.add("japan", "Concord pool aluminium to Japan ($m, memo)", lambda y, r: f"='Electro champions'!AL{r}")
    D.add("union_lost", "Union business lost to the champions ($m, memo)", lambda y, r: f"=Labour!BH{r}")
    return D, dict(drive=drive, wired=wired, kwh=kwh, elp=elp, veh=veh, kwhh=kwhh, farm=farm, fva=fva, wpts=wpts, lev=lev,
                   fel=fel, fch=fch, gro=gro, prem=prem, earn=earn, une=une, ush=ush, ab=ab, dem=dem, ug=ug, air_px=D.air_px, hm=hm)


# ------------------------------------------------------------------ Prices (C2)
def build_prices(wb, d):
    P = new_sheet(wb, "Prices", "Dynamics", "Prices: what things cost in Pacifica and against the Union (CR-056, C2)",
                  "Reported only: nominal GDP, the Budget and the checks are untouched. A consumer deflator against the Union "
                  "(L) from relative prices with 1917-19 budget weights (to verify); services and rent follow the income lead "
                  "(Balassa-Samuelson). The technological-deflation columns are prices relative to Pacifica's own price level.")
    D = "Dynamics!"
    usc = us_col(P, "cpi")
    hp = P.add("p_level", "Pacifica's price level (1913 = 1)", lambda y, r: f"=Economy!H{r}", group="Power")
    pw = P.add("pw_p", "Power to homes, Pacifica (cents/kWh)", lambda y, r: f"={D}{d['elp']}{r}*Economy!H{r}*res_mult")
    pwu = us_col(P, "kwh_res")
    relp = P.add("rel_power", "Power to homes against the Union", lambda y, r: f"=IF({pwu}{r}>0,{pw}{r}/{pwu}{r},1)", fmt="0.00")
    relf = P.add("rel_food", "Food against the Union", group="Relative prices",
                 fn=lambda y, r: 1 if y == FIRST else (f"=1-IF(dyn_mode=0,0,food_pass*{D}{d['fva']}{r}/MAX(1,{D}{d['farm']}{r}*Economy!J{r-1}/Economy!H{r-1}))"),
                 fmt="0.00")
    rels = P.add("rel_serv", "Services and rent against the Union", lambda y, r: f"=MAX(1,Economy!R{r})^(1-bs_theta)", fmt="0.00",
                 note="(Pacifica's GDP per person / the US's)^(1 − bs_theta).")
    cpi = P.add("cpi_rel", "Consumer prices against the Union",
                lambda y, r: (f"=0.35*{relf}{r}+0.17*{rels}{r}+0.15+0.02*{relp}{r}+0.03+0.05*app_rel+0.03*car_rel+0.03*fuel_rel+0.17*{rels}{r}"),
                fmt="0.00", note="Weights: food .35, rent .17, clothing .15, power .02, other fuel .03, furnishings and appliances .05, "
                "the car .03, motor fuel .03, services and other .17 (BLS 1917-19 survey, to verify). Clothing and other fuel at 1.")
    r13 = row(1913)
    P.add("cons_x", "Household consumption per person / US, money", lambda y, r: f"='Energy link'!AK{r}", group="Consumption", fmt="0.00")
    P.add("cons_xr", "… at Union prices", lambda y, r: f"=IF(ISNUMBER('Energy link'!AK{r}),'Energy link'!AK{r}/{cpi}{r},\"\")", fmt="0.00")
    P.add("cons_real", "Household consumption per person, 1913 Pacifican prices ($)",
          lambda y, r: f"='Energy link'!AI{r}/(Economy!H{r}*{cpi}{r}/${cpi}${r13})")
    g = "Technological deflation (relative to Pacifica's price level, 1913 = 1)"
    P.add("td_power", "Power to homes", lambda y, r: f"=({pw}{r}/{hp}{r})/(${pw}${r13}/${hp}${r13})", group=g, fmt="0.00")
    P.add("td_alu", "Aluminium (pool price)", lambda y, r: f"=IF('Electro champions'!T{r}>0,('Electro champions'!T{r}/{hp}{r})/('Electro champions'!T${r13}/{hp}${r13}),\"\")", fmt="0.00")
    usc_car = us_col(P, "car")
    P.add("td_car", "A car", lambda y, r: f"=IF({usc_car}{r}>0,({usc_car}{r}*car_rel/{hp}{r})/(${usc_car}${r13}*car_rel/${hp}${r13}),\"\")", fmt="0.00")
    P.add("td_air", "An aircraft (Wright's curve, 1924 = 1)", lambda y, r: f"=Dynamics!{d['air_px']}{r}", fmt="0.00")
    return P, dict(cpi=cpi, relp=relp, relf=relf, rels=rels, pw=pw)


# ------------------------------------------------------------------ Life (benchmark years)
def build_life(wb, d, p):
    ws = wb.create_sheet("Life", index=wb.sheetnames.index("Prices") + 1)
    B = wb["Budget"]
    ws["A1"].value = "Life in Pacifica at benchmark years (CR-056)"
    ws["A2"].value = ("What a family earns, buys and does with its time, for the active case and dyn_mode. Pacifican prices are the "
                      "Union's historical prices × Pacifica's relative prices (Prices). Hours of work = price / hourly earnings "
                      "(50 weeks). Every US anchor TO VERIFY unless the Dynamics or Prices note says verified. All MODEL.")
    ws["A3"].value = "Built by finance/build/cr056_dynamics.py. Reported only; nothing here feeds the model."
    for c, s in (("A1", B["A1"]), ("A2", B["A2"]), ("A3", B["A3"])):
        ws[c]._style = copy.copy(s._style)
    hdr, body, grp = B["B5"]._style, B["B6"]._style, B["B4"]._style
    dsh, psh = "Dynamics!", "Prices!"
    dcols = wb["Dynamics"]
    pcol = {wb["Prices"].cell(5, c).value: openpyxl.utils.get_column_letter(c) for c in range(1, wb["Prices"].max_column + 1)}
    dcol = {dcols.cell(5, c).value: openpyxl.utils.get_column_letter(c) for c in range(1, dcols.max_column + 1)}

    def U(key):  # a US anchor value at year y, from the script (constants, sourced in Dynamics/Prices notes)
        vals = interp(US[key][0], before=0)
        return lambda y: round(vals[y], 4)

    hr = lambda r: f"(Dynamics!{d['earn']}{r}/(Dynamics!{d['hours']}{r}*50))"  # noqa: E731
    items = [
        ("Earnings", "Average earnings, Pacifica ($)", lambda y, r: f"=Dynamics!{d['earn']}{r}", "#,##0"),
        (None, "Average earnings, Union ($)", lambda y, r: f"=Dynamics!{d['une']}{r}", "#,##0"),
        (None, "… Pacifica / Union, at Union prices", lambda y, r: f"=Dynamics!{d['earn']}{r}/Dynamics!{d['une']}{r}/Prices!{p['cpi']}{r}", "0.00"),
        (None, "Family income, with a working wife's chance ($)",
         lambda y, r: f"=Dynamics!{d['earn']}{r}*(1+({U('married')(y)}+IF(dyn_mode=0,0,Dynamics!{d['wpts']}{r}))*w_rel)", "#,##0"),
        ("Prices (Pacifica, current)", "A kWh at home (cents)", lambda y, r: f"=Prices!{p['pw']}{r}", "0.0"),
        (None, "A basic car ($)", lambda y, r: f"={U('car')(y)}*car_rel", "#,##0"),
        (None, "A gallon of motor fuel (cents)", lambda y, r: f"={U('gas')(y)}*fuel_rel", "0"),
        (None, "A pound of bread (cents)", lambda y, r: f"={U('bread')(y)}*Prices!{p['relf']}{r}", "0.0"),
        (None, "A quart of milk (cents)", lambda y, r: f"={U('milk')(y)}*Prices!{p['relf']}{r}", "0.0"),
        (None, "A haircut (cents)", lambda y, r: f"={U('haircut')(y)}*Prices!{p['rels']}{r}", "0"),
        (None, "A cinema ticket (cents)", lambda y, r: f"={U('cinema')(y)}*Prices!{p['rels']}{r}", "0"),
        (None, "A radio set ($)", lambda y, r: (f"={U('radio')(y)}*app_rel" if U('radio')(y) > 0 else "—"), "0"),
        ("In hours of work", "A car (hours)", lambda y, r: f"={U('car')(y)}*car_rel/{hr(r)}", "#,##0"),
        (None, "A month's power, 1 wired home (hours)", lambda y, r: f"=Prices!{p['pw']}{r}/100*Dynamics!{d['kwhh']}{r}/12/{hr(r)}", "0.0"),
        (None, "A haircut (hours)", lambda y, r: f"={U('haircut')(y)}*Prices!{p['rels']}{r}/100/{hr(r)}", "0.00"),
        (None, "A radio (hours)", lambda y, r: (f"={U('radio')(y)}*app_rel/{hr(r)}" if U('radio')(y) > 0 else "—"), "0"),
        ("The home", "Homes wired, Pacifica", lambda y, r: f"=Dynamics!{d['wired']}{r}", "0%"),
        (None, "Homes wired, Union", lambda y, r: U("wired")(y), "0%"),
        (None, "kWh a wired home", lambda y, r: f"=Dynamics!{d['kwhh']}{r}", "#,##0"),
        (None, "Homes with a radio", lambda y, r: f"=MIN(0.95,{U('radio_own')(y)}*Dynamics!{d['wired']}{r}/{U('wired')(y)})", "0%"),
        (None, "Homes with an electric washer", lambda y, r: f"=MIN(0.9,{U('washer')(y)}*Dynamics!{d['wired']}{r}/{U('wired')(y)})", "0%"),
        (None, "Homes with a refrigerator", lambda y, r: f"=MIN(0.9,{U('fridge')(y)}*Dynamics!{d['wired']}{r}/{U('wired')(y)})", "0%"),
        (None, "Food's share of the budget", lambda y, r: f"=0.35*Prices!{p['relf']}{r}/Prices!{p['cpi']}{r}", "0%"),
        ("Getting about", "Motor vehicles per home, Pacifica", lambda y, r: f"=Dynamics!{d['veh']}{r}*Economy!B{r}/(Dynamics!{d['hm']}{r}*1000)", "0.00"),
        (None, "Motor vehicles per home, Union", lambda y, r: f"={U('veh')(y)}*{U('hh')(y)}", "0.00"),
        ("Time and work", "Hours a week, Pacifica", lambda y, r: f"=Dynamics!{d['hours']}{r}", "0.0"),
        (None, "Hours a week, Union", lambda y, r: f"=Dynamics!{d['hours_u']}{r}", "0.0"),
        (None, "Housework hours a week, Pacifica",
         lambda y, r: f"={U('housework')(y)}*(1-hw_elec*MAX(0,Dynamics!{d['wired']}{r}-{U('wired')(y)}))", "0.0"),
        (None, "Housework hours a week, Union", lambda y, r: U("housework")(y), "0.0"),
        (None, "Women in paid work, Pacifica", lambda y, r: f"={U('women')(y)}+IF(dyn_mode=0,0,Dynamics!{d['wpts']}{r})", "0.0%"),
        (None, "Married women in paid work, Pacifica", lambda y, r: f"={U('married')(y)}+IF(dyn_mode=0,0,Dynamics!{d['wpts']}{r})", "0.0%"),
        (None, "Women in paid work, Union", lambda y, r: U("women")(y), "0.0%"),
    ]
    ws.cell(5, 1).value, ws.cell(5, 2).value = "Group", "Item"
    for c in (1, 2):
        ws.cell(5, c)._style = copy.copy(hdr)
    for j, y in enumerate(BENCH):
        ws.cell(5, 3 + j).value = y
        ws.cell(5, 3 + j)._style = copy.copy(hdr)
    for i, (grp_, lab, fn, fmt) in enumerate(items):
        rr = 6 + i
        ws.cell(rr, 1).value = grp_
        ws.cell(rr, 1)._style = copy.copy(grp)
        ws.cell(rr, 2).value = lab
        ws.cell(rr, 2)._style = copy.copy(body)
        for j, y in enumerate(BENCH):
            cell = ws.cell(rr, 3 + j)
            cell.value = fn(y, row(y))
            cell._style = copy.copy(body)
            cell.number_format = fmt
    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 46
    for j in range(len(BENCH)):
        ws.column_dimensions[openpyxl.utils.get_column_letter(3 + j)].width = 11
    ws.freeze_panes = "C6"
    return ws


# ------------------------------------------------------------------ hooks into the existing model
def hook(wb, d):
    E, C = wb["Economy"], wb["Champions"]
    for y in YEARS:
        r, p = row(y), row(y) - 1
        j = E[f"J{r}"].value
        want = f"=B{r}*F{r}*(1+I{r})*G{r}*H{r}/1000000"
        assert j == want, (y, j)
        E[f"J{r}"].value = f"=B{r}*F{r}*(1+I{r})*(1+IF(dyn_mode=0,0,Dynamics!{d['lev']}{r}))*G{r}*H{r}/1000000"
        c = E[f"C{r}"].value
        assert c == f"=Paths!L{r}*IF($A{r}>=1896,prod_factor,1)", (y, c)
        E[f"C{r}"].value = f"=IF(AND(dyn_mode=2,$A{r}>=dyn_start),Dynamics!{d['gro']}{r},Paths!L{r}*IF($A{r}>=1896,prod_factor,1))"
        dd = E[f"D{r}"].value
        if y > FIRST:
            assert dd == f"=IF(O{p}>0,MIN(dev_cap,dev_return*'Debt & cash'!N{p}/O{p}),0)", (y, dd)
            E[f"D{r}"].value = (f"=IF(AND(dyn_mode=2,$A{r}>=dyn_start),IF(O{p}>0,MIN(dev_cap,Dynamics!{d['prem']}{r}*'Debt & cash'!N{p}/O{p}),0),"
                                f"IF(O{p}>0,MIN(dev_cap,dev_return*'Debt & cash'!N{p}/O{p}),0))")
        z = C[f"Z{r}"].value
        assert z == f"=X{r}*Y{r}*chem_va*B{r}", (y, z)
        C[f"Z{r}"].value = f"=X{r}*Y{r}*(1+IF(dyn_mode=0,0,Dynamics!{d['fch']}{r}))*chem_va*B{r}"
        af = C[f"AF{r}"].value
        assert af == f"=AC{r}*AD{r}*elec_va*B{r}", (y, af)
        C[f"AF{r}"].value = f"=AC{r}*AD{r}*(1+IF(dyn_mode=0,0,Dynamics!{d['fel']}{r}))*elec_va*B{r}"
    base.note(E["C5"], (E["C5"].comment.text + "\n\n" if E["C5"].comment else "")
              + "CR-056: in dyn_mode 2, from dyn_start, growth derived from capital, power and base progress (Dynamics).", 120)
    base.note(E["D5"], (E["D5"].comment.text + "\n\n" if E["D5"].comment else "")
              + "CR-056: in dyn_mode 2 the Fund earns only its premium over the ordinary return on capital (Dynamics).", 120)
    base.note(E["J5"], (E["J5"].comment.text + "\n\n" if E["J5"].comment else "")
              + "CR-056: × (1 + the Dynamics level factor) in dyn_mode 1 and 2.", 120)


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
    data = {k: [float(x[j]) for x in rdr[1:]] for j, k in enumerate(hdr) if k != "year"}
    for k in NEED:
        if f"{k}__story" not in data:
            raise SystemExit(f"{a.energy_csv} lacks {k}: re-run energy/build/export_energy.py")

    wb = openpyxl.load_workbook(a.src)
    if "Dynamics" in wb.sheetnames:
        raise SystemExit("Dynamics sheet already exists: build from the CR-051/054/055 workbook")
    base.add_levers(wb, LEVERS)
    D, d = build_dynamics(wb, data)
    P, p = build_prices(wb, d)
    d["hours"] = D.add("hours_p", "Hours a week, Pacifica",
                       lambda y, r: f"=Dynamics!{d['ush']}{r}*MAX(0.5,Economy!R{r}/Prices!{p['cpi']}{r})^(-hrs_eps)*(1-hrs_slump*(1-Economy!G{r}))",
                       group="C5 hours (reported)", fmt="0.0",
                       note="US standard hours × (Pacifica's real income lead at Union prices)^(−hrs_eps) × (1 − hrs_slump × Pacifica's output gap): reported, not a driver.")
    d["hours_u"] = D.add("hours_u", "Hours a week, Union", lambda y, r: f"=Dynamics!{d['ush']}{r}*(1-hrs_slump*Dynamics!{d['ug']}{r})", fmt="0.0",
                         note="US standard hours less short time at the US output gap (Dynamics, C7; 1930-32 only).")
    build_life(wb, d, p)
    hook(wb, d)
    X = wb["Energy link"]
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "5 Nov: CR-056"
    Ch.cell(n, 2).value = "The dynamic layer"
    Ch.cell(n, 3).value = (
        "dyn_mode (Levers; saved 0): 1 adds the channels on top of Paths!L, 2 replaces Paths!L from 1900 by growth from capital, "
        "power and base progress. Channels: unit electric drive (C1), induced R&D into the electrical and chemical shares (C3), "
        "pumped acres and nitrogen on farms (C4), women's work from wired homes (C5); reported: prices and a consumer deflator "
        "(C2, Prices), the aircraft learning curve (C6), the slump decomposed (C7), wages, hours and the life table (C8, Life). "
        "Hooks: Economy C, D, J; Champions Z, AF; each the old formula at dyn_mode 0. Energy outputs SHA-256 " + sha[:16] + "…. MODEL.")
    for c in range(1, 4):
        Ch.cell(n, c)._style = copy.copy(Ch.cell(n - 1, c)._style)
    S = wb["Start"]
    r0 = S.max_row + 1
    for i, (nm, txt) in enumerate((("Dynamics", "CR-056: the dynamic layer's channels (dyn_mode on Levers)."),
                                   ("Prices", "CR-056: relative prices, the consumer deflator against the Union, technological deflation."),
                                   ("Life", "CR-056: life in Pacifica at benchmark years."),
                                   ("Layers", "CR-056: the accounting model and both dynamic modes side by side, Story and Stress (values)."))):
        S.cell(r0 + i, 1).value = nm
        S.cell(r0 + i, 2).value = txt
        for c in (1, 2):
            S.cell(r0 + i, c)._style = copy.copy(S.cell(81, c)._style)
    wb.save(a.dst)
    print(f"saved {a.dst}")


if __name__ == "__main__":
    main()
