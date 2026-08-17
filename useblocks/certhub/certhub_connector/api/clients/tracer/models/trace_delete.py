from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_type import NodeType
from ..models.relation_type import RelationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceDelete")


@_attrs_define
class TraceDelete:
    """
    Attributes:
        source (str):
        source_type (NodeType):
        source_version (str):
        target (str):
        target_type (NodeType):
        target_version (str):
        relation_type (RelationType | Unset):
        delete_backward (bool | Unset):  Default: False.
        backward_relation_type (None | RelationType | Unset):
    """

    source: str
    source_type: NodeType
    source_version: str
    target: str
    target_type: NodeType
    target_version: str
    relation_type: RelationType | Unset = UNSET
    delete_backward: bool | Unset = False
    backward_relation_type: None | RelationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type.value

        source_version = self.source_version

        target = self.target

        target_type = self.target_type.value

        target_version = self.target_version

        relation_type: str | Unset = UNSET
        if not isinstance(self.relation_type, Unset):
            relation_type = self.relation_type.value

        delete_backward = self.delete_backward

        backward_relation_type: None | str | Unset
        if isinstance(self.backward_relation_type, Unset):
            backward_relation_type = UNSET
        elif isinstance(self.backward_relation_type, RelationType):
            backward_relation_type = self.backward_relation_type.value
        else:
            backward_relation_type = self.backward_relation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceVersion": source_version,
                "target": target,
                "targetType": target_type,
                "targetVersion": target_version,
            }
        )
        if relation_type is not UNSET:
            field_dict["relation_type"] = relation_type
        if delete_backward is not UNSET:
            field_dict["delete_backward"] = delete_backward
        if backward_relation_type is not UNSET:
            field_dict["backward_relation_type"] = backward_relation_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = NodeType(d.pop("sourceType"))

        source_version = d.pop("sourceVersion")

        target = d.pop("target")

        target_type = NodeType(d.pop("targetType"))

        target_version = d.pop("targetVersion")

        _relation_type = d.pop("relation_type", UNSET)
        relation_type: RelationType | Unset
        if isinstance(_relation_type, Unset):
            relation_type = UNSET
        else:
            relation_type = RelationType(_relation_type)

        delete_backward = d.pop("delete_backward", UNSET)

        def _parse_backward_relation_type(data: object) -> None | RelationType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backward_relation_type_type_0 = RelationType(data)

                return backward_relation_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RelationType | Unset, data)

        backward_relation_type = _parse_backward_relation_type(
            d.pop("backward_relation_type", UNSET)
        )

        trace_delete = cls(
            source=source,
            source_type=source_type,
            source_version=source_version,
            target=target,
            target_type=target_type,
            target_version=target_version,
            relation_type=relation_type,
            delete_backward=delete_backward,
            backward_relation_type=backward_relation_type,
        )

        trace_delete.additional_properties = d
        return trace_delete

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
