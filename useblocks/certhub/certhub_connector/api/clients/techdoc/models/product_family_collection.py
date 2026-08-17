from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_family import ProductFamily


T = TypeVar("T", bound="ProductFamilyCollection")


@_attrs_define
class ProductFamilyCollection:
    """
    Attributes:
        product_families (list[ProductFamily]):
    """

    product_families: list[ProductFamily]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_families = []
        for product_families_item_data in self.product_families:
            product_families_item = product_families_item_data.to_dict()
            product_families.append(product_families_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_families": product_families,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product_family import ProductFamily

        d = dict(src_dict)
        product_families = []
        _product_families = d.pop("product_families")
        for product_families_item_data in _product_families:
            product_families_item = ProductFamily.from_dict(product_families_item_data)

            product_families.append(product_families_item)

        product_family_collection = cls(
            product_families=product_families,
        )

        product_family_collection.additional_properties = d
        return product_family_collection

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
