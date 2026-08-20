"""English operator UI labels for Sterilisator 20A."""

from __future__ import annotations

from sterilisator_20a.constants import UI_LANGUAGE, CycleState

_STATUS_BY_STATE: dict[CycleState, str] = {
    CycleState.IDLE: "Idle — ready to start",
    CycleState.RUNNING: "Cycle in progress",
    CycleState.COMPLETE: "Sterilization complete — safe to unload",
    CycleState.FAULT: "Fault — cycle aborted",
}

_ALERT_DOOR_LOCKED = "Door locked for sterilization"
_ALERT_DOOR_OPEN_OK = "Door may be opened"


# @need-ids: DOUT_018
def ui_messages_for_state(state: CycleState) -> dict[str, str]:
    """English status and door alert for one cycle state."""
    locked = state is CycleState.RUNNING
    return {
        "language": UI_LANGUAGE,
        "state": state.value,
        "cycle_status": _STATUS_BY_STATE[state],
        "alert_door": _ALERT_DOOR_LOCKED if locked else _ALERT_DOOR_OPEN_OK,
    }


# @need-ids: DOUT_018
def ui_messages() -> dict[str, dict[str, str]]:
    """Full English UI catalog keyed by cycle state."""
    return {
        state.value: ui_messages_for_state(state) for state in CycleState
    }


# @need-ids: DOUT_018
def ui_labels_are_english(
    messages: dict[str, str] | dict[str, dict[str, str]] | None = None,
) -> bool:
    """Confirm UI language is English and required status/alert text is present.

    Accepts either a single-state payload or the full catalog from ``ui_messages``.
    """
    if messages is None:
        catalog: dict[str, dict[str, str]] = ui_messages()
    elif not messages:
        return False
    else:
        first = next(iter(messages.values()))
        if isinstance(first, dict):
            catalog = messages  # type: ignore[assignment]
        else:
            catalog = {"_": messages}  # type: ignore[dict-item]

    for payload in catalog.values():
        if payload.get("language") != "en":
            return False
        if not str(payload.get("cycle_status", "")).strip():
            return False
        if not str(payload.get("alert_door", "")).strip():
            return False
    return True
