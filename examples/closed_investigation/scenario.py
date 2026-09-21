from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import sys

# Allow direct execution without installing the package.
# 允許未安裝 package 時直接執行 example。
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from mcds.action import ActionKind, ActionTest, ModelActionExpectation
from mcds.adapters import (
    DeterministicActionResult,
    DeterministicScenarioAdapter,
)
from mcds.evidence import Operator, Predicate
from mcds.investigation import InvestigationCycle, InvestigationState
from mcds.model import CandidateModel, ModelExpectation
from mcds.observation import (
    Observation,
    ObservationTime,
    Provenance,
    SourceKind,
)


CASE_ID = "case_closed_investigation_001"
SUBJECT = "operation:OP001"


def predicate(attribute: str, value: object) -> Predicate:
    """Build a structured equality predicate.

    建立 structured equality predicate。
    """

    return Predicate(
        subject=SUBJECT,
        attribute=attribute,
        operator=Operator.EQ,
        expected_value=value,
    )


def observation(attribute: str, value: object) -> Observation:
    """Build deterministic evidence for the example adapter.

    為 example adapter 建立 deterministic evidence。
    """

    now = datetime.now(timezone.utc)
    provenance = Provenance(
        source_kind=SourceKind.API,
        source_ref=f"deterministic:{attribute}",
        collector="closed-investigation-adapter",
        collected_at=now,
    )
    return Observation(
        case_id=CASE_ID,
        subject=SUBJECT,
        attribute=attribute,
        value=value,
        time=ObservationTime(
            occurred_at=None,
            observed_at=now,
            collected_at=now,
        ),
        provenance=provenance,
    )


def candidate_model(
    name: str,
    causal_claim: str,
    expectations: tuple[tuple[str, Predicate], ...],
) -> CandidateModel:
    """Build a candidate model with expectations across several actions.

    建立一個跨多個 actions 具有 expectations 的 candidate model。
    """

    return CandidateModel(
        case_id=CASE_ID,
        name=name,
        causal_claim=causal_claim,
        scope="Operation OP001 processing and response path",
        falsification_conditions=(
            "A directly observed result contradicts an expected predicate.",
        ),
        expectations=tuple(
            ModelExpectation(action_name, expected_predicate)
            for action_name, expected_predicate in expectations
        ),
    )


def build_state_and_adapter() -> tuple[
    InvestigationState,
    DeterministicScenarioAdapter,
]:
    """Build the complete deterministic closed-loop scenario.

    建立完整 deterministic closed-loop scenario。
    """

    processing_pending = predicate("processing_state", "pending")
    processing_completed = predicate("processing_state", "completed")
    response_not_created = predicate("response_created", False)
    response_created = predicate("response_created", True)
    response_not_delivered = predicate("response_delivered", False)
    response_delivered = predicate("response_delivered", True)

    received_not_completed = candidate_model(
        "received_not_completed",
        "The operation was received but remains pending.",
        (("query_processing_state", processing_pending),),
    )
    completed_no_response = candidate_model(
        "completed_no_response",
        "Processing completed but no response was created.",
        (
            ("query_processing_state", processing_completed),
            ("query_response_creation", response_not_created),
        ),
    )
    response_created_not_delivered = candidate_model(
        "response_created_not_delivered",
        "A response was created but was not delivered.",
        (
            ("query_processing_state", processing_completed),
            ("query_response_creation", response_created),
            ("query_response_delivery", response_not_delivered),
        ),
    )
    response_delivered_state_not_updated = candidate_model(
        "response_delivered_state_not_updated",
        "The response was delivered but downstream state was not updated.",
        (
            ("query_processing_state", processing_completed),
            ("query_response_creation", response_created),
            ("query_response_delivery", response_delivered),
        ),
    )

    models = (
        received_not_completed,
        completed_no_response,
        response_created_not_delivered,
        response_delivered_state_not_updated,
    )

    query_processing_state = ActionTest(
        name="query_processing_state",
        kind=ActionKind.READ_ONLY_QUERY,
        procedure="Read the processing state for OP001.",
        expectations=tuple(
            ModelActionExpectation(
                model.model_id,
                tuple(
                    expectation.predicate
                    for expectation in model.expectations
                    if expectation.action_name == "query_processing_state"
                ),
            )
            for model in models
        ),
        hard_constraints=("Read-only query",),
    )
    query_response_creation = ActionTest(
        name="query_response_creation",
        kind=ActionKind.READ_ONLY_QUERY,
        procedure="Read whether a response was created for OP001.",
        expectations=tuple(
            ModelActionExpectation(
                model.model_id,
                tuple(
                    expectation.predicate
                    for expectation in model.expectations
                    if expectation.action_name == "query_response_creation"
                ),
            )
            for model in models
            if any(
                expectation.action_name == "query_response_creation"
                for expectation in model.expectations
            )
        ),
        prerequisites=frozenset({"processing_completed_known"}),
        hard_constraints=("Read-only query",),
    )
    query_response_delivery = ActionTest(
        name="query_response_delivery",
        kind=ActionKind.READ_ONLY_QUERY,
        procedure="Read whether the response was delivered for OP001.",
        expectations=tuple(
            ModelActionExpectation(
                model.model_id,
                tuple(
                    expectation.predicate
                    for expectation in model.expectations
                    if expectation.action_name == "query_response_delivery"
                ),
            )
            for model in models
            if any(
                expectation.action_name == "query_response_delivery"
                for expectation in model.expectations
            )
        ),
        prerequisites=frozenset({"response_created_known"}),
        hard_constraints=("Read-only query",),
    )

    state = InvestigationState(
        case_id=CASE_ID,
        models=models,
        actions=(
            query_processing_state,
            query_response_creation,
            query_response_delivery,
        ),
    )

    adapter = DeterministicScenarioAdapter(
        (
            DeterministicActionResult(
                action_name="query_processing_state",
                observations=(
                    observation("processing_state", "completed"),
                ),
                summary_en="Processing state is completed.",
                summary_zh_hk="Processing state 為 completed。",
            ),
            DeterministicActionResult(
                action_name="query_response_creation",
                observations=(observation("response_created", True),),
                summary_en="A response was created.",
                summary_zh_hk="已建立 response。",
            ),
            DeterministicActionResult(
                action_name="query_response_delivery",
                observations=(observation("response_delivered", False),),
                summary_en="The response was not delivered.",
                summary_zh_hk="Response 未送達。",
            ),
        )
    )
    return state, adapter


def main() -> None:
    """Run the complete deterministic investigation.

    執行完整 deterministic investigation。
    """

    initial_state, adapter = build_state_and_adapter()
    result = InvestigationCycle(adapter).run(
        initial_state,
        max_cycles=5,
    )

    print("Closed investigation / Closed investigation")
    print("Executed actions / 已執行 actions:")
    for index, action_name in enumerate(adapter.execution_order, start=1):
        print(f"  {index}. {action_name}")

    print()
    print("Final active models / 最後 active models:")
    for model in result.final_state.active_models:
        print(f"  - {model.name}: {model.status.value}")

    print()
    print(
        "Stop reason / 停止原因:",
        result.final_stop_decision.reason.value,
    )
    print("Cycles / Cycles:", result.final_state.cycle_number)
    print("Revision events / Revision events:", len(result.final_state.revision_events))
    print("Cycle events / Cycle events:", len(result.final_state.cycle_events))


if __name__ == "__main__":
    main()
