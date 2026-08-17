"""Domain tests for the SaMD Sterilisator 20A."""

from __future__ import annotations

import pytest

from sterilisator_20a.constants import (
    MAX_CYCLE_MINUTES,
    TARGET_TEMPERATURE_C,
    TEMPERATURE_TOLERANCE_C,
    SterilizerError,
)
from sterilisator_20a.cycle.controller import (
    cycle_within_time_budget,
    reported_cycle_duration_minutes,
    run_sterilization_cycle,
    temperature_within_range,
)
from sterilisator_20a.enclosure.footprint import DimensionsCm, device_dimensions_cm, footprint_within_limits
from sterilisator_20a.ui.messages import ui_labels_are_english, ui_messages


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
    result = run_sterilization_cycle(
        peak_temperature_c=121.0,
        duration_minutes=45.0,
    )
    assert result.temperature_ok is True


# @need-ids: VERIF_002
@pytest.mark.certhub_test("VERIF_002")
def test_sterilization_cycle_time() -> None:
    assert cycle_within_time_budget(0.0) is True
    assert cycle_within_time_budget(45.0) is True
    assert cycle_within_time_budget(60.0) is True
    reported = reported_cycle_duration_minutes(45.0)
    assert reported <= MAX_CYCLE_MINUTES
    assert cycle_within_time_budget(reported) is True
    result = run_sterilization_cycle(
        peak_temperature_c=121.0,
        duration_minutes=50.0,
    )
    assert result.duration_ok is True
    with pytest.raises(SterilizerError):
        reported_cycle_duration_minutes(-1.0)


# @need-ids: VERIF_003
@pytest.mark.certhub_test("VERIF_003")
def test_user_interface_labeling() -> None:
    messages = ui_messages()
    assert messages["language"] == "en"
    assert ui_labels_are_english(messages) is True
    assert ui_labels_are_english(
        {
            "language": "de",
            "cycle_status": "Zyklus läuft",
            "alert_door": "Tür verriegelt",
            "alert_complete": "Sterilisation abgeschlossen",
        }
    ) is False


# @need-ids: VERIF_004
@pytest.mark.certhub_test("VERIF_004")
def test_device_footprint() -> None:
    dims = device_dimensions_cm()
    assert footprint_within_limits(dims) is True
    assert footprint_within_limits(
        DimensionsCm(width=50.0, depth=40.0, height=35.0)
    )
    assert footprint_within_limits(
        DimensionsCm(width=50.1, depth=40.0, height=35.0)
    ) is False
    assert footprint_within_limits(
        DimensionsCm(width=50.0, depth=40.1, height=35.0)
    ) is False
    assert footprint_within_limits(
        DimensionsCm(width=50.0, depth=40.0, height=35.1)
    ) is False
