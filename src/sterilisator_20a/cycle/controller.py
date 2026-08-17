"""Cycle control functions for Sterilisator 20A."""

from __future__ import annotations

from dataclasses import dataclass

from sterilisator_20a.constants import (
    MAX_CYCLE_MINUTES,
    TARGET_TEMPERATURE_C,
    TEMPERATURE_TOLERANCE_C,
    SterilizerError,
)


@dataclass(frozen=True)
class CycleResult:
    peak_temperature_c: float
    duration_minutes: float
    temperature_ok: bool
    duration_ok: bool


# @need-ids: DOUT_018
def temperature_within_range(peak_temperature_c: float) -> bool:
    """Return True when chamber peak temperature is within 121°C ± 2°C."""
    low = TARGET_TEMPERATURE_C - TEMPERATURE_TOLERANCE_C
    high = TARGET_TEMPERATURE_C + TEMPERATURE_TOLERANCE_C
    return low <= peak_temperature_c <= high


# @need-ids: DOUT_018
def reported_cycle_duration_minutes(measured_minutes: float) -> float:
    """Return the cycle duration used for acceptance (≤ 60 minutes when GREEN)."""
    if measured_minutes < 0:
        raise SterilizerError(
            f"Cycle duration must be non-negative, got {measured_minutes}"
        )
    # GATE_DURATION: make break replaces the next line so VERIF_002 fails.
    return measured_minutes


# @need-ids: DOUT_018
def cycle_within_time_budget(duration_minutes: float) -> bool:
    """Return True when total cycle time does not exceed 60 minutes."""
    reported = reported_cycle_duration_minutes(duration_minutes)
    return reported <= MAX_CYCLE_MINUTES


# @need-ids: DOUT_018
def run_sterilization_cycle(
    *,
    peak_temperature_c: float,
    duration_minutes: float,
) -> CycleResult:
    """Simulate one sterilization cycle and evaluate temperature + duration."""
    duration = reported_cycle_duration_minutes(duration_minutes)
    temperature_ok = temperature_within_range(peak_temperature_c)
    duration_ok = duration <= MAX_CYCLE_MINUTES
    return CycleResult(
        peak_temperature_c=peak_temperature_c,
        duration_minutes=duration,
        temperature_ok=temperature_ok,
        duration_ok=duration_ok,
    )
