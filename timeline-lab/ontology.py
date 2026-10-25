"""Executable subset of the v0.10 ontology for the rescue/settlement dilemma."""
from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_validator

ENGINE_VERSION = '0.2'


class Closed(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True, allow_inf_nan=False)


class LabNumber(Closed):
    value: float
    label: Literal['LAB']


class Goal(Closed):
    id: str
    owner_role: str
    capacity: Literal['personal', 'institutional']
    description: str
    mechanism: str
    label: Literal['LAB']


class Concession(Closed):
    senate_support: LabNumber
    mediator_support: LabNumber
    description: str


class RelationshipRules(Closed):
    report_credibility: LabNumber
    belief_thresholds: dict[str, LabNumber]
    disclosure_threshold: LabNumber
    honour_bonus: LabNumber
    breach_penalty: LabNumber


class Drama(Closed):
    label: Literal['LAB']
    assumption: str
    assurance_terms: list[str]
    goals: list[Goal]
    concessions: dict[str, Concession]
    rules: RelationshipRules


class Entity(Closed):
    id: str
    name: str
    kind: Literal['person', 'office', 'institution', 'collective']
    registry_id: str | None
    acting_role: str | None
    member_of: str | None


class EvidenceRecord(Closed):
    id: str
    revision_id: str
    provenance_refs: list[str]
    label: Literal['LAB'] = 'LAB'


class Observation(EvidenceRecord):
    recipient_id: str
    event_ref: str
    received_at: str
    payload: dict[str, Any]


class WorldFact(EvidenceRecord):
    predicate: str
    value: str
    at: str
    state_owner: str


class Assertion(EvidenceRecord):
    speaker_id: str
    proposition: str
    asserted_value: str
    made_at: str
    audience: str | list[str]
    event_ref: str


class Belief(EvidenceRecord):
    actor_id: str
    proposition: str
    value: str
    observation_refs: list[str]
    update_rule: str
    at: str


class Commitment(EvidenceRecord):
    promisor_id: str
    promisee_id: str
    terms: list[str]
    made_at: str
    visibility: Literal['private', 'public']
    status: Literal['pending', 'honoured', 'breached']
    legally_binding: Literal[False] = False


class Plan(EvidenceRecord):
    owner_id: str
    goal_refs: list[str]
    status: Literal['active', 'achieved', 'frustrated', 'unknown']
    support_refs: list[str]
    owner_assessment: Literal['unknown'] = 'unknown'


class DecisionContext(EvidenceRecord):
    decision_maker_id: str
    acting_for_id: str
    role: str
    information_snapshot: dict[str, Any]
    goal_refs: list[str]
    commitment_refs: list[str]
    authority_state: str
    decision_rule: str


class DecisionRecord(EvidenceRecord):
    context_ref: str
    actor_id: str
    acting_for_id: str
    at: str
    action: str
    selected: dict[str, Any]
    considered_alternatives: list[str]
    observation_refs: list[str]
    belief_refs: list[str]
    information_used: dict[str, Any]
    private_inputs: dict[str, Any]
    goal_refs: list[str]
    commitment_refs: list[str]
    reasons: list[str]
    selection_origin: Literal['actor_procedure', 'author_override']
    random_address: str


class ActionAttempt(EvidenceRecord):
    decision_ref: str
    actor_id: str
    action: str
    at: str


class Adjudication(EvidenceRecord):
    attempt_ref: str
    disposition: Literal['executed', 'superseded']
    actual_legal_status: str
    event_ref: str


class RealizedEvent(EvidenceRecord):
    event_type: str
    happened_at: str
    participant_id: str | None
    facts: dict[str, Any]
    cause_refs: list[str]
    audience: str | list[str]


class MetricDefinition(Closed):
    id: str
    name: str
    units: str
    owner_role: str
    definition: str
    mechanism: str
    input_refs: list[str]
    coverage: Literal['modelled', 'proxy', 'unmodelled']
    label: Literal['LAB']


