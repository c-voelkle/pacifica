"""Small, local scenario sketch. All generated histories and utilities are LAB."""
from __future__ import annotations

import hashlib
import json
import math
import random
from collections import Counter
from copy import deepcopy
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator
from ontology import Drama, MetricDefinition, ENGINE_VERSION, validate_drama
from relationships import Relationships

Label = Literal['APPROVED', 'PROPOSED', 'OPEN', 'MODEL', 'LAB', 'CHECK']
ROLES = ('executive', 'legislature', 'mediator', 'government', 'military', 'subscribers', 'lenders')


class Record(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True, allow_inf_nan=False)


class Tagged(Record):
    value: float | int | str | None = None
    weight: float | None = None
    weight_per_concession: float | None = None
    label: Label

    @model_validator(mode='after')
    def one_value(self):
        if sum(v is not None for v in (self.value, self.weight, self.weight_per_concession)) != 1:
            raise ValueError('A labeled input needs exactly one non-null value/weight')
        return self

    def number(self) -> float:
        for v in (self.value, self.weight, self.weight_per_concession):
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                return float(v)
        raise ValueError('Expected a numeric labeled input')


class Person(Record):
    registry_id: str
    role: str


class Faction(Record):
    leader: str
    registry_id: str | None
    cohesion: Tagged


class Actor(Record):
    name: str
    control: Literal['controlled', 'independent']
    registry_id: str | None = None
    catalog_role: str | None = None
    note: str | None = None
    stance: str | None = None
    rule: str | None = None
    factions: dict[str, Faction] = Field(default_factory=dict)
    persons: dict[str, Person] = Field(default_factory=dict)
    decisions: dict[str, list[str]] = Field(default_factory=dict)
    reasons_against: dict[str, Tagged] = Field(default_factory=dict)
    reasons_for: dict[str, Tagged] = Field(default_factory=dict)
    reasons_for_accepting: dict[str, Tagged] = Field(default_factory=dict)
    params: dict[str, Tagged] = Field(default_factory=dict)
    holdings_musd: dict[str, Tagged] = Field(default_factory=dict)


class Source(Record):
    repository: str
    commit: str
    passages: list[str]


class Window(Record):
    id: str
    title: str
    question: str
    start: str
    end: str
    step: Literal['month']
    sources: Source


class Lever(Record):
    options: list[str | int | float | bool]
    canon: str | int | float | bool | list[str] | None = None
    canon_window: str | None = None
    multi_select: bool = False
    label: Label


class Distribution(Record):
    dist: Literal['uniform', 'bernoulli']
    low: float | None = None
    high: float | None = None
    p: float | None = None
    label: Literal['LAB']

    @model_validator(mode='after')
    def bounds(self):
        if self.dist == 'uniform':
            if self.low is None or self.high is None or not 0 <= self.low <= self.high <= 1 or self.p is not None:
                raise ValueError('Uniform uncertainty needs 0 <= low <= high <= 1')
        elif self.p is None or not 0 <= self.p <= 1 or self.low is not None or self.high is not None:
            raise ValueError('Bernoulli uncertainty needs only 0 <= p <= 1')
        return self


class Scheduled(Record):
    month: str
    id: str
    label: Label
    effect: str


class Conditional(Record):
    id: str
    label: Label
    when: str
    effect: str
    judgment_month: Tagged | None = None


class Events(Record):
    scheduled: list[Scheduled]
    conditional: list[Conditional]


class Measure(Record):
    id: str
    kind: Literal['bool', 'category', 'money', 'count', 'score']
    values: list[str] | None = None


class Reference(Record):
    when: str | int
    what: str
    label: Label


class Execution(Record):
    roles: dict[str, str]
    worlds: dict[str, str]
    phases: dict[str, Tagged]
    defaults: dict[str, Tagged]
    coefficients: dict[str, Tagged]
    events: dict[str, str]
    observation_note: str


