from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KUStatistics")


@_attrs_define
class KUStatistics:
    """
    Attributes:
        ku_name (str):
        ku_history_id (str):
        ku_current_version (str):
        ku_has_approved (bool):
        ku_is_latest_approved (bool):
        ku_latest_approved_version (str):
    """

    ku_name: str
    ku_history_id: str
    ku_current_version: str
    ku_has_approved: bool
    ku_is_latest_approved: bool
    ku_latest_approved_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ku_name = self.ku_name

        ku_history_id = self.ku_history_id

        ku_current_version = self.ku_current_version

        ku_has_approved = self.ku_has_approved

        ku_is_latest_approved = self.ku_is_latest_approved

        ku_latest_approved_version = self.ku_latest_approved_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ku_name": ku_name,
                "ku_history_id": ku_history_id,
                "ku_current_version": ku_current_version,
                "ku_has_approved": ku_has_approved,
                "ku_is_latest_approved": ku_is_latest_approved,
                "ku_latest_approved_version": ku_latest_approved_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ku_name = d.pop("ku_name")

        ku_history_id = d.pop("ku_history_id")

        ku_current_version = d.pop("ku_current_version")

        ku_has_approved = d.pop("ku_has_approved")

        ku_is_latest_approved = d.pop("ku_is_latest_approved")

        ku_latest_approved_version = d.pop("ku_latest_approved_version")

        ku_statistics = cls(
            ku_name=ku_name,
            ku_history_id=ku_history_id,
            ku_current_version=ku_current_version,
            ku_has_approved=ku_has_approved,
            ku_is_latest_approved=ku_is_latest_approved,
            ku_latest_approved_version=ku_latest_approved_version,
        )

        ku_statistics.additional_properties = d
        return ku_statistics

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
