from enum import Enum


class MatchDecisionAction(str, Enum):
    ACCEPT = "accept"
    MODIFY = "modify"
    REJECT = "reject"

    def __str__(self) -> str:
        return str(self.value)
