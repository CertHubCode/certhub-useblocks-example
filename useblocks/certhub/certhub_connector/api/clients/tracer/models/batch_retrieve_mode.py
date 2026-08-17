from enum import Enum


class BatchRetrieveMode(str, Enum):
    LEGACY_CONNECTED_NODES = "legacy_connected_nodes"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
