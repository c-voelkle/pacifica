import sys
import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


class AppTests(unittest.TestCase):
    def test_run_compare_export_branch_and_grid(self):
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py'), default_timeout=45).run()
        self.assertFalse(app.exception)
        next(b for b in app.button if b.label == 'Run histories').click().run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.session_state['result']['histories']), 1000)
        self.assertGreaterEqual(len(app.dataframe), 2)
        app.selectbox(key='run_credit_size_musd').set_value(400)
        next(b for b in app.button if b.label == 'Run histories').click().run()
        self.assertFalse(app.exception)
        self.assertTrue(any('Previous' in frame.value.columns for frame in app.dataframe))
        app.selectbox(key='branch_credit_size_musd').set_value(750)
        next(b for b in app.button if b.label == 'Branch this history').click().run()
        self.assertFalse(app.exception)
        self.assertIn('branch_result', app.session_state)
        next(x for x in app.selectbox if x.label == 'Worlds per setting').set_value(100)
        next(b for b in app.button if b.label == 'Run grid').click().run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.session_state['grid']), 4)
        self.assertTrue(any(x.type == 'download_button' for x in app))

    def test_discover_inspect_and_bookmark_story(self):
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py'), default_timeout=60).run()
        next(b for b in app.button if b.label == 'Discover story alternatives').click().run()
        self.assertFalse(app.exception)
        found = app.session_state['exploration']
        self.assertGreater(found['proposals'], 1)
        self.assertEqual(found['evaluations'], found['proposals'] * 25)
        next(x for x in app.selectbox if x.label == 'Find a kind of story').set_value('Broken assurance').run()
        self.assertFalse(app.exception)
        self.assertTrue(any('breach' in x.value.lower() for x in app.subheader))
        next(x for x in app.selectbox if x.label == 'Trace a metric').set_value('treasury_cash_musd').run()
        self.assertFalse(app.exception)
        self.assertTrue(any(x.label == 'Download bookmark bundle' for x in app if x.type == 'download_button'))


if __name__ == '__main__':
    unittest.main()
