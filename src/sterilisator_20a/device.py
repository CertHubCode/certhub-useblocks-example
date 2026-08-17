"""Sterilisator 20A — example SaMD product under test.

Need IDs follow CertHub-synced V-Model types (SYSREQ / DOUT / VERIF).
CodeLinks markers target the Sterilizer 20A Design Output (``DOUT_018``).
"""

from sterilisator_20a.constants import (
    MAX_CYCLE_MINUTES,
    MAX_DEPTH_CM,
    MAX_HEIGHT_CM,
    MAX_WIDTH_CM,
    TARGET_TEMPERATURE_C,
    TEMPERATURE_TOLERANCE_C,
    UI_LANGUAGE,
    SterilizerError,
)
from sterilisator_20a.cycle.controller import (
    CycleResult,
    cycle_within_time_budget,
    reported_cycle_duration_minutes,
    run_sterilization_cycle,
    temperature_within_range,
)
from sterilisator_20a.enclosure.footprint import (
    DimensionsCm,
    device_dimensions_cm,
    footprint_within_limits,
)
from sterilisator_20a.ui.messages import ui_labels_are_english, ui_messages

__all__ = [
    "CycleResult",
    "DimensionsCm",
    "MAX_CYCLE_MINUTES",
    "MAX_DEPTH_CM",
    "MAX_HEIGHT_CM",
    "MAX_WIDTH_CM",
    "SterilizerError",
    "TARGET_TEMPERATURE_C",
    "TEMPERATURE_TOLERANCE_C",
    "UI_LANGUAGE",
    "cycle_within_time_budget",
    "device_dimensions_cm",
    "footprint_within_limits",
    "reported_cycle_duration_minutes",
    "run_sterilization_cycle",
    "temperature_within_range",
    "ui_labels_are_english",
    "ui_messages",
]
