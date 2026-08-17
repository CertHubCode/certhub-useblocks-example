from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_guidance_response_task_states import (
        ProductGuidanceResponseTaskStates,
    )


T = TypeVar("T", bound="ProductGuidanceResponse")


@_attrs_define
class ProductGuidanceResponse:
    """
    Attributes:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        task_states (ProductGuidanceResponseTaskStates):
        id (None | str | Unset):
    """

    product_history_id: str
    task_states: ProductGuidanceResponseTaskStates
    id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_history_id = self.product_history_id

        task_states = self.task_states.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_history_id": product_history_id,
                "task_states": task_states,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product_guidance_response_task_states import (
            ProductGuidanceResponseTaskStates,
        )

        d = dict(src_dict)
        product_history_id = d.pop("product_history_id")

        task_states = ProductGuidanceResponseTaskStates.from_dict(d.pop("task_states"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        product_guidance_response = cls(
            product_history_id=product_history_id,
            task_states=task_states,
            id=id,
        )

        product_guidance_response.additional_properties = d
        return product_guidance_response

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
