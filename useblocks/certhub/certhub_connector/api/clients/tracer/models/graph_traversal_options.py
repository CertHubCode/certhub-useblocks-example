from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.graph_traversal_options_direction import GraphTraversalOptionsDirection
from ..models.node_type import NodeType
from ..models.relation_type import RelationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphTraversalOptions")


@_attrs_define
class GraphTraversalOptions:
    """
    Attributes:
        direction (GraphTraversalOptionsDirection | Unset):  Default: GraphTraversalOptionsDirection.FORWARD.
        allowed_node_types (list[NodeType] | None | Unset):
        excluded_node_types (list[NodeType] | None | Unset):
        allowed_relation_types (list[RelationType] | None | Unset):
        excluded_relation_types (list[RelationType] | None | Unset):
        max_depth (int | Unset):  Default: 2.
    """

    direction: GraphTraversalOptionsDirection | Unset = (
        GraphTraversalOptionsDirection.FORWARD
    )
    allowed_node_types: list[NodeType] | None | Unset = UNSET
    excluded_node_types: list[NodeType] | None | Unset = UNSET
    allowed_relation_types: list[RelationType] | None | Unset = UNSET
    excluded_relation_types: list[RelationType] | None | Unset = UNSET
    max_depth: int | Unset = 2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        allowed_node_types: list[str] | None | Unset
        if isinstance(self.allowed_node_types, Unset):
            allowed_node_types = UNSET
        elif isinstance(self.allowed_node_types, list):
            allowed_node_types = []
            for allowed_node_types_type_0_item_data in self.allowed_node_types:
                allowed_node_types_type_0_item = (
                    allowed_node_types_type_0_item_data.value
                )
                allowed_node_types.append(allowed_node_types_type_0_item)

        else:
            allowed_node_types = self.allowed_node_types

        excluded_node_types: list[str] | None | Unset
        if isinstance(self.excluded_node_types, Unset):
            excluded_node_types = UNSET
        elif isinstance(self.excluded_node_types, list):
            excluded_node_types = []
            for excluded_node_types_type_0_item_data in self.excluded_node_types:
                excluded_node_types_type_0_item = (
                    excluded_node_types_type_0_item_data.value
                )
                excluded_node_types.append(excluded_node_types_type_0_item)

        else:
            excluded_node_types = self.excluded_node_types

        allowed_relation_types: list[str] | None | Unset
        if isinstance(self.allowed_relation_types, Unset):
            allowed_relation_types = UNSET
        elif isinstance(self.allowed_relation_types, list):
            allowed_relation_types = []
            for allowed_relation_types_type_0_item_data in self.allowed_relation_types:
                allowed_relation_types_type_0_item = (
                    allowed_relation_types_type_0_item_data.value
                )
                allowed_relation_types.append(allowed_relation_types_type_0_item)

        else:
            allowed_relation_types = self.allowed_relation_types

        excluded_relation_types: list[str] | None | Unset
        if isinstance(self.excluded_relation_types, Unset):
            excluded_relation_types = UNSET
        elif isinstance(self.excluded_relation_types, list):
            excluded_relation_types = []
            for (
                excluded_relation_types_type_0_item_data
            ) in self.excluded_relation_types:
                excluded_relation_types_type_0_item = (
                    excluded_relation_types_type_0_item_data.value
                )
                excluded_relation_types.append(excluded_relation_types_type_0_item)

        else:
            excluded_relation_types = self.excluded_relation_types

        max_depth = self.max_depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direction is not UNSET:
            field_dict["direction"] = direction
        if allowed_node_types is not UNSET:
            field_dict["allowed_node_types"] = allowed_node_types
        if excluded_node_types is not UNSET:
            field_dict["excluded_node_types"] = excluded_node_types
        if allowed_relation_types is not UNSET:
            field_dict["allowed_relation_types"] = allowed_relation_types
        if excluded_relation_types is not UNSET:
            field_dict["excluded_relation_types"] = excluded_relation_types
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _direction = d.pop("direction", UNSET)
        direction: GraphTraversalOptionsDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = GraphTraversalOptionsDirection(_direction)

        def _parse_allowed_node_types(data: object) -> list[NodeType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_node_types_type_0 = []
                _allowed_node_types_type_0 = data
                for allowed_node_types_type_0_item_data in _allowed_node_types_type_0:
                    allowed_node_types_type_0_item = NodeType(
                        allowed_node_types_type_0_item_data
                    )

                    allowed_node_types_type_0.append(allowed_node_types_type_0_item)

                return allowed_node_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NodeType] | None | Unset, data)

        allowed_node_types = _parse_allowed_node_types(
            d.pop("allowed_node_types", UNSET)
        )

        def _parse_excluded_node_types(data: object) -> list[NodeType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_node_types_type_0 = []
                _excluded_node_types_type_0 = data
                for excluded_node_types_type_0_item_data in _excluded_node_types_type_0:
                    excluded_node_types_type_0_item = NodeType(
                        excluded_node_types_type_0_item_data
                    )

                    excluded_node_types_type_0.append(excluded_node_types_type_0_item)

                return excluded_node_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NodeType] | None | Unset, data)

        excluded_node_types = _parse_excluded_node_types(
            d.pop("excluded_node_types", UNSET)
        )

        def _parse_allowed_relation_types(
            data: object,
        ) -> list[RelationType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_relation_types_type_0 = []
                _allowed_relation_types_type_0 = data
                for (
                    allowed_relation_types_type_0_item_data
                ) in _allowed_relation_types_type_0:
                    allowed_relation_types_type_0_item = RelationType(
                        allowed_relation_types_type_0_item_data
                    )

                    allowed_relation_types_type_0.append(
                        allowed_relation_types_type_0_item
                    )

                return allowed_relation_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RelationType] | None | Unset, data)

        allowed_relation_types = _parse_allowed_relation_types(
            d.pop("allowed_relation_types", UNSET)
        )

        def _parse_excluded_relation_types(
            data: object,
        ) -> list[RelationType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_relation_types_type_0 = []
                _excluded_relation_types_type_0 = data
                for (
                    excluded_relation_types_type_0_item_data
                ) in _excluded_relation_types_type_0:
                    excluded_relation_types_type_0_item = RelationType(
                        excluded_relation_types_type_0_item_data
                    )

                    excluded_relation_types_type_0.append(
                        excluded_relation_types_type_0_item
                    )

                return excluded_relation_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RelationType] | None | Unset, data)

        excluded_relation_types = _parse_excluded_relation_types(
            d.pop("excluded_relation_types", UNSET)
        )

        max_depth = d.pop("max_depth", UNSET)

        graph_traversal_options = cls(
            direction=direction,
            allowed_node_types=allowed_node_types,
            excluded_node_types=excluded_node_types,
            allowed_relation_types=allowed_relation_types,
            excluded_relation_types=excluded_relation_types,
            max_depth=max_depth,
        )

        graph_traversal_options.additional_properties = d
        return graph_traversal_options

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
