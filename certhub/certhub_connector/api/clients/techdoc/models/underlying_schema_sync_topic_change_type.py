from enum import Enum


class UnderlyingSchemaSyncTopicChangeType(str, Enum):
    NEW = "new"
    REMOVE = "remove"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
