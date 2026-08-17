from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_topic_type import KnowledgeTopicType

if TYPE_CHECKING:
    from ..models.records_summary import RecordsSummary


T = TypeVar("T", bound="KTAnalytics")


@_attrs_define
class KTAnalytics:
    """
    Attributes:
        knowledge_topic_id (str):
        knowledge_topic_name (str):
        type_ (KnowledgeTopicType):
        records_summary (RecordsSummary):
        related_product_id (str):
        related_knowledge_unit_id (str):
    """

    knowledge_topic_id: str
    knowledge_topic_name: str
    type_: KnowledgeTopicType
    records_summary: RecordsSummary
    related_product_id: str
    related_knowledge_unit_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_topic_id = self.knowledge_topic_id

        knowledge_topic_name = self.knowledge_topic_name

        type_ = self.type_.value

        records_summary = self.records_summary.to_dict()

        related_product_id = self.related_product_id

        related_knowledge_unit_id = self.related_knowledge_unit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_topic_id": knowledge_topic_id,
                "knowledge_topic_name": knowledge_topic_name,
                "type": type_,
                "records_summary": records_summary,
                "related_product_id": related_product_id,
                "related_knowledge_unit_id": related_knowledge_unit_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.records_summary import RecordsSummary

        d = dict(src_dict)
        knowledge_topic_id = d.pop("knowledge_topic_id")

        knowledge_topic_name = d.pop("knowledge_topic_name")

        type_ = KnowledgeTopicType(d.pop("type"))

        records_summary = RecordsSummary.from_dict(d.pop("records_summary"))

        related_product_id = d.pop("related_product_id")

        related_knowledge_unit_id = d.pop("related_knowledge_unit_id")

        kt_analytics = cls(
            knowledge_topic_id=knowledge_topic_id,
            knowledge_topic_name=knowledge_topic_name,
            type_=type_,
            records_summary=records_summary,
            related_product_id=related_product_id,
            related_knowledge_unit_id=related_knowledge_unit_id,
        )

        kt_analytics.additional_properties = d
        return kt_analytics

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
