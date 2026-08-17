from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parent_entity import ParentEntity
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKnowledgeUnitsFromExisting")


@_attrs_define
class CreateKnowledgeUnitsFromExisting:
    """Model for creating a KU from existing KU schema or KU

    Attributes:
        parent_entity (ParentEntity):
        ku_schema_ids (list[str] | None | Unset): ID of existing knowledge unit schema to copy from
        ku_history_ids (list[str] | None | Unset): History ID of knowledge unit to create schema from
        include_content (bool | Unset): Whether to include content in the copy Default: False.
        include_traces (bool | Unset): Whether to include traces in the copy Default: True.
        ignore_knowledge_topics (bool | None | Unset): Whether to ignore knowledge topics in the copy
        product_history_id (str | Unset): Target product history id to add the knowledge units Default: ''.
        create_from_unapproved_schemas (bool | Unset): Whether to create from unapproved schemas Default: False.
    """

    parent_entity: ParentEntity
    ku_schema_ids: list[str] | None | Unset = UNSET
    ku_history_ids: list[str] | None | Unset = UNSET
    include_content: bool | Unset = False
    include_traces: bool | Unset = True
    ignore_knowledge_topics: bool | None | Unset = UNSET
    product_history_id: str | Unset = ""
    create_from_unapproved_schemas: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_entity = self.parent_entity.value

        ku_schema_ids: list[str] | None | Unset
        if isinstance(self.ku_schema_ids, Unset):
            ku_schema_ids = UNSET
        elif isinstance(self.ku_schema_ids, list):
            ku_schema_ids = self.ku_schema_ids

        else:
            ku_schema_ids = self.ku_schema_ids

        ku_history_ids: list[str] | None | Unset
        if isinstance(self.ku_history_ids, Unset):
            ku_history_ids = UNSET
        elif isinstance(self.ku_history_ids, list):
            ku_history_ids = self.ku_history_ids

        else:
            ku_history_ids = self.ku_history_ids

        include_content = self.include_content

        include_traces = self.include_traces

        ignore_knowledge_topics: bool | None | Unset
        if isinstance(self.ignore_knowledge_topics, Unset):
            ignore_knowledge_topics = UNSET
        else:
            ignore_knowledge_topics = self.ignore_knowledge_topics

        product_history_id = self.product_history_id

        create_from_unapproved_schemas = self.create_from_unapproved_schemas

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_entity": parent_entity,
            }
        )
        if ku_schema_ids is not UNSET:
            field_dict["ku_schema_ids"] = ku_schema_ids
        if ku_history_ids is not UNSET:
            field_dict["ku_history_ids"] = ku_history_ids
        if include_content is not UNSET:
            field_dict["include_content"] = include_content
        if include_traces is not UNSET:
            field_dict["include_traces"] = include_traces
        if ignore_knowledge_topics is not UNSET:
            field_dict["ignore_knowledge_topics"] = ignore_knowledge_topics
        if product_history_id is not UNSET:
            field_dict["product_history_id"] = product_history_id
        if create_from_unapproved_schemas is not UNSET:
            field_dict["create_from_unapproved_schemas"] = (
                create_from_unapproved_schemas
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        parent_entity = ParentEntity(d.pop("parent_entity"))

        def _parse_ku_schema_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ku_schema_ids_type_0 = cast(list[str], data)

                return ku_schema_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ku_schema_ids = _parse_ku_schema_ids(d.pop("ku_schema_ids", UNSET))

        def _parse_ku_history_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ku_history_ids_type_0 = cast(list[str], data)

                return ku_history_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ku_history_ids = _parse_ku_history_ids(d.pop("ku_history_ids", UNSET))

        include_content = d.pop("include_content", UNSET)

        include_traces = d.pop("include_traces", UNSET)

        def _parse_ignore_knowledge_topics(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ignore_knowledge_topics = _parse_ignore_knowledge_topics(
            d.pop("ignore_knowledge_topics", UNSET)
        )

        product_history_id = d.pop("product_history_id", UNSET)

        create_from_unapproved_schemas = d.pop("create_from_unapproved_schemas", UNSET)

        create_knowledge_units_from_existing = cls(
            parent_entity=parent_entity,
            ku_schema_ids=ku_schema_ids,
            ku_history_ids=ku_history_ids,
            include_content=include_content,
            include_traces=include_traces,
            ignore_knowledge_topics=ignore_knowledge_topics,
            product_history_id=product_history_id,
            create_from_unapproved_schemas=create_from_unapproved_schemas,
        )

        create_knowledge_units_from_existing.additional_properties = d
        return create_knowledge_units_from_existing

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