class Scenario(Record):
    schema_version: Literal['timeline-lab-sketch/0.2'] = Field(alias='schema')
    scenario: Window
    actors: dict[str, Actor]
    world: dict[str, dict[str, Tagged | str]]
    levers: dict[str, Lever]
    uncertainty: dict[str, Distribution]
    events: Events
    measures: list[Measure]
    canon_reference: list[Reference]
    protected: list[str]
    open_items: list[str]
    execution: Execution
    drama: Drama
    metric_catalog: list[MetricDefinition]

    @cached_property
    def digest(self):
        return hashlib.sha256(json.dumps(self.model_dump(by_alias=True), sort_keys=True,
                                        separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()

    def actor(self, role):
        return self.actors[self.execution.roles[role]]

    def coefficient(self, key):
        return self.execution.coefficients[key].number()

    def param(self, role, key):
        return self.actor(role).params[key].number()

    def phase(self, key):
        return str(self.execution.phases[key].value)


def months(start, end):
    def ordinal(value):
        year, month = map(int, value.split('-'))
        if not 1 <= month <= 12:
            raise ValueError(f'Invalid month: {value}')
        return year * 12 + month - 1
    first, last = ordinal(start), ordinal(end)
    if first > last:
        raise ValueError('Scenario start is after its end')
    return [f'{n // 12:04d}-{n % 12 + 1:02d}' for n in range(first, last + 1)]


def chosen(scenario, overrides=None):
    """Canon levers plus explicitly labeled defaults for the two OPEN choices."""
    result = {}
    for name, lever in scenario.levers.items():
        fallback = scenario.execution.defaults.get(name)
        value = fallback.value if fallback else lever.canon
        result[name] = deepcopy(value)
    result.update(overrides or {})
    if set(result) != set(scenario.levers):
        raise ValueError('Unknown lever')
    for name, value in result.items():
        lever = scenario.levers[name]
        values = value if lever.multi_select and isinstance(value, list) else [value]
        if lever.multi_select and (not isinstance(value, list) or len(values) != len(set(values))):
            raise ValueError(f'{name}: choose a list without duplicates')
        if any(not any(type(v) is type(o) and v == o for o in lever.options) for v in values):
            raise ValueError(f'{name}: choose from {lever.options}, received {value!r}')
    return result


def bounded(value):
    return max(0.0, min(1.0, value))


def observe(events, actor_id):
    """Only delivered facts enter a decision. Narrator reasons/private draws never do."""
    facts = {}
    for event in events:
        if event['audience'] == 'public' or actor_id in event['audience']:
            facts.update(event['facts'])
    return facts


@dataclass
class History:
    world: int
    seed: int
    scenario_hash: str
    levers: dict
    branch: dict | None
    draws: dict
    events: list
    series: list
    measures: dict
    semantics: dict = field(default_factory=dict)

    def export(self, scenario):
        from dataclasses import asdict
        from stories import candidate
        from metrics import samples
        from ontology import entity_catalog, bundle
        return {**asdict(self), 'status': 'DRAFT / LAB', 'engine_version': ENGINE_VERSION,
                'scenario': scenario.model_dump(by_alias=True),
                'entities': entity_catalog(scenario), 'story': candidate(scenario, self).model_dump(),
                'ontology': bundle(scenario, self),
                'metric_samples': [m.model_dump() for m in samples(scenario, self)],
                'note': 'Illustrative histories from LAB rules, not calibrated probabilities or canon.'}


COEFFICIENTS = '''decision_noise senate_support_base senate_mood_weight senate_opposition_weight
loan_approval_threshold loan_refusal_threshold treaty_delay_margin indemnity_threshold
broker_threshold public_opposition_threshold subscription_risk_base partial_subscription_margin
partial_subscription_fraction government_accept_threshold government_counter_margin
government_ratification_threshold army_lobby_threshold army_obstruct_threshold army_growth
army_recovery cabinet_run_loss cabinet_obstruction_loss cabinet_failed_payment_loss
cabinet_second_run_loss cabinet_recovery london_grievance lender_return_relief
alternative_payment_weight alternative_devaluation_weight alternative_liquidation_weight'''.split()
COEFFICIENTS.append('reserve_buffer_musd')
PARAMS = {
    'executive': [], 'lenders': [],
    'legislature': ['two_thirds_threshold', 'initial_trust_in_executive', 'trust_loss_per_illegal_month'],
    'mediator': ['min_concessions_to_broker', 'brokering_effect_on_tate_cohesion'],
    'government': ['initial_trust_in_julian', 'promise_in_japanese_trust_bonus',
                   'broken_promise_trust_penalty', 'initial_cabinet_stability'],
    'military': ['initial_influence', 'cabinet_fall_threshold'],
    'subscribers': ['guarantee_risk_reduction', 'concord_tie_risk_reduction'],
}
LEVER_KEYS = '''credit_size_musd public_share tie_to_concord consent_path offer_month
promise_in_japanese if_senate_refuses_loan concessions_1928 assurance_strategy commitment_priority'''.split()
UNCERTAINTY_KEYS = '''share_not_renewed sf_syndicate_appetite army_opportunism senate_mood
victoria_brokering_skill lenders_return_probability second_run_if_reserves_short better_offer_appears'''.split()
DECISIONS = {
    'executive': {},
    'legislature': dict(rescue_loan_vote=['approve', 'approve_with_public_cap', 'refuse'],
                        treaty_consent=['consent', 'refuse', 'delay'], indemnity_act=['pass', 'refuse']),
    'mediator': dict(settlement_role=['broker_settlement', 'stay_aloof', 'oppose_publicly']),
    'government': dict(response_to_offer=['accept', 'counteroffer', 'refuse'],
                       alternative_if_refused=['stop_paying_abroad', 'let_yen_fall', 'let_banks_fail'],
                       concord_ratification=['ratify_conditionally', 'refuse']),
    'military': dict(posture=['cooperate', 'lobby_against', 'obstruct']),
    'subscribers': dict(subscription=['subscribe_full', 'subscribe_partial', 'refuse']),
    'lenders': dict(per_month=['renew', 'withdraw', 'return_if_stabilized']),
}


def exact_keys(mapping, expected, name):
    if set(mapping) != set(expected):
        raise ValueError(f'{name}: missing {set(expected) - set(mapping)}, unknown {set(mapping) - set(expected)}')


def validate(s):
    """Check executable dictionaries as well as Pydantic's closed record shapes."""
    exact_keys(s.execution.roles, ROLES, 'roles')
    exact_keys(s.actors, s.execution.roles.values(), 'actors')
    if len(set(s.execution.roles.values())) != len(ROLES):
        raise ValueError('Every role requires a distinct actor')
    for role in ROLES:
        a = s.actor(role)
        if a.control != ('controlled' if role == 'executive' else 'independent'):
            raise ValueError('Only the executive role is controlled')
        exact_keys(a.params, PARAMS[role], f'{role}.params')
        if a.decisions != DECISIONS[role]:
            raise ValueError(f'{role}: unsupported or missing decision/options')
        for p in a.params.values():
            p.number()
    exact_keys(s.execution.coefficients, COEFFICIENTS, 'coefficients')
    if any(x.label != 'LAB' or x.number() < 0 for x in s.execution.coefficients.values()):
        raise ValueError('Execution coefficients must be nonnegative LAB numbers')
    exact_keys(s.execution.worlds, ['domestic', 'partner'], 'world roles')
    exact_keys(s.world, s.execution.worlds.values(), 'world')
    exact_keys(s.levers, LEVER_KEYS, 'levers')
    exact_keys(s.uncertainty, UNCERTAINTY_KEYS, 'uncertainty')
    exact_keys(s.execution.defaults, ['offer_month', 'if_senate_refuses_loan', 'assurance_strategy', 'commitment_priority'], 'defaults')
    exact_keys(s.execution.phases, ['settlement', 'council'], 'phases')
    exact_keys(s.execution.events, ['crisis', 'moratorium', 'payments', 'declaration', 'court', 'council'], 'events')
    scheduled = {e.id: e for e in s.events.scheduled}
    conditional = {e.id: e for e in s.events.conditional}
    exact_keys(scheduled, [s.execution.events[k] for k in ('crisis', 'moratorium', 'payments')], 'scheduled events')
    exact_keys(conditional, [s.execution.events[k] for k in ('declaration', 'court', 'council')], 'conditional events')
    window = months(s.scenario.start, s.scenario.end)
    if any(e.month not in window for e in s.events.scheduled) or any(s.phase(k) not in window for k in s.execution.phases):
        raise ValueError('An event/phase is outside the scenario window')
    if len(s.actor('legislature').factions) != 1:
        raise ValueError('This sketch needs the one configured legislative faction')
    exact_keys(s.actor('legislature').reasons_for,
               ['concessions_offered', 'victoria_brokering', 'ka_lokahi_declaration', 'trust_in_executive'], 'legislative reasons')
    exact_keys(s.actor('legislature').reasons_against,
               ['cost_share_65_percent', 'dilution_64m_vs_27m', 'prerogative_precedent', 'county_boards_leverage', 'coupon_clipper_grievance'], 'legislative opposition')
    exact_keys(s.actor('government').reasons_for_accepting,
               ['no_better_offer', 'saionji_counsel_army_risk', 'real_value_of_concord', 'conditional_approval_hedge', 'trust_in_julian'], 'government reasons')
    exact_keys(s.actor('government').reasons_against,
               ['sovereignty_cost_if_tied', 'credit_shortfall_vs_need', 'thalassia_bakufu_criticism'], 'government opposition')
    chosen(s)
    if any(type(v) not in (float, int) or not 0 <= v <= 1 for v in s.levers['public_share'].options):
        raise ValueError('Public shares must be between zero and one')
    if any(type(v) not in (float, int) or v <= 0 for v in s.levers['credit_size_musd'].options):
        raise ValueError('Credit options must be positive numbers')
    if sum(s.coefficient(k) for k in COEFFICIENTS if k.startswith('alternative_')) <= 0:
        raise ValueError('At least one Japanese alternative must have positive weight')
    for m in s.measures:
        if m.kind == 'category' and not m.values:
            raise ValueError('Category measures need declared values')
    validate_drama(s)
    from metrics import resolve_input
    for definition in s.metric_catalog:
        for ref in definition.input_refs:
            resolve_input(s, ref)
    Engine(s, 0)  # validates required numeric starting state before any run
    return s


def load_scenario(path):
    import yaml

    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in result:
                raise ValueError(f'YAML keys must be unique strings: {key!r}')
            result[key] = loader.construct_object(value_node, deep=deep)
        return result

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    try:
        data = yaml.load(Path(path).read_text(encoding='utf-8-sig'), Loader=UniqueLoader)
    except yaml.YAMLError as exc:
        raise ValueError(f'Invalid scenario YAML: {exc}') from exc
    return validate(Scenario.model_validate(data))


class Engine:
    def __init__(self, scenario, world, seed=None):
        self.s, self.world = scenario, world
        self.hash = scenario.digest
        self.seed = seed if seed is not None else int.from_bytes(
            hashlib.sha256(f'{self.hash}:{world}'.encode()).digest()[:8], 'big')
        self.months = months(scenario.scenario.start, scenario.scenario.end)
        rng = random.Random(self.seed)
        self.draws = {'uncertainty': {k: rng.uniform(d.low, d.high) if d.dist == 'uniform'
                                     else rng.random() < d.p for k, d in sorted(scenario.uncertainty.items())}}
        # Draw the full tape in advance: branch-dependent code cannot shift external shocks.
        self.draws['monthly'] = {m: {r: rng.random() for r in ROLES} for m in self.months}
        self.events, self.series, self.beliefs = [], [], {}
        self.views = {actor_id: {} for actor_id in scenario.actors}
        self.c = {k: v.number() for k, v in scenario.execution.coefficients.items()}.__getitem__
        self.conditional = {e.id: e for e in scenario.events.conditional}
        self.partner = scenario.world[scenario.execution.worlds['partner']]
        self.domestic = scenario.world[scenario.execution.worlds['domestic']]
        exact_keys(self.partner, ['short_foreign_funding_musd', 'share_not_renewed', 'bank_losses_musd',
                                 'new_capital_musd', 'boj_lending_musd', 'external_need_six_weeks_imports_musd',
                                 'grievance_toward_london'], 'partner state')
        exact_keys(self.domestic, ['concord_status', 'legality', 'public_credit_tolerance_musd'], 'domestic state')
        if self.domestic['concord_status'] != 'none' or self.domestic['legality'] != 'lawful':
            raise ValueError('This crisis sketch starts before a Concord and with lawful government')
        if self.domestic['public_credit_tolerance_musd'].number() < 0:
            raise ValueError('Public credit tolerance cannot be negative')
        for value in self.partner.values():
            if value.number() < 0:
                raise ValueError('Starting financial stocks and scores cannot be negative')
        self.n = lambda k: self.partner[k].number()
        u = self.draws['uncertainty']
        need = max(0.0, self.n('external_need_six_weeks_imports_musd') + self.n('short_foreign_funding_musd') *
                   (u['share_not_renewed'] - self.n('share_not_renewed')))
        self.state = dict(need=need, payment_need=max(0.0, need - self.c('reserve_buffer_musd')),
                          buffer_met=False, offer=None, offer_revision=0, concessions=[], concession_revision=0,
                          loan_vote=None, treaty_vote=None, government_reply=None, ratified=False,
                          subscription=0.0, mediator_role=None, military_posture='cooperate',
                          lenders_returned=False, lender_withdrawal=False, declaration=False,
                          concord=self.domestic['concord_status'], legality=self.domestic['legality'],
                          court='none', council=False, payments_done=False, payments_met=False,
                          credit_drawn=0.0, public_drawn=0.0, committed=0.0, public_share=0.0,
                          japan_path=None, illegal_months=0, faction='cohesive', cabinet_fallen=False,
                          cabinet=scenario.param('government', 'initial_cabinet_stability'),
                          army=scenario.param('military', 'initial_influence'),
                          grievance=self.n('grievance_toward_london'))
        self.state['settlement_presented'] = False
        for role in ROLES:
            self.beliefs[role] = dict(loan_revision=-1, treaty_revision=None, offer_revision=-1,
                                     promise_revision=-1, promised=False, broken=False, mediation_revision=-1)
        self.beliefs['legislature']['trust'] = scenario.param('legislature', 'initial_trust_in_executive')
        self.beliefs['government']['trust'] = scenario.param('government', 'initial_trust_in_julian')
        self.last_offer = None
        self.relationships = Relationships(self)

    def emit(self, month, kind, actor, action, facts=None, reason='', label='LAB', audience='public'):
        self.deliver(dict(month=month, kind=kind, actor=actor, action=action, label=label,
                          facts=facts or {}, reason=reason, audience=audience,
                          cause_refs=[self.relationships.executing] if self.relationships.executing and kind != 'state' else []))

    def deliver(self, event):
        event.setdefault('id', f'event-{len(self.events)}')
        self.events.append(event)
        for actor_id, facts in self.views.items():
            if event['audience'] == 'public' or actor_id in event['audience']:
                facts.update(event['facts'])
        self.relationships.delivered(event)

    def publish(self, month):
        # Public institutional facts, not private beliefs, decision scores or random draws.
        # State is scalar except for the offer and concessions; copy those explicitly
        # so earlier logs remain fixed without recursively copying every scalar monthly.
        facts = dict(self.state)
        facts['offer'] = dict(self.state['offer']) if self.state['offer'] else None
        facts['concessions'] = list(self.state['concessions'])
        self.emit(month, 'state', None, 'public_update', facts)

    def decide(self, role, info, private, noise, month, controls):
        s, c, u = self.s, self.c, self.draws['uncertainty']
        offer = info.get('offer')
        result = []
        self.relationships.observe(role, info, private, month)
        def act(action, **data):
            if action in ('rescue_loan_vote', 'treaty_consent', 'response_to_offer', 'concord_ratification', 'subscription'):
                data['offer_revision'] = info['offer_revision']
            result.append((action, data))
            self.relationships.record(role, action, data, info, private, month)
        for action, data in self.relationships.actions(role, info, private, noise, month, controls):
            act(action, **data)
        if role == 'executive':
            proposed = {k: v for k, v in controls.items() if k not in ('concessions_1928', 'assurance_strategy', 'commitment_priority')}
            if month >= controls['offer_month'] and not info.get('payments_done') and proposed != self.last_offer:
                act('offer_credit', offer=proposed)
                self.last_offer = deepcopy(proposed)
            eligible = month >= s.phase('settlement') or controls['consent_path'] == 'renegotiate_first'
            offered = self.relationships.concessions(info, controls)
            if eligible and (offered != info.get('concessions', []) or not info['settlement_presented']):
                act('offer_concessions', concessions=offered, requested=controls['concessions_1928'],
                    priority=controls['commitment_priority'])
            if (info.get('treaty_vote') == 'refuse' and info.get('ratified') and
                    info.get('concord') not in ('provisional', 'consented', 'lapsed') and
                    controls['consent_path'] == 'provisional_application'):
                act('provisional_application')
            return result
        if role == 'legislature':
            if info.get('legality') == 'illegal_provisional_application':
                private['trust'] = bounded(private['trust'] - s.param(role, 'trust_loss_per_illegal_month'))
            if not offer:
                return result
            a = s.actor(role)
            support = private['trust'] * a.reasons_for['trust_in_executive'].number()
            support += sum(s.drama.concessions[k].senate_support.value for k in info['concessions'])
            support += bool(info['declaration']) * a.reasons_for['ka_lokahi_declaration'].number()
            broker = info['mediator_role'] == 'broker_settlement'
            support += broker * a.reasons_for['victoria_brokering'].number()
            cohesion = next(iter(a.factions.values())).cohesion.number()
            cohesion = bounded(cohesion + broker * s.param('mediator', 'brokering_effect_on_tate_cohesion'))
            opposition = sum(x.number() for x in a.reasons_against.values()) * cohesion
            score = c('senate_support_base') + u['senate_mood'] * c('senate_mood_weight') + support
            score += noise - opposition * c('senate_opposition_weight')
            if private['loan_revision'] != info['offer_revision'] and not info['payments_done']:
                exposure = offer['credit_size_musd'] * offer['public_share']
                tolerance = self.domestic['public_credit_tolerance_musd'].number()
                vote = 'approve' if score >= c('loan_approval_threshold') and exposure <= tolerance else (
                    'approve_with_public_cap' if score >= c('loan_refusal_threshold') else 'refuse')
                act('rescue_loan_vote', vote=vote, utility=score)
                private['loan_revision'] = info['offer_revision']
            revision = (info['offer_revision'], info['concession_revision'], info['mediator_role'], info.get('assurance_report'))
            if offer['tie_to_concord'] and private['treaty_revision'] != revision and info['concord'] != 'consented':
                threshold = s.param(role, 'two_thirds_threshold')
                vote = 'consent' if score >= threshold else ('delay' if score >= threshold - c('treaty_delay_margin') else 'refuse')
                act('treaty_consent', vote=vote, utility=score)
                private['treaty_revision'] = revision
            if info['treaty_vote'] == 'consent' and info['legality'] == 'illegal_provisional_application':
                act('indemnity_act', vote='pass' if score >= c('indemnity_threshold') else 'refuse', utility=score)
        elif role == 'mediator':
            revision = info.get('concession_revision', 0)
            if (month >= s.phase('settlement') and private['mediation_revision'] != revision and
                    (info.get('legality') == 'illegal_provisional_application' or info.get('treaty_vote') == 'refuse')):
                enough = sum(s.drama.concessions[k].mediator_support.value for k in info['concessions']) >= s.param(role, 'min_concessions_to_broker')
                score = u['victoria_brokering_skill'] + noise
                if private.get('assurance_assessment') == 'honoured':
                    score += s.drama.rules.honour_bonus.value
                if private.get('assurance_assessment') == 'breached':
                    enough = False
                action = 'broker_settlement' if enough and score >= c('broker_threshold') else (
                    'oppose_publicly' if not enough and score >= c('public_opposition_threshold') else 'stay_aloof')
                if private.get('assurance_assessment') == 'breached':
                    action = 'stay_aloof'  # Private withdrawal is not a public disclosure.
                act('settlement_role', choice=action, utility=score)
                private['mediation_revision'] = revision
        elif role == 'government':
            if offer and private['promise_revision'] != info['offer_revision']:
                if offer['promise_in_japanese'] and not private['promised']:
                    private['trust'] = bounded(private['trust'] + s.param(role, 'promise_in_japanese_trust_bonus'))
                    private['promised'] = True
                private['promise_revision'] = info['offer_revision']
            if offer and info['payments_done'] and not info['payments_met'] and not private['broken']:
                if private['promised']:
                    private['trust'] = bounded(private['trust'] - s.param(role, 'broken_promise_trust_penalty'))
                private['broken'] = True
            if info.get('payments_done') and not info['payments_met'] and info['japan_path'] is None:
                weights = [c(k) for k in ('alternative_payment_weight', 'alternative_devaluation_weight', 'alternative_liquidation_weight')]
                draw = self.draws['monthly'][month][role] * sum(weights)
                index = 0 if draw < weights[0] else (1 if draw < sum(weights[:2]) else 2)
                act('alternative_if_refused', choice=s.actor(role).decisions['alternative_if_refused'][index])
            if not offer or info['payments_done'] or private['offer_revision'] == info['offer_revision']:
                return result
            a = s.actor(role)
            features = dict(no_better_offer=not info.get('better_offer_available', False), saionji_counsel_army_risk=info['army'],
                            real_value_of_concord=offer['tie_to_concord'], conditional_approval_hedge=offer['tie_to_concord'],
                            trust_in_julian=private['trust'])
            score = sum(a.reasons_for_accepting[k].number() * value for k, value in features.items()) + noise
            coverage = min(1.0, offer['credit_size_musd'] / info['need']) if info['need'] else 1.0
            score -= a.reasons_against['sovereignty_cost_if_tied'].number() * offer['tie_to_concord']
            score -= a.reasons_against['credit_shortfall_vs_need'].number() * (1 - coverage)
            score -= a.reasons_against['thalassia_bakufu_criticism'].number() * info['army'] * offer['tie_to_concord']
            response = 'accept' if coverage >= 1 and score >= c('government_accept_threshold') else (
                'counteroffer' if score >= -c('government_counter_margin') else 'refuse')
            terms = dict(requested_credit_musd=max(info['need'], offer['credit_size_musd']),
                         untied_credit=offer['tie_to_concord']) if response == 'counteroffer' else {}
            act('response_to_offer', choice=response, utility=score, **terms)
            if response == 'accept' and offer['tie_to_concord']:
                act('concord_ratification', choice='ratify_conditionally' if score >= c('government_ratification_threshold') else 'refuse')
            private['offer_revision'] = info['offer_revision']
        elif role == 'subscribers':
            if offer and not info['payments_done'] and private['offer_revision'] != info['offer_revision']:
                risk = c('subscription_risk_base') - offer['public_share']
                risk -= s.param(role, 'guarantee_risk_reduction')
                risk -= offer['tie_to_concord'] * s.param(role, 'concord_tie_risk_reduction')
                score = u['sf_syndicate_appetite'] - risk + noise
                choice = 'subscribe_full' if score >= 0 else ('subscribe_partial' if score >= -c('partial_subscription_margin') else 'refuse')
                act('subscription', choice=choice, utility=score)
                private['offer_revision'] = info['offer_revision']
        elif role == 'military':
            score = (u['army_opportunism'] + 1 - info['cabinet'] + info['army']) / len(('opportunism', 'weakness', 'influence')) + noise
            choice = 'obstruct' if score >= c('army_obstruct_threshold') else ('lobby_against' if score >= c('army_lobby_threshold') else 'cooperate')
            if choice != info['military_posture']:
                act('posture', choice=choice, utility=score)
        elif role == 'lenders':
            if info.get('crisis') and not info['lender_withdrawal']:
                act('per_month', choice='withdraw')
            elif info['payments_met'] and not info['lenders_returned']:
                # The role's fixed monthly draw, not a draw consumed conditionally.
                if self.draws['monthly'][month][role] < u['lenders_return_probability']:
                    act('per_month', choice='return_if_stabilized')
        return result

    def resolve(self, month, decisions):
        w, s = self.state, self.s
        for role, action, data in decisions:
            self.relationships.begin(month, role, action)
            self.emit(month, 'decision' if role == 'executive' else 'response', s.execution.roles[role], action,
                      reason=json.dumps(data, ensure_ascii=False, sort_keys=True),
                      audience=self.relationships.audience(action, data, role))
            if 'offer_revision' in data and data['offer_revision'] != w['offer_revision']:
                self.emit(month, 'consequence', None, 'reply_to_superseded_offer',
                          reason='This response concerns the previous terms; revised terms need a fresh response.')
                continue
            if self.relationships.resolve(month, role, action, data):
                continue
            if action == 'offer_credit':
                w.update(offer=deepcopy(data['offer']), offer_revision=w['offer_revision'] + 1,
                         loan_vote=None, treaty_vote=None, government_reply=None, ratified=False, subscription=0.0)
            elif action == 'offer_concessions':
                w.update(concessions=list(data['concessions']), concession_revision=w['concession_revision'] + 1,
                         settlement_presented=True)
            elif action == 'provisional_application':
                w.update(concord='provisional', legality='illegal_provisional_application')
            elif action == 'rescue_loan_vote':
                w['loan_vote'] = data['vote']
            elif action == 'treaty_consent':
                w['treaty_vote'] = data['vote']
                if data['vote'] == 'refuse' and w['concord'] == 'none':
                    w['concord'] = 'refused'
            elif action == 'indemnity_act' and data['vote'] == 'pass':
                w['legality'] = 'indemnified'
                if w['court'] == 'pending':
                    w['court'] = 'mooted'
                    self.emit(month, 'consequence', None, 'case_mooted')
            elif action == 'settlement_role':
                w['mediator_role'] = data['choice']
                if data['choice'] == 'broker_settlement':
                    w['faction'] = 'split'
            elif action == 'response_to_offer':
                w['government_reply'] = data['choice']
            elif action == 'alternative_if_refused':
                w['japan_path'] = dict(stop_paying_abroad='stopped_paying_abroad', let_yen_fall='yen_fell', let_banks_fail='banks_failed')[data['choice']]
            elif action == 'concord_ratification':
                w['ratified'] = data['choice'] == 'ratify_conditionally'
            elif action == 'subscription':
                w['subscription'] = {'subscribe_full': 1.0, 'subscribe_partial': self.c('partial_subscription_fraction'), 'refuse': 0.0}[data['choice']]
            elif action == 'posture':
                w['military_posture'] = data['choice']
            elif action == 'per_month':
                if data['choice'] == 'withdraw':
                    w['lender_withdrawal'] = True
                    w['grievance'] = bounded(w['grievance'] + self.c('london_grievance'))
                else:
                    w['lenders_returned'] = True
                    w['grievance'] = bounded(w['grievance'] - self.c('lender_return_relief'))
        self.relationships.executing = None
        if w['ratified'] and w['treaty_vote'] == 'consent' and w['concord'] != 'lapsed':
            w['concord'] = 'consented'
            if w['faction'] == 'split':
                w['faction'] = 'abstains'

    def settle_credit(self, month):
        w, offer = self.state, self.state['offer']
        w['payments_done'] = True
        if offer and w['government_reply'] == 'accept' and (not offer['tie_to_concord'] or w['ratified']):
            ceiling, share = offer['credit_size_musd'], offer['public_share']
            private = ceiling * (1 - share) * w['subscription']
            public = ceiling * share
            if w['loan_vote'] == 'approve_with_public_cap':
                public = min(public, self.domestic['public_credit_tolerance_musd'].number())
            elif w['loan_vote'] != 'approve':
                fallback = offer['if_senate_refuses_loan']
                if w['loan_vote'] is None or fallback == 'withdraw_offer':
                    public = private = 0.0
                elif fallback == 'private_only':
                    public, share, ceiling = 0.0, 0.0, private
                    self.emit(month, 'consequence', None, 'private_only_credit', reason='Effective public share is zero; the private commitment limits the facility.')
                else:
                    self.emit(month, 'consequence', self.s.execution.roles['executive'], 'unauthorized_public_credit',
                              reason='Public credit proceeds without a legislative appropriation; this does not confer treaty authority.')
            capacity = min(ceiling, public / share if share else ceiling,
                           private / (1 - share) if share < 1 else ceiling)
            w.update(committed=capacity, public_share=share, credit_drawn=min(w['need'], capacity))
            w['public_drawn'] = w['credit_drawn'] * share
        w['payments_met'] = w['credit_drawn'] >= w['payment_need']
        w['buffer_met'] = w['credit_drawn'] >= w['need']
        if w['payments_met']:
            w['japan_path'] = 'rescued'
        self.emit(month, 'consequence', None, 'payments_met' if w['payments_met'] else 'payments_short',
                  reason=f"Payment need {w['payment_need']:.2f}; need including reserve target {w['need']:.2f}; drawn {w['credit_drawn']:.2f}; public {w['public_drawn']:.2f} (period $m; LAB from MODEL inputs).")

    def finish_month(self, month, moratorium):
        w, s, c = self.state, self.s, self.c
        if w['payments_met']:
            w['cabinet'] = bounded(w['cabinet'] + c('cabinet_recovery'))
            w['army'] = bounded(w['army'] - c('army_recovery'))
        elif not moratorium:
            loss = c('cabinet_failed_payment_loss') if w['payments_done'] else c('cabinet_run_loss')
            w['cabinet'] = bounded(w['cabinet'] - loss)
            w['army'] = bounded(w['army'] + c('army_growth') * self.draws['uncertainty']['army_opportunism'])
        if w['military_posture'] == 'obstruct':
            w['cabinet'] = bounded(w['cabinet'] - c('cabinet_obstruction_loss'))
        if not w['cabinet_fallen'] and w['cabinet'] < s.param('military', 'cabinet_fall_threshold'):
            w['cabinet_fallen'], w['army'] = True, 1.0
            self.emit(month, 'consequence', None, 'cabinet_falls')
        if w['cabinet_fallen']:
            w['army'] = 1.0
        if w['legality'] == 'illegal_provisional_application':
            w['illegal_months'] += 1
        conditional = self.conditional
        def event(key):
            e = conditional[s.execution.events[key]]
            self.emit(month, 'consequence', None, e.id, reason=e.effect, label=e.label)
        if w['concord'] == 'provisional' and not w['declaration']:
            w['declaration'] = True
            event('declaration')
        if w['legality'] == 'illegal_provisional_application' and w['court'] == 'none':
            w['court'] = 'pending'
            event('court')
        judgment = conditional[s.execution.events['court']].judgment_month.value
        if w['court'] == 'pending' and month >= judgment:
            w['court'] = 'judgment'
            self.emit(month, 'consequence', None, 'judgment_reached', reason='The sketch does not invent the court ruling.')
        if w['concord'] in ('provisional', 'consented') and month >= s.phase('council') and not w['council']:
            w['council'] = True
            event('council')
        if month == self.months[-1] and w['ratified'] and w['concord'] != 'consented':
            w['concord'] = 'lapsed'
            self.emit(month, 'consequence', None, 'conditional_ratification_lapses', reason='No Pacifican consent by the end of this sketch (LAB timing). Credit obligations survive.')
        self.publish(month)
        self.series.append(dict(month=month, credit_drawn_musd=w['credit_drawn'], public_drawn_musd=w['public_drawn'],
                                effective_public_share=w['public_share'], credit_committed_musd=w['committed'],
                                reserve_target_met=w['buffer_met'], payment_need_musd=w['payment_need'],
                                funding_target_musd=w['need'], payments_done=w['payments_done'],
                                payments_met=w['payments_met'], concord=w['concord'], court=w['court'], legality=w['legality'],
                                mediator_role=w['mediator_role'], illegal_months=w['illegal_months'],
                                assurance_status=self.relationships.commitment.status if self.relationships.commitment else 'not_made',
                                mediator_assessment=self.beliefs['mediator'].get('assurance_assessment', 'unknown'),
                                public_assurance_report=self.views[self.s.execution.roles['government']].get('assurance_report', 'not_disclosed'),
                                army_influence=w['army'], cabinet_stability=w['cabinet'],
                                japan_trust=self.beliefs['government']['trust'], senate_trust=self.beliefs['legislature']['trust']))

    def run(self, controls, branch=None, hidden_events=()):
        base = chosen(self.s, controls)
        active = deepcopy(base)
        if branch:
            exact_keys(branch, ['month', 'lever', 'value'], 'branch')
            if branch['month'] not in self.months or branch['lever'] not in self.s.levers:
                raise ValueError('Invalid branch month or lever')
            chosen(self.s, {**base, branch['lever']: branch['value']})
            deadline = next(e.month for e in self.s.events.scheduled if e.id == self.s.execution.events['payments'])
            if branch['lever'] not in ('consent_path', 'concessions_1928', 'commitment_priority') and branch['month'] >= deadline:
                raise ValueError('That credit decision is already settled at the payment deadline; branch earlier')
            if branch['lever'] == 'offer_month' and branch['value'] < branch['month']:
                raise ValueError('A branch cannot move an offer into its unchanged past')
        self.publish(self.months[0])
        for month in self.months:
            if branch and month == branch['month']:
                if branch['value'] == active[branch['lever']]:
                    raise ValueError('Choose a different value for the branch decision')
                if branch['lever'] == 'assurance_strategy' and self.relationships.commitment:
                    raise ValueError('An assurance already made cannot be erased; branch before it was offered')
                if branch['lever'] in ('consent_path', 'concessions_1928') and self.state['concord'] == 'consented':
                    raise ValueError('Consent is already settled; branch before that decision')
                if branch['lever'] == 'consent_path' and self.state['concord'] == 'provisional':
                    raise ValueError('Provisional application already happened; branch before that decision')
                active[branch['lever']] = deepcopy(branch['value'])
                self.emit(month, 'decision', self.s.execution.roles['executive'], 'author_branch', reason=json.dumps(branch))
            moratorium = False
            for event in self.s.events.scheduled:
                if event.month != month:
                    continue
                self.emit(month, 'chance', None, event.id, reason=event.effect, label=event.label)
                if event.id == self.s.execution.events['crisis']:
                    self.emit(month, 'state', None, 'crisis_observed', {'crisis': True})
                    if self.draws['uncertainty']['better_offer_appears']:
                        self.emit(month, 'chance', None, 'competing_offer_available',
                                  facts={'better_offer_available': True},
                                  reason='The government learns of another possible offer (LAB).',
                                  audience=[self.s.execution.roles['government']])
                if event.id == self.s.execution.events['moratorium']:
                    moratorium = True
                if event.id == self.s.execution.events['payments']:
                    self.settle_credit(month)
                    if not self.state['buffer_met'] and self.draws['uncertainty']['second_run_if_reserves_short']:
                        self.state['cabinet'] = bounded(self.state['cabinet'] - self.c('cabinet_second_run_loss'))
                        self.emit(month, 'chance', None, 'second_bank_run')
                    self.publish(month)
            for event in hidden_events:
                if event['month'] == month:
                    self.deliver(deepcopy(event))
            # Freeze all observations before resolution; actor iteration order grants no foresight.
            decisions = []
            for role in ROLES:
                info = self.views[self.s.execution.roles[role]]
                noise = (self.draws['monthly'][month][role] * 2 - 1) * self.c('decision_noise')
                decisions.extend((role, action, data) for action, data in
                                 self.decide(role, info, self.beliefs[role], noise, month, active))
            self.resolve(month, decisions)
            self.finish_month(month, moratorium)
        w = self.state
        measures = dict(june_payments_met=w['payments_met'], japan_path=w['japan_path'], credit_drawn_musd=w['credit_drawn'],
                        public_drawn_musd=w['public_drawn'], concord_status_end=w['concord'], months_of_illegal_application=w['illegal_months'],
                        cabinet_survives=not w['cabinet_fallen'], army_influence_end=w['army'],
                        japan_trust_in_julian_end=self.beliefs['government']['trust'],
                        senate_trust_in_executive_end=self.beliefs['legislature']['trust'], tate_bloc_end=w['faction'],
                        grievance_toward_london_end=w['grievance'], monterey_case_end=w['court'])
        exact_keys(measures, [m.id for m in self.s.measures], 'measures')
        for measure in self.s.measures:
            if measure.kind == 'category' and measures[measure.id] not in measure.values:
                raise ValueError(f'Unsupported outcome: {measure.id}')
        return History(self.world, self.seed, self.hash, base, branch, self.draws, self.events, self.series, measures,
                       self.relationships.export())


def simulate(scenario, world=0, levers=None, seed=None, branch=None, hidden_events=()):
    if not isinstance(world, int) or world < 0:
        raise ValueError('World number must be a nonnegative integer')
    return Engine(scenario, world, seed).run(levers, branch, hidden_events)


def batch(scenario, count=1000, levers=None, start=0):
    if not 1 <= count <= 10000 or start < 0:
        raise ValueError('Choose 1–10,000 worlds and a nonnegative start')
    controls = chosen(scenario, levers)
    return [simulate(scenario, world, controls) for world in range(start, start + count)]


def outcome_counts(histories):
    keys = ['june_payments_met', 'japan_path', 'concord_status_end', 'cabinet_survives', 'tate_bloc_end', 'monterey_case_end']
    return {key: dict(Counter(str(h.measures[key]) for h in histories)) for key in keys}


def diverse(histories, limit=5):
    """Greedy max-min Jaccard distance over dated event pairs; deterministic ties."""
    def signature(h):
        seq = [(e['month'], e['actor'], e['action'], e['reason']) for e in h.events if e['kind'] != 'state']
        # Utilities differ numerically but do not turn identical decisions into different plots.
        tokens = []
        for month, actor, action, reason in seq:
            try:
                data = json.loads(reason)
                choice = data.get('choice', data.get('vote', '')) if isinstance(data, dict) else ''
            except (ValueError, TypeError):
                choice = ''
            tokens.append((month, actor, action, choice))
        return set(zip([None] + tokens, tokens))
    if not histories:
        return []
    signatures = [signature(h) for h in histories]
    selected, distances = [0], [1.0] * len(histories)
    while len(selected) < min(limit, len(histories)):
        last = signatures[selected[-1]]
        for i, sig in enumerate(signatures):
            distances[i] = min(distances[i], 1 - len(last & sig) / max(1, len(last | sig)))
        for i in selected:
            distances[i] = -1
        candidate = max(range(len(histories)), key=lambda i: distances[i])
        if distances[candidate] <= 0:
            break
        selected.append(candidate)
    return [histories[i] for i in selected]


def bands(histories):
    """Observed quantiles over all worlds, including failures."""
    rows = []
    for i, step in enumerate(histories[0].series):
        for key in ('credit_drawn_musd', 'public_drawn_musd', 'army_influence', 'cabinet_stability', 'japan_trust', 'senate_trust'):
            values = sorted(h.series[i][key] for h in histories)
            def quantile(p):
                position = (len(values) - 1) * p
                lo, hi = math.floor(position), math.ceil(position)
                return values[lo] + (values[hi] - values[lo]) * (position - lo)
            rows.append(dict(month=step['month'], measure=key, low=quantile(.1), median=quantile(.5), high=quantile(.9)))
    return rows
