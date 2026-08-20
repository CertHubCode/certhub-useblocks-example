"""Domain tests for the SaMD Sterilisator 20A."""

from __future__ import annotations

import pytest

from sterilisator_20a.constants import (
    MAX_CYCLE_MINUTES,
    TARGET_TEMPERATURE_C,
    TEMPERATURE_TOLERANCE_C,
    CycleState,
    SterilizerError,
)
from sterilisator_20a.cycle.controller import (
    cycle_within_time_budget,
    reported_cycle_duration_minutes,
    start_cycle,
    temperature_within_range,
)
from sterilisator_20a.safety.door import (
    door_may_open,
    door_must_lock,
    may_start_cycle,
)
from sterilisator_20a.ui.messages import (
    ui_labels_are_english,
    ui_messages,
    ui_messages_for_state,
)


# @need-ids: VERIF_001
@pytest.mark.certhub_test("VERIF_001")
def test_sterilization_temperature_accuracy() -> None:
    assert temperature_within_range(TARGET_TEMPERATURE_C) is True
    assert temperature_within_range(
        TARGET_TEMPERATURE_C - TEMPERATURE_TOLERANCE_C
    )
    assert temperature_within_range(
        TARGET_TEMPERATURE_C + TEMPERATURE_TOLERANCE_C
    )
    assert temperature_within_range(
        TARGET_TEMPERATURE_C - TEMPERATURE_TOLERANCE_C - 0.1
    ) is False
    assert temperature_within_range(
        TARGET_TEMPERATURE_C + TEMPERATURE_TOLERANCE_C + 0.1
    ) is False
    result = start_cycle(
        door_closed=True,
        peak_temperature_c=121.0,
        duration_minutes=45.0,
    )
    assert result.temperature_ok is True
    # State may be COMPLETE or FAULT if duration is broken (make break); temp is independent.
    assert result.state in (CycleState.COMPLETE, CycleState.FAULT)


# @need-ids: VERIF_002
@pytest.mark.certhub_test("VERIF_002")
def test_sterilization_cycle_time() -> None:
    assert cycle_within_time_budget(0.0) is True
    assert cycle_within_time_budget(45.0) is True
    assert cycle_within_time_budget(60.0) is True
    reported = reported_cycle_duration_minutes(45.0)
    assert reported <= MAX_CYCLE_MINUTES
    assert cycle_within_time_budget(reported) is True
    result = start_cycle(
        door_closed=True,
        peak_temperature_c=121.0,
        duration_minutes=50.0,
    )
    assert result.duration_ok is True
    assert result.state is CycleState.COMPLETE
    with pytest.raises(SterilizerError):
        reported_cycle_duration_minutes(-1.0)


# @need-ids: VERIF_003
@pytest.mark.certhub_test("VERIF_003")
def test_door_interlock() -> None:
    assert may_start_cycle(door_closed=True) is True
    assert may_start_cycle(door_closed=False) is False
    with pytest.raises(SterilizerError, match="door is open"):
        start_cycle(
            door_closed=False,
            peak_temperature_c=121.0,
            duration_minutes=45.0,
        )

    assert door_must_lock(CycleState.RUNNING) is True
    assert door_may_open(CycleState.RUNNING) is False
    for state in (CycleState.IDLE, CycleState.COMPLETE, CycleState.FAULT):
        assert door_must_lock(state) is False
        assert door_may_open(state) is True

    ok = start_cycle(
        door_closed=True,
        peak_temperature_c=121.0,
        duration_minutes=45.0,
    )
    assert ok.state is not CycleState.RUNNING
    assert ok.door_locked is False
    assert door_may_open(ok.state) is True

    fault = start_cycle(
        door_closed=True,
        peak_temperature_c=130.0,
        duration_minutes=45.0,
    )
    assert fault.state is CycleState.FAULT
    assert fault.door_locked is False
    assert door_may_open(fault.state) is True


# @need-ids: VERIF_004
@pytest.mark.certhub_test("VERIF_004")
def test_user_interface_labeling() -> None:
    catalog = ui_messages()
    assert ui_labels_are_english(catalog) is True
    for state in CycleState:
        payload = ui_messages_for_state(state)
        assert payload["language"] == "en"
        assert payload["state"] == state.value
        assert payload["cycle_status"]
        assert payload["alert_door"]
    running = ui_messages_for_state(CycleState.RUNNING)
    assert "locked" in running["alert_door"].lower()
    assert ui_labels_are_english(
        {
            "language": "de",
            "state": "running",
            "cycle_status": "Zyklus läuft",
            "alert_door": "Tür verriegelt",
        }
    ) is False
