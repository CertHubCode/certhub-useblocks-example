from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph_traversal_options import GraphTraversalOptions
    from ..models.node_impact_request_changed_object_type_0 import (
        NodeImpactRequestChangedObjectType0,
    )


T = TypeVar("T", bound="NodeImpactRequest")


@_attrs_define
class NodeImpactRequest:
    """
    Attributes:
        filter_ (GraphTraversalOptions):
        changed_object (NodeImpactRequestChangedObjectType0 | None | Unset):
    """

    filter_: GraphTraversalOptions
    changed_object: NodeImpactRequestChangedObjectType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.node_impact_request_changed_object_type_0 import (
            NodeImpactRequestChangedObjectType0,
        )

        filter_ = self.filter_.to_dict()

        changed_object: dict[str, Any] | None | Unset
        if isinstance(self.changed_object, Unset):
            changed_object = UNSET
        elif isinstance(self.changed_object, NodeImpactRequestChangedObjectType0):
            changed_object = self.changed_object.to_dict()
        else:
            changed_object = self.changed_object

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
            }
        )
        if changed_object is not UNSET:
            field_dict["changed_object"] = changed_object

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.graph_traversal_options import GraphTraversalOptions
        from ..models.node_impact_request_changed_object_type_0 import (
            NodeImpactRequestChangedObjectType0,
        )

        d = dict(src_dict)
        filter_ = GraphTraversalOptions.from_dict(d.pop("filter"))

        def _parse_changed_object(
            data: object,
        ) -> NodeImpactRequestChangedObjectType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                changed_object_type_0 = NodeImpactRequestChangedObjectType0.from_dict(
                    data
                )

                return changed_object_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NodeImpactRequestChangedObjectType0 | None | Unset, data)

        changed_object = _parse_changed_object(d.pop("changed_object", UNSET))

        node_impact_request = cls(
            filter_=filter_,
            changed_object=changed_object,
        )

        node_impact_request.additional_properties = d
        return node_impact_request

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
