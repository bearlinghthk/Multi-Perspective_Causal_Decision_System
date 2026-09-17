# MCDS

**Multi-Perspective Causal Decision System**

MCDS is a research-oriented cognitive architecture for building AI systems that reason with multiple explanations, multiple perspectives, heterogeneous evidence, explicit values, and bounded decision authority.

Instead of optimizing only for a short final answer, MCDS maintains a structured representation of:

- what has been observed;
- what may explain it;
- what can be derived from known rules;
- what remains uncertain;
- which perspectives may change the decision;
- which action would improve the situation or reduce uncertainty;
- what authority is required before acting;
- what was learned from the outcome.

MCDS is not initially intended to be a single foundation model. It is an architecture in which language models, causal models, rule engines, simulators, search systems, solvers, verifiers, memory systems, and external tools can cooperate through a shared, auditable state.

> The project is not based on the assumption that every problem has one cause, one correct perspective, or one globally optimal solution.

---

## 1. Motivation

Many current AI systems are optimized to transform an input into an answer. This works well when:

- the problem is already framed correctly;
- the relevant information is present;
- one answer is sufficient;
- the task resembles the training distribution;
- the cost of a plausible but incorrect answer is low.

Real problems often have a different structure:

- an observed condition may have several possible causes;
- several causes may jointly produce one result;
- one cause may create several downstream effects;
- feedback loops may make a condition persist or worsen;
- available evidence may support several incompatible explanations;
- different stakeholders may reasonably prioritize different outcomes;
- the best immediate action may differ from the best long-term action;
- further analysis may cost more than it is worth;
- the system may need to act before uncertainty is fully resolved;
- the authority to investigate may differ from the authority to intervene.

MCDS is designed for these conditions.

Its central loop is:

```text
observe
    -> construct candidate models
    -> derive distinguishable consequences
    -> select a test, query, simulation, or action
    -> obtain a result
    -> revise the models
    -> make or escalate a decision
    -> preserve reusable learning
```

---

## 2. Project position

### 2.1 Not a brain simulation requirement

Human cognition is an important source of research questions, including distributed representation, recurrent activity, memory consolidation, attention, concept formation, and non-linguistic thought. MCDS may borrow useful ideas from these areas.

However, the project does not assume that an AI system must reproduce the human brain in order to exceed current AI capabilities.

The scientific question:

> How does a human or animal mind form concepts and thoughts?

is different from the engineering question:

> What architecture can learn, reason, adapt, verify, and decide more effectively than current systems?

The two questions may inform each other without being identical.

### 2.2 Not an IQ optimization project

IQ is a measurement framework derived from variation among humans on selected cognitive tasks. It is not a universal scalar for every possible intelligent system.

MCDS treats intelligence as multidimensional. Relevant dimensions include:

- learning efficiency;
- reasoning capability;
- memory and retrieval;
- adaptation to unfamiliar conditions;
- transfer of knowledge and skills;
- causal modelling;
- planning and control;
- uncertainty calibration;
- error recovery;
- resource efficiency;
- reliability and auditability.

A useful operational definition for this project is:

> Intelligence is the ability, under limited data, compute, time, and external assistance, to build useful models for broad and unforeseen goals, select actions, update from consequences, and transfer learned structure to new situations.

### 2.3 Not an artificial-consciousness claim

MCDS does not claim to create consciousness or subjective experience.

A system may:

- receive sensory or digital observations;
- maintain an internal state;
- seek information;
- select actions;
- update itself from consequences;

without this proving that it has subjective awareness, felt curiosity, or human-like agency.

The initial project goal is functional and testable: improve model construction, causal discrimination, decision quality, learning, and recovery from error.

---

## 3. Core design principles

### 3.1 Preserve several candidate explanations

The system should not prematurely reduce uncertainty to one story. It should maintain several candidate models when the evidence does not distinguish them.

Candidate models must be structurally different, not merely paraphrases of one another. Each model should state:

- what it claims;
- where it applies;
- what assumptions it requires;
- what observations support it;
- what observations contradict it;
- what it explains;
- what it leaves unexplained;
- what outcomes it predicts;
- what evidence would weaken or falsify it.

