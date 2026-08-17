from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MissingFieldName")


@_attrs_define
class MissingFieldName:
    """
    Attributes:
        record_display_name (str):
        missing_field_name (str):
    """

    record_display_name: str
    missing_field_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_display_name = self.record_display_name

        missing_field_name = self.missing_field_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "record_display_name": record_display_name,
                "missing_field_name": missing_field_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        record_display_name = d.pop("record_display_name")

        missing_field_name = d.pop("missing_field_name")

        missing_field_name = cls(
            record_display_name=record_display_name,
            missing_field_name=missing_field_name,
        )

        missing_field_name.additional_properties = d
        return missing_field_name

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
