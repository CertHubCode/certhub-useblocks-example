from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_type import NodeType
from ..models.relation_type import RelationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyTracesRequest")


@_attrs_define
class CopyTracesRequest:
    """
    Attributes:
        source_node_id (str):
        source_node_type (NodeType):
        target_node_id (str):
        target_node_type (NodeType):
        source_node_version (None | str | Unset):
        target_node_version (None | str | Unset):
        include_automatic (bool | Unset):  Default: False.
        include_outdated (bool | Unset):  Default: False.
        excluded_targets (list[str] | None | Unset):
        included_relation_types (list[RelationType] | None | Unset):
        excluded_relation_types (list[RelationType] | None | Unset):
    """

    source_node_id: str
    source_node_type: NodeType
    target_node_id: str
    target_node_type: NodeType
    source_node_version: None | str | Unset = UNSET
    target_node_version: None | str | Unset = UNSET
    include_automatic: bool | Unset = False
    include_outdated: bool | Unset = False
    excluded_targets: list[str] | None | Unset = UNSET
    included_relation_types: list[RelationType] | None | Unset = UNSET
    excluded_relation_types: list[RelationType] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_node_id = self.source_node_id

        source_node_type = self.source_node_type.value

        target_node_id = self.target_node_id

        target_node_type = self.target_node_type.value

        source_node_version: None | str | Unset
        if isinstance(self.source_node_version, Unset):
            source_node_version = UNSET
        else:
            source_node_version = self.source_node_version

        target_node_version: None | str | Unset
        if isinstance(self.target_node_version, Unset):
            target_node_version = UNSET
        else:
            target_node_version = self.target_node_version

        include_automatic = self.include_automatic

        include_outdated = self.include_outdated

        excluded_targets: list[str] | None | Unset
        if isinstance(self.excluded_targets, Unset):
            excluded_targets = UNSET
        elif isinstance(self.excluded_targets, list):
            excluded_targets = self.excluded_targets

        else:
            excluded_targets = self.excluded_targets

        included_relation_types: list[str] | None | Unset
        if isinstance(self.included_relation_types, Unset):
            included_relation_types = UNSET
        elif isinstance(self.included_relation_types, list):
            included_relation_types = []
            for (
                included_relation_types_type_0_item_data
            ) in self.included_relation_types:
                included_relation_types_type_0_item = (
                    included_relation_types_type_0_item_data.value
                )
                included_relation_types.append(included_relation_types_type_0_item)

        else:
            included_relation_types = self.included_relation_types

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_node_id": source_node_id,
                "source_node_type": source_node_type,
                "target_node_id": target_node_id,
                "target_node_type": target_node_type,
            }
        )
        if source_node_version is not UNSET:
            field_dict["source_node_version"] = source_node_version
        if target_node_version is not UNSET:
            field_dict["target_node_version"] = target_node_version
        if include_automatic is not UNSET:
            field_dict["include_automatic"] = include_automatic
        if include_outdated is not UNSET:
            field_dict["include_outdated"] = include_outdated
        if excluded_targets is not UNSET:
            field_dict["excluded_targets"] = excluded_targets
        if included_relation_types is not UNSET:
            field_dict["included_relation_types"] = included_relation_types
        if excluded_relation_types is not UNSET:
            field_dict["excluded_relation_types"] = excluded_relation_types

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_node_id = d.pop("source_node_id")

        source_node_type = NodeType(d.pop("source_node_type"))

        target_node_id = d.pop("target_node_id")

        target_node_type = NodeType(d.pop("target_node_type"))

        def _parse_source_node_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_node_version = _parse_source_node_version(
            d.pop("source_node_version", UNSET)
        )

        def _parse_target_node_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_node_version = _parse_target_node_version(
            d.pop("target_node_version", UNSET)
        )

        include_automatic = d.pop("include_automatic", UNSET)

        include_outdated = d.pop("include_outdated", UNSET)

        def _parse_excluded_targets(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_targets_type_0 = cast(list[str], data)

                return excluded_targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        excluded_targets = _parse_excluded_targets(d.pop("excluded_targets", UNSET))

        def _parse_included_relation_types(
            data: object,
        ) -> list[RelationType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                included_relation_types_type_0 = []
                _included_relation_types_type_0 = data
                for (
                    included_relation_types_type_0_item_data
                ) in _included_relation_types_type_0:
                    included_relation_types_type_0_item = RelationType(
                        included_relation_types_type_0_item_data
                    )

                    included_relation_types_type_0.append(
                        included_relation_types_type_0_item
                    )

                return included_relation_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RelationType] | None | Unset, data)

        included_relation_types = _parse_included_relation_types(
            d.pop("included_relation_types", UNSET)
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

        copy_traces_request = cls(
            source_node_id=source_node_id,
            source_node_type=source_node_type,
            target_node_id=target_node_id,
            target_node_type=target_node_type,
            source_node_version=source_node_version,
            target_node_version=target_node_version,
            include_automatic=include_automatic,
            include_outdated=include_outdated,
            excluded_targets=excluded_targets,
            included_relation_types=included_relation_types,
            excluded_relation_types=excluded_relation_types,
        )

        copy_traces_request.additional_properties = d
        return copy_traces_request

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
