from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_retrieve_mode import BatchRetrieveMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_retrieve_node import BatchRetrieveNode


T = TypeVar("T", bound="BatchRetrieveRequest")


@_attrs_define
class BatchRetrieveRequest:
    """
    Attributes:
        nodes (list[BatchRetrieveNode]):
        n_hops (int | Unset):  Default: 1.
        mode (BatchRetrieveMode | None | Unset):  Default: BatchRetrieveMode.LEGACY_CONNECTED_NODES.
    """

    nodes: list[BatchRetrieveNode]
    n_hops: int | Unset = 1
    mode: BatchRetrieveMode | None | Unset = BatchRetrieveMode.LEGACY_CONNECTED_NODES
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        n_hops = self.n_hops

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, BatchRetrieveMode):
            mode = self.mode.value
        else:
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodes": nodes,
            }
        )
        if n_hops is not UNSET:
            field_dict["n_hops"] = n_hops
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_retrieve_node import BatchRetrieveNode

        d = dict(src_dict)
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = BatchRetrieveNode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        n_hops = d.pop("n_hops", UNSET)

        def _parse_mode(data: object) -> BatchRetrieveMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_0 = BatchRetrieveMode(data)

                return mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchRetrieveMode | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        batch_retrieve_request = cls(
            nodes=nodes,
            n_hops=n_hops,
            mode=mode,
        )

        batch_retrieve_request.additional_properties = d
        return batch_retrieve_request

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
