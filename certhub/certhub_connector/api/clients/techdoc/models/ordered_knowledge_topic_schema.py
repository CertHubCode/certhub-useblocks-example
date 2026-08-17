from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderedKnowledgeTopicSchema")


@_attrs_define
class OrderedKnowledgeTopicSchema:
    """
    Attributes:
        knowledge_topic_schema_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        index (int):
    """

    knowledge_topic_schema_id: str
    index: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_topic_schema_id = self.knowledge_topic_schema_id

        index = self.index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_topic_schema_id": knowledge_topic_schema_id,
                "index": index,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        knowledge_topic_schema_id = d.pop("knowledge_topic_schema_id")

        index = d.pop("index")

        ordered_knowledge_topic_schema = cls(
            knowledge_topic_schema_id=knowledge_topic_schema_id,
            index=index,
        )

        ordered_knowledge_topic_schema.additional_properties = d
        return ordered_knowledge_topic_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
