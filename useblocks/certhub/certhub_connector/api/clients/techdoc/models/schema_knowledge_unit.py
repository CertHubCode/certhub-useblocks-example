from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_knowledge_topic import SchemaKnowledgeTopic


T = TypeVar("T", bound="SchemaKnowledgeUnit")


@_attrs_define
class SchemaKnowledgeUnit:
    """
    Attributes:
        knowledge_unit_name (str):
        knowledge_topics (list[SchemaKnowledgeTopic]):
        id (None | str | Unset):
    """

    knowledge_unit_name: str
    knowledge_topics: list[SchemaKnowledgeTopic]
    id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_unit_name = self.knowledge_unit_name

        knowledge_topics = []
        for knowledge_topics_item_data in self.knowledge_topics:
            knowledge_topics_item = knowledge_topics_item_data.to_dict()
            knowledge_topics.append(knowledge_topics_item)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_unit_name": knowledge_unit_name,
                "knowledge_topics": knowledge_topics,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schema_knowledge_topic import SchemaKnowledgeTopic

        d = dict(src_dict)
        knowledge_unit_name = d.pop("knowledge_unit_name")

        knowledge_topics = []
        _knowledge_topics = d.pop("knowledge_topics")
        for knowledge_topics_item_data in _knowledge_topics:
            knowledge_topics_item = SchemaKnowledgeTopic.from_dict(
                knowledge_topics_item_data
            )

            knowledge_topics.append(knowledge_topics_item)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        schema_knowledge_unit = cls(
            knowledge_unit_name=knowledge_unit_name,
            knowledge_topics=knowledge_topics,
            id=id,
        )

        schema_knowledge_unit.additional_properties = d
        return schema_knowledge_unit

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
