"""Cohort-component population engine: single years of age 0..100+, two sexes,
any number of groups, annual steps.

Each step, for every group:
  1. deaths: survivors = population × (1 − q(age, sex)) from the group's life table;
  2. ageing: survivors move up one year of age (100+ is open);
  3. births: female population at mid-step × age-specific fertility, split by the
     sex ratio at birth (105:100); infants are exposed to half a year of risk;
  4. migration: net arrivals added with an age-sex profile.

Standard library only. All rates come from data files; this module has no
historical numbers of its own.
"""
from __future__ import annotations

import math
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

import cdwest

DATA = Path(__file__).resolve().parent / "data"
N = cdwest.MAX_AGE + 1  # ages 0..100 (100 = 100+)
SRB_MALE = 1.05 / 2.05


def load(name: str) -> dict:
    return tomllib.loads((DATA / f"{name}.toml").read_text(encoding="utf-8"))


def interp(years: list[float], values: list[float], year: float) -> float:
    pts = [(y, v) for y, v in zip(years, values) if v == v]  # drop nan
    if year <= pts[0][0]:
        return pts[0][1]
    if year >= pts[-1][0]:
        return pts[-1][1]
    for (y0, v0), (y1, v1) in zip(pts, pts[1:]):
        if y0 <= year <= y1:
            return v0 + (v1 - v0) * (year - y0) / (y1 - y0)
    raise ValueError(year)


# ---------------------------------------------------------------------------
# Rates
# ---------------------------------------------------------------------------

@dataclass
class Rates:
    e0: float
    tfr: float

    def asfr(self) -> list[float]:
        shape = _fertility_shape()
        return [self.tfr * s for s in shape]


_SHAPE: list[float] | None = None


def _fertility_shape() -> list[float]:
    global _SHAPE
    if _SHAPE is None:
        f = load("rates")["fertility_shape"]
        w5 = [n * m for n, m in zip(f["natural"], f["married"])]
        total = sum(w5) * 5
        shape = [0.0] * N
        for i, w in enumerate(w5):
            for a in range(15 + 5 * i, 20 + 5 * i):
                shape[a] = w / total
        _SHAPE = shape
    return _SHAPE


def series_rates(series: str, year: float) -> Rates:
    r = load("rates")[series]
    return Rates(e0=interp(r["years"], r["e0"], year),
                 tfr=interp(r.get("tfr_years", r["years"]), r["tfr"], year))


# ---------------------------------------------------------------------------
# Populations
# ---------------------------------------------------------------------------

@dataclass
class Group:
    name: str
    F: list[float] = field(default_factory=lambda: [0.0] * N)
    M: list[float] = field(default_factory=lambda: [0.0] * N)

    def total(self) -> float:
        return sum(self.F) + sum(self.M)

    def add(self, F: list[float], M: list[float]) -> None:
        self.F = [a + b for a, b in zip(self.F, F)]
        self.M = [a + b for a, b in zip(self.M, M)]

    def scale(self, k: float) -> None:
        self.F = [x * k for x in self.F]
        self.M = [x * k for x in self.M]

    def between(self, sex: str, lo: int, hi: int) -> float:
        """People aged lo..hi inclusive."""
        arr = self.F if sex == "F" else self.M
        return sum(arr[lo:hi + 1])


def step(g: Group, rates: Rates, net_migrants: tuple[list[float], list[float]] | None = None) -> dict:
    """Advance one year. Returns {'births', 'deaths', 'excess'} for the year."""
    lt = cdwest.life_table(round(rates.e0, 2))
    asfr = rates.asfr()
    deaths = 0.0
    new = {}
    for sex in "FM":
        arr = getattr(g, sex)
        q = lt[sex]
        out = [0.0] * N
        for a in range(N):
            surv = arr[a] * (1 - q[a])
            deaths += arr[a] - surv
            out[min(a + 1, N - 1)] += surv
        new[sex] = out
    # births from the mid-year female population (average of start and survivors)
    births = sum(asfr[a] * (g.F[a] + new["F"][min(a + 1, N - 1)]) / 2 for a in range(N))
    for sex, share in (("M", SRB_MALE), ("F", 1 - SRB_MALE)):
        b = births * share
        survive_half = 1 - lt[sex][0] / 2
        new[sex][0] = b * survive_half
        deaths += b * (1 - survive_half)
    g.F, g.M = new["F"], new["M"]
    if net_migrants:
        g.add(*net_migrants)
        # a negative profile larger than a cell would drive it below zero
        g.F = [max(0.0, x) for x in g.F]
        g.M = [max(0.0, x) for x in g.M]
    return {"births": births, "deaths": deaths}


def stable_structure(rates: Rates, total: float, male_share: float | None = None, years: int = 200) -> Group:
    """Age-sex structure of a population that has lived under `rates` for a long time,
    scaled to `total`. With `male_share`, the adult sexes are rebalanced to that share
    (for male-heavy frontier populations)."""
    g = Group("stable")
    g.F = [1.0] * N
    g.M = [1.0] * N
    for _ in range(years):
        step(g, rates)
        t = g.total()
        g.scale(1 / t)
    g.scale(total)
    if male_share is not None:
        _rebalance_adults(g, male_share)
    return g


def _rebalance_adults(g: Group, male_share: float) -> None:
    total = g.total()
    kids_F, kids_M = sum(g.F[:15]), sum(g.M[:15])
    adults = total - kids_F - kids_M
    want_M = male_share * total - kids_M
    want_F = adults - want_M
    have_M, have_F = sum(g.M[15:]), sum(g.F[15:])
    if want_M > 0 and want_F > 0:
        for a in range(15, N):
            g.M[a] *= want_M / have_M
            g.F[a] *= want_F / have_F


def migrant_profile(n: float, male_share: float, child_share: float) -> tuple[list[float], list[float]]:
    """Age-sex distribution for `n` net migrants (negative n = net departures)."""
    a = load("assumptions")["migration"]
    mean, sd = a["adult_mean_age"], a["adult_sd"]
    adult_w = [math.exp(-((x - mean) / sd) ** 2 / 2) if 15 <= x <= 55 else 0.0 for x in range(N)]
    s = sum(adult_w)
    adult_w = [w / s for w in adult_w]
    kids = n * child_share
    adults = n - kids
    F = [0.0] * N
    M = [0.0] * N
    for x in range(15):
        F[x] = M[x] = kids / 30
    for x in range(N):
        M[x] += adults * male_share * adult_w[x]
        F[x] += adults * (1 - male_share) * adult_w[x]
    return F, M


def merge(*profiles: tuple[list[float], list[float]]) -> tuple[list[float], list[float]]:
    F = [sum(p[0][x] for p in profiles) for x in range(N)]
    M = [sum(p[1][x] for p in profiles) for x in range(N)]
    return F, M
