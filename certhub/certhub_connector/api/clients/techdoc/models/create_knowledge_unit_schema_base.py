from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKnowledgeUnitSchemaBase")


@_attrs_define
class CreateKnowledgeUnitSchemaBase:
    """Base model for creating a knowledge unit schema

    Attributes:
        knowledge_unit_name (str):
        knowledge_unit_description (None | str | Unset):
        knowledge_topic_schemas (list[str] | None | Unset):
        is_not_editable_for_children (bool | None | Unset):  Default: False.
        library_ids (list[str] | None | Unset):
    """

    knowledge_unit_name: str
    knowledge_unit_description: None | str | Unset = UNSET
    knowledge_topic_schemas: list[str] | None | Unset = UNSET
    is_not_editable_for_children: bool | None | Unset = False
    library_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_unit_name = self.knowledge_unit_name

        knowledge_unit_description: None | str | Unset
        if isinstance(self.knowledge_unit_description, Unset):
            knowledge_unit_description = UNSET
        else:
            knowledge_unit_description = self.knowledge_unit_description

        knowledge_topic_schemas: list[str] | None | Unset
        if isinstance(self.knowledge_topic_schemas, Unset):
            knowledge_topic_schemas = UNSET
        elif isinstance(self.knowledge_topic_schemas, list):
            knowledge_topic_schemas = self.knowledge_topic_schemas

        else:
            knowledge_topic_schemas = self.knowledge_topic_schemas

        is_not_editable_for_children: bool | None | Unset
        if isinstance(self.is_not_editable_for_children, Unset):
            is_not_editable_for_children = UNSET
        else:
            is_not_editable_for_children = self.is_not_editable_for_children

        library_ids: list[str] | None | Unset
        if isinstance(self.library_ids, Unset):
            library_ids = UNSET
        elif isinstance(self.library_ids, list):
            library_ids = self.library_ids

        else:
            library_ids = self.library_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_unit_name": knowledge_unit_name,
            }
        )
        if knowledge_unit_description is not UNSET:
            field_dict["knowledge_unit_description"] = knowledge_unit_description
        if knowledge_topic_schemas is not UNSET:
            field_dict["knowledge_topic_schemas"] = knowledge_topic_schemas
        if is_not_editable_for_children is not UNSET:
            field_dict["is_not_editable_for_children"] = is_not_editable_for_children
        if library_ids is not UNSET:
            field_dict["library_ids"] = library_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        knowledge_unit_name = d.pop("knowledge_unit_name")

        def _parse_knowledge_unit_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_description = _parse_knowledge_unit_description(
            d.pop("knowledge_unit_description", UNSET)
        )

        def _parse_knowledge_topic_schemas(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                knowledge_topic_schemas_type_0 = cast(list[str], data)

                return knowledge_topic_schemas_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        knowledge_topic_schemas = _parse_knowledge_topic_schemas(
            d.pop("knowledge_topic_schemas", UNSET)
        )

        def _parse_is_not_editable_for_children(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_not_editable_for_children = _parse_is_not_editable_for_children(
            d.pop("is_not_editable_for_children", UNSET)
        )

        def _parse_library_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                library_ids_type_0 = cast(list[str], data)

                return library_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        library_ids = _parse_library_ids(d.pop("library_ids", UNSET))

        create_knowledge_unit_schema_base = cls(
            knowledge_unit_name=knowledge_unit_name,
            knowledge_unit_description=knowledge_unit_description,
            knowledge_topic_schemas=knowledge_topic_schemas,
            is_not_editable_for_children=is_not_editable_for_children,
            library_ids=library_ids,
        )

        create_knowledge_unit_schema_base.additional_properties = d
        return create_knowledge_unit_schema_base

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
