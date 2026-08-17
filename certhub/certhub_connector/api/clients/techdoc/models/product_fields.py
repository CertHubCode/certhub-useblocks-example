from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_fields_values import ProductFieldsValues


T = TypeVar("T", bound="ProductFields")


@_attrs_define
class ProductFields:
    """
    Attributes:
        present_fields (list[str]):
        missing_fields (list[str]):
        values (ProductFieldsValues):
        has_product_family (bool):
        product_family_count (int):
    """

    present_fields: list[str]
    missing_fields: list[str]
    values: ProductFieldsValues
    has_product_family: bool
    product_family_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        present_fields = self.present_fields

        missing_fields = self.missing_fields

        values = self.values.to_dict()

        has_product_family = self.has_product_family

        product_family_count = self.product_family_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "present_fields": present_fields,
                "missing_fields": missing_fields,
                "values": values,
                "has_product_family": has_product_family,
                "product_family_count": product_family_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product_fields_values import ProductFieldsValues

        d = dict(src_dict)
        present_fields = cast(list[str], d.pop("present_fields"))

        missing_fields = cast(list[str], d.pop("missing_fields"))

        values = ProductFieldsValues.from_dict(d.pop("values"))

        has_product_family = d.pop("has_product_family")

        product_family_count = d.pop("product_family_count")

        product_fields = cls(
            present_fields=present_fields,
            missing_fields=missing_fields,
            values=values,
            has_product_family=has_product_family,
            product_family_count=product_family_count,
        )

        product_fields.additional_properties = d
        return product_fields

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