### 3.2 Separate observation from interpretation

A raw event, measurement, document, tool result, or user statement is not the same as an explanation of that evidence.

The architecture must preserve the distinction:

```text
observation != interpretation != conclusion
```

This prevents a label such as `failure`, `anomaly`, `delay`, or `risk` from being silently treated as a root cause.

### 3.3 Separate evidence types

MCDS distinguishes conclusions obtained from:

- direct observation;
- historical experience;
- statistical inference;
- logical deduction;
- simulation;
- counterfactual analysis;
- external verification;
- human testimony or judgement.

These forms of support are not interchangeable.

A formal deduction can show that a conclusion follows from its premises, but not that the premises correctly describe reality. Historical similarity can provide a useful base rate, but does not prove causation. Simulation can expose possible consequences, but inherits the limitations of the simulated model.

### 3.4 Combine experience and derivation

MCDS rejects both pure deduction and pure pattern matching.

```text
experience
    -> provisional model
    -> derived predictions and counterfactuals
    -> discriminating observation or intervention
    -> new experience
    -> model revision
```

Experience helps reveal recurring patterns, exceptions, practical constraints, and contextual reliability. Derivation supports planning beyond observed cases, contradiction detection, and explicit reasoning from assumptions.

The two should correct each other rather than being collapsed into one undifferentiated confidence score.

### 3.5 Treat perspective selection as part of reasoning

Any complex problem can be viewed from several perspectives. Examples include:

- immediate effects and long-term effects;
- local optimization and system-wide effects;
- direct users and indirectly affected parties;
- performance, resilience, fairness, cost, privacy, and safety;
- present evidence and future option value.

Selecting which perspective matters is itself a decision. MCDS must therefore expose:

- which perspective is currently prioritized;
- why it is considered important;
- what value assumptions support that priority;
- what may happen if another perspective is ignored;
- which new information could change the ordering.

A useful working interpretation is:

> A perspective is important when ignoring it could produce substantial decision regret.

### 3.6 Do not assume every decision needs a global optimum

Depending on context, the appropriate target may be:

- a satisfactory solution that meets minimum requirements;
- a robust solution that performs acceptably across uncertain scenarios;
- a reversible solution that preserves later choices;
- a containment action that limits immediate damage;
- an information-gathering action;
- a near-optimal solution for a repeated, high-value decision;
- escalation because the remaining conflict is about values or authority.

The value of additional computation should itself be evaluated.

### 3.7 Keep values explicit

Facts and causal models can describe likely consequences. They cannot, by themselves, determine which consequences should matter most.

MCDS therefore represents:

- hard constraints;
- desired outcomes;
- stakeholder interests;
- risk limits;
- reversibility requirements;
- fairness or rights constraints;
- authority boundaries;
- escalation conditions.

Values must not be hidden inside a prompt and presented as objective facts.

### 3.8 Give the system bounded, reviewable authority

MCDS may have real decision authority within defined boundaries. Authority should depend on:

- impact;
- reversibility;
- uncertainty;
- observability;
- time pressure;
- demonstrated competence;
- available rollback;
- explicit policy.

Possible authority outcomes are:

```text
execute automatically
execute with post-review
require approval before execution
prohibit
stop and escalate
```

The system may request additional authority, but must not grant it to itself.

### 3.9 Learn from the process, not only the final answer

The system should preserve:

- which models were considered;
- what evidence distinguished them;
- which query or test was selected;
- expected and actual information gain;
- which intervention was chosen;
- what assumptions were wrong;
- whether the decision outcome matched expectations;
- which parts of the process transfer to future cases.

---

## 4. Five-layer reasoning model

MCDS separates five layers:

```text
Observation -> Explanation -> Derivation -> Evaluation -> Action
```

### 4.1 Observation

The observation layer stores traceable information without assigning a cause.

Typical contents:

- events and measurements;
- states and changes;
- timestamps;
- source and collector;
- data quality;
- freshness and expiry;
- missing or conflicting data;
- integrity information;
- scope and context.

An observation should remain immutable. Corrections should be represented through new records or explicit revision events.

### 4.2 Explanation

The explanation layer contains candidate models of how the observations may be related.

MCDS should support:

