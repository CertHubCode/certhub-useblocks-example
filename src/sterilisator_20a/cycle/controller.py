"""Cycle control for Sterilisator 20A (temperature, duration, states)."""

from __future__ import annotations

from dataclasses import dataclass

from sterilisator_20a.constants import (
    MAX_CYCLE_MINUTES,
    TARGET_TEMPERATURE_C,
    TEMPERATURE_TOLERANCE_C,
    CycleState,
    SterilizerError,
)
from sterilisator_20a.safety.door import door_must_lock, may_start_cycle


@dataclass(frozen=True)
class CycleResult:
    peak_temperature_c: float
    duration_minutes: float
    temperature_ok: bool
    duration_ok: bool
    state: CycleState
    door_locked: bool


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
def start_cycle(
    *,
    door_closed: bool,
    peak_temperature_c: float,
    duration_minutes: float,
) -> CycleResult:
    """Run one sterilization cycle when the door is closed.

    Evaluates temperature and duration, then ends in ``complete`` or ``fault``.
    The returned result is never left in ``running``.
    """
    if not may_start_cycle(door_closed):
        raise SterilizerError("Cannot start cycle while chamber door is open")

    duration = reported_cycle_duration_minutes(duration_minutes)
    temperature_ok = temperature_within_range(peak_temperature_c)
    duration_ok = duration <= MAX_CYCLE_MINUTES
    state = (
        CycleState.COMPLETE
        if temperature_ok and duration_ok
        else CycleState.FAULT
    )
    return CycleResult(
        peak_temperature_c=peak_temperature_c,
        duration_minutes=duration,
        temperature_ok=temperature_ok,
        duration_ok=duration_ok,
        state=state,
        door_locked=door_must_lock(state),
    )


# Backwards-compatible alias used by older call sites / docs.
run_sterilization_cycle = start_cycle
