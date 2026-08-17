from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ku_statistics import KUStatistics
    from ..models.product_family_fields import ProductFamilyFields


T = TypeVar("T", bound="ProductFamilyAnalytics")


@_attrs_define
class ProductFamilyAnalytics:
    """
    Attributes:
        product_family_id (str):
        product_family_name (str):
        product_family_fields (ProductFamilyFields):
        knowledge_unit_count (int):
        ku_statistics (list[KUStatistics]):
    """

    product_family_id: str
    product_family_name: str
    product_family_fields: ProductFamilyFields
    knowledge_unit_count: int
    ku_statistics: list[KUStatistics]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_family_id = self.product_family_id

        product_family_name = self.product_family_name

        product_family_fields = self.product_family_fields.to_dict()

        knowledge_unit_count = self.knowledge_unit_count

        ku_statistics = []
        for ku_statistics_item_data in self.ku_statistics:
            ku_statistics_item = ku_statistics_item_data.to_dict()
            ku_statistics.append(ku_statistics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_family_id": product_family_id,
                "product_family_name": product_family_name,
                "product_family_fields": product_family_fields,
                "knowledge_unit_count": knowledge_unit_count,
                "ku_statistics": ku_statistics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ku_statistics import KUStatistics
        from ..models.product_family_fields import ProductFamilyFields

        d = dict(src_dict)
        product_family_id = d.pop("product_family_id")

        product_family_name = d.pop("product_family_name")

        product_family_fields = ProductFamilyFields.from_dict(
            d.pop("product_family_fields")
        )

        knowledge_unit_count = d.pop("knowledge_unit_count")

        ku_statistics = []
        _ku_statistics = d.pop("ku_statistics")
        for ku_statistics_item_data in _ku_statistics:
            ku_statistics_item = KUStatistics.from_dict(ku_statistics_item_data)

            ku_statistics.append(ku_statistics_item)

        product_family_analytics = cls(
            product_family_id=product_family_id,
            product_family_name=product_family_name,
            product_family_fields=product_family_fields,
            knowledge_unit_count=knowledge_unit_count,
            ku_statistics=ku_statistics,
        )

        product_family_analytics.additional_properties = d
        return product_family_analytics

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
