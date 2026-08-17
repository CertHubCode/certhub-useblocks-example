from enum import Enum


class Software(str, Enum):
    EMBEDDED = "Embedded"
    NOSOFTWARE = "NoSoftware"
    SOFTWARE_ONLY = "Software Only"

    def __str__(self) -> str:
        return str(self.value)
