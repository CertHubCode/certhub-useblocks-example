"""Shared constants and errors for Sterilisator 20A."""

from __future__ import annotations

from enum import Enum

TARGET_TEMPERATURE_C = 121.0
TEMPERATURE_TOLERANCE_C = 2.0
MAX_CYCLE_MINUTES = 60.0
UI_LANGUAGE = "en"


class CycleState(str, Enum):
    """Operator-visible cycle states for the tabletop sterilizer."""

    IDLE = "idle"
    RUNNING = "running"
    COMPLETE = "complete"
    FAULT = "fault"


class SterilizerError(ValueError):
    """Raised when sterilizer inputs or operating limits are violated."""
