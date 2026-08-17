from enum import Enum


class GuidanceTaskState(str, Enum):
    DONE = "done"
    NA = "na"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
