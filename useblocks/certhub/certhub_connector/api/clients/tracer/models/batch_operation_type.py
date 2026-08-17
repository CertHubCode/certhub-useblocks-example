from enum import Enum


class BatchOperationType(str, Enum):
    CREATE = "create"
    DELETE = "delete"
    DELETE_BY_ID = "delete_by_id"

    def __str__(self) -> str:
        return str(self.value)
