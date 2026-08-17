from enum import Enum


class IssuingEntityTypeEnum(str, Enum):
    EUDAMED = "EUDAMED"
    GS1 = "GS1"
    HIBCC = "HIBCC"
    ICCBBA = "ICCBBA"
    IFA = "IFA"

    def __str__(self) -> str:
        return str(self.value)
