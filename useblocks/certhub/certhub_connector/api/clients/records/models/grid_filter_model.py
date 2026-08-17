from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grid_logic_operator import GridLogicOperator

if TYPE_CHECKING:
    from ..models.grid_filter_item import GridFilterItem


T = TypeVar("T", bound="GridFilterModel")


@_attrs_define
class GridFilterModel:
    """
    Attributes:
        items (list[GridFilterItem]):
        logic_operator (GridLogicOperator):
    """

    items: list[GridFilterItem]
    logic_operator: GridLogicOperator
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        logic_operator = self.logic_operator.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "logicOperator": logic_operator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grid_filter_item import GridFilterItem

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GridFilterItem.from_dict(items_item_data)

            items.append(items_item)

        logic_operator = GridLogicOperator(d.pop("logicOperator"))

        grid_filter_model = cls(
            items=items,
            logic_operator=logic_operator,
        )

        grid_filter_model.additional_properties = d
        return grid_filter_model

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
