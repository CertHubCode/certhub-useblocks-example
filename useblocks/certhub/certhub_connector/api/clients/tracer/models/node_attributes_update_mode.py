from enum import Enum


class NodeAttributesUpdateMode(str, Enum):
    CREATE_NEW = "create_new"
    IN_PLACE = "in_place"

    def __str__(self) -> str:
        return str(self.value)
