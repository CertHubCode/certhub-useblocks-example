from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsRequestModel")


@_attrs_define
class AnalyticsRequestModel:
    """
    Attributes:
        product_history_ids (list[str] | None | Unset):
        kt_ids (list[str] | None | Unset):
        product_family_history_ids (list[str] | None | Unset):
    """

    product_history_ids: list[str] | None | Unset = UNSET
    kt_ids: list[str] | None | Unset = UNSET
    product_family_history_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_history_ids: list[str] | None | Unset
        if isinstance(self.product_history_ids, Unset):
            product_history_ids = UNSET
        elif isinstance(self.product_history_ids, list):
            product_history_ids = self.product_history_ids

        else:
            product_history_ids = self.product_history_ids

        kt_ids: list[str] | None | Unset
        if isinstance(self.kt_ids, Unset):
            kt_ids = UNSET
        elif isinstance(self.kt_ids, list):
            kt_ids = self.kt_ids

        else:
            kt_ids = self.kt_ids

        product_family_history_ids: list[str] | None | Unset
        if isinstance(self.product_family_history_ids, Unset):
            product_family_history_ids = UNSET
        elif isinstance(self.product_family_history_ids, list):
            product_family_history_ids = self.product_family_history_ids

        else:
            product_family_history_ids = self.product_family_history_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_history_ids is not UNSET:
            field_dict["product_history_ids"] = product_history_ids
        if kt_ids is not UNSET:
            field_dict["kt_ids"] = kt_ids
        if product_family_history_ids is not UNSET:
            field_dict["product_family_history_ids"] = product_family_history_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_product_history_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                product_history_ids_type_0 = cast(list[str], data)

                return product_history_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        product_history_ids = _parse_product_history_ids(
            d.pop("product_history_ids", UNSET)
        )

        def _parse_kt_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kt_ids_type_0 = cast(list[str], data)

                return kt_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        kt_ids = _parse_kt_ids(d.pop("kt_ids", UNSET))

        def _parse_product_family_history_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                product_family_history_ids_type_0 = cast(list[str], data)

                return product_family_history_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        product_family_history_ids = _parse_product_family_history_ids(
            d.pop("product_family_history_ids", UNSET)
        )

        analytics_request_model = cls(
            product_history_ids=product_history_ids,
            kt_ids=kt_ids,
            product_family_history_ids=product_family_history_ids,
        )

        analytics_request_model.additional_properties = d
        return analytics_request_model

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
