from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KnowledgeUnitOption")


@_attrs_define
class KnowledgeUnitOption:
    """Optimized DTO for Dropdowns/Lists.
    Flattens the relationship between History, Product, and Latest Version.

        Attributes:
            knowledge_unit_history_id (str): The Knowledge Unit History ID (stable ID) Example: 5eb7cf5a86d9755df3a6c593.
            current_revision_id (str): The ID of the latest revision Example: 5eb7cf5a86d9755df3a6c593.
            knowledge_unit_name (str):
            product_name (str):
            version_string (str):
            product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
            from_family (bool):
    """

    knowledge_unit_history_id: str
    current_revision_id: str
    knowledge_unit_name: str
    product_name: str
    version_string: str
    product_history_id: str
    from_family: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_unit_history_id = self.knowledge_unit_history_id

        current_revision_id = self.current_revision_id

        knowledge_unit_name = self.knowledge_unit_name

        product_name = self.product_name

        version_string = self.version_string

        product_history_id = self.product_history_id

        from_family = self.from_family

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_unit_history_id": knowledge_unit_history_id,
                "current_revision_id": current_revision_id,
                "knowledge_unit_name": knowledge_unit_name,
                "product_name": product_name,
                "version_string": version_string,
                "product_history_id": product_history_id,
                "from_family": from_family,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        knowledge_unit_history_id = d.pop("knowledge_unit_history_id")

        current_revision_id = d.pop("current_revision_id")

        knowledge_unit_name = d.pop("knowledge_unit_name")

        product_name = d.pop("product_name")

        version_string = d.pop("version_string")

        product_history_id = d.pop("product_history_id")

        from_family = d.pop("from_family")

        knowledge_unit_option = cls(
            knowledge_unit_history_id=knowledge_unit_history_id,
            current_revision_id=current_revision_id,
            knowledge_unit_name=knowledge_unit_name,
            product_name=product_name,
            version_string=version_string,
            product_history_id=product_history_id,
            from_family=from_family,
        )

        knowledge_unit_option.additional_properties = d
        return knowledge_unit_option

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
