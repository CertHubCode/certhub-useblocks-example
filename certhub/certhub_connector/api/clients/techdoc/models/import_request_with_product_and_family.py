from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportRequestWithProductAndFamily")


@_attrs_define
class ImportRequestWithProductAndFamily:
    """Request model for importing units or schemas with product and family

    Attributes:
        files (list[str]): JSON files in string format to import
        product_history_id (None | str | Unset): ID of product history to associate with imported schemas
        family_id (None | str | Unset): ID of product family to associate with imported schemas
    """

    files: list[str]
    product_history_id: None | str | Unset = UNSET
    family_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = self.files

        product_history_id: None | str | Unset
        if isinstance(self.product_history_id, Unset):
            product_history_id = UNSET
        else:
            product_history_id = self.product_history_id

        family_id: None | str | Unset
        if isinstance(self.family_id, Unset):
            family_id = UNSET
        else:
            family_id = self.family_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
            }
        )
        if product_history_id is not UNSET:
            field_dict["product_history_id"] = product_history_id
        if family_id is not UNSET:
            field_dict["family_id"] = family_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        files = cast(list[str], d.pop("files"))

        def _parse_product_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_history_id = _parse_product_history_id(
            d.pop("product_history_id", UNSET)
        )

        def _parse_family_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family_id = _parse_family_id(d.pop("family_id", UNSET))

        import_request_with_product_and_family = cls(
            files=files,
            product_history_id=product_history_id,
            family_id=family_id,
        )

        import_request_with_product_and_family.additional_properties = d
        return import_request_with_product_and_family

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
