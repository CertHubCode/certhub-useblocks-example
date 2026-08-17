from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.record_fields import RecordFields
    from ..models.records_summary_input_types import RecordsSummaryInputTypes


T = TypeVar("T", bound="RecordsSummary")


@_attrs_define
class RecordsSummary:
    """
    Attributes:
        records (list[RecordFields]):
        records_with_missing_fields (int):
        input_types (RecordsSummaryInputTypes):
    """

    records: list[RecordFields]
    records_with_missing_fields: int
    input_types: RecordsSummaryInputTypes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        records_with_missing_fields = self.records_with_missing_fields

        input_types = self.input_types.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "records": records,
                "records_with_missing_fields": records_with_missing_fields,
                "input_types": input_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.record_fields import RecordFields
        from ..models.records_summary_input_types import RecordsSummaryInputTypes

        d = dict(src_dict)
        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = RecordFields.from_dict(records_item_data)

            records.append(records_item)

        records_with_missing_fields = d.pop("records_with_missing_fields")

        input_types = RecordsSummaryInputTypes.from_dict(d.pop("input_types"))

        records_summary = cls(
            records=records,
            records_with_missing_fields=records_with_missing_fields,
            input_types=input_types,
        )

        records_summary.additional_properties = d
        return records_summary

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
