from enum import Enum


class Regulation(str, Enum):
    IVDR = "IVDR"
    MDR = "MDR"

    def __str__(self) -> str:
        return str(self.value)
