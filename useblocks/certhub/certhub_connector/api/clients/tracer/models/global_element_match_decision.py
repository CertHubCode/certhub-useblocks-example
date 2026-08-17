from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlobalElementMatchDecision")


@_attrs_define
class GlobalElementMatchDecision:
    """
    Attributes:
        record_id (str):
        type_ (str):
        object_id (str):
    """

    record_id: str
    type_: str
    object_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        type_ = self.type_

        object_id = self.object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "record_id": record_id,
                "type": type_,
                "object_id": object_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        record_id = d.pop("record_id")

        type_ = d.pop("type")

        object_id = d.pop("object_id")

        global_element_match_decision = cls(
            record_id=record_id,
            type_=type_,
            object_id=object_id,
        )

        global_element_match_decision.additional_properties = d
        return global_element_match_decision

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
