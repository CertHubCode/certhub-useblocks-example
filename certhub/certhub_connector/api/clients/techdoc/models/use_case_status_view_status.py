from enum import Enum


class UseCaseStatusViewStatus(str, Enum):
    COMPLETE = "complete"
    DUPLICATE = "duplicate"
    INCOMPLETE = "incomplete"

    def __str__(self) -> str:
        return str(self.value)
