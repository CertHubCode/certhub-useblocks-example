from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    Self,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_type import NodeType
from ..models.relation_type import RelationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchTraceDeleteByTargetOperation")


@_attrs_define
class BatchTraceDeleteByTargetOperation:
    """
    Attributes:
        operation (Literal['delete']):
        target (str):
        target_type (NodeType):
        target_version (str):
        source (str):
        source_type (NodeType):
        source_version (str):
        relation_type (RelationType):
        delete_backward (bool | Unset):  Default: False.
        backward_relation_type (None | RelationType | Unset):
    """

    operation: Literal["delete"]
    target: str
    target_type: NodeType
    target_version: str
    source: str
    source_type: NodeType
    source_version: str
    relation_type: RelationType
    delete_backward: bool | Unset = False
    backward_relation_type: None | RelationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        target = self.target

        target_type = self.target_type.value

        target_version = self.target_version

        source = self.source

        source_type = self.source_type.value

        source_version = self.source_version

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
                "operation": operation,
                "target": target,
                "targetType": target_type,
                "targetVersion": target_version,
                "source": source,
                "sourceType": source_type,
                "sourceVersion": source_version,
                "relation_type": relation_type,
            }
        )
        if delete_backward is not UNSET:
            field_dict["delete_backward"] = delete_backward
        if backward_relation_type is not UNSET:
            field_dict["backward_relation_type"] = backward_relation_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        operation = cast(Literal["delete"], d.pop("operation"))
        if operation != "delete":
            raise ValueError(f"operation must match const 'delete', got '{operation}'")

        target = d.pop("target")

        target_type = NodeType(d.pop("targetType"))

        target_version = d.pop("targetVersion")

        source = d.pop("source")

        source_type = NodeType(d.pop("sourceType"))

        source_version = d.pop("sourceVersion")

        relation_type = RelationType(d.pop("relation_type"))

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

        batch_trace_delete_by_target_operation = cls(
            operation=operation,
            target=target,
            target_type=target_type,
            target_version=target_version,
            source=source,
            source_type=source_type,
            source_version=source_version,
            relation_type=relation_type,
            delete_backward=delete_backward,
            backward_relation_type=backward_relation_type,
        )

        batch_trace_delete_by_target_operation.additional_properties = d
        return batch_trace_delete_by_target_operation

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
