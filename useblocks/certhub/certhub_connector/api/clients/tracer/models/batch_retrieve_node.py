from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_type import NodeType

T = TypeVar("T", bound="BatchRetrieveNode")


@_attrs_define
class BatchRetrieveNode:
    """
    Attributes:
        node_id (str):
        node_type (NodeType):
        version (str):
    """

    node_id: str
    node_type: NodeType
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        node_type = self.node_type.value

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "node_type": node_type,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        node_id = d.pop("node_id")

        node_type = NodeType(d.pop("node_type"))

        version = d.pop("version")

        batch_retrieve_node = cls(
            node_id=node_id,
            node_type=node_type,
            version=version,
        )

        batch_retrieve_node.additional_properties = d
        return batch_retrieve_node

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
