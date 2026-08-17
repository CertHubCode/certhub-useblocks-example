from enum import Enum


class Reusable(str, Enum):
    OTHER = "Other"
    SINGLE_USE = "Single Use"
    SURGICAL_REUSABLE_INSTRUMENT = "Surgical Reusable Instrument"

    def __str__(self) -> str:
        return str(self.value)
