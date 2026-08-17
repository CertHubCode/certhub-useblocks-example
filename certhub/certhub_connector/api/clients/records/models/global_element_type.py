from enum import Enum


class GlobalElementType(str, Enum):
    PRODUCT_DATA_COLLECTION = "product_data_collection"
    SYSTEM_CONTEXT_COLLECTION = "system_context_collection"

    def __str__(self) -> str:
        return str(self.value)
