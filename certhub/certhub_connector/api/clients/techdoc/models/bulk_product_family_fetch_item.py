from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkProductFamilyFetchItem")


@_attrs_define
class BulkProductFamilyFetchItem:
    """A single product family to resolve in a bulk fetch request.

    Attributes:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (None | str | Unset):
        latest_approved (bool | Unset):  Default: False.
    """

    history_id: str
    version: None | str | Unset = UNSET
    latest_approved: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        history_id = self.history_id

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        latest_approved = self.latest_approved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history_id": history_id,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if latest_approved is not UNSET:
            field_dict["latest_approved"] = latest_approved

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        history_id = d.pop("history_id")

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        latest_approved = d.pop("latest_approved", UNSET)

        bulk_product_family_fetch_item = cls(
            history_id=history_id,
            version=version,
            latest_approved=latest_approved,
        )

        bulk_product_family_fetch_item.additional_properties = d
        return bulk_product_family_fetch_item

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
