from enum import Enum


class ManualTraceSource(str, Enum):
    USE_CASE = "use_case"

    def __str__(self) -> str:
        return str(self.value)
