import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from model import Engine, Scenario, batch, chosen, load_scenario, simulate, validate
from ontology import entity_catalog
from metrics import samples, resolve_input, comparison
from stories import bookmark, candidate, explore, replay_bookmark, select
from run import DEFAULT_SCENARIO


class DramaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = load_scenario(DEFAULT_SCENARIO)
        cls.keep = dict(assurance_strategy='private', commitment_priority='honour_assurance', concessions_1928=[])
        cls.break_word = dict(cls.keep, commitment_priority='preserve_discretion')
        cls.kept = batch(cls.s, 30, cls.keep)
        cls.broken = batch(cls.s, 30, cls.break_word)

    def test_same_finances_different_commitments_and_cooperation(self):
        different = False
        for a, b in zip(self.kept, self.broken):
            self.assertEqual(a.draws, b.draws)
            self.assertEqual(a.measures['credit_drawn_musd'], b.measures['credit_drawn_musd'])
            self.assertEqual(a.semantics['commitments'][0]['status'], 'honoured')
            self.assertEqual(b.semantics['commitments'][0]['status'], 'breached')
            self.assertNotEqual(candidate(self.s, a).causal_signature, candidate(self.s, b).causal_signature)
            different |= a.measures['concord_status_end'] != b.measures['concord_status_end']
        self.assertTrue(different)

    def test_priority_changes_executed_terms_and_records_the_cost(self):
        a, b = self.kept[0], self.broken[0]
        first = lambda h: next(d for d in h.semantics['decisions'] if d['action'] == 'offer_concessions')
        self.assertEqual(set(first(a)['selected']['concessions']), set(self.s.drama.assurance_terms))
        self.assertEqual(first(b)['selected']['concessions'], [])
        self.assertEqual(first(a)['selected']['requested'], [])
        self.assertTrue(first(a)['goal_refs'])
        self.assertIn('honour_assurance', first(a)['reasons'][0])
        self.assertEqual(a.semantics['plans'][0]['status'], 'achieved')
        self.assertEqual(b.semantics['plans'][0]['status'], 'frustrated')

    def test_private_assurance_is_not_public_knowledge(self):
        h = self.kept[0]
        actor = self.s.execution.roles['government']
        government = [d for d in h.semantics['decisions'] if d['actor_id'] == actor]
        self.assertTrue(government)
        self.assertTrue(all('assurance_known' not in d['information_used'] for d in government))
        delivery = next(e for e in h.events if e['action'] == 'assurance_delivered')
        self.assertNotEqual(delivery['audience'], 'public')
        self.assertNotIn(actor, delivery['audience'])

    def test_truthful_disclosure_can_be_doubted_by_another_recipient(self):
        h = next(h for h in self.broken if any(e['action'] == 'assurance_breach_disclosed' for e in h.events))
        disclosed = next(e for e in h.events if e['action'] == 'assurance_breach_disclosed')
        beliefs = [b for b in h.semantics['beliefs'] if b['proposition'] == 'reported_assurance_breach']
        by_actor = {b['actor_id']: b for b in beliefs}
        self.assertEqual(by_actor[self.s.execution.roles['legislature']]['value'], 'accepted')
        self.assertEqual(by_actor[self.s.execution.roles['government']]['value'], 'doubted')
        self.assertTrue(all(b['at'] > disclosed['month'] for b in beliefs))
        breached = next(r for r in h.series if r['assurance_status'] == 'breached')
        learned = next(r for r in h.series if r['mediator_assessment'] == 'breached')
        self.assertLess(breached['month'], learned['month'])

    def test_concealed_actual_breach_cannot_change_an_uninformed_decision(self):
        e = Engine(self.s, 0)
        e.publish(self.s.scenario.start)
        role = 'mediator'
        info = deepcopy(e.views[self.s.execution.roles[role]])
        controls = chosen(self.s)
        a = e.decide(role, info, deepcopy(e.beliefs[role]), 0.0, self.s.phase('settlement'), controls)
        # An adjudicator-only change, with identical actor information.
        e.relationships.commitment = self.broken[0].semantics['commitments'][0]
        b = e.decide(role, info, deepcopy(e.beliefs[role]), 0.0, self.s.phase('settlement'), controls)
        self.assertEqual(a, b)

    def test_political_breach_does_not_itself_create_illegal_authority(self):
        h = simulate(self.s, levers=dict(self.break_word, consent_path='wait_for_senate'))
        self.assertEqual(h.semantics['commitments'][0]['status'], 'breached')
        self.assertFalse(h.semantics['commitments'][0]['legally_binding'])
        self.assertEqual(h.measures['months_of_illegal_application'], 0)

    def test_equal_concession_counts_have_different_effects(self):
        weak = ['five_year_first_term', 'quota_review_at_renewal']
        oversight = self.s.drama.assurance_terms
        a = batch(self.s, 20, {'concessions_1928': weak})
        b = batch(self.s, 20, {'concessions_1928': oversight})
        self.assertTrue(any(x.measures != y.measures for x, y in zip(a, b)))
        self.assertTrue(all(x.draws == y.draws for x, y in zip(a, b)))

    def test_ontology_links_observations_attempts_and_contexts(self):
        payload = self.kept[0].export(self.s)
        bundle = payload['ontology']
        observation_ids = {o['id'] for o in bundle['observations']}
        goals = {g['id'] for g in bundle['goals']}
        belief_ids = {b['id'] for b in bundle['beliefs']}
        context_ids = {c['id'] for c in bundle['contexts']}
        entities = {e['id'] for e in payload['entities']}
        for d in bundle['decisions']:
            self.assertTrue(set(d['observation_refs']) <= observation_ids)
            self.assertTrue(set(d['goal_refs']) <= goals)
            self.assertTrue(set(d['belief_refs']) <= belief_ids)
            self.assertIn(d['context_ref'], context_ids)
            self.assertIn(d['acting_for_id'], entities)
        self.assertEqual(len(bundle['contexts']), len(bundle['attempts']))
        self.assertEqual(len(bundle['attempts']), len(bundle['adjudications']))
        persons = [e for e in entity_catalog(self.s) if e['member_of']]
        self.assertTrue(persons)
        self.assertTrue(all(e['acting_role'] is None for e in persons))

    def test_metrics_keep_unknowns_units_inputs_and_support(self):
        h = self.kept[0]
        measured = {m.metric_id: m for m in samples(self.s, h)}
        cash = measured['treasury_cash_musd']
        self.assertIsNone(cash.value)
        self.assertTrue(cash.missing_reason)
        self.assertEqual(cash.coverage, 'unmodelled')
        self.assertEqual(measured['public_drawn_musd'].units, 'period_USD_million')
        event_ids = {e['id'] for e in h.events}
        for m in measured.values():
            self.assertEqual(m.scenario_hash, h.scenario_hash)
            self.assertTrue(set(m.event_refs) <= event_ids)
            for ref in m.input_refs:
                self.assertIsNotNone(resolve_input(self.s, ref))
        self.assertEqual(measured['payment_gap_musd'].value,
                         max(0, h.series[-1]['payment_need_musd'] - h.measures['credit_drawn_musd']))
        self.assertTrue(comparison(self.s, h, self.broken[0]))

    def test_open_exploration_keeps_financially_similar_distinct_plots(self):
        found = explore(self.s, 3)
        self.assertEqual(found['evaluations'], found['proposals'] * found['root_worlds'])
        representatives = select(self.s, found['histories'], limit=100)
        self.assertTrue(any(c['status'] == 'breached' for h, _ in representatives for c in h.semantics['commitments']))
        self.assertTrue(any(c['status'] == 'honoured' for h, _ in representatives for c in h.semantics['commitments']))
        self.assertEqual(select(self.s, found['histories'], condition='Broken assurance'),
                         select(self.s, found['histories'], condition='Broken assurance'))

    def test_bookmark_replays_and_rejects_tampering(self):
        record = bookmark(self.s, self.kept[0], 'A costly assurance creates the settlement.')
        restored_s, h, saved = replay_bookmark(json.loads(record.model_dump_json()))
        self.assertEqual(h, self.kept[0])
        forged = record.model_dump()
        forged['candidate']['title'] = 'Invented story'
        with self.assertRaises(ValueError):
            replay_bookmark(forged)
        forged = record.model_dump()
        forged['history']['ontology']['observations'][0]['payload'] = {'invented': True}
        with self.assertRaises(ValueError):
            replay_bookmark(forged)

    def test_priority_change_can_have_no_material_effect(self):
        a = simulate(self.s, levers={'assurance_strategy': 'private', 'commitment_priority': 'honour_assurance'})
        b = simulate(self.s, levers={'assurance_strategy': 'private', 'commitment_priority': 'preserve_discretion'})
        self.assertEqual(a.measures, b.measures)
        self.assertEqual(a.semantics['commitments'][0]['status'], 'honoured')
        self.assertEqual(b.semantics['commitments'][0]['status'], 'honoured')

    def test_relationship_branch_preserves_prefix_and_is_conditional(self):
        original = self.kept[0]
        branch = dict(month=self.s.phase('settlement'), lever='commitment_priority', value='preserve_discretion')
        h = simulate(self.s, original.world, original.levers, original.seed, branch)
        self.assertEqual(original.draws, h.draws)
        prefix = lambda h: [e for e in h.events if e['month'] < branch['month']]
        self.assertEqual(prefix(original), prefix(h))
        self.assertEqual(candidate(self.s, h).claim_basis, 'mechanical_consequence')
        self.assertEqual(h.semantics['commitments'][0]['status'], 'breached')

    def test_schema_rejects_incomplete_relationship_contracts(self):
        for modify in (lambda d: d['drama']['rules']['belief_thresholds'].pop('government'),
                       lambda d: d['drama']['concessions'].pop('polytechnic_audit'),
                       lambda d: d['metric_catalog'].pop()):
            data = self.s.model_dump(by_alias=True)
            modify(data)
            with self.assertRaises(ValueError):
                validate(Scenario.model_validate(data))


if __name__ == '__main__':
    unittest.main()
