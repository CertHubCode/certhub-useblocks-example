from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateKnowledgeTopicSchema")


@_attrs_define
class DuplicateKnowledgeTopicSchema:
    """
    Attributes:
        kt_schema_id (None | str | Unset): ID of existing knowledge topic schema to copy from
        kt_id (None | str | Unset): ID of knowledge topic to create schema from
        include_content (bool | Unset): Whether to include content in the copy Default: False.
    """

    kt_schema_id: None | str | Unset = UNSET
    kt_id: None | str | Unset = UNSET
    include_content: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kt_schema_id: None | str | Unset
        if isinstance(self.kt_schema_id, Unset):
            kt_schema_id = UNSET
        else:
            kt_schema_id = self.kt_schema_id

        kt_id: None | str | Unset
        if isinstance(self.kt_id, Unset):
            kt_id = UNSET
        else:
            kt_id = self.kt_id

        include_content = self.include_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kt_schema_id is not UNSET:
            field_dict["kt_schema_id"] = kt_schema_id
        if kt_id is not UNSET:
            field_dict["kt_id"] = kt_id
        if include_content is not UNSET:
            field_dict["include_content"] = include_content

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_kt_schema_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kt_schema_id = _parse_kt_schema_id(d.pop("kt_schema_id", UNSET))

        def _parse_kt_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kt_id = _parse_kt_id(d.pop("kt_id", UNSET))

        include_content = d.pop("include_content", UNSET)

        duplicate_knowledge_topic_schema = cls(
            kt_schema_id=kt_schema_id,
            kt_id=kt_id,
            include_content=include_content,
        )

        duplicate_knowledge_topic_schema.additional_properties = d
        return duplicate_knowledge_topic_schema

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
