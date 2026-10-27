"""Coale–Demeny "West" model life tables, single-year survival.

Port of the regression system in Coale & Demeny, *Regional Model Life Tables
and Stable Populations* (1966; 2nd ed. 1983), as implemented in the R package
demogR (`cdmltw`, Holland Jones) with Jim Oeppen's 2018 corrections
(optimised e10 index values; corrected Gompertz extension above age 80;
corrected infant separation factors). Source file read:
https://raw.githubusercontent.com/cran/demogR/master/R/cdmltw.R

Use `life_table(e0)` to get single-year probabilities of dying for both sexes
at the West level whose both-sex life expectancy at birth equals `e0`.
Valid range: e0 ≈ 18–80 (levels 1–25). Lower values are clamped to level 1;
historical mortality worse than that (war, massacre, famine) is not a life
table and is reported separately by the models as excess loss.
"""
from __future__ import annotations

import math
from functools import lru_cache

AGES5 = [0, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
MAX_AGE = 100  # single-year ages 0..99, plus an open 100+ group

COEF = {
    "F": {
        "eten": [21.40549, 25.32904, 28.86351, 32.07396, 35.01032, 37.71173, 40.20992,
                 42.53003, 44.69388, 46.71830, 48.61905, 50.40814, 52.08187, 53.35198,
                 54.56192, 55.83317, 57.16274, 58.54485, 59.97243, 61.43625, 62.99381,
                 65.49800, 68.71056, 72.92253, 78.62273],
        "ax": [.53774, .39368, .10927, .08548, .10979, .1358, .15134, .17032, .18464, .1939,
               .20138, .2535, .31002, .43445, .53481, .69394, .84589],
        "bx": [-.008044, -.006162, -.001686, -.00132, -.001672, -.002051, -.002276, -.002556,
               -.002745, -.002828, -.002831, -.003487, -.004118, -.005646, -.00646, -.007713,
               -.008239],
        "a1x": [5.8992, 7.4576, 6.2018, 5.9627, 5.9335, 5.9271, 5.8145, 5.6578, 5.3632, 4.96,
                4.5275, 4.4244, 4.3131, 4.3439, 4.2229, 4.1838, 4.1294],
        "b1x": [-.05406, -.08834, -.0741, -.07181, -.06812, -.06577, -.06262, -.05875, -.05232,
                -.0438, -.03436, -.03004, -.02554, -.02295, -.01773, -.01376, -.00978],
        "m105": (0.613, 1.75),
        "a0": (0.050, 3.00, 0.35),   # a0 = c + k*q0 if q0 < 0.1 else cap
    },
    "M": {
        "eten": [21.86761, 25.44740, 28.67272, 31.60223, 34.28159, 36.74631, 39.02583,
                 41.14277, 43.11689, 44.96458, 46.69839, 48.33115, 49.85796, 51.01729,
                 52.12115, 53.28135, 54.49441, 55.75599, 57.05851, 58.39447, 59.81638,
                 62.10227, 65.03413, 68.87841, 74.08120],
        "ax": [0.63726, 0.40548, 0.10393, 0.07435, 0.09880, 0.14009, 0.15785, 0.18260, 0.21175,
               0.25049, 0.27894, 0.33729, 0.38425, 0.48968, 0.59565, 0.73085, 0.89876],
        "bx": [-0.009958, -0.006653, -0.001662, -0.001183, -0.001539, -0.002183, -0.002479,
               -0.002875, -0.003312, -0.003864, -0.004158, -0.004856, -0.005190, -0.006300,
               -0.007101, -0.007911, -0.008695],
        "a1x": [5.8061, 7.1062, 5.4472, 5.0654, 4.8700, 5.0677, 5.2660, 5.3438, 5.2792,
                5.0415, 4.6666, 4.4506, 4.2202, 4.1851, 4.1249, 4.1051, 4.1133],
        "b1x": [-0.05338, -0.08559, -0.06295, -0.05817, -0.05070, -0.05156, -0.05471,
                -0.05511, -0.05229, -0.04573, -0.03637, -0.02961, -0.02256, -0.01891,
                -0.01491, -0.01161, -0.00895],
        "m105": (0.551, 1.75),
        "a0": (0.0425, 2.875, 0.33),
    },
}
FEMALE_SHARE_AT_BIRTH = 1 / 2.05  # sex ratio at birth 105 males per 100 females


def _nqx(sex: str, e10: float) -> list[float]:
    c = COEF[sex]
    out = []
    for ax, bx, a1x, b1x in zip(c["ax"], c["bx"], c["a1x"], c["b1x"]):
        lin = ax + bx * e10
        log = 1e-4 * 10 ** (a1x + b1x * e10)
        slope = (1 / math.log(10)) * (bx / b1x) / log
        q = (lin + log) / 2
        if lin <= log:
            q = lin if slope < 1 else log
        out.append(min(max(q, 0.0), 1.0))
    return out


def _lx_single(sex: str, e10: float) -> list[float]:
    """Survivorship l(x) for single ages 0..MAX_AGE+20."""
    q = _nqx(sex, e10)
    knots = [1.0]
    for qi in q:
        knots.append(knots[-1] * (1 - qi))          # l at 1,5,...,75,80
    ages = AGES5 + [80]
    # Gompertz extension above 80 (Oeppen-corrected)
    l75, q75 = knots[16], q[16]
    nL75 = 5 * l75 * (1 - q75) + 2.5 * l75 * q75
    m77 = l75 * q75 / nL75
    c0, c1 = COEF[sex]["m105"]
    m105 = c0 + c1 * q75
    kappa = math.log(m105 / m77) / 27.5
    m80 = m77 * math.exp(kappa * 2.5)
    l80 = knots[17]
    lx = []
    for x in range(MAX_AGE + 21):
        if x >= 80:
            t = x - 80
            lx.append(l80 * math.exp(-(m80 / kappa) * (math.exp(kappa * t) - 1)))
            continue
        i = max(k for k, a in enumerate(ages) if a <= x)
        a0, a1 = ages[i], ages[i + 1]
        la, lb = knots[i], knots[i + 1]
        # constant hazard within each age group: log-linear l(x)
        lx.append(la * (lb / la) ** ((x - a0) / (a1 - a0)) if lb > 0 else 0.0)
    return lx


def _e0(sex: str, lx: list[float]) -> float:
    q0 = 1 - lx[1]
    c, k, cap = COEF[sex]["a0"]
    a0 = c + k * q0 if q0 < 0.1 else cap
    total = lx[1] + a0 * (lx[0] - lx[1])
    for x in range(1, len(lx) - 1):
        total += (lx[x] + lx[x + 1]) / 2
    return total


@lru_cache(maxsize=None)
def _level_table():
    """(level, e0_both, e10_F, e10_M) on a fine grid of fractional levels."""
    rows = []
    n = len(COEF["F"]["eten"])
    steps = 20
    for i in range((n - 1) * steps + 1):
        s = i / steps
        lo, frac = int(s), s - int(s)
        hi = min(lo + 1, n - 1)
        e10 = {sex: COEF[sex]["eten"][lo] * (1 - frac) + COEF[sex]["eten"][hi] * frac for sex in "FM"}
        eF = _e0("F", _lx_single("F", e10["F"]))
        eM = _e0("M", _lx_single("M", e10["M"]))
        e_both = FEMALE_SHARE_AT_BIRTH * eF + (1 - FEMALE_SHARE_AT_BIRTH) * eM
        rows.append((s, e_both, e10["F"], e10["M"]))
    return rows


@lru_cache(maxsize=4096)
def life_table(e0: float) -> dict:
    """Single-year q(x) for F and M at the West level matching both-sex e0.

    Returns {"F": [q0..q99, q100+=1], "M": [...], "e0": achieved, "clamped": bool}.
    """
    rows = _level_table()
    clamped = e0 < rows[0][1] or e0 > rows[-1][1]
    target = min(max(e0, rows[0][1]), rows[-1][1])
    for (s0, e_a, f_a, m_a), (s1, e_b, f_b, m_b) in zip(rows, rows[1:]):
        if e_a <= target <= e_b:
            w = 0 if e_b == e_a else (target - e_a) / (e_b - e_a)
            e10 = {"F": f_a + w * (f_b - f_a), "M": m_a + w * (m_b - m_a)}
            break
    out = {"e0": target, "clamped": clamped}
    for sex in "FM":
        lx = _lx_single(sex, e10[sex])
        q = [1 - lx[x + 1] / lx[x] if lx[x] > 0 else 1.0 for x in range(MAX_AGE)]
        q.append(1.0)  # open group: everyone dies eventually; handled as survival within 100+
        # survival within the open 100+ group from the Gompertz tail
        tail = sum(lx[MAX_AGE:])
        q[MAX_AGE] = 1 - (sum(lx[MAX_AGE + 1:]) / tail if tail > 0 else 0.0)
        out[sex] = q
    return out


def e0_range() -> tuple[float, float]:
    rows = _level_table()
    return rows[0][1], rows[-1][1]
