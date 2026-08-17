from enum import Enum


class DeleteLibraryMode(str, Enum):
    DELETE_ALL = "delete_all"
    UNLINK_SCHEMAS = "unlink_schemas"

    def __str__(self) -> str:
        return str(self.value)
