from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resolved_node_entity import ResolvedNodeEntity


T = TypeVar("T", bound="ResolvedTrace")


@_attrs_define
class ResolvedTrace:
    """
    Attributes:
        trace_id (None | str):
        relation_type (str):
        resolved_source (None | ResolvedNodeEntity):
        resolved_target (None | ResolvedNodeEntity):
    """

    trace_id: None | str
    relation_type: str
    resolved_source: None | ResolvedNodeEntity
    resolved_target: None | ResolvedNodeEntity
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resolved_node_entity import ResolvedNodeEntity

        trace_id: None | str
        trace_id = self.trace_id

        relation_type = self.relation_type

        resolved_source: dict[str, Any] | None
        if isinstance(self.resolved_source, ResolvedNodeEntity):
            resolved_source = self.resolved_source.to_dict()
        else:
            resolved_source = self.resolved_source

        resolved_target: dict[str, Any] | None
        if isinstance(self.resolved_target, ResolvedNodeEntity):
            resolved_target = self.resolved_target.to_dict()
        else:
            resolved_target = self.resolved_target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trace_id": trace_id,
                "relation_type": relation_type,
                "resolved_source": resolved_source,
                "resolved_target": resolved_target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resolved_node_entity import ResolvedNodeEntity

        d = dict(src_dict)

        def _parse_trace_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        trace_id = _parse_trace_id(d.pop("trace_id"))

        relation_type = d.pop("relation_type")

        def _parse_resolved_source(data: object) -> None | ResolvedNodeEntity:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolved_source_type_0 = ResolvedNodeEntity.from_dict(data)

                return resolved_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResolvedNodeEntity, data)

        resolved_source = _parse_resolved_source(d.pop("resolved_source"))

        def _parse_resolved_target(data: object) -> None | ResolvedNodeEntity:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolved_target_type_0 = ResolvedNodeEntity.from_dict(data)

                return resolved_target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResolvedNodeEntity, data)

        resolved_target = _parse_resolved_target(d.pop("resolved_target"))

        resolved_trace = cls(
            trace_id=trace_id,
            relation_type=relation_type,
            resolved_source=resolved_source,
            resolved_target=resolved_target,
        )

        resolved_trace.additional_properties = d
        return resolved_trace

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
