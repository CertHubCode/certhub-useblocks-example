from enum import Enum


class MatrixType(str, Enum):
    REQUIREMENTS = "requirements"
    REQUIREMENTS_LEGACY = "requirements_legacy"

    def __str__(self) -> str:
        return str(self.value)
