from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slim_library_response import SlimLibraryResponse


T = TypeVar("T", bound="SlimKnowledgeUnitSchemaResponse")


@_attrs_define
class SlimKnowledgeUnitSchemaResponse:
    """
    Attributes:
        id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_name (str):
        major_version (int):
        minor_version (int):
        is_latest_approved (bool):
        read_only (bool):
        libraries (list[SlimLibraryResponse] | Unset):
    """

    id: str
    knowledge_unit_schema_history_id: str
    knowledge_unit_name: str
    major_version: int
    minor_version: int
    is_latest_approved: bool
    read_only: bool
    libraries: list[SlimLibraryResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        knowledge_unit_schema_history_id = self.knowledge_unit_schema_history_id

        knowledge_unit_name = self.knowledge_unit_name

        major_version = self.major_version

        minor_version = self.minor_version

        is_latest_approved = self.is_latest_approved

        read_only = self.read_only

        libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()
                libraries.append(libraries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "knowledge_unit_schema_history_id": knowledge_unit_schema_history_id,
                "knowledge_unit_name": knowledge_unit_name,
                "major_version": major_version,
                "minor_version": minor_version,
                "is_latest_approved": is_latest_approved,
                "read_only": read_only,
            }
        )
        if libraries is not UNSET:
            field_dict["libraries"] = libraries

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.slim_library_response import SlimLibraryResponse

        d = dict(src_dict)
        id = d.pop("id")

        knowledge_unit_schema_history_id = d.pop("knowledge_unit_schema_history_id")

        knowledge_unit_name = d.pop("knowledge_unit_name")

        major_version = d.pop("major_version")

        minor_version = d.pop("minor_version")

        is_latest_approved = d.pop("is_latest_approved")

        read_only = d.pop("read_only")

        _libraries = d.pop("libraries", UNSET)
        libraries: list[SlimLibraryResponse] | Unset = UNSET
        if _libraries is not UNSET:
            libraries = []
            for libraries_item_data in _libraries:
                libraries_item = SlimLibraryResponse.from_dict(libraries_item_data)

                libraries.append(libraries_item)

        slim_knowledge_unit_schema_response = cls(
            id=id,
            knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
            knowledge_unit_name=knowledge_unit_name,
            major_version=major_version,
            minor_version=minor_version,
            is_latest_approved=is_latest_approved,
            read_only=read_only,
            libraries=libraries,
        )

        slim_knowledge_unit_schema_response.additional_properties = d
        return slim_knowledge_unit_schema_response

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
