from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VersionData")


@_attrs_define
class VersionData:
    """
    Attributes:
        version (str):
        revision_id (str): the id of each revision
        commit_message (None | str):
        is_latest_approved (bool | None):
    """

    version: str
    revision_id: str
    commit_message: None | str
    is_latest_approved: bool | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        revision_id = self.revision_id

        commit_message: None | str
        commit_message = self.commit_message

        is_latest_approved: bool | None
        is_latest_approved = self.is_latest_approved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "revision_id": revision_id,
                "commit_message": commit_message,
                "is_latest_approved": is_latest_approved,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        version = d.pop("version")

        revision_id = d.pop("revision_id")

        def _parse_commit_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        commit_message = _parse_commit_message(d.pop("commit_message"))

        def _parse_is_latest_approved(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_latest_approved = _parse_is_latest_approved(d.pop("is_latest_approved"))

        version_data = cls(
            version=version,
            revision_id=revision_id,
            commit_message=commit_message,
            is_latest_approved=is_latest_approved,
        )

        version_data.additional_properties = d
        return version_data

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
