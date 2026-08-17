from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node import Node


T = TypeVar("T", bound="BatchNodeAttributesUpdateResult")


@_attrs_define
class BatchNodeAttributesUpdateResult:
    """
    Attributes:
        success (bool):
        source_identifier (str):
        target_identifier (None | str | Unset):
        node (Node | None | Unset):
        error (None | str | Unset):
    """

    success: bool
    source_identifier: str
    target_identifier: None | str | Unset = UNSET
    node: Node | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.node import Node

        success = self.success

        source_identifier = self.source_identifier

        target_identifier: None | str | Unset
        if isinstance(self.target_identifier, Unset):
            target_identifier = UNSET
        else:
            target_identifier = self.target_identifier

        node: dict[str, Any] | None | Unset
        if isinstance(self.node, Unset):
            node = UNSET
        elif isinstance(self.node, Node):
            node = self.node.to_dict()
        else:
            node = self.node

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "source_identifier": source_identifier,
            }
        )
        if target_identifier is not UNSET:
            field_dict["target_identifier"] = target_identifier
        if node is not UNSET:
            field_dict["node"] = node
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node import Node

        d = dict(src_dict)
        success = d.pop("success")

        source_identifier = d.pop("source_identifier")

        def _parse_target_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_identifier = _parse_target_identifier(d.pop("target_identifier", UNSET))

        def _parse_node(data: object) -> Node | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                node_type_0 = Node.from_dict(data)

                return node_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Node | None | Unset, data)

        node = _parse_node(d.pop("node", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        batch_node_attributes_update_result = cls(
            success=success,
            source_identifier=source_identifier,
            target_identifier=target_identifier,
            node=node,
            error=error,
        )

        batch_node_attributes_update_result.additional_properties = d
        return batch_node_attributes_update_result

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
