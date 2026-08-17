from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_topic_detail_response import KnowledgeTopicDetailResponse


T = TypeVar("T", bound="BulkKnowledgeTopicFetchResult")


@_attrs_define
class BulkKnowledgeTopicFetchResult:
    """Per-item result, returned in request order. One failure does not fail the batch.

    Attributes:
        requested_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        success (bool):
        knowledge_topic (KnowledgeTopicDetailResponse | None | Unset):
        error (None | str | Unset):
    """

    requested_id: str
    success: bool
    knowledge_topic: KnowledgeTopicDetailResponse | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.knowledge_topic_detail_response import (
            KnowledgeTopicDetailResponse,
        )

        requested_id = self.requested_id

        success = self.success

        knowledge_topic: dict[str, Any] | None | Unset
        if isinstance(self.knowledge_topic, Unset):
            knowledge_topic = UNSET
        elif isinstance(self.knowledge_topic, KnowledgeTopicDetailResponse):
            knowledge_topic = self.knowledge_topic.to_dict()
        else:
            knowledge_topic = self.knowledge_topic

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requested_id": requested_id,
                "success": success,
            }
        )
        if knowledge_topic is not UNSET:
            field_dict["knowledge_topic"] = knowledge_topic
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_topic_detail_response import (
            KnowledgeTopicDetailResponse,
        )

        d = dict(src_dict)
        requested_id = d.pop("requested_id")

        success = d.pop("success")

        def _parse_knowledge_topic(
            data: object,
        ) -> KnowledgeTopicDetailResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                knowledge_topic_type_0 = KnowledgeTopicDetailResponse.from_dict(data)

                return knowledge_topic_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KnowledgeTopicDetailResponse | None | Unset, data)

        knowledge_topic = _parse_knowledge_topic(d.pop("knowledge_topic", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        bulk_knowledge_topic_fetch_result = cls(
            requested_id=requested_id,
            success=success,
            knowledge_topic=knowledge_topic,
            error=error,
        )

        bulk_knowledge_topic_fetch_result.additional_properties = d
        return bulk_knowledge_topic_fetch_result

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
