from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecordDuplicateBatch")


@_attrs_define
class RecordDuplicateBatch:
    """
    Attributes:
        source_ku_id (str):
        source_kt_id (str):
        source_product_id (None | str):
        target_ku_id (str):
        target_kt_id (str):
        target_product_id (None | str):
    """

    source_ku_id: str
    source_kt_id: str
    source_product_id: None | str
    target_ku_id: str
    target_kt_id: str
    target_product_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_ku_id = self.source_ku_id

        source_kt_id = self.source_kt_id

        source_product_id: None | str
        source_product_id = self.source_product_id

        target_ku_id = self.target_ku_id

        target_kt_id = self.target_kt_id

        target_product_id: None | str
        target_product_id = self.target_product_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_ku_id": source_ku_id,
                "source_kt_id": source_kt_id,
                "source_product_id": source_product_id,
                "target_ku_id": target_ku_id,
                "target_kt_id": target_kt_id,
                "target_product_id": target_product_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_ku_id = d.pop("source_ku_id")

        source_kt_id = d.pop("source_kt_id")

        def _parse_source_product_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_product_id = _parse_source_product_id(d.pop("source_product_id"))

        target_ku_id = d.pop("target_ku_id")

        target_kt_id = d.pop("target_kt_id")

        def _parse_target_product_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_product_id = _parse_target_product_id(d.pop("target_product_id"))

        record_duplicate_batch = cls(
            source_ku_id=source_ku_id,
            source_kt_id=source_kt_id,
            source_product_id=source_product_id,
            target_ku_id=target_ku_id,
            target_kt_id=target_kt_id,
            target_product_id=target_product_id,
        )

        record_duplicate_batch.additional_properties = d
        return record_duplicate_batch

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
