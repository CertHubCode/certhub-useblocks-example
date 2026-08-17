"""Shared constants and errors for Sterilisator 20A."""

from __future__ import annotations

TARGET_TEMPERATURE_C = 121.0
TEMPERATURE_TOLERANCE_C = 2.0
MAX_CYCLE_MINUTES = 60.0
MAX_WIDTH_CM = 50.0
MAX_DEPTH_CM = 40.0
MAX_HEIGHT_CM = 35.0
UI_LANGUAGE = "en"


class SterilizerError(ValueError):
    """Raised when sterilizer inputs or operating limits are violated."""