class MetricSample(Closed):
    metric_id: str
    value: float | int | str | bool | None
    missing_reason: str | None
    period: str
    scenario_hash: str
    engine_version: str
    world: int
    seed: int
    owner_id: str
    units: str
    coverage: str
    label: Literal['LAB']
    mechanism: str
    input_refs: list[str]
    event_refs: list[str]

    @model_validator(mode='after')
    def explicit_missingness(self):
        if (self.value is None) != (self.missing_reason is not None):
            raise ValueError('An unavailable metric requires a missing reason, never a zero')
        return self


class StoryCandidate(Closed):
    id: str
    world: int
    title: str
    focal_actor: str
    goal: str
    obstacle: str
    choice: str
    sacrifice: str | None
    consequence: str
    next_dilemma: str
    support_refs: list[str]
    decision_refs: list[str]
    causal_signature: list[str]
    claim_basis: Literal['actor_generated', 'mechanical_consequence']
    assumption_refs: list[str]
    element_statuses: dict[str, Literal['supported', 'unresolved', 'not_assessed']]


class StoryBookmark(Closed):
    schema_version: Literal['timeline-lab-bookmark/0.2']
    engine_version: Literal['0.2']
    id: str
    rationale: str
    candidate: StoryCandidate
    history: dict[str, Any]


def entity_catalog(scenario):
    """Persons remain distinct from the institution; descriptive people gain no controller."""
    roles = {actor: role for role, actor in scenario.execution.roles.items()}
    entities = []
    for actor_id, actor in scenario.actors.items():
        role = roles[actor_id]
        kind = 'person' if role in ('executive', 'mediator') else 'institution'
        entities.append(Entity(id=actor_id, name=actor.name, kind=kind, registry_id=actor.registry_id,
                               acting_role=role, member_of=None))
        if role == 'executive':
            entities.append(Entity(id=f'{actor_id}:office', name='Executive office', kind='office',
                                   registry_id=None, acting_role=None, member_of=None))
        for person_id, person in actor.persons.items():
            entities.append(Entity(id=f'{actor_id}:{person_id}', name=person_id,
                                   kind='person', registry_id=person.registry_id,
                                   acting_role=None, member_of=actor_id))
    return [entity.model_dump() for entity in entities]


def bundle(s, h):
    """Materialize typed evidence for a selected history, not every ensemble path."""
    from collections import defaultdict, deque
    base = dict(revision_id=s.digest, provenance_refs=['scenario:/drama', 'mechanism:model/0.2'])
    observations, realized, attempts, adjudications, contexts, plans, assertions = [], [], [], [], [], [], []
    indexed = defaultdict(deque)
    for event in h.events:
        if event['action'] == 'assurance_breach_disclosed':
            assertions.append(Assertion(**base, id=f"assertion:{event['id']}", speaker_id=event['actor'],
                proposition='settlement_assurance_fulfilment', asserted_value='breached', made_at=event['month'],
                audience=event['audience'], event_ref=event['id']).model_dump())
        if event['kind'] in ('decision', 'response') and event['action'] != 'author_branch':
            indexed[(event['month'], event['actor'], event['action'])].append(event)
        if event['facts']:
            for actor in s.actors:
                if event['audience'] == 'public' or actor in event['audience']:
                    observations.append(Observation(**base, id=f"observation:{actor}:{event['id']}",
                        recipient_id=actor, event_ref=event['id'], received_at=event['month'], payload=event['facts']).model_dump())
        if event['kind'] not in ('state', 'decision', 'response'):
            realized.append(RealizedEvent(**base, id=event['id'], event_type=event['action'],
                happened_at=event['month'], participant_id=event['actor'], facts=event['facts'],
                cause_refs=event.get('cause_refs', []), audience=event['audience']).model_dump())
    reverse_roles = {v: k for k, v in s.execution.roles.items()}
    for d in h.semantics.get('decisions', []):
        role = reverse_roles[d['actor_id']]
        contexts.append(DecisionContext(**base, id=f"context:{d['id']}", decision_maker_id=d['actor_id'],
            acting_for_id=d['acting_for_id'], role=role, information_snapshot=d['information_used'],
            goal_refs=d['goal_refs'], commitment_refs=d['commitment_refs'],
            authority_state=str(d['information_used'].get('legality', 'unknown')), decision_rule=f'model.decide:{role}/0.2').model_dump())
        event = indexed[(d['at'], d['actor_id'], d['action'])].popleft()
        aid = f"attempt:{d['id']}"
        attempts.append(ActionAttempt(**base, id=aid, decision_ref=d['id'], actor_id=d['actor_id'], action=d['action'], at=d['at']).model_dump())
        following = h.events[int(event['id'].split('-')[-1])+1:][:1]
        disposition = 'superseded' if following and following[0]['action'] == 'reply_to_superseded_offer' else 'executed'
        legal = 'illegal_provisional_application' if d['action'] == 'provisional_application' else 'not_assessed'
        adjudications.append(Adjudication(**base, id=f"adjudication:{d['id']}", attempt_ref=aid,
            disposition=disposition, actual_legal_status=legal, event_ref=event['id']).model_dump())
    for goal in s.drama.goals:
        ds = [d for d in h.semantics.get('decisions', []) if goal.id in d['goal_refs']]
        plans.append(Plan(**base, id=f'plan:{goal.id}', owner_id=s.execution.roles[goal.owner_role],
                          goal_refs=[goal.id], status='unknown', support_refs=[d['id'] for d in ds]).model_dump())
    facts = [WorldFact(**base, id=f'fact:{key}', predicate=key, value=str(value),
                       at=s.scenario.end, state_owner=owner).model_dump()
             for key, value, owner in [('concord_status', h.measures['concord_status_end'], 'model.resolve'),
                 ('assurance_fulfilment', h.semantics.get('commitments', [{}])[0].get('status', 'not_made')
                    if h.semantics.get('commitments') else 'not_made', 'relationships.resolve')]]
    return {**h.semantics, 'goals': [g.model_dump() for g in s.drama.goals],
            'plans': h.semantics.get('plans', []) + plans,
            'world_facts': facts, 'assertions': assertions,
            'contexts': contexts, 'observations': observations, 'attempts': attempts,
            'adjudications': adjudications, 'realized_events': realized,
            'intervention': dict(mode='policy_from_month', specification=h.branch) if h.branch else None}


