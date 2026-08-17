from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connected_nodes_response_target_node_map import (
        ConnectedNodesResponseTargetNodeMap,
    )
    from ..models.edge_with_depth import EdgeWithDepth
    from ..models.node import Node


T = TypeVar("T", bound="ConnectedNodesResponse")


@_attrs_define
class ConnectedNodesResponse:
    """
    Attributes:
        source_node (Node):
        target_node_map (ConnectedNodesResponseTargetNodeMap):
        edges (list[EdgeWithDepth] | None | Unset):
    """

    source_node: Node
    target_node_map: ConnectedNodesResponseTargetNodeMap
    edges: list[EdgeWithDepth] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_node = self.source_node.to_dict()

        target_node_map = self.target_node_map.to_dict()

        edges: list[dict[str, Any]] | None | Unset
        if isinstance(self.edges, Unset):
            edges = UNSET
        elif isinstance(self.edges, list):
            edges = []
            for edges_type_0_item_data in self.edges:
                edges_type_0_item = edges_type_0_item_data.to_dict()
                edges.append(edges_type_0_item)

        else:
            edges = self.edges

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_node": source_node,
                "target_node_map": target_node_map,
            }
        )
        if edges is not UNSET:
            field_dict["edges"] = edges

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.connected_nodes_response_target_node_map import (
            ConnectedNodesResponseTargetNodeMap,
        )
        from ..models.edge_with_depth import EdgeWithDepth
        from ..models.node import Node

        d = dict(src_dict)
        source_node = Node.from_dict(d.pop("source_node"))

        target_node_map = ConnectedNodesResponseTargetNodeMap.from_dict(
            d.pop("target_node_map")
        )

        def _parse_edges(data: object) -> list[EdgeWithDepth] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                edges_type_0 = []
                _edges_type_0 = data
                for edges_type_0_item_data in _edges_type_0:
                    edges_type_0_item = EdgeWithDepth.from_dict(edges_type_0_item_data)

                    edges_type_0.append(edges_type_0_item)

                return edges_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EdgeWithDepth] | None | Unset, data)

        edges = _parse_edges(d.pop("edges", UNSET))

        connected_nodes_response = cls(
            source_node=source_node,
            target_node_map=target_node_map,
            edges=edges,
        )

        connected_nodes_response.additional_properties = d
        return connected_nodes_response

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
