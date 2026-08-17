from enum import Enum


class ConditionalFieldStatus(str, Enum):
    HIDDEN = "hidden"
    MISSING = "missing"
    PRESENT = "present"

    def __str__(self) -> str:
        return str(self.value)