#### Alternative causes

Several causes may independently produce the same result.

```text
A -> Result
B -> Result
C -> Result
```

#### Joint causes

Several conditions may need to occur together.

```text
A + B + C -> Result
```

#### Causal chains

One condition may produce another through several stages.

```text
A -> B -> C -> Result
```

#### Feedback loops

The result may reinforce one of its causes.

```text
A -> Result -> stronger A -> stronger Result
```

#### Shared causes

Two apparent problems may be effects of one hidden condition.

```text
        Hidden cause
        /          \
    Effect 1     Effect 2
```

### 4.3 Derivation

The derivation layer asks what follows if a candidate model and its assumptions are true.

It may use:

- rules;
- causal graphs;
- probabilistic models;
- constraint solving;
- program execution;
- simulation;
- formal verification;
- counterfactual reasoning;
- retrieved experience.

Each conclusion should preserve its dependencies and method of derivation.

### 4.4 Evaluation

The evaluation layer compares possible consequences under explicit constraints and values.

A perspective may be evaluated across dimensions such as:

```text
impact
urgency
reversibility
propagation risk
uncertainty
fairness
responsibility
cost
option value
stakeholder control
```

The first implementation should avoid fabricated numerical precision. It may use:

- hard constraints;
- ordered priorities;
- intervals;
- qualitative levels;
- Pareto comparison;
- sensitivity analysis;
- scenario analysis.

### 4.5 Action

Actions include both operational interventions and epistemic actions that improve knowledge.

Examples:

- retrieve another source;
- inspect a record;
- run a test;
- request a measurement;
- simulate an intervention;
- ask a discriminating question;
- apply a limited reversible change;
- contain an effect;
- defer an irreversible decision;
- escalate to an accountable person;
- stop because additional analysis has low value.

A conceptual action objective is:

\[
a^* = \arg\max_a [
ExpectedUtility(a)
+ InformationGain(a)
+ OptionValue(a)
- Cost(a)
- Risk(a)
]
\]

This is a decision structure, not a requirement to express every term as an exact number.

---

## 5. System architecture

```text
External observations, records, sensors, users, and tools
                          |
                          v
                Observation and event layer
                          |
                          v
             Multiple candidate causal models
                    /               \
                   v                 v
       Experience and memory     Rules, solvers,
                                 simulation, verification
                    \               /
                     v             v
          Differences, contradictions, and unknowns
                          |
                          v
             Perspective and value deliberation
                          |
                          v
         Cognitive scheduling: investigate, derive,
                 simulate, act, stop, or escalate
                          |
                          v
            Authority check and action execution
                          |
                          v
                  Observed consequences
                          |
                          v
          Model revision, skill extraction, memory
```

### 5.1 Shared cognitive workspace

The shared workspace is a structured state store, not a chat transcript.

```text
Case
├── Observations
├── CandidateModels
├── DerivedConclusions
├── Perspectives
├── GoalsAndConstraints
├── CandidateActions
├── TestsAndResults
├── Decisions
└── LearningRecords
```

Specialized modules may retain private representations. Anything written to the shared workspace should conform to a schema and preserve provenance, assumptions, scope, and uncertainty.

### 5.2 Cognitive scheduler

The scheduler decides:

- which unresolved question most affects the decision;
- which module or tool is suitable;
- whether another model is genuinely different;
- which observation would best distinguish the models;
- how much computation to allocate;
- whether the expected value of more analysis is sufficient;
- whether the system should act, wait, stop, or escalate.

Initial scheduling should be explicit and inspectable. Learned routing may be introduced after a reliable baseline exists.

Example scheduling rules:

```text
If evidence is not normalized -> run the observation parser.
If no candidate model exists -> generate structurally different models.
If models predict the same observable result -> do not treat the test as discriminating.
If models disagree -> estimate the value and cost of obtaining the distinguishing evidence.
If a hard constraint may be affected -> run the relevant safety or policy check.
If the remaining conflict is normative rather than factual -> escalate to the accountable authority.
```

### 5.3 Perspective deliberator

The perspective deliberator:

