"""Regression tests for lint_canon.py. Run:
python3 -m unittest discover -s book-agent/revision/tests -v
"""
import sys
import tempfile
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
import lint_canon  # noqa: E402


def lint_text(text: str, facts: Path = lint_canon.FACTS):
    people, events, forbidden = lint_canon.load_facts(facts)
    linter = lint_canon.Linter(people, events, forbidden, lint_canon.registry_ids(),
                               lint_canon.registry_names())
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "draft.md"
        path.write_text(text, encoding="utf-8")
        linter.lint(path)
    return [f.check for f in linter.findings]


class CurrentCanon(unittest.TestCase):
    def test_canon_is_clean(self):
        self.assertEqual(lint_canon.main([]), 0)


class Drafts(unittest.TestCase):
    def test_wrong_age(self):
        self.assertIn("age", lint_text("Noe acts. In January 1888 the twenty-four-year-old physician petitions."))

    def test_right_age(self):
        self.assertEqual(lint_text("Noe acts. In January 1888 the twenty-seven-year-old physician petitions."), [])

    def test_wrong_death_year_and_season(self):
        self.assertIn("death", lint_text("Noe dies in the spring of 1889 during a typhoid outbreak she is fighting."))
        self.assertIn("death", lint_text("Noe dies in the spring of 1888 while fighting an outbreak."))

    def test_pronoun_from_previous_paragraph(self):
        text = "Noe retains her health work.\n\nShe dies in the spring of 1889 during the outbreak."
        self.assertIn("death", lint_text(text))

    def test_possessive_is_not_the_subject(self):
        self.assertEqual(lint_text("Silas is Elias's eldest son, born in 1851 to Abigail Merritt."), [])

    def test_other_person_blocks_pronoun(self):
        self.assertEqual(lint_text("Elias builds the fleet. Kiyoshi commands it. He dies in Siberia in 1920."), [])

    def test_change_log_sentence_is_exempt(self):
        self.assertEqual(lint_text("The correction moves Noe's death from autumn 1888 to spring 1889."), [])

    def test_event_year(self):
        self.assertIn("event", lint_text("Hollerith's punched cards begin to tabulate the recovered registers in 1890."))

    def test_unknown_id(self):
        self.assertIn("id", lint_text("See CT-NOBODY-REAL for details."))

    def test_forbidden_culprit_hint(self):
        self.assertIn("forbidden", lint_text("The physician signs the certificate on instructions from the palace."))

    def test_date_change_lists_every_old_site(self):
        text = (BASE / "canon_facts.toml").read_text(encoding="utf-8")
        text = text.replace("died = 1888", "died = 1889").replace('died_season = "autumn"', 'died_season = "spring"')
        with tempfile.TemporaryDirectory() as d:
            facts = Path(d) / "facts.toml"
            facts.write_text(text, encoding="utf-8")
            people, events, forbidden = lint_canon.load_facts(facts)
            linter = lint_canon.Linter(people, events, forbidden, lint_canon.registry_ids(),
                                       lint_canon.registry_names())
            for path in lint_canon.DEFAULT_FILES:
                linter.lint(path)
        sites = {f.where for f in linter.findings}
        root = BASE.parent.parent
        expected = [  # (file, text of a passage that states Noe's 1888 death)
            ("AGENTS.md", "before her ambiguous death in 1888"),
            ("book-agent/revision/master_storyline.md", "contested typhoid outbreak of 1888"),
            ("book-agent/revision/master_storyline.md", "She dies in the autumn of 1888"),
            ("book-agent/revision/master_storyline.md", "Her 1888 death has an official typhoid account"),
            ("book-agent/revision/character_bible.md", "**Died:** autumn 1888"),
            ("book-agent/revision/character_bible.md", "She dies during an autumn 1888 typhoid outbreak"),
        ]
        for rel, text in expected:
            lines = (root / rel).read_text(encoding="utf-8").splitlines()
            line = next(i for i, l in enumerate(lines, 1) if text in l)
            self.assertTrue(any(s.endswith(f"{Path(rel).name}:{line}") for s in sites), f"{rel}:{line}")

if __name__ == "__main__":
    unittest.main()
