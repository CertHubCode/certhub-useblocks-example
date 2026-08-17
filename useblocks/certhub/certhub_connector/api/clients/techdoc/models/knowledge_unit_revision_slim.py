from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KnowledgeUnitRevisionSlim")


@_attrs_define
class KnowledgeUnitRevisionSlim:
    """Minimal revision info for slim list endpoints.

    Attributes:
        id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version_string (str):
        is_latest_approved (bool):
    """

    id: str
    version_string: str
    is_latest_approved: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version_string = self.version_string

        is_latest_approved = self.is_latest_approved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version_string": version_string,
                "is_latest_approved": is_latest_approved,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        version_string = d.pop("version_string")

        is_latest_approved = d.pop("is_latest_approved")

        knowledge_unit_revision_slim = cls(
            id=id,
            version_string=version_string,
            is_latest_approved=is_latest_approved,
        )

        knowledge_unit_revision_slim.additional_properties = d
        return knowledge_unit_revision_slim

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
