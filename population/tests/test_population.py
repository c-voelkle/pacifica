"""Population model tests. Run: python3 -m unittest discover -s population/tests -v"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cdwest  # noqa: E402
import cohort  # noqa: E402
import historical  # noqa: E402
import canon  # noqa: E402


class LifeTables(unittest.TestCase):
    def test_west_levels_match_published_female_e0(self):
        for level in (1, 5, 9, 13, 17, 21, 25):
            e10 = cdwest.COEF["F"]["eten"][level - 1]
            e0 = cdwest._e0("F", cdwest._lx_single("F", e10))
            self.assertAlmostEqual(e0, 17.5 + 2.5 * level, delta=0.2, msg=f"level {level}")

    def test_interpolated_e0_is_hit(self):
        for e0 in (25.0, 39.5, 51.8, 60.9):
            self.assertAlmostEqual(cdwest.life_table(e0)["e0"], e0, places=1)


class Engine(unittest.TestCase):
    def test_migrant_profile_sums_to_n(self):
        F, M = cohort.migrant_profile(1000, 0.7, 0.2)
        self.assertAlmostEqual(sum(F) + sum(M), 1000, places=6)
        self.assertAlmostEqual(sum(M[15:]) / (sum(F[15:]) + sum(M[15:])), 0.7, places=6)

    def test_stable_population_growth_is_plausible(self):
        r = cohort.Rates(39.5, 5.42)  # US white 1850 (Haines)
        g = cohort.stable_structure(r, 100000)
        res = cohort.step(g, r)
        self.assertTrue(35 < res["births"] / 100 < 45)           # crude birth rate, observed 43.3
        self.assertTrue(0.5 < (g.total() / 100000 - 1) * 100 < 2.5)  # growth % a year


class History(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cal = historical.calibrate_native_hawaiian()

    def test_native_hawaiian_decline_within_six_percent(self):
        ch = self.cal["chosen"]
        for y, obs in self.cal["obs"].items():
            self.assertLess(abs(ch["fit"][y] / obs - 1), 0.06, y)

    def test_calibration_passes_independent_age_test(self):
        self.assertTrue(self.cal["any_pass"])

    def test_chinese_natural_increase_negative(self):
        rows = [r for r in historical.california() if r["group"] == "chinese"]
        self.assertTrue(all(r["natural_increase_total"] < 0 for r in rows))


class Canon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.meta = canon.run("our_timeline")

    def test_gap_decomposition_adds_up(self):
        for r in self.rows:
            resid = r["sheet_total"] - r["model_total"] - sum(r["gap_by_group"].values())
            self.assertLess(abs(resid), 5, r["year"])

    def test_workbook_is_not_modified(self):
        import hashlib
        before = hashlib.sha256(canon.WORKBOOK.read_bytes()).hexdigest()
        canon.read_sheet()
        self.assertEqual(hashlib.sha256(canon.WORKBOOK.read_bytes()).hexdigest(), before)


if __name__ == "__main__":
    unittest.main()
