import json
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from model import Engine, Scenario, bands, batch, chosen, diverse, load_scenario, observe, simulate, validate
from run import DEFAULT_SCENARIO, grid, parse_assignments, write_json


class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = load_scenario(DEFAULT_SCENARIO)
        cls.runs = batch(cls.s, 1000)

    def changed_scenario(self, edit):
        data = deepcopy(self.s.model_dump(by_alias=True))
        edit(data)
        return validate(Scenario.model_validate(data))

    def test_fixed_seed_and_batch_identity(self):
        for number in (0, 37, 999):
            h = self.runs[number]
            self.assertEqual(h, simulate(self.s, number))
            self.assertEqual(h, simulate(self.s, number, seed=h.seed))
        self.assertEqual(self.runs[37:40], batch(self.s, 3, start=37))

    def test_branch_preserves_prefix_and_draws(self):
        baseline = self.runs[37]
        branch = dict(month=self.s.phase('settlement'), lever='concessions_1928', value=[])
        changed = simulate(self.s, baseline.world, baseline.levers, baseline.seed, branch)
        self.assertEqual(baseline.draws, changed.draws)
        before = lambda h: [e for e in h.events if e['month'] < branch['month']]
        self.assertEqual(before(baseline), before(changed))
        self.assertEqual([x for x in baseline.series if x['month'] < branch['month']],
                         [x for x in changed.series if x['month'] < branch['month']])
        self.assertEqual(changed, simulate(self.s, 37, seed=baseline.seed, branch=branch))

    def test_changed_lever_keeps_matched_external_draws(self):
        changed = batch(self.s, 100, {'credit_size_musd': 400})
        self.assertTrue(any(a.measures != b.measures for a, b in zip(self.runs, changed)))
        for a, b in zip(self.runs, changed):
            self.assertEqual(a.draws, b.draws)
            self.assertEqual(a.seed, b.seed)

    def test_unobserved_event_does_not_change_decision(self):
        executive = self.s.execution.roles['executive']
        senate = self.s.execution.roles['legislature']
        engine = Engine(self.s, 0)
        engine.publish(self.s.scenario.start)
        facts = deepcopy(engine.state)
        facts.update(offer=chosen(self.s), offer_revision=1)
        engine.emit(self.s.scenario.start, 'state', None, 'offer_seen', facts)
        before = deepcopy(engine.views[senate])
        private = deepcopy(engine.beliefs['legislature'])
        concealed = dict(month=self.s.scenario.start, kind='chance', actor=None, action='concealed_test',
                         label='LAB', reason='Test only', audience=[executive],
                         facts={'concessions': self.s.levers['concessions_1928'].options,
                                'mediator_role': 'broker_settlement'})
        engine.deliver(concealed)
        self.assertEqual(before, engine.views[senate])
        self.assertEqual(observe(engine.events, senate), before)
        args = (0.0, self.s.scenario.start, chosen(self.s))
        first = engine.decide('legislature', before, deepcopy(private), *args)
        hidden = engine.decide('legislature', engine.views[senate], deepcopy(private), *args)
        self.assertEqual(first, hidden)
        # A positive control proves that the same information can influence a recipient.
        engine.deliver({**concealed, 'audience': [senate]})
        revealed = engine.decide('legislature', engine.views[senate], deepcopy(private), *args)
        self.assertNotEqual(first, revealed)

    def test_canon_sequence_and_other_paths_emerge(self):
        def has_choice(history, action, key, value):
            return any(e['action'] == action and json.loads(e['reason']).get(key) == value
                       for e in history.events if e['action'] == action)
        matches = [h for h in self.runs if h.measures['june_payments_met']
                   and h.measures['concord_status_end'] == 'consented'
                   and h.measures['monterey_case_end'] == 'mooted'
                   and h.measures['months_of_illegal_application'] > 0
                   and has_choice(h, 'rescue_loan_vote', 'vote', 'approve')
                   and has_choice(h, 'treaty_consent', 'vote', 'refuse')
                   and has_choice(h, 'settlement_role', 'choice', 'broker_settlement')]
        self.assertTrue(matches, 'The qualitative canon sequence must occur without forcing it')
        self.assertTrue(any(not h.measures['june_payments_met'] for h in self.runs))
        self.assertTrue(any(h.measures['concord_status_end'] == 'lapsed' for h in self.runs))
        # Reference text does not control transitions. Use the same explicit seed after metadata changes.
        no_reference = self.changed_scenario(lambda d: d.update(canon_reference=[]))
        h = matches[0]
        replay = simulate(no_reference, h.world, seed=h.seed)
        self.assertEqual(h.events, replay.events)

    def test_credit_conservation_including_fallbacks(self):
        runs = self.runs[:100]
        for fallback in self.s.levers['if_senate_refuses_loan'].options:
            runs += batch(self.s, 50, {'if_senate_refuses_loan': fallback, 'public_share': 0.5})
        for h in runs:
            final = h.series[-1]
            self.assertLessEqual(h.measures['credit_drawn_musd'], final['credit_committed_musd'])
            self.assertLessEqual(final['credit_committed_musd'], h.levers['credit_size_musd'])
            self.assertAlmostEqual(h.measures['public_drawn_musd'],
                                   h.measures['credit_drawn_musd'] * final['effective_public_share'])
            self.assertGreaterEqual(h.measures['public_drawn_musd'], 0)

    def test_private_only_fallback_has_no_public_exposure(self):
        h = next((h for h in batch(self.s, 300, {'if_senate_refuses_loan': 'private_only', 'public_share': 0.5})
                  if any(e['action'] == 'private_only_credit' for e in h.events)), None)
        self.assertIsNotNone(h)
        self.assertEqual(h.measures['public_drawn_musd'], 0)
        self.assertEqual(h.series[-1]['effective_public_share'], 0)
        self.assertGreater(h.measures['credit_drawn_musd'], 0)

    def test_late_offer_cannot_use_same_month_acceptances(self):
        late = batch(self.s, 50, {'offer_month': self.s.levers['offer_month'].options[-1]})
        self.assertTrue(all(h.measures['credit_drawn_musd'] == 0 for h in late))
        self.assertTrue(any(not h.measures['june_payments_met'] for h in late))

    def test_reserve_shortfall_is_not_automatically_a_missed_payment(self):
        partial = [h for h in batch(self.s, 100, {'public_share': 0.5})
                   if h.measures['june_payments_met'] and not h.series[-1]['reserve_target_met']]
        self.assertTrue(partial)
        self.assertTrue(all(h.measures['credit_drawn_musd'] >= h.series[-1]['payment_need_musd'] for h in partial))
        # Force the reserve shock on/off; do not depend on a rare sampled overlap.
        for probability in (0.0, 1.0):
            scenario = self.changed_scenario(lambda d: d['uncertainty']['second_run_if_reserves_short'].update(p=probability))
            h = simulate(scenario, levers=partial[0].levers, seed=partial[0].seed)
            self.assertTrue(h.measures['june_payments_met'])
            self.assertEqual(any(e['action'] == 'second_bank_run' for e in h.events), bool(probability))

    def test_yaml_loader_rejects_duplicate_and_nonstring_keys(self):
        directory = Path(__file__).resolve().parents[1] / 'exports'
        directory.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=directory) as folder:
            path = Path(folder) / 'invalid.yaml'
            for source in ('schema: first\nschema: second\n', '1: invalid\n', 'scenario: [unterminated'):
                path.write_text(source, encoding='utf-8')
                with self.assertRaises(ValueError):
                    load_scenario(path)

    def test_mapping_order_does_not_change_hash_or_draws(self):
        reordered = self.changed_scenario(lambda d: d.update(uncertainty=dict(reversed(list(d['uncertainty'].items())))))
        self.assertEqual(self.s.digest, reordered.digest)
        self.assertEqual(self.runs[37], simulate(reordered, 37))

    def test_revised_offer_requires_fresh_responses(self):
        branch = dict(month='1927-04', lever='credit_size_musd', value=750)
        h = simulate(self.s, 37, branch=branch)
        april = next(row['facts'] for row in reversed(h.events)
                     if row['month'] == branch['month'] and row['action'] == 'public_update')
        self.assertEqual(april['offer']['credit_size_musd'], 750)
        self.assertIsNone(april['government_reply'])
        self.assertIsNone(april['loan_vote'])
        self.assertFalse(april['ratified'])
        self.assertTrue(any(e['action'] == 'reply_to_superseded_offer' for e in h.events))
        self.assertTrue(any(e['month'] == '1927-05' and e['action'] == 'response_to_offer' for e in h.events))

    def test_competing_offer_must_be_delivered_to_government(self):
        engine = Engine(self.s, 0)
        engine.state.update(offer=chosen(self.s), offer_revision=1)
        engine.publish(self.s.scenario.start)
        role, actor = 'government', self.s.execution.roles['government']
        def decide():
            return engine.decide(role, engine.views[actor], deepcopy(engine.beliefs[role]),
                                 0.0, self.s.scenario.start, chosen(self.s))
        baseline = decide()
        engine.draws['uncertainty']['better_offer_appears'] = not engine.draws['uncertainty']['better_offer_appears']
        self.assertEqual(baseline, decide())
        engine.emit(self.s.scenario.start, 'chance', None, 'competing_offer_available',
                    {'better_offer_available': True}, audience=[actor])
        self.assertNotEqual(baseline, decide())

    def test_missing_unknown_and_nonfinite_inputs_rejected(self):
        edits = [lambda d: d.update(typo=True),
                 lambda d: d['actors'][d['execution']['roles']['government']].update(typo=True),
                 lambda d: d['execution']['coefficients'].update(noies={'value': .1, 'label': 'LAB'}),
                 lambda d: d['execution']['coefficients'].pop('decision_noise'),
                 lambda d: d['world'][d['execution']['worlds']['partner']].pop('new_capital_musd'),
                 lambda d: d['world'][d['execution']['worlds']['partner']]['new_capital_musd'].update(value=None),
                 lambda d: d['uncertainty']['senate_mood'].update(low=float('nan')),
                 lambda d: d['actors'][d['execution']['roles']['legislature']]['decisions'].update(vtoe=['approve'])]
        for edit in edits:
            with self.subTest(edit=edit), self.assertRaises(ValueError):
                self.changed_scenario(edit)

    def test_actor_ids_are_data_not_code(self):
        data = deepcopy(self.s.model_dump(by_alias=True))
        aliases = {key: f'actor_{i}' for i, key in enumerate(data['actors'])}
        data['actors'] = {aliases[k]: v for k, v in data['actors'].items()}
        data['execution']['roles'] = {k: aliases[v] for k, v in data['execution']['roles'].items()}
        renamed = validate(Scenario.model_validate(data))
        original = self.runs[0]
        h = simulate(renamed, seed=original.seed)
        self.assertEqual(original.measures, h.measures)
        self.assertTrue(all(e['actor'] is None or e['actor'] in aliases.values() for e in h.events))

    def test_grid_matches_direct_runs_and_keeps_failures(self):
        rows = grid(self.s, {'credit_size_musd': [400, 600]}, 20)
        for row in rows:
            direct = batch(self.s, 20, row['levers'])
            self.assertEqual(row['rescue_rate'], sum(h.measures['june_payments_met'] for h in direct) / 20)
            self.assertEqual(sum(row['outcomes']['japan_path'].values()), 20)

    def test_history_selection_and_bands(self):
        selected = diverse(self.runs)
        self.assertEqual(len(selected), 5)
        self.assertEqual(selected, diverse(self.runs))
        self.assertEqual(len({h.world for h in selected}), 5)
        rows = bands(self.runs[:20])
        self.assertEqual(len(rows), 6 * len(self.runs[0].series))
        self.assertTrue(all(r['low'] <= r['median'] <= r['high'] for r in rows))

    def test_export_round_trip_and_canon_protection(self):
        h = self.runs[0]
        payload = json.loads(json.dumps(h.export(self.s), allow_nan=False))
        restored = validate(Scenario.model_validate(payload['scenario']))
        replay = simulate(restored, payload['world'], payload['levers'], payload['seed'], payload['branch'])
        self.assertEqual(replay.events, payload['events'])
        self.assertEqual(replay.measures, payload['measures'])
        exports = Path(__file__).resolve().parents[1] / 'exports'
        exports.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=exports) as folder:
            self.assertTrue(Path(folder).resolve().is_relative_to(exports.resolve()))
            output = Path(folder) / 'history.json'
            write_json(payload, output)
            with self.assertRaises(FileExistsError):
                write_json(payload, output)
        with self.assertRaises(ValueError):
            write_json(payload, Path(__file__).resolve().parents[2] / 'book-agent' / 'do-not-create.json')

    def test_protected_facts_are_not_invented(self):
        for h in self.runs[:50]:
            generated = json.dumps(h.events).lower()
            for word in ('altai', 'murderer', 'donner', 'president', 'common finance minister'):
                self.assertNotIn(word, generated)

    def test_invalid_branch_and_cli_inputs(self):
        with self.assertRaises(ValueError):
            chosen(self.s, {'public_share': '0.5'})
        with self.assertRaises(ValueError):
            batch(self.s, 0)
        with self.assertRaises(ValueError):
            parse_assignments(['public_share=0.5', 'public_share=0.25'])
        with self.assertRaises(ValueError):
            simulate(self.s, branch=dict(month=self.s.scenario.end, lever='credit_size_musd', value=400))
        with self.assertRaises(ValueError):
            simulate(self.s, branch=dict(month=self.s.scenario.start, lever='credit_size_musd', value=600))


if __name__ == '__main__':
    unittest.main()