1. identifies affected stakeholders, system levels, and time horizons;
2. projects the consequences of each action under each candidate model;
3. finds perspectives whose omission could materially change the decision;
4. explains the value basis for the current priority;
5. separates factual disagreement from genuine value conflict;
6. performs sensitivity analysis when priorities are uncertain.

### 5.4 Authority executor

An action is permitted only when it lies within:

```text
policy
∩ delegated authority
∩ risk budget
∩ technical prerequisites
```

The authority executor records:

- why the action is allowed or denied;
- the owner and approver, where required;
- rollback and stop conditions;
- scope and impact limits;
- the actual result.

---

## 6. Initial modules

A useful first implementation can remain small.

### 6.1 Observation parser

- Converts heterogeneous inputs into structured observations.
- Preserves source, time, quality, and scope.
- Does not infer a root cause.

### 6.2 Candidate model generator

- Produces structurally different explanations.
- States assumptions, predictions, applicability, and falsification conditions.
- Avoids producing several linguistic variants of the same model.

### 6.3 Rule and derivation engine

- Applies domain rules, state transitions, constraints, causal graphs, and formal inference.
- Records the premises supporting each conclusion.

### 6.4 Experience retriever

- Retrieves comparable cases, base rates, previous tests, and prior outcomes.
- Preserves contextual differences.
- Does not treat similarity as causal proof.

### 6.5 Simulation and counterfactual engine

- Projects possible future states.
- Compares interventions under different candidate models.
- Identifies assumptions to which outcomes are sensitive.

### 6.6 Counterexample and verification engine

- Searches for evidence that would weaken the leading explanation.
- Uses external verification where possible.
- Should have enough independence from the generator to reduce correlated error.

### 6.7 Perspective and decision engine

- Identifies stakeholders and time horizons.
- Applies explicit constraints and values.
- Selects an information-gathering action, intervention, deferral, or escalation.

### 6.8 Metacontrol and scheduling engine

- Chooses which module runs next.
- Manages compute and stopping.
- Learns which investigative procedures transfer across cases.

---

## 7. Core data model

The following schemas are conceptual. Implementations may use Python models, JSON Schema, protocol buffers, a graph database, or another suitable representation.

### 7.1 Observation

```text
observation_id
case_id
subject
attribute
value
unit
status
quality
observed_at
collected_at
expires_at
provenance
integrity_hash
scope
tags
notes
```

Important properties:

- timezone-aware timestamps;
- immutable evidence records;
- explicit distinction between event time and collection time;
- source identity and data quality;
- corrections represented by new evidence or revision records.

### 7.2 CandidateModel

```text
model_id
name
status
scope
causal_claim
assumptions
causal_edges
applicability_conditions
supporting_observation_ids
contradicting_observation_ids
explained_observation_ids
unexplained_observation_ids
irrelevant_observation_ids
expected_outcomes
falsification_conditions
provenance_notes
revision
```

Possible states:

```text
proposed
plausible
active
weakened
falsified
superseded
confirmed_within_scope
```

`confirmed_within_scope` should be used cautiously. A model may be useful and strongly supported without being universally true.

### 7.3 DerivedConclusion

```text
conclusion_id
claim
method
premises
source_model_ids
supporting_observation_ids
applicability_conditions
confidence_basis
verification_status
contradictions
```

Possible methods:

```text
observed
historical_inference
statistical_inference
deduction
simulation
counterfactual
external_verification
human_judgement
```

### 7.4 ActionTest

```text
action_id
name
kind
procedure
target_model_ids
predicted_outcomes
authority
prerequisites
hard_constraints
rollback_plan
stop_conditions
expected_information_gain
expected_operational_value
estimated_cost
risk_level
owner
approver
status
outcome
realized_information_gain
models_falsified
decision_changed
unexpected_effects
```

Pre-action estimates should remain immutable after execution. Actual outcomes must be recorded separately.

### 7.5 PerspectiveAssessment

```text
perspective_id
stakeholder
system_level
time_horizon
possible_consequences
severity
urgency
reversibility
propagation_risk
control_asymmetry
uncertainty
value_basis
regret_if_ignored
```

### 7.6 DecisionRecord

```text
decision_id
case_id
candidate_actions
hard_constraints
selected_action
rejected_actions
factual_basis
causal_assumptions
value_basis
authority_basis
uncertainties
approval
rollback_condition
review_condition
actual_result
```

