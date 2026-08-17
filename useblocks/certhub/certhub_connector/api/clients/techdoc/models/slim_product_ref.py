from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SlimProductRef")


@_attrs_define
class SlimProductRef:
    """Minimal product reference: only identity fields, no nested data.

    Attributes:
        field_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        name (str):
    """

    field_id: str
    product_history_id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        product_history_id = self.product_history_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "product_history_id": product_history_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field_id = d.pop("_id")

        product_history_id = d.pop("product_history_id")

        name = d.pop("name")

        slim_product_ref = cls(
            field_id=field_id,
            product_history_id=product_history_id,
            name=name,
        )

        slim_product_ref.additional_properties = d
        return slim_product_ref

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
