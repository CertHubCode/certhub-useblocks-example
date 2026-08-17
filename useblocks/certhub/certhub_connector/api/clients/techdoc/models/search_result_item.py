from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_entity_type import SearchEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResultItem")


@_attrs_define
class SearchResultItem:
    """A single search hit — only the id and the info needed to build a link.

    Attributes:
        id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        type_ (SearchEntityType):
        name (str):
        product_history_id (None | str | Unset):
        knowledge_unit_history_id (None | str | Unset):
    """

    id: str
    type_: SearchEntityType
    name: str
    product_history_id: None | str | Unset = UNSET
    knowledge_unit_history_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        name = self.name

        product_history_id: None | str | Unset
        if isinstance(self.product_history_id, Unset):
            product_history_id = UNSET
        else:
            product_history_id = self.product_history_id

        knowledge_unit_history_id: None | str | Unset
        if isinstance(self.knowledge_unit_history_id, Unset):
            knowledge_unit_history_id = UNSET
        else:
            knowledge_unit_history_id = self.knowledge_unit_history_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "name": name,
            }
        )
        if product_history_id is not UNSET:
            field_dict["product_history_id"] = product_history_id
        if knowledge_unit_history_id is not UNSET:
            field_dict["knowledge_unit_history_id"] = knowledge_unit_history_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = SearchEntityType(d.pop("type"))

        name = d.pop("name")

        def _parse_product_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_history_id = _parse_product_history_id(
            d.pop("product_history_id", UNSET)
        )

        def _parse_knowledge_unit_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_history_id = _parse_knowledge_unit_history_id(
            d.pop("knowledge_unit_history_id", UNSET)
        )

        search_result_item = cls(
            id=id,
            type_=type_,
            name=name,
            product_history_id=product_history_id,
            knowledge_unit_history_id=knowledge_unit_history_id,
        )

        search_result_item.additional_properties = d
        return search_result_item

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
