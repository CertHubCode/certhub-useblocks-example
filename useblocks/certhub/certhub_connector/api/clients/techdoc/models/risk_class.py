from enum import Enum


class RiskClass(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    I = "I"
    IIA = "IIa"
    IIB = "IIb"
    III = "III"

    def __str__(self) -> str:
        return str(self.value)
