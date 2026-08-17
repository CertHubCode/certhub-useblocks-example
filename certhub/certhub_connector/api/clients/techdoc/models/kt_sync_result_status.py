from enum import Enum


class KtSyncResultStatus(str, Enum):
    FAILED = "failed"
    SKIPPED_NO_TRACE = "skipped_no_trace"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
