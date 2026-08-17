from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.last_action_type import LastActionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditInfo")


@_attrs_define
class AuditInfo:
    """
    Attributes:
        user_id_created (str):
        timestamp_created (datetime.datetime):
        last_action (LastActionType):
        user_id_last_updated (None | str | Unset):
        timestamp_last_updated (datetime.datetime | None | Unset):
        direct_approval_published_at (datetime.datetime | None | Unset):
        direct_approval_published_by (None | str | Unset):
    """

    user_id_created: str
    timestamp_created: datetime.datetime
    last_action: LastActionType
    user_id_last_updated: None | str | Unset = UNSET
    timestamp_last_updated: datetime.datetime | None | Unset = UNSET
    direct_approval_published_at: datetime.datetime | None | Unset = UNSET
    direct_approval_published_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id_created = self.user_id_created

        timestamp_created = self.timestamp_created.isoformat()

        last_action = self.last_action.value

        user_id_last_updated: None | str | Unset
        if isinstance(self.user_id_last_updated, Unset):
            user_id_last_updated = UNSET
        else:
            user_id_last_updated = self.user_id_last_updated

        timestamp_last_updated: None | str | Unset
        if isinstance(self.timestamp_last_updated, Unset):
            timestamp_last_updated = UNSET
        elif isinstance(self.timestamp_last_updated, datetime.datetime):
            timestamp_last_updated = self.timestamp_last_updated.isoformat()
        else:
            timestamp_last_updated = self.timestamp_last_updated

        direct_approval_published_at: None | str | Unset
        if isinstance(self.direct_approval_published_at, Unset):
            direct_approval_published_at = UNSET
        elif isinstance(self.direct_approval_published_at, datetime.datetime):
            direct_approval_published_at = self.direct_approval_published_at.isoformat()
        else:
            direct_approval_published_at = self.direct_approval_published_at

        direct_approval_published_by: None | str | Unset
        if isinstance(self.direct_approval_published_by, Unset):
            direct_approval_published_by = UNSET
        else:
            direct_approval_published_by = self.direct_approval_published_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id_created": user_id_created,
                "timestamp_created": timestamp_created,
                "last_action": last_action,
            }
        )
        if user_id_last_updated is not UNSET:
            field_dict["user_id_last_updated"] = user_id_last_updated
        if timestamp_last_updated is not UNSET:
            field_dict["timestamp_last_updated"] = timestamp_last_updated
        if direct_approval_published_at is not UNSET:
            field_dict["direct_approval_published_at"] = direct_approval_published_at
        if direct_approval_published_by is not UNSET:
            field_dict["direct_approval_published_by"] = direct_approval_published_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_id_created = d.pop("user_id_created")

        timestamp_created = datetime.datetime.fromisoformat(d.pop("timestamp_created"))

        last_action = LastActionType(d.pop("last_action"))

        def _parse_user_id_last_updated(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id_last_updated = _parse_user_id_last_updated(
            d.pop("user_id_last_updated", UNSET)
        )

        def _parse_timestamp_last_updated(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timestamp_last_updated_type_0 = datetime.datetime.fromisoformat(data)

                return timestamp_last_updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timestamp_last_updated = _parse_timestamp_last_updated(
            d.pop("timestamp_last_updated", UNSET)
        )

        def _parse_direct_approval_published_at(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                direct_approval_published_at_type_0 = datetime.datetime.fromisoformat(
                    data
                )

                return direct_approval_published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        direct_approval_published_at = _parse_direct_approval_published_at(
            d.pop("direct_approval_published_at", UNSET)
        )

        def _parse_direct_approval_published_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direct_approval_published_by = _parse_direct_approval_published_by(
            d.pop("direct_approval_published_by", UNSET)
        )

        audit_info = cls(
            user_id_created=user_id_created,
            timestamp_created=timestamp_created,
            last_action=last_action,
            user_id_last_updated=user_id_last_updated,
            timestamp_last_updated=timestamp_last_updated,
            direct_approval_published_at=direct_approval_published_at,
            direct_approval_published_by=direct_approval_published_by,
        )

        audit_info.additional_properties = d
        return audit_info

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
