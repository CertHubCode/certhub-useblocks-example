from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkKnowledgeTopicFetchRequest")


@_attrs_define
class BulkKnowledgeTopicFetchRequest:
    """
    Attributes:
        knowledge_topic_ids (list[str] | Unset):
        include_use_case_config (bool | Unset):  Default: False.
    """

    knowledge_topic_ids: list[str] | Unset = UNSET
    include_use_case_config: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_topic_ids: list[str] | Unset = UNSET
        if not isinstance(self.knowledge_topic_ids, Unset):
            knowledge_topic_ids = self.knowledge_topic_ids

        include_use_case_config = self.include_use_case_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if knowledge_topic_ids is not UNSET:
            field_dict["knowledge_topic_ids"] = knowledge_topic_ids
        if include_use_case_config is not UNSET:
            field_dict["include_use_case_config"] = include_use_case_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        knowledge_topic_ids = cast(list[str], d.pop("knowledge_topic_ids", UNSET))

        include_use_case_config = d.pop("include_use_case_config", UNSET)

        bulk_knowledge_topic_fetch_request = cls(
            knowledge_topic_ids=knowledge_topic_ids,
            include_use_case_config=include_use_case_config,
        )

        bulk_knowledge_topic_fetch_request.additional_properties = d
        return bulk_knowledge_topic_fetch_request

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
