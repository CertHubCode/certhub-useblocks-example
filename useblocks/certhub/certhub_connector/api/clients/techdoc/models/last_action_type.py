from enum import Enum


class LastActionType(str, Enum):
    CREATED = "created"
    PUBLISHED = "published"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
