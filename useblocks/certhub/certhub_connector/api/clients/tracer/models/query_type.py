from enum import Enum


class QueryType(str, Enum):
    GRAPH = "graph"
    TRACES_LIST = "traces_list"
    TRACES_LIST_WITH_REFERENCE_TRACES = "traces_list_with_reference_traces"

    def __str__(self) -> str:
        return str(self.value)
