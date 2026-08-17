from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KnowledgeTopicSchemaView")


@_attrs_define
class KnowledgeTopicSchemaView:
    """Base model for viewing knowledge topic schema

    Attributes:
        id (str):
        knowledge_topic_name (str):
        knowledge_topic_schema_history_id (str):
        knowledge_unit_schema_history_id (str):
        knowledge_unit_schema_name (str):
        knowledge_unit_schema_version (str):
    """

    id: str
    knowledge_topic_name: str
    knowledge_topic_schema_history_id: str
    knowledge_unit_schema_history_id: str
    knowledge_unit_schema_name: str
    knowledge_unit_schema_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        knowledge_topic_name = self.knowledge_topic_name

        knowledge_topic_schema_history_id = self.knowledge_topic_schema_history_id

        knowledge_unit_schema_history_id = self.knowledge_unit_schema_history_id

        knowledge_unit_schema_name = self.knowledge_unit_schema_name

        knowledge_unit_schema_version = self.knowledge_unit_schema_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "knowledge_topic_name": knowledge_topic_name,
                "knowledge_topic_schema_history_id": knowledge_topic_schema_history_id,
                "knowledge_unit_schema_history_id": knowledge_unit_schema_history_id,
                "knowledge_unit_schema_name": knowledge_unit_schema_name,
                "knowledge_unit_schema_version": knowledge_unit_schema_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        knowledge_topic_name = d.pop("knowledge_topic_name")

        knowledge_topic_schema_history_id = d.pop("knowledge_topic_schema_history_id")

        knowledge_unit_schema_history_id = d.pop("knowledge_unit_schema_history_id")

        knowledge_unit_schema_name = d.pop("knowledge_unit_schema_name")

        knowledge_unit_schema_version = d.pop("knowledge_unit_schema_version")

        knowledge_topic_schema_view = cls(
            id=id,
            knowledge_topic_name=knowledge_topic_name,
            knowledge_topic_schema_history_id=knowledge_topic_schema_history_id,
            knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
            knowledge_unit_schema_name=knowledge_unit_schema_name,
            knowledge_unit_schema_version=knowledge_unit_schema_version,
        )

        knowledge_topic_schema_view.additional_properties = d
        return knowledge_topic_schema_view

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