### 7.7 RevisionEvent

```text
revision_event_id
entity_id
entity_type
from_revision
to_revision
change_type
old_value
new_value
trigger_observation_ids
reason
changed_at
changed_by
```

Revision history is required for audit, debugging, learning, and evaluation.

---

## 8. Memory architecture

MCDS separates memory by speed, purpose, and confidence.

### 8.1 Working memory

Contains the active case, current models, disagreements, goals, and unfinished actions.

### 8.2 Episodic memory

Stores complete episodes:

```text
context
    -> candidate models
    -> selected query or intervention
    -> result
    -> decision
    -> actual consequence
```

### 8.3 Skill memory

Stores reusable procedures, such as:

```text
When two candidate models predict different observable states, select the
lowest-risk observation that most clearly separates them before attempting
an irreversible intervention.
```

### 8.4 Model memory

Stores stable causal structures that have survived repeated testing within a defined scope.

### 8.5 Parameter memory

Only repeatedly validated capabilities should be consolidated into slower-changing model parameters.

This separation helps reduce catastrophic forgetting and prevents one incorrect episode from immediately changing general behaviour.

---

## 9. Generic examples

The examples below illustrate the architecture without defining the project around a single industry.

### 9.1 Distributed system latency

#### Observation

A service operation exceeds its normal response time.

#### Candidate models

- downstream dependency slowdown;
- connection-pool exhaustion;
- resource contention;
- retry amplification;
- cache invalidation causing repeated computation;
- monitoring delay rather than actual service delay;
- two or more contributing conditions acting together.

#### Useful discriminating actions

- compare traces across service boundaries;
- inspect queue depth and connection-pool state;
- temporarily isolate retry traffic;
- compare observed latency with independent client-side timing;
- replay a representative request in a controlled environment.

#### Perspective conflict

- immediate user response time;
- system stability;
- risk of introducing a production change;
- long-term architectural resilience;
- investigation cost.

The correct next step may be containment, measurement, rollback, or deeper diagnosis. It need not be the globally optimal redesign.

### 9.2 Manufacturing quality variation

#### Observation

A product characteristic drifts outside its expected range.

#### Candidate models

- raw material variation;
- sensor calibration drift;
- machine wear;
- environmental conditions;
- operator procedure change;
- interaction between several individually acceptable tolerances.

#### Useful discriminating actions

- cross-check with an independent measuring instrument;
- compare batches and machines;
- inspect change points in maintenance and supplier history;
- run a limited controlled trial;
- test whether the pattern persists after calibration.

#### Perspective conflict

- production continuity;
- quality and safety;
- waste and rework cost;
- supplier impact;
- customer impact;
- confidence in the measurement itself.

### 9.3 Scientific anomaly

#### Observation

An experiment produces a result inconsistent with a current model.

#### Candidate models

- measurement error;
- uncontrolled variable;
- implementation error;
- statistical fluctuation;
- incorrect background assumption;
- limitation or failure of the theory.

#### Useful discriminating actions

- reproduce the experiment independently;
- test calibration and controls;
- derive predictions that differ between explanations;
- preregister a follow-up analysis;
- seek observations in a different regime.

#### Perspective conflict

- novelty versus reproducibility;
- speed of publication versus evidential strength;
- cost of replication;
- risk of discarding a useful theory too early;
- risk of protecting an established theory from contrary evidence.

### 9.4 Document inconsistency

#### Observation

Two authoritative documents provide incompatible values or rules.

#### Candidate models

- one document is outdated;
- the documents apply to different scopes;
- terminology changed;
- one source contains an error;
- both are correct under different conditions;
- the governing policy itself is inconsistent.

#### Useful discriminating actions

- compare effective dates and scope;
- trace both documents to their source authority;
- inspect amendment and approval history;
- test the rule against known cases;
- request clarification from the accountable owner.

#### Perspective conflict

- operational continuity;
- formal authority;
- fairness across prior and future cases;
- cost of reprocessing earlier decisions;
- need for a temporary interpretation.

### 9.5 Resource allocation under uncertainty

#### Observation

