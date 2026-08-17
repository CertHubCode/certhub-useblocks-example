from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKUSchemaLibrary")


@_attrs_define
class UpdateKUSchemaLibrary:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        knowledge_unit_schema_ids (list[str] | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    knowledge_unit_schema_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        knowledge_unit_schema_ids: list[str] | None | Unset
        if isinstance(self.knowledge_unit_schema_ids, Unset):
            knowledge_unit_schema_ids = UNSET
        elif isinstance(self.knowledge_unit_schema_ids, list):
            knowledge_unit_schema_ids = self.knowledge_unit_schema_ids

        else:
            knowledge_unit_schema_ids = self.knowledge_unit_schema_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if knowledge_unit_schema_ids is not UNSET:
            field_dict["knowledge_unit_schema_ids"] = knowledge_unit_schema_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_knowledge_unit_schema_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                knowledge_unit_schema_ids_type_0 = cast(list[str], data)

                return knowledge_unit_schema_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        knowledge_unit_schema_ids = _parse_knowledge_unit_schema_ids(
            d.pop("knowledge_unit_schema_ids", UNSET)
        )

        update_ku_schema_library = cls(
            name=name,
            description=description,
            knowledge_unit_schema_ids=knowledge_unit_schema_ids,
        )

        update_ku_schema_library.additional_properties = d
        return update_ku_schema_library

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
