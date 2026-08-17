from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_properties import ProductProperties


T = TypeVar("T", bound="CreateProductFamily")


@_attrs_define
class CreateProductFamily:
    """
    Attributes:
        name (str):
        product_properties (ProductProperties):
    """

    name: str
    product_properties: ProductProperties
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        product_properties = self.product_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "product_properties": product_properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product_properties import ProductProperties

        d = dict(src_dict)
        name = d.pop("name")

        product_properties = ProductProperties.from_dict(d.pop("product_properties"))

        create_product_family = cls(
            name=name,
            product_properties=product_properties,
        )

        create_product_family.additional_properties = d
        return create_product_family

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
