from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_family_fields_values import ProductFamilyFieldsValues


T = TypeVar("T", bound="ProductFamilyFields")


@_attrs_define
class ProductFamilyFields:
    """
    Attributes:
        present_fields (list[str]):
        missing_fields (list[str]):
        values (ProductFamilyFieldsValues):
    """

    present_fields: list[str]
    missing_fields: list[str]
    values: ProductFamilyFieldsValues
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        present_fields = self.present_fields

        missing_fields = self.missing_fields

        values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "present_fields": present_fields,
                "missing_fields": missing_fields,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product_family_fields_values import ProductFamilyFieldsValues

        d = dict(src_dict)
        present_fields = cast(list[str], d.pop("present_fields"))

        missing_fields = cast(list[str], d.pop("missing_fields"))

        values = ProductFamilyFieldsValues.from_dict(d.pop("values"))

        product_family_fields = cls(
            present_fields=present_fields,
            missing_fields=missing_fields,
            values=values,
        )

        product_family_fields.additional_properties = d
        return product_family_fields

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
