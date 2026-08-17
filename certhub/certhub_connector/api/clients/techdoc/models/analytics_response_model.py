from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kt_analytics import KTAnalytics
    from ..models.product_analytics import ProductAnalytics
    from ..models.product_family_analytics import ProductFamilyAnalytics


T = TypeVar("T", bound="AnalyticsResponseModel")


@_attrs_define
class AnalyticsResponseModel:
    """
    Attributes:
        products (list[ProductAnalytics]):
        kts (list[KTAnalytics]):
        product_families (list[ProductFamilyAnalytics] | Unset):
    """

    products: list[ProductAnalytics]
    kts: list[KTAnalytics]
    product_families: list[ProductFamilyAnalytics] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        kts = []
        for kts_item_data in self.kts:
            kts_item = kts_item_data.to_dict()
            kts.append(kts_item)

        product_families: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_families, Unset):
            product_families = []
            for product_families_item_data in self.product_families:
                product_families_item = product_families_item_data.to_dict()
                product_families.append(product_families_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
                "kts": kts,
            }
        )
        if product_families is not UNSET:
            field_dict["product_families"] = product_families

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kt_analytics import KTAnalytics
        from ..models.product_analytics import ProductAnalytics
        from ..models.product_family_analytics import ProductFamilyAnalytics

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = ProductAnalytics.from_dict(products_item_data)

            products.append(products_item)

        kts = []
        _kts = d.pop("kts")
        for kts_item_data in _kts:
            kts_item = KTAnalytics.from_dict(kts_item_data)

            kts.append(kts_item)

        _product_families = d.pop("product_families", UNSET)
        product_families: list[ProductFamilyAnalytics] | Unset = UNSET
        if _product_families is not UNSET:
            product_families = []
            for product_families_item_data in _product_families:
                product_families_item = ProductFamilyAnalytics.from_dict(
                    product_families_item_data
                )

                product_families.append(product_families_item)

        analytics_response_model = cls(
            products=products,
            kts=kts,
            product_families=product_families,
        )

        analytics_response_model.additional_properties = d
        return analytics_response_model

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
