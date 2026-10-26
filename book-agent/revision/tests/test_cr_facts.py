"""Tests for cr_facts.py, run on temporary copies of the register and facts file."""
import json
import shutil
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
import cr_facts  # noqa: E402

NOE = {"person": "CT-JULIAN-MOTHER", "set": {"died": 1889, "died_season": "spring"},
       "was": {"died": 1888, "died_season": "autumn"}}


class Sandbox(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.facts, self.register = d / "canon_facts.toml", d / "change_requests.json"
        shutil.copy(cr_facts.FACTS, self.facts)
        shutil.copy(cr_facts.REGISTER, self.register)
        self._orig = cr_facts.FACTS, cr_facts.REGISTER
        cr_facts.FACTS, cr_facts.REGISTER = self.facts, self.register

    def tearDown(self):
        cr_facts.FACTS, cr_facts.REGISTER = self._orig
        self.tmp.cleanup()

    def add_cr(self, status, facts):
        reg = json.loads(self.register.read_text(encoding="utf-8"))
        reg["requests"].append({"id": "CR-099", "status": status, "title": "test", "requirements": [],
                                "open": [], "facts": facts})
        self.register.write_text(json.dumps(reg, ensure_ascii=False), encoding="utf-8")

    def person(self, pid):
        data = tomllib.loads(self.facts.read_text(encoding="utf-8"))
        return next(p for p in data["person"] if p["id"] == pid)

    def test_apply_updates_value_source_and_keeps_toml_valid(self):
        self.add_cr("approved_direct_author_correction_integrated", [NOE])
        self.assertEqual(cr_facts.main(["apply", "CR-099"]), 0)
        noe = self.person("CT-JULIAN-MOTHER")
        self.assertEqual((noe["died"], noe["died_season"]), (1889, "spring"))
        self.assertIn("CR-099", noe["source"])
        self.assertIn("# Pacifica canon facts", self.facts.read_text(encoding="utf-8"))  # comments kept
        self.assertEqual(cr_facts.main(["check"]), 0)

    def test_unapproved_cr_is_refused(self):
        self.add_cr("proposed", [NOE])
        self.assertEqual(cr_facts.main(["apply", "CR-099"]), 2)
        self.assertEqual(self.person("CT-JULIAN-MOTHER")["died"], 1888)

    def test_stale_was_is_refused(self):
        stale = dict(NOE, was={"died": 1887})
        self.add_cr("approved_direction", [stale])
        self.assertEqual(cr_facts.main(["apply", "CR-099"]), 2)
        self.assertEqual(self.person("CT-JULIAN-MOTHER")["died"], 1888)

    def test_check_catches_register_facts_drift(self):
        self.add_cr("approved_direction", [NOE])
        self.assertEqual(cr_facts.main(["check"]), 1)

    def test_add_person_event_and_forbidden(self):
        self.add_cr("approved_direction", [
            {"add_person": {"id": "CT-KEAWE-TEST", "aliases": ["Test Person"], "born": 1890}},
            {"add_event": {"id": "test-event", "year": 1900,
                           "patterns": ["test treaty of (?P<year>1[89]\\d\\d)"]}},
            {"add_forbidden": {"pattern": "Test Person is the murderer", "message": "test"}},
        ])
        self.assertEqual(cr_facts.main(["apply", "CR-099"]), 0)
        data = tomllib.loads(self.facts.read_text(encoding="utf-8"))
        self.assertTrue(any(p["id"] == "CT-KEAWE-TEST" for p in data["person"]))
        ev = next(e for e in data["event"] if e["id"] == "test-event")
        self.assertEqual(ev["patterns"], ["test treaty of (?P<year>1[89]\\d\\d)"])
        self.assertEqual(cr_facts.main(["check"]), 0)

    def test_preview_does_not_write(self):
        before = self.facts.read_text(encoding="utf-8")
        draft = Path(self.tmp.name) / "CR-099-draft.md"
        draft.write_text("# Draft\n\n## Fact changes\n\n```json\n" + json.dumps([NOE]) + "\n```\n",
                         encoding="utf-8")
        self.assertEqual(cr_facts.main(["preview", str(draft)]), 0)
        self.assertEqual(self.facts.read_text(encoding="utf-8"), before)

    def test_draft_without_section_is_an_error(self):
        draft = Path(self.tmp.name) / "d.md"
        draft.write_text("# Draft\n\nNo facts here.\n", encoding="utf-8")
        self.assertEqual(cr_facts.main(["preview", str(draft)]), 2)


if __name__ == "__main__":
    unittest.main()
