from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_knowledge_base import CreateKnowledgeBase


T = TypeVar("T", bound="BodyCreateKnowledgeUnitKuPost")


@_attrs_define
class BodyCreateKnowledgeUnitKuPost:
    """
    Attributes:
        knowledge_unit (CreateKnowledgeBase):
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
    """

    knowledge_unit: CreateKnowledgeBase
    product_history_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_unit = self.knowledge_unit.to_dict()

        product_history_id = self.product_history_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_unit": knowledge_unit,
                "product_history_id": product_history_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_knowledge_base import CreateKnowledgeBase

        d = dict(src_dict)
        knowledge_unit = CreateKnowledgeBase.from_dict(d.pop("knowledge_unit"))

        product_history_id = d.pop("product_history_id")

        body_create_knowledge_unit_ku_post = cls(
            knowledge_unit=knowledge_unit,
            product_history_id=product_history_id,
        )

        body_create_knowledge_unit_ku_post.additional_properties = d
        return body_create_knowledge_unit_ku_post

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
