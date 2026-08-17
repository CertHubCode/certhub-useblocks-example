from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conditional_field_status import ConditionalFieldStatus
from ..models.input_type import InputType

T = TypeVar("T", bound="ConditionalField")


@_attrs_define
class ConditionalField:
    """
    Attributes:
        key (str):
        input_type (InputType):
        status (ConditionalFieldStatus):
        hide_expression (str):
    """

    key: str
    input_type: InputType
    status: ConditionalFieldStatus
    hide_expression: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        input_type = self.input_type.value

        status = self.status.value

        hide_expression = self.hide_expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "input_type": input_type,
                "status": status,
                "hide_expression": hide_expression,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        input_type = InputType(d.pop("input_type"))

        status = ConditionalFieldStatus(d.pop("status"))

        hide_expression = d.pop("hide_expression")

        conditional_field = cls(
            key=key,
            input_type=input_type,
            status=status,
            hide_expression=hide_expression,
        )

        conditional_field.additional_properties = d
        return conditional_field

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
