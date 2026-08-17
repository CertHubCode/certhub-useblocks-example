from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.underlying_schema_sync_topic_change_type import (
    UnderlyingSchemaSyncTopicChangeType,
)

T = TypeVar("T", bound="UnderlyingSchemaSyncTopic")


@_attrs_define
class UnderlyingSchemaSyncTopic:
    """One Knowledge Topic that 'Update Underlying Schema' would actually
    change - updating its existing Knowledge Topic Schema counterpart
    ("update"), creating a brand new one because it has no trace ("new"), or
    removing a schema entry that no longer has any corresponding Product
    Knowledge Topic ("remove", e.g. the KT was deleted from the Product).

    For "remove", knowledge_topic_history_id/knowledge_topic_name describe
    the Knowledge Topic Schema being removed (there is no Product KT anymore
    to describe it from).

        Attributes:
            knowledge_topic_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
            knowledge_topic_name (str):
            change_type (UnderlyingSchemaSyncTopicChangeType):
    """

    knowledge_topic_history_id: str
    knowledge_topic_name: str
    change_type: UnderlyingSchemaSyncTopicChangeType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_topic_history_id = self.knowledge_topic_history_id

        knowledge_topic_name = self.knowledge_topic_name

        change_type = self.change_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_topic_history_id": knowledge_topic_history_id,
                "knowledge_topic_name": knowledge_topic_name,
                "change_type": change_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        knowledge_topic_history_id = d.pop("knowledge_topic_history_id")

        knowledge_topic_name = d.pop("knowledge_topic_name")

        change_type = UnderlyingSchemaSyncTopicChangeType(d.pop("change_type"))

        underlying_schema_sync_topic = cls(
            knowledge_topic_history_id=knowledge_topic_history_id,
            knowledge_topic_name=knowledge_topic_name,
            change_type=change_type,
        )

        underlying_schema_sync_topic.additional_properties = d
        return underlying_schema_sync_topic

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
