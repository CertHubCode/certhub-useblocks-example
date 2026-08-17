from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKnowledgeUnitSchemasFromExisting")


@_attrs_define
class CreateKnowledgeUnitSchemasFromExisting:
    """Model for creating a KU from existing KU schema or KU

    Attributes:
        ku_schema_ids (list[str] | None | Unset):
        ku_ids (list[str] | None | Unset):
        include_content (bool | Unset):  Default: False.
        library_ids (list[str] | None | Unset):
    """

    ku_schema_ids: list[str] | None | Unset = UNSET
    ku_ids: list[str] | None | Unset = UNSET
    include_content: bool | Unset = False
    library_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ku_schema_ids: list[str] | None | Unset
        if isinstance(self.ku_schema_ids, Unset):
            ku_schema_ids = UNSET
        elif isinstance(self.ku_schema_ids, list):
            ku_schema_ids = self.ku_schema_ids

        else:
            ku_schema_ids = self.ku_schema_ids

        ku_ids: list[str] | None | Unset
        if isinstance(self.ku_ids, Unset):
            ku_ids = UNSET
        elif isinstance(self.ku_ids, list):
            ku_ids = self.ku_ids

        else:
            ku_ids = self.ku_ids

        include_content = self.include_content

        library_ids: list[str] | None | Unset
        if isinstance(self.library_ids, Unset):
            library_ids = UNSET
        elif isinstance(self.library_ids, list):
            library_ids = self.library_ids

        else:
            library_ids = self.library_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ku_schema_ids is not UNSET:
            field_dict["ku_schema_ids"] = ku_schema_ids
        if ku_ids is not UNSET:
            field_dict["ku_ids"] = ku_ids
        if include_content is not UNSET:
            field_dict["include_content"] = include_content
        if library_ids is not UNSET:
            field_dict["library_ids"] = library_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

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

        def _parse_ku_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ku_ids_type_0 = cast(list[str], data)

                return ku_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ku_ids = _parse_ku_ids(d.pop("ku_ids", UNSET))

        include_content = d.pop("include_content", UNSET)

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

        create_knowledge_unit_schemas_from_existing = cls(
            ku_schema_ids=ku_schema_ids,
            ku_ids=ku_ids,
            include_content=include_content,
            library_ids=library_ids,
        )

        create_knowledge_unit_schemas_from_existing.additional_properties = d
        return create_knowledge_unit_schemas_from_existing

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
