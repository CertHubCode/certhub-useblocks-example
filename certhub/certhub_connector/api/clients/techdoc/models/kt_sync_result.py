from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kt_sync_result_status import KtSyncResultStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="KtSyncResult")


@_attrs_define
class KtSyncResult:
    """Per-knowledge-topic outcome of an 'Update Underlying Schema' action.

    Attributes:
        knowledge_topic_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_topic_name (str):
        status (KtSyncResultStatus):
        reason (None | str | Unset):
    """

    knowledge_topic_history_id: str
    knowledge_topic_name: str
    status: KtSyncResultStatus
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_topic_history_id = self.knowledge_topic_history_id

        knowledge_topic_name = self.knowledge_topic_name

        status = self.status.value

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_topic_history_id": knowledge_topic_history_id,
                "knowledge_topic_name": knowledge_topic_name,
                "status": status,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        knowledge_topic_history_id = d.pop("knowledge_topic_history_id")

        knowledge_topic_name = d.pop("knowledge_topic_name")

        status = KtSyncResultStatus(d.pop("status"))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        kt_sync_result = cls(
            knowledge_topic_history_id=knowledge_topic_history_id,
            knowledge_topic_name=knowledge_topic_name,
            status=status,
            reason=reason,
        )

        kt_sync_result.additional_properties = d
        return kt_sync_result

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