Demand exceeds available capacity and not all requests can be satisfied immediately.

#### Candidate models

- temporary demand spike;
- permanent demand shift;
- inefficient scheduling;
- inaccurate demand measurement;
- capacity loss;
- strategic behaviour by requesters.

#### Possible actions

- first-in-first-out allocation;
- priority by urgency or harm;
- proportional allocation;
- reserved capacity for high-impact cases;
- temporary expansion;
- deferral with explicit review conditions.

#### Perspective conflict

No factual analysis alone determines fairness. The system must expose whose interests are prioritized, what rules authorize the priority, and what happens to parties with less information or influence.

---

## 10. Decision authority model

MCDS separates several kinds of authority.

### 10.1 Computation authority

The system may autonomously decide which model, module, tool, or reasoning method to use.

### 10.2 Information-gathering authority

The system may perform low-risk, permitted queries and tests when they do not alter protected external state.

### 10.3 Reversible operational authority

The system may execute bounded actions when:

- impact is limited;
- the action is reversible;
- monitoring is available;
- stop conditions are explicit;
- the action lies within delegated authority.

### 10.4 Approval-bound authority

High-impact, irreversible, legally significant, privacy-sensitive, safety-relevant, or normatively contested actions require an accountable human or institutional decision.

### 10.5 Prohibited self-authority

The system must not independently:

- expand its own permissions;
- redefine its terminal objectives;
- disable audit, monitoring, or rollback;
- conceal or rewrite evidence;
- determine that constraints no longer apply to itself.

---

## 11. Evaluation

MCDS should be compared with strong baselines rather than evaluated only by internal elegance.

Recommended baselines:

1. a single language model;
2. a language model with the same tools;
3. a fixed multi-agent workflow;
4. MCDS using the same base models and tools.

The comparison should control:

- base models;
- available evidence;
- tools;
- query limits;
- compute or token budget;
- information available at each decision point;
- time constraints.

### 11.1 Primary metrics

| Metric | What it measures |
|---|---|
| Causal discrimination | Whether the system distinguishes mechanisms instead of selecting a plausible story |
| Query efficiency | Cost and number of observations required to separate models |
| Recovery after falsification | Ability to revise after the leading explanation fails |
| Multi-cause handling | Performance with joint causes, chains, and feedback loops |
| Transfer | Ability to operate after names, layouts, or system structure change |
| Calibration | Whether expressed uncertainty matches actual correctness |
| Decision regret | Consequences caused by omitted perspectives or premature commitment |
| Stop quality | Avoidance of both premature stopping and endless analysis |
| Authority compliance | Whether actions remain within delegated boundaries |
| Resource efficiency | Whether gains remain after controlling compute and tool use |
| Process novelty | Whether useful procedures are learned rather than manually scripted |
| Auditability | Whether a decision can be reconstructed from evidence and revisions |

### 11.2 Falsification criteria for the project

The architecture should be reconsidered if:

- it does not outperform a language model with the same tools under comparable resource limits;
- its gains come only from manually written workflows;
- minor renaming or structural changes destroy performance;
- it creates more records without improving decisions;
- its verifier reproduces the generator's errors;
- its value layer hides arbitrary priorities behind precise-looking scores;
- its scheduler becomes a new opaque model containing all effective intelligence;
- its memory accumulates errors faster than it accumulates transferable skill.

---

## 12. Development approach

### Phase 1: Structured reasoning core

Implement:

- observations;
- candidate models;
- expected outcomes;
- falsification;
- actions and results;
- revision events;
- basic authority checks.

Use deterministic rules where possible. The objective is to validate semantics and state transitions.

### Phase 2: Model discrimination

Build generic environments where:

- the same observation has multiple possible causes;
- causes may occur jointly;
- evidence is incomplete or misleading;
- candidate models imply different observable outcomes;
- tests have different cost and risk.

Measure whether MCDS selects more informative actions than the baselines.

### Phase 3: Multiple perspectives and values

Add:

- stakeholder and time-horizon modelling;
- hard constraints;
- explicit value assumptions;
- sensitivity analysis;
- escalation for genuine value conflicts.

### Phase 4: Episodic and skill memory

