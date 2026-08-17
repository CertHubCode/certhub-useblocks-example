from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schema_knowledge_topic_input import SchemaKnowledgeTopicInput


T = TypeVar("T", bound="SchemaKnowledgeTopicSchema")


@_attrs_define
class SchemaKnowledgeTopicSchema:
    """
    Attributes:
        components (list[SchemaKnowledgeTopicInput]):
    """

    components: list[SchemaKnowledgeTopicInput]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "components": components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schema_knowledge_topic_input import SchemaKnowledgeTopicInput

        d = dict(src_dict)
        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = SchemaKnowledgeTopicInput.from_dict(components_item_data)

            components.append(components_item)

        schema_knowledge_topic_schema = cls(
            components=components,
        )

        schema_knowledge_topic_schema.additional_properties = d
        return schema_knowledge_topic_schema

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
