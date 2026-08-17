from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_knowledge_topic import CreateKnowledgeTopic


T = TypeVar("T", bound="BodyCreateNewKnowledgeTopicKtPost")


@_attrs_define
class BodyCreateNewKnowledgeTopicKtPost:
    """
    Attributes:
        knowledge_topic (CreateKnowledgeTopic):
        knowledge_unit_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
    """

    knowledge_topic: CreateKnowledgeTopic
    knowledge_unit_history_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_topic = self.knowledge_topic.to_dict()

        knowledge_unit_history_id = self.knowledge_unit_history_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_topic": knowledge_topic,
                "knowledge_unit_history_id": knowledge_unit_history_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_knowledge_topic import CreateKnowledgeTopic

        d = dict(src_dict)
        knowledge_topic = CreateKnowledgeTopic.from_dict(d.pop("knowledge_topic"))

        knowledge_unit_history_id = d.pop("knowledge_unit_history_id")

        body_create_new_knowledge_topic_kt_post = cls(
            knowledge_topic=knowledge_topic,
            knowledge_unit_history_id=knowledge_unit_history_id,
        )

        body_create_new_knowledge_topic_kt_post.additional_properties = d
        return body_create_new_knowledge_topic_kt_post

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
