"""Door interlock helpers for Sterilisator 20A."""

from __future__ import annotations

from sterilisator_20a.constants import CycleState


# @need-ids: DOUT_018
def door_must_lock(state: CycleState) -> bool:
    """Return True when the door must remain locked (cycle running)."""
    return state is CycleState.RUNNING


# @need-ids: DOUT_018
def door_may_open(state: CycleState) -> bool:
    """Return True when the operator may open the door."""
    return state in (CycleState.IDLE, CycleState.COMPLETE, CycleState.FAULT)


# @need-ids: DOUT_018
def may_start_cycle(door_closed: bool) -> bool:
    """Return True when a cycle may start (chamber door closed)."""
    return door_closed
