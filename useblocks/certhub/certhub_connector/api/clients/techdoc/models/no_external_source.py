from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    Self,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoExternalSource")


@_attrs_define
class NoExternalSource:
    """
    Attributes:
        is_external (Literal['false'] | Unset):  Default: 'false'.
    """

    is_external: Literal["false"] | Unset = "false"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_external = self.is_external

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_external is not UNSET:
            field_dict["is_external"] = is_external

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        is_external = cast(Literal["false"] | Unset, d.pop("is_external", UNSET))
        if is_external != "false" and not isinstance(is_external, Unset):
            raise ValueError(
                f"is_external must match const 'false', got '{is_external}'"
            )

        no_external_source = cls(
            is_external=is_external,
        )

        no_external_source.additional_properties = d
        return no_external_source

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
