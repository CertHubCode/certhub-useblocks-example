from enum import Enum


class NodeDeleteMode(str, Enum):
    DELETE_RELATED_EDGES = "delete_related_edges"
    ONLY_NODE = "only_node"

    def __str__(self) -> str:
        return str(self.value)
