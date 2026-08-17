from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_topic_type import KnowledgeTopicType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_knowledge_topic_schema import SchemaKnowledgeTopicSchema


T = TypeVar("T", bound="SchemaKnowledgeTopic")


@_attrs_define
class SchemaKnowledgeTopic:
    """
    Attributes:
        knowledge_topic_name (str):
        type_ (KnowledgeTopicType):
        knowledge_topic_schema (SchemaKnowledgeTopicSchema):
        id (None | str | Unset):
    """

    knowledge_topic_name: str
    type_: KnowledgeTopicType
    knowledge_topic_schema: SchemaKnowledgeTopicSchema
    id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_topic_name = self.knowledge_topic_name

        type_ = self.type_.value

        knowledge_topic_schema = self.knowledge_topic_schema.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_topic_name": knowledge_topic_name,
                "type": type_,
                "knowledge_topic_schema": knowledge_topic_schema,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schema_knowledge_topic_schema import SchemaKnowledgeTopicSchema

        d = dict(src_dict)
        knowledge_topic_name = d.pop("knowledge_topic_name")

        type_ = KnowledgeTopicType(d.pop("type"))

        knowledge_topic_schema = SchemaKnowledgeTopicSchema.from_dict(
            d.pop("knowledge_topic_schema")
        )

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        schema_knowledge_topic = cls(
            knowledge_topic_name=knowledge_topic_name,
            type_=type_,
            knowledge_topic_schema=knowledge_topic_schema,
            id=id,
        )

        schema_knowledge_topic.additional_properties = d
        return schema_knowledge_topic

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
