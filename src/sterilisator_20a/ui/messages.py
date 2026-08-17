"""UI message helpers for Sterilisator 20A."""

from __future__ import annotations

from sterilisator_20a.constants import UI_LANGUAGE


# @need-ids: DOUT_018
def ui_messages() -> dict[str, str]:
    """Operator-facing cycle status and alert strings (English)."""
    return {
        "language": UI_LANGUAGE,
        "cycle_status": "Cycle in progress",
        "alert_door": "Door locked for sterilization",
        "alert_complete": "Sterilization complete — safe to unload",
    }


# @need-ids: DOUT_018
def ui_labels_are_english(messages: dict[str, str] | None = None) -> bool:
    """Confirm UI language is English and status/alert text is present."""
    payload = messages if messages is not None else ui_messages()
    if payload.get("language") != "en":
        return False
    required = ("cycle_status", "alert_door", "alert_complete")
    return all(bool(payload.get(key, "").strip()) for key in required)
