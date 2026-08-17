from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.full_knowledge_unit_view import FullKnowledgeUnitView
    from ..models.skipped_knowledge_topic import SkippedKnowledgeTopic


T = TypeVar("T", bound="DuplicateKnowledgeUnitResponse")


@_attrs_define
class DuplicateKnowledgeUnitResponse:
    """Response model for duplicating a knowledge unit

    Attributes:
        data (FullKnowledgeUnitView):
        skipped_knowledge_topics (list[SkippedKnowledgeTopic] | Unset): Array of skipped knowledge topics with their
            reasons
    """

    data: FullKnowledgeUnitView
    skipped_knowledge_topics: list[SkippedKnowledgeTopic] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        skipped_knowledge_topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skipped_knowledge_topics, Unset):
            skipped_knowledge_topics = []
            for skipped_knowledge_topics_item_data in self.skipped_knowledge_topics:
                skipped_knowledge_topics_item = (
                    skipped_knowledge_topics_item_data.to_dict()
                )
                skipped_knowledge_topics.append(skipped_knowledge_topics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if skipped_knowledge_topics is not UNSET:
            field_dict["skipped_knowledge_topics"] = skipped_knowledge_topics

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.full_knowledge_unit_view import FullKnowledgeUnitView
        from ..models.skipped_knowledge_topic import SkippedKnowledgeTopic

        d = dict(src_dict)
        data = FullKnowledgeUnitView.from_dict(d.pop("data"))

        _skipped_knowledge_topics = d.pop("skipped_knowledge_topics", UNSET)
        skipped_knowledge_topics: list[SkippedKnowledgeTopic] | Unset = UNSET
        if _skipped_knowledge_topics is not UNSET:
            skipped_knowledge_topics = []
            for skipped_knowledge_topics_item_data in _skipped_knowledge_topics:
                skipped_knowledge_topics_item = SkippedKnowledgeTopic.from_dict(
                    skipped_knowledge_topics_item_data
                )

                skipped_knowledge_topics.append(skipped_knowledge_topics_item)

        duplicate_knowledge_unit_response = cls(
            data=data,
            skipped_knowledge_topics=skipped_knowledge_topics,
        )

        duplicate_knowledge_unit_response.additional_properties = d
        return duplicate_knowledge_unit_response

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
