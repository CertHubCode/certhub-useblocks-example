#!/usr/bin/env python3
"""Deterministic GREEN/RED mutation for the Cadence gate toggle."""

from __future__ import annotations

import sys
from pathlib import Path

DEVICE = (
    Path(__file__).resolve().parents[1]
    / "src"
    / "sterilisator_20a"
    / "cycle"
    / "controller.py"
)

GREEN_LINE = "    return measured_minutes"
RED_LINE = (
    "    return 75.0  # GATE BREAK: always exceed 60 → VERIF_002 fails"
)


def mutate(mode: str) -> None:
    text = DEVICE.read_text(encoding="utf-8")
    if mode == "break":
        if RED_LINE in text:
            print("Already broken")
            return
        if GREEN_LINE not in text:
            raise SystemExit("Could not find GREEN duration line to break")
        new = text.replace(GREEN_LINE, RED_LINE, 1)
    elif mode == "fix":
        if GREEN_LINE in text and RED_LINE not in text:
            print("Already fixed")
            return
        if RED_LINE not in text:
            raise SystemExit("Could not find RED break line to fix")
        new = text.replace(RED_LINE, GREEN_LINE, 1)
    else:
        raise SystemExit(f"Unknown mode: {mode}")
    DEVICE.write_text(new, encoding="utf-8")
    print(f"Mutation '{mode}' applied to {DEVICE}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"break", "fix"}:
        raise SystemExit("Usage: gate_mutate.py [break|fix]")
    mutate(sys.argv[1])