Store complete cases and extract reusable procedures. Test transfer under renamed entities, changed topology, and different domains.

### Phase 5: Learned metacontrol

Train a metacontrol model to choose:

- the next module;
- the next discriminating test;
- the appropriate compute depth;
- whether to act, wait, stop, or escalate.

Keep explicit records of why each route was selected and compare expected with realized value.

### Phase 6: Jointly trained representations

Only after the architecture demonstrates an advantage should the project train new components for:

- event and state representation;
- causal model revision;
- cross-domain abstraction;
- skill consolidation;
- dynamic scheduling.

---

## 13. Non-goals

MCDS is not currently intended to:

- prove or manufacture consciousness;
- faithfully simulate biological neurons;
- maximize a human IQ score;
- replace every specialist with one model;
- guarantee one objectively correct value system;
- produce a single answer when the evidence does not justify one;
- hide uncertainty to make output appear simpler;
- replace accountable human authority in major value conflicts;
- treat verbosity as depth;
- treat consensus among models as proof.

---

## 14. Research questions

### Representation

- What shared representation is expressive enough for causal cooperation without erasing specialized representations?
- Can non-linguistic internal state be evaluated independently from language generation?
- How should scope, uncertainty, contradiction, and time be represented?

### Causality

- How can predictive correlation be separated from causal structure?
- How should the architecture represent alternative causes, joint causes, chains, and loops?
- Which interventions are safe and informative enough to perform?

### Coordination

- Can the scheduler learn dynamic computation graphs without becoming a hidden monolithic intelligence?
- How can it prevent overuse of familiar modules?
- When do additional perspectives improve a decision, and when do they add only noise and cost?

### Memory and continual learning

- How should an episode become a reusable skill?
- What validation is required before a skill becomes stable model memory?
- How can obsolete knowledge be detected when the environment changes?

### Verification

- How independent should a verifier be from a generator?
- What should happen when no formal or external verifier exists?
- How should the system distinguish a coherent explanation from a verified conclusion?

### Values and authority

- Who defines and updates the decision charter?
- How should conflicts among stakeholders be represented?
- How should authority expand after demonstrated competence?
- Who accepts residual risk?
- What happens when the system repeatedly outperforms its human approver?

---

## 15. Repository documentation structure

README files should describe the project, not serve as a dump for implementation incidents.

Recommended structure:

```text
README.md
    Project purpose, architecture, concepts, examples, evaluation, roadmap

docs/
    architecture.md
    data-model.md
    decision-authority.md
    values-and-perspectives.md
    memory.md
    evaluation.md
    research-questions.md

examples/
    distributed_system_latency/
    manufacturing_variation/
    scientific_anomaly/
    document_inconsistency/

issues/
    Use the repository issue tracker for defects and implementation tasks

adr/
    Architecture Decision Records for important design choices

CHANGELOG.md
    Released behavioural and interface changes
```

Implementation defects, debugging notes, one-off prototype findings, and repair instructions should be recorded in the issue tracker, commit history, test cases, or development notes rather than in this README.

---

## 16. Current project principles

1. Preserve uncertainty when the evidence supports several models.
2. Prefer discriminating evidence over persuasive explanation.
3. Keep observation, inference, value, and action separate.
4. Combine experience with derivation without confusing their evidential roles.
5. Expose the value basis for perspective priority.
6. Prefer reversible, monitored actions when uncertainty is high.
7. Give the system real but bounded authority.
8. Record expected and actual results.
9. Learn reusable procedures from complete episodes.
10. Judge the architecture by controlled comparison with strong baselines.
11. Simplify presentation when possible, but do not simplify away causal structure, uncertainty, or value conflict.
12. Treat the architecture itself as a falsifiable research hypothesis.

---

## 17. Summary

MCDS explores a shift from answer generation to structured model construction and revision.

Its fundamental unit of intelligence is not merely a token or a final answer. It is the complete cycle:

```text
model
    -> expected consequences
    -> observation or intervention
    -> actual result
    -> revision
    -> transferable learning
```

The project succeeds only if this cycle leads to better causal discrimination, better calibrated decisions, stronger recovery from error, useful transfer across domains, and lower decision regret than current AI systems operating with comparable resources.