def validate_drama(s):
    roles = set(s.execution.roles)
    ids = [g.id for g in s.drama.goals]
    if len(ids) != len(set(ids)) or {g.owner_role for g in s.drama.goals} != roles:
        raise ValueError('Goals need unique IDs and registered actor roles')
    mechanisms = dict(executive='commitment_priority', mediator='assurance_assessment_and_mediation',
        legislature='weighted_concession_and_authority_rule', government='credit_coverage_and_acceptance_rule',
        military='military_posture_rule', subscribers='subscription_rule', lenders='renewal_rule')
    if any(g.mechanism != mechanisms[g.owner_role] for g in s.drama.goals):
        raise ValueError('Every goal requires a supported bounded mechanism binding')
    if any(c.senate_support.value < 0 or c.mediator_support.value < 0 for c in s.drama.concessions.values()):
        raise ValueError('Concession support effects must be nonnegative LAB values')
    if set(s.drama.concessions) != set(s.levers['concessions_1928'].options):
        raise ValueError('Every concession needs distinct declared effects')
    if not s.drama.assurance_terms or not set(s.drama.assurance_terms) <= set(s.drama.concessions):
        raise ValueError('Assurance terms must name supported concessions')
    if set(s.drama.rules.belief_thresholds) != {'legislature', 'government'}:
        raise ValueError('Disclosure belief rules require the two declared recipients')
    for number in s.drama.rules.model_dump().values():
        values = number.values() if 'value' not in number else [number]
        if any(not 0 <= v['value'] <= 1 for v in values):
            raise ValueError('Relationship thresholds/weights must be between zero and one')
    metric_ids = [m.id for m in s.metric_catalog]
    required = {m.id for m in s.measures} | {'payment_gap_musd', 'reserve_shortfall_musd',
        'credit_committed_musd', 'consent_month', 'indemnity_month', 'assurance_status',
        'disclosure_month', 'treasury_cash_musd'}
    if len(metric_ids) != len(set(metric_ids)) or set(metric_ids) != required:
        raise ValueError('Metric catalog must define each supported measure and explicit unavailable cash')
    if any(m.owner_role not in roles for m in s.metric_catalog):
        raise ValueError('A metric needs an explicit registered owner')
