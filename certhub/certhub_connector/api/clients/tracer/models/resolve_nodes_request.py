from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolve_nodes_request_linked_entity_filters_type_0 import (
        ResolveNodesRequestLinkedEntityFiltersType0,
    )


T = TypeVar("T", bound="ResolveNodesRequest")


@_attrs_define
class ResolveNodesRequest:
    """Request body for POST /node/resolve (node_identifiers may be empty).

    Attributes:
        node_identifiers (list[str] | Unset):
        include_data (bool | Unset):  Default: False.
        with_linked_entities (bool | Unset):  Default: False.
        linked_entity_filters (None | ResolveNodesRequestLinkedEntityFiltersType0 | Unset): When with_linked_entities is
            True: maps each node identifier to allowed linked_* groups (e.g. linked_documents,
            linked_global_element_entries). None means resolve requested nodes only — no hop-1 trace targets are loaded.
    """

    node_identifiers: list[str] | Unset = UNSET
    include_data: bool | Unset = False
    with_linked_entities: bool | Unset = False
    linked_entity_filters: (
        None | ResolveNodesRequestLinkedEntityFiltersType0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resolve_nodes_request_linked_entity_filters_type_0 import (
            ResolveNodesRequestLinkedEntityFiltersType0,
        )

        node_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.node_identifiers, Unset):
            node_identifiers = self.node_identifiers

        include_data = self.include_data

        with_linked_entities = self.with_linked_entities

        linked_entity_filters: dict[str, Any] | None | Unset
        if isinstance(self.linked_entity_filters, Unset):
            linked_entity_filters = UNSET
        elif isinstance(
            self.linked_entity_filters, ResolveNodesRequestLinkedEntityFiltersType0
        ):
            linked_entity_filters = self.linked_entity_filters.to_dict()
        else:
            linked_entity_filters = self.linked_entity_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_identifiers is not UNSET:
            field_dict["node_identifiers"] = node_identifiers
        if include_data is not UNSET:
            field_dict["include_data"] = include_data
        if with_linked_entities is not UNSET:
            field_dict["with_linked_entities"] = with_linked_entities
        if linked_entity_filters is not UNSET:
            field_dict["linked_entity_filters"] = linked_entity_filters

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resolve_nodes_request_linked_entity_filters_type_0 import (
            ResolveNodesRequestLinkedEntityFiltersType0,
        )

        d = dict(src_dict)
        node_identifiers = cast(list[str], d.pop("node_identifiers", UNSET))

        include_data = d.pop("include_data", UNSET)

        with_linked_entities = d.pop("with_linked_entities", UNSET)

        def _parse_linked_entity_filters(
            data: object,
        ) -> None | ResolveNodesRequestLinkedEntityFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                linked_entity_filters_type_0 = (
                    ResolveNodesRequestLinkedEntityFiltersType0.from_dict(data)
                )

                return linked_entity_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | ResolveNodesRequestLinkedEntityFiltersType0 | Unset, data
            )

        linked_entity_filters = _parse_linked_entity_filters(
            d.pop("linked_entity_filters", UNSET)
        )

        resolve_nodes_request = cls(
            node_identifiers=node_identifiers,
            include_data=include_data,
            with_linked_entities=with_linked_entities,
            linked_entity_filters=linked_entity_filters,
        )

        resolve_nodes_request.additional_properties = d
        return resolve_nodes_request

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
