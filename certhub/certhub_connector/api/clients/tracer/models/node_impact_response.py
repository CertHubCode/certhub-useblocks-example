from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node_impact_response_impacted_resolved_nodes import (
        NodeImpactResponseImpactedResolvedNodes,
    )


T = TypeVar("T", bound="NodeImpactResponse")


@_attrs_define
class NodeImpactResponse:
    """V1: list of resolved node entities that are impacted by the changed object
    V2: additional information about impacted fields
    V3: diff between old and new values (maybe in tiptap format)

        Attributes:
            impacted_resolved_nodes (NodeImpactResponseImpactedResolvedNodes):
    """

    impacted_resolved_nodes: NodeImpactResponseImpactedResolvedNodes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        impacted_resolved_nodes = self.impacted_resolved_nodes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "impacted_resolved_nodes": impacted_resolved_nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node_impact_response_impacted_resolved_nodes import (
            NodeImpactResponseImpactedResolvedNodes,
        )

        d = dict(src_dict)
        impacted_resolved_nodes = NodeImpactResponseImpactedResolvedNodes.from_dict(
            d.pop("impacted_resolved_nodes")
        )

        node_impact_response = cls(
            impacted_resolved_nodes=impacted_resolved_nodes,
        )

        node_impact_response.additional_properties = d
        return node_impact_response

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
