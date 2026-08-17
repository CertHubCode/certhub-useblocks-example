from enum import Enum


class KnowledgeTopicType(str, Enum):
    MULTI_RECORD = "multi_record"
    PRODUCT_DATA_COLLECTION = "product_data_collection"
    SINGLE_RECORD = "single_record"

    def __str__(self) -> str:
        return str(self.value)
