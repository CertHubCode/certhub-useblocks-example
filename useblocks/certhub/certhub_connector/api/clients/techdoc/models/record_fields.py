from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_field import ConditionalField
    from ..models.missing_field_name import MissingFieldName
    from ..models.record_fields_missing_fields import RecordFieldsMissingFields
    from ..models.record_fields_present_fields import RecordFieldsPresentFields


T = TypeVar("T", bound="RecordFields")


@_attrs_define
class RecordFields:
    """
    Attributes:
        record_id (str):
        present_fields (RecordFieldsPresentFields):
        missing_fields (RecordFieldsMissingFields):
        conditional_fields (list[ConditionalField] | Unset):
        missing_field_names (list[MissingFieldName] | Unset):
    """

    record_id: str
    present_fields: RecordFieldsPresentFields
    missing_fields: RecordFieldsMissingFields
    conditional_fields: list[ConditionalField] | Unset = UNSET
    missing_field_names: list[MissingFieldName] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        present_fields = self.present_fields.to_dict()

        missing_fields = self.missing_fields.to_dict()

        conditional_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditional_fields, Unset):
            conditional_fields = []
            for conditional_fields_item_data in self.conditional_fields:
                conditional_fields_item = conditional_fields_item_data.to_dict()
                conditional_fields.append(conditional_fields_item)

        missing_field_names: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.missing_field_names, Unset):
            missing_field_names = []
            for missing_field_names_item_data in self.missing_field_names:
                missing_field_names_item = missing_field_names_item_data.to_dict()
                missing_field_names.append(missing_field_names_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "record_id": record_id,
                "present_fields": present_fields,
                "missing_fields": missing_fields,
            }
        )
        if conditional_fields is not UNSET:
            field_dict["conditional_fields"] = conditional_fields
        if missing_field_names is not UNSET:
            field_dict["missing_field_names"] = missing_field_names

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.conditional_field import ConditionalField
        from ..models.missing_field_name import MissingFieldName
        from ..models.record_fields_missing_fields import RecordFieldsMissingFields
        from ..models.record_fields_present_fields import RecordFieldsPresentFields

        d = dict(src_dict)
        record_id = d.pop("record_id")

        present_fields = RecordFieldsPresentFields.from_dict(d.pop("present_fields"))

        missing_fields = RecordFieldsMissingFields.from_dict(d.pop("missing_fields"))

        _conditional_fields = d.pop("conditional_fields", UNSET)
        conditional_fields: list[ConditionalField] | Unset = UNSET
        if _conditional_fields is not UNSET:
            conditional_fields = []
            for conditional_fields_item_data in _conditional_fields:
                conditional_fields_item = ConditionalField.from_dict(
                    conditional_fields_item_data
                )

                conditional_fields.append(conditional_fields_item)

        _missing_field_names = d.pop("missing_field_names", UNSET)
        missing_field_names: list[MissingFieldName] | Unset = UNSET
        if _missing_field_names is not UNSET:
            missing_field_names = []
            for missing_field_names_item_data in _missing_field_names:
                missing_field_names_item = MissingFieldName.from_dict(
                    missing_field_names_item_data
                )

                missing_field_names.append(missing_field_names_item)

        record_fields = cls(
            record_id=record_id,
            present_fields=present_fields,
            missing_fields=missing_fields,
            conditional_fields=conditional_fields,
            missing_field_names=missing_field_names,
        )

        record_fields.additional_properties = d
        return record_fields

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
