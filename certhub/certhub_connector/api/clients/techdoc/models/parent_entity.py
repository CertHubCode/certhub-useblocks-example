from enum import Enum


class ParentEntity(str, Enum):
    PRODUCT = "PRODUCT"
    PRODUCT_FAMILY = "PRODUCT_FAMILY"

    def __str__(self) -> str:
        return str(self.value)
