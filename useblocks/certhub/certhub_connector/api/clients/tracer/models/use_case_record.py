from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.requirement_use_case import RequirementUseCase
from ..types import UNSET, Unset

T = TypeVar("T", bound="UseCaseRecord")


@_attrs_define
class UseCaseRecord:
    """
    Attributes:
        record_id (str):
        related_use_case_topic (RequirementUseCase):
        name (None | str | Unset):
        description (None | str | Unset):
        previous_use_case_record (None | Unset | UseCaseRecord):
    """

    record_id: str
    related_use_case_topic: RequirementUseCase
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    previous_use_case_record: None | Unset | UseCaseRecord = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        related_use_case_topic = self.related_use_case_topic.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        previous_use_case_record: dict[str, Any] | None | Unset
        if isinstance(self.previous_use_case_record, Unset):
            previous_use_case_record = UNSET
        elif isinstance(self.previous_use_case_record, UseCaseRecord):
            previous_use_case_record = self.previous_use_case_record.to_dict()
        else:
            previous_use_case_record = self.previous_use_case_record

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "record_id": record_id,
                "related_use_case_topic": related_use_case_topic,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if previous_use_case_record is not UNSET:
            field_dict["previous_use_case_record"] = previous_use_case_record

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        record_id = d.pop("record_id")

        related_use_case_topic = RequirementUseCase(d.pop("related_use_case_topic"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_previous_use_case_record(
            data: object,
        ) -> None | Unset | UseCaseRecord:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_use_case_record_type_0 = UseCaseRecord.from_dict(data)

                return previous_use_case_record_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UseCaseRecord, data)

        previous_use_case_record = _parse_previous_use_case_record(
            d.pop("previous_use_case_record", UNSET)
        )

        use_case_record = cls(
            record_id=record_id,
            related_use_case_topic=related_use_case_topic,
            name=name,
            description=description,
            previous_use_case_record=previous_use_case_record,
        )

        use_case_record.additional_properties = d
        return use_case_record

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
