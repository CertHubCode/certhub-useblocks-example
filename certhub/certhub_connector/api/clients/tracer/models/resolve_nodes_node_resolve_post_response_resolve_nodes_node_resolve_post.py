from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resolved_node_entity import ResolvedNodeEntity
    from ..models.resolved_node_entity_with_linked_entities import (
        ResolvedNodeEntityWithLinkedEntities,
    )


T = TypeVar("T", bound="ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost")


@_attrs_define
class ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost:
    """ """

    additional_properties: dict[
        str, None | ResolvedNodeEntity | ResolvedNodeEntityWithLinkedEntities
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resolved_node_entity import ResolvedNodeEntity
        from ..models.resolved_node_entity_with_linked_entities import (
            ResolvedNodeEntityWithLinkedEntities,
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, ResolvedNodeEntity) or isinstance(
                prop, ResolvedNodeEntityWithLinkedEntities
            ):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resolved_node_entity import ResolvedNodeEntity
        from ..models.resolved_node_entity_with_linked_entities import (
            ResolvedNodeEntityWithLinkedEntities,
        )

        d = dict(src_dict)
        resolve_nodes_node_resolve_post_response_resolve_nodes_node_resolve_post = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> None | ResolvedNodeEntity | ResolvedNodeEntityWithLinkedEntities:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = ResolvedNodeEntity.from_dict(data)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = (
                        ResolvedNodeEntityWithLinkedEntities.from_dict(data)
                    )

                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(
                    None | ResolvedNodeEntity | ResolvedNodeEntityWithLinkedEntities,
                    data,
                )

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        resolve_nodes_node_resolve_post_response_resolve_nodes_node_resolve_post.additional_properties = additional_properties
        return resolve_nodes_node_resolve_post_response_resolve_nodes_node_resolve_post

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> None | ResolvedNodeEntity | ResolvedNodeEntityWithLinkedEntities:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: None | ResolvedNodeEntity | ResolvedNodeEntityWithLinkedEntities,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
