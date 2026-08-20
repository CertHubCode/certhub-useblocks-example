"""Sterilisator 20A — example SaMD product under test.

Need IDs follow CertHub-synced V-Model types (SYSREQ / DOUT / VERIF).
CodeLinks markers target the Sterilizer 20A Design Output (``DOUT_018``).
"""

from sterilisator_20a.constants import (
    MAX_CYCLE_MINUTES,
    TARGET_TEMPERATURE_C,
    TEMPERATURE_TOLERANCE_C,
    UI_LANGUAGE,
    CycleState,
    SterilizerError,
)
from sterilisator_20a.cycle.controller import (
    CycleResult,
    cycle_within_time_budget,
    reported_cycle_duration_minutes,
    run_sterilization_cycle,
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

__all__ = [
    "MAX_CYCLE_MINUTES",
    "TARGET_TEMPERATURE_C",
    "TEMPERATURE_TOLERANCE_C",
    "UI_LANGUAGE",
    "CycleResult",
    "CycleState",
    "SterilizerError",
    "cycle_within_time_budget",
    "door_may_open",
    "door_must_lock",
    "may_start_cycle",
    "reported_cycle_duration_minutes",
    "run_sterilization_cycle",
    "start_cycle",
    "temperature_within_range",
    "ui_labels_are_english",
    "ui_messages",
    "ui_messages_for_state",
]
