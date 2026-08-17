from enum import Enum


class SoftwareClass(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    NOSOFTWARE = "NoSoftware"

    def __str__(self) -> str:
        return str(self.value)
