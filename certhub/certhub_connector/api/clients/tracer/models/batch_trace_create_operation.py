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

from ..models.automatic_trace_source import AutomaticTraceSource
from ..models.manual_trace_source import ManualTraceSource
from ..models.node_type import NodeType
from ..models.relation_type import RelationType
from ..models.trace_origin import TraceOrigin
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchTraceCreateOperation")


@_attrs_define
class BatchTraceCreateOperation:
    """
    Attributes:
        operation (Literal['create']):
        source (str):
        source_type (NodeType):
        source_version (str):
        target (str):
        target_type (NodeType):
        target_version (str):
        relation_type (RelationType):
        create_bidirectional (bool | Unset):  Default: False.
        backward_relation_type (None | RelationType | Unset):
        origin (TraceOrigin | Unset):
        automatic_source (AutomaticTraceSource | None | Unset):
        manual_source (ManualTraceSource | None | Unset):
    """

    operation: Literal["create"]
    source: str
    source_type: NodeType
    source_version: str
    target: str
    target_type: NodeType
    target_version: str
    relation_type: RelationType
    create_bidirectional: bool | Unset = False
    backward_relation_type: None | RelationType | Unset = UNSET
    origin: TraceOrigin | Unset = UNSET
    automatic_source: AutomaticTraceSource | None | Unset = UNSET
    manual_source: ManualTraceSource | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        source = self.source

        source_type = self.source_type.value

        source_version = self.source_version

        target = self.target

        target_type = self.target_type.value

        target_version = self.target_version

        relation_type = self.relation_type.value

        create_bidirectional = self.create_bidirectional

        backward_relation_type: None | str | Unset
        if isinstance(self.backward_relation_type, Unset):
            backward_relation_type = UNSET
        elif isinstance(self.backward_relation_type, RelationType):
            backward_relation_type = self.backward_relation_type.value
        else:
            backward_relation_type = self.backward_relation_type

        origin: str | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.value

        automatic_source: None | str | Unset
        if isinstance(self.automatic_source, Unset):
            automatic_source = UNSET
        elif isinstance(self.automatic_source, AutomaticTraceSource):
            automatic_source = self.automatic_source.value
        else:
            automatic_source = self.automatic_source

        manual_source: None | str | Unset
        if isinstance(self.manual_source, Unset):
            manual_source = UNSET
        elif isinstance(self.manual_source, ManualTraceSource):
            manual_source = self.manual_source.value
        else:
            manual_source = self.manual_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
                "source": source,
                "sourceType": source_type,
                "sourceVersion": source_version,
                "target": target,
                "targetType": target_type,
                "targetVersion": target_version,
                "relation_type": relation_type,
            }
        )
        if create_bidirectional is not UNSET:
            field_dict["create_bidirectional"] = create_bidirectional
        if backward_relation_type is not UNSET:
            field_dict["backward_relation_type"] = backward_relation_type
        if origin is not UNSET:
            field_dict["origin"] = origin
        if automatic_source is not UNSET:
            field_dict["automatic_source"] = automatic_source
        if manual_source is not UNSET:
            field_dict["manual_source"] = manual_source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        operation = cast(Literal["create"], d.pop("operation"))
        if operation != "create":
            raise ValueError(f"operation must match const 'create', got '{operation}'")

        source = d.pop("source")

        source_type = NodeType(d.pop("sourceType"))

        source_version = d.pop("sourceVersion")

        target = d.pop("target")

        target_type = NodeType(d.pop("targetType"))

        target_version = d.pop("targetVersion")

        relation_type = RelationType(d.pop("relation_type"))

        create_bidirectional = d.pop("create_bidirectional", UNSET)

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

        _origin = d.pop("origin", UNSET)
        origin: TraceOrigin | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = TraceOrigin(_origin)

        def _parse_automatic_source(
            data: object,
        ) -> AutomaticTraceSource | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                automatic_source_type_0 = AutomaticTraceSource(data)

                return automatic_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutomaticTraceSource | None | Unset, data)

        automatic_source = _parse_automatic_source(d.pop("automatic_source", UNSET))

        def _parse_manual_source(data: object) -> ManualTraceSource | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manual_source_type_0 = ManualTraceSource(data)

                return manual_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ManualTraceSource | None | Unset, data)

        manual_source = _parse_manual_source(d.pop("manual_source", UNSET))

        batch_trace_create_operation = cls(
            operation=operation,
            source=source,
            source_type=source_type,
            source_version=source_version,
            target=target,
            target_type=target_type,
            target_version=target_version,
            relation_type=relation_type,
            create_bidirectional=create_bidirectional,
            backward_relation_type=backward_relation_type,
            origin=origin,
            automatic_source=automatic_source,
            manual_source=manual_source,
        )

        batch_trace_create_operation.additional_properties = d
        return batch_trace_create_operation

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
