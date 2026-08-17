from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_topic_type import KnowledgeTopicType

T = TypeVar("T", bound="KnowledgeTopicVersionEntry")


@_attrs_define
class KnowledgeTopicVersionEntry:
    """One (KU revision, KT revision) pair with version and approval status.

    Attributes:
        kt_revision_id (str):
        kt_history_id (str):
        kt_name (str):
        ku_revision_id (str):
        ku_history_id (str):
        ku_version (str):
        is_approved (bool):
        type_ (KnowledgeTopicType):
    """

    kt_revision_id: str
    kt_history_id: str
    kt_name: str
    ku_revision_id: str
    ku_history_id: str
    ku_version: str
    is_approved: bool
    type_: KnowledgeTopicType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kt_revision_id = self.kt_revision_id

        kt_history_id = self.kt_history_id

        kt_name = self.kt_name

        ku_revision_id = self.ku_revision_id

        ku_history_id = self.ku_history_id

        ku_version = self.ku_version

        is_approved = self.is_approved

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kt_revision_id": kt_revision_id,
                "kt_history_id": kt_history_id,
                "kt_name": kt_name,
                "ku_revision_id": ku_revision_id,
                "ku_history_id": ku_history_id,
                "ku_version": ku_version,
                "is_approved": is_approved,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kt_revision_id = d.pop("kt_revision_id")

        kt_history_id = d.pop("kt_history_id")

        kt_name = d.pop("kt_name")

        ku_revision_id = d.pop("ku_revision_id")

        ku_history_id = d.pop("ku_history_id")

        ku_version = d.pop("ku_version")

        is_approved = d.pop("is_approved")

        type_ = KnowledgeTopicType(d.pop("type"))

        knowledge_topic_version_entry = cls(
            kt_revision_id=kt_revision_id,
            kt_history_id=kt_history_id,
            kt_name=kt_name,
            ku_revision_id=ku_revision_id,
            ku_history_id=ku_history_id,
            ku_version=ku_version,
            is_approved=is_approved,
            type_=type_,
        )

        knowledge_topic_version_entry.additional_properties = d
        return knowledge_topic_version_entry

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
