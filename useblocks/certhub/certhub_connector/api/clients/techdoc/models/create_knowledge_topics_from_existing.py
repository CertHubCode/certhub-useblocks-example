from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parent_entity import ParentEntity
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKnowledgeTopicsFromExisting")


@_attrs_define
class CreateKnowledgeTopicsFromExisting:
    """Model for creating a KT from existing KT schema or KT

    Attributes:
        parent_entity (ParentEntity):
        kt_schema_ids (list[str] | None | Unset): ID of existing knowledge topic schema to copy from
        kt_ids (list[str] | None | Unset): ID of knowledge topic to create schema from
        include_content (bool | Unset): Whether to include content in the copy Default: False.
        include_traces (bool | Unset): Whether to include traces in the copy Default: True.
        knowledge_unit_history_id (str | Unset): knowledge unit history id to add the knowledge topics Default: ''.
    """

    parent_entity: ParentEntity
    kt_schema_ids: list[str] | None | Unset = UNSET
    kt_ids: list[str] | None | Unset = UNSET
    include_content: bool | Unset = False
    include_traces: bool | Unset = True
    knowledge_unit_history_id: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_entity = self.parent_entity.value

        kt_schema_ids: list[str] | None | Unset
        if isinstance(self.kt_schema_ids, Unset):
            kt_schema_ids = UNSET
        elif isinstance(self.kt_schema_ids, list):
            kt_schema_ids = self.kt_schema_ids

        else:
            kt_schema_ids = self.kt_schema_ids

        kt_ids: list[str] | None | Unset
        if isinstance(self.kt_ids, Unset):
            kt_ids = UNSET
        elif isinstance(self.kt_ids, list):
            kt_ids = self.kt_ids

        else:
            kt_ids = self.kt_ids

        include_content = self.include_content

        include_traces = self.include_traces

        knowledge_unit_history_id = self.knowledge_unit_history_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_entity": parent_entity,
            }
        )
        if kt_schema_ids is not UNSET:
            field_dict["kt_schema_ids"] = kt_schema_ids
        if kt_ids is not UNSET:
            field_dict["kt_ids"] = kt_ids
        if include_content is not UNSET:
            field_dict["include_content"] = include_content
        if include_traces is not UNSET:
            field_dict["include_traces"] = include_traces
        if knowledge_unit_history_id is not UNSET:
            field_dict["knowledge_unit_history_id"] = knowledge_unit_history_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        parent_entity = ParentEntity(d.pop("parent_entity"))

        def _parse_kt_schema_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kt_schema_ids_type_0 = cast(list[str], data)

                return kt_schema_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        kt_schema_ids = _parse_kt_schema_ids(d.pop("kt_schema_ids", UNSET))

        def _parse_kt_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kt_ids_type_0 = cast(list[str], data)

                return kt_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        kt_ids = _parse_kt_ids(d.pop("kt_ids", UNSET))

        include_content = d.pop("include_content", UNSET)

        include_traces = d.pop("include_traces", UNSET)

        knowledge_unit_history_id = d.pop("knowledge_unit_history_id", UNSET)

        create_knowledge_topics_from_existing = cls(
            parent_entity=parent_entity,
            kt_schema_ids=kt_schema_ids,
            kt_ids=kt_ids,
            include_content=include_content,
            include_traces=include_traces,
            knowledge_unit_history_id=knowledge_unit_history_id,
        )

        create_knowledge_topics_from_existing.additional_properties = d
        return create_knowledge_topics_from_existing

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
