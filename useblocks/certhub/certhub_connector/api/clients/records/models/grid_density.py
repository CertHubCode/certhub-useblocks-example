from enum import Enum


class GridDensity(str, Enum):
    COMFORTABLE = "comfortable"
    COMPACT = "compact"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
