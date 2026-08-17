from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automatic_trace_source import AutomaticTraceSource
from ..models.manual_trace_source import ManualTraceSource
from ..models.trace_origin import TraceOrigin
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceMetadata")


@_attrs_define
class TraceMetadata:
    """Additional metadata for traces, including origin information

    Attributes:
        origin (TraceOrigin | Unset):
        automatic_source (AutomaticTraceSource | None | Unset):
        manual_source (ManualTraceSource | None | Unset):
    """

    origin: TraceOrigin | Unset = UNSET
    automatic_source: AutomaticTraceSource | None | Unset = UNSET
    manual_source: ManualTraceSource | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        field_dict.update({})
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

        trace_metadata = cls(
            origin=origin,
            automatic_source=automatic_source,
            manual_source=manual_source,
        )

        trace_metadata.additional_properties = d
        return trace_metadata

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
