from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalElementBulkRequest")


@_attrs_define
class GlobalElementBulkRequest:
    """
    Attributes:
        ids (list[str]):
        include_schema (bool | Unset):  Default: True.
    """

    ids: list[str]
    include_schema: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        include_schema = self.include_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if include_schema is not UNSET:
            field_dict["include_schema"] = include_schema

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        include_schema = d.pop("include_schema", UNSET)

        global_element_bulk_request = cls(
            ids=ids,
            include_schema=include_schema,
        )

        global_element_bulk_request.additional_properties = d
        return global_element_bulk_request

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
