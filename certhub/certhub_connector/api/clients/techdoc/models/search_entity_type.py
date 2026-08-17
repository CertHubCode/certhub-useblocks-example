from enum import Enum


class SearchEntityType(str, Enum):
    KNOWLEDGE_TOPIC = "KNOWLEDGE_TOPIC"
    KNOWLEDGE_UNIT = "KNOWLEDGE_UNIT"
    PRODUCT = "PRODUCT"

    def __str__(self) -> str:
        return str(self.value)
