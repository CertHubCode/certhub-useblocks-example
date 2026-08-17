from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MigrateTargetRequest")


@_attrs_define
class MigrateTargetRequest:
    """
    Attributes:
        old_node_identifier (str):
        new_node_identifier (str):
    """

    old_node_identifier: str
    new_node_identifier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        old_node_identifier = self.old_node_identifier

        new_node_identifier = self.new_node_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "old_node_identifier": old_node_identifier,
                "new_node_identifier": new_node_identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        old_node_identifier = d.pop("old_node_identifier")

        new_node_identifier = d.pop("new_node_identifier")

        migrate_target_request = cls(
            old_node_identifier=old_node_identifier,
            new_node_identifier=new_node_identifier,
        )

        migrate_target_request.additional_properties = d
        return migrate_target_request

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
