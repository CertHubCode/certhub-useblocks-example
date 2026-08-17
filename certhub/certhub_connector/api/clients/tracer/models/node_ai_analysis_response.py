from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node_ai_analysis_response_impacted_resolved_nodes import (
        NodeAIAnalysisResponseImpactedResolvedNodes,
    )


T = TypeVar("T", bound="NodeAIAnalysisResponse")


@_attrs_define
class NodeAIAnalysisResponse:
    """
    Attributes:
        reply (str):
        source_node_identifier (str):
        impacted_resolved_nodes (NodeAIAnalysisResponseImpactedResolvedNodes):
    """

    reply: str
    source_node_identifier: str
    impacted_resolved_nodes: NodeAIAnalysisResponseImpactedResolvedNodes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reply = self.reply

        source_node_identifier = self.source_node_identifier

        impacted_resolved_nodes = self.impacted_resolved_nodes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reply": reply,
                "source_node_identifier": source_node_identifier,
                "impacted_resolved_nodes": impacted_resolved_nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node_ai_analysis_response_impacted_resolved_nodes import (
            NodeAIAnalysisResponseImpactedResolvedNodes,
        )

        d = dict(src_dict)
        reply = d.pop("reply")

        source_node_identifier = d.pop("source_node_identifier")

        impacted_resolved_nodes = NodeAIAnalysisResponseImpactedResolvedNodes.from_dict(
            d.pop("impacted_resolved_nodes")
        )

        node_ai_analysis_response = cls(
            reply=reply,
            source_node_identifier=source_node_identifier,
            impacted_resolved_nodes=impacted_resolved_nodes,
        )

        node_ai_analysis_response.additional_properties = d
        return node_ai_analysis_response

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
