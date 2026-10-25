"""A small promise / verification / disclosure / cooperation mechanism, all LAB."""
from copy import deepcopy
from collections import defaultdict, deque
from ontology import Belief, Commitment, DecisionRecord, Plan


class Relationships:
    def __init__(self, engine):
        self.e = engine
        self.commitment = None
        self.decisions, self.beliefs = [], []
        self.receipts = {actor: {} for actor in engine.s.actors}
        self.last_review = None
        self.plans = []
        self.pending = defaultdict(deque)
        self.executing = None

    def begin(self, month, role, action):
        queue = self.pending[(month, role, action)]
        self.executing = queue.popleft() if queue else None

    def envelope(self, record_id):
        return dict(id=record_id, revision_id=self.e.hash, provenance_refs=['scenario:/drama', 'mechanism:relationships/0.2'])

    def delivered(self, event):
        for actor, receipts in self.receipts.items():
            if event['audience'] == 'public' or actor in event['audience']:
                for key in event['facts']:
                    receipts[key] = f"observation:{actor}:{event['id']}"

    def observe(self, role, info, private, month):
        actor, rules = self.e.s.execution.roles[role], self.e.s.drama.rules
        if role == 'mediator' and info.get('assurance_known') and info.get('settlement_presented'):
            value = 'honoured' if set(info['assurance_terms']) <= set(info['concessions']) else 'breached'
            if private.get('assurance_assessment') != value:
                private['assurance_assessment'] = value
                self.believe(actor, 'settlement_assurance_fulfilment', value, month,
                             ['assurance_known', 'assurance_terms', 'concessions', 'settlement_presented'])
        if role in rules.belief_thresholds and info.get('assurance_report') and not private.get('assurance_report_seen'):
            accepted = info['report_credibility'] >= rules.belief_thresholds[role].value
            private['assurance_report_seen'] = True
            private['assurance_report_accepted'] = accepted
            if accepted:
                private['trust'] = max(0.0, private['trust'] - rules.breach_penalty.value)
            self.believe(actor, 'reported_assurance_breach', 'accepted' if accepted else 'doubted', month,
                         ['assurance_report', 'report_credibility'])

    def believe(self, actor, proposition, value, month, keys):
        refs = sorted({self.receipts[actor][key] for key in keys if key in self.receipts[actor]})
        record = Belief(**self.envelope(f'belief-{len(self.beliefs)}'), actor_id=actor,
                        proposition=proposition, value=value, observation_refs=refs,
                        update_rule='delivered_terms_or_recipient_credibility_threshold', at=month)
        self.beliefs.append(record.model_dump())

    def actions(self, role, info, private, noise, month, controls):
        s, rules = self.e.s, self.e.s.drama.rules
        if role == 'executive' and month >= controls['offer_month'] and not info.get('assurance_known'):
            if controls['assurance_strategy'] != 'none':
                return [('make_assurance', dict(strategy=controls['assurance_strategy'], terms=s.drama.assurance_terms))]
        if role == 'mediator' and info.get('assurance_known') and info.get('settlement_presented'):
            revision = (info['concession_revision'], private.get('assurance_assessment'))
            if revision != self.last_review:
                self.last_review = revision
                score = self.e.draws['uncertainty']['victoria_brokering_skill'] + noise
                choice = 'support' if private['assurance_assessment'] == 'honoured' else (
                    'disclose_breach' if score >= rules.disclosure_threshold.value else 'withhold_cooperation')
                return [('review_assurance', dict(choice=choice, assessment=private['assurance_assessment'],
                         utility=score, disclosure_threshold=rules.disclosure_threshold.value))]
        return []

    def concessions(self, info, controls):
        result = list(controls['concessions_1928'])
        if info.get('assurance_known') and controls['commitment_priority'] == 'honour_assurance':
            result = list(dict.fromkeys(result + info['assurance_terms']))
        return result

    def audience(self, action, data, role):
        if action == 'make_assurance' and data['strategy'] == 'private':
            return [self.e.s.execution.roles[k] for k in ('executive', 'mediator')]
        if action == 'review_assurance' and data['choice'] != 'disclose_breach':
            return [self.e.s.execution.roles[k] for k in ('executive', 'mediator')]
        return 'public'

    def resolve(self, month, role, action, data):
        e, s = self.e, self.e.s
        if action == 'make_assurance':
            if self.commitment:
                return True
            self.commitment = Commitment(**self.envelope('settlement-assurance'),
                promisor_id=s.execution.roles['executive'], promisee_id=s.execution.roles['mediator'],
                terms=list(data['terms']), made_at=month, visibility=data['strategy'], status='pending')
            self.plans.append(Plan(**self.envelope('plan-settlement-assurance'),
                owner_id=s.execution.roles['executive'], goal_refs=[g.id for g in s.drama.goals
                    if g.owner_role == 'executive' and g.capacity == 'personal'],
                status='active', support_refs=['settlement-assurance']))
            e.emit(month, 'consequence', s.execution.roles[role], 'assurance_delivered',
                   {'assurance_known': True, 'assurance_terms': list(data['terms'])},
                   reason='LAB nonbinding political assurance; distinct from a legal obligation.',
                   audience=self.audience(action, data, role))
            return True
        if action == 'offer_concessions' and self.commitment:
            self.commitment.status = 'honoured' if set(self.commitment.terms) <= set(data['concessions']) else 'breached'
            self.plans[0].status = 'achieved' if self.commitment.status == 'honoured' else 'frustrated'
        if action == 'review_assurance':
            if data['choice'] == 'disclose_breach':
                e.emit(month, 'consequence', s.execution.roles[role], 'assurance_breach_disclosed',
                       {'assurance_report': 'breached', 'report_credibility': s.drama.rules.report_credibility.value},
                       reason='A recipient reports an observed breach; audiences apply their own credibility rules.')
            return True
        return False

    def record(self, role, action, data, info, private, month):
        s, actor = self.e.s, self.e.s.execution.roles[role]
        goals = [g.id for g in s.drama.goals if g.owner_role == role]
        alternatives = s.actor(role).decisions.get(action, [])
        if action == 'offer_concessions':
            alternatives = ['offer requested terms', 'include promised oversight terms']
            why = f"Priority {data['priority']}; requested {data['requested']}; actual offer {data['concessions']}."
        elif action == 'make_assurance':
            alternatives, why = ['none', 'private', 'public'], 'The selected policy offers an assurance; counterpart cooperation is not supplied.'
        elif action == 'review_assurance':
            alternatives = ['support', 'withhold_cooperation', 'disclose_breach']
            why = f"Observed assessment {data['assessment']}; disclosure score {data['utility']:.3f} versus {data['disclosure_threshold']:.3f}."
        else:
            why = 'Executed role rule using the recorded delivered facts, private inputs and selected policy.'
            if 'utility' in data:
                why += f" Utility {data['utility']:.3f}; applicable thresholds are retained in the scenario."
        if not alternatives:
            alternatives = ['act under selected policy', 'defer or choose a different policy']
        record = DecisionRecord(**self.envelope(f'decision-{len(self.decisions)}'), actor_id=actor,
            context_ref=f'context:decision-{len(self.decisions)}',
            acting_for_id=f'{actor}:office' if role == 'executive' else actor, at=month, action=action, selected=deepcopy(data),
            considered_alternatives=list(alternatives),
            belief_refs=[b['id'] for b in self.beliefs if b['actor_id'] == actor],
            observation_refs=sorted(set(self.receipts[actor].values())), information_used=deepcopy(info),
            private_inputs=deepcopy(private), goal_refs=goals,
            commitment_refs=['settlement-assurance'] if info.get('assurance_known') else [],
            reasons=[why], selection_origin='actor_procedure', random_address=f'monthly/{month}/{role}')
        self.decisions.append(record.model_dump())
        self.pending[(month, role, action)].append(record.id)

    def export(self):
        return dict(commitments=[self.commitment.model_dump()] if self.commitment else [],
                    beliefs=self.beliefs, decisions=self.decisions, plans=[p.model_dump() for p in self.plans])
