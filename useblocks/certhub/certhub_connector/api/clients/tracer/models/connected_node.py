from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relation_type import RelationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.node import Node
    from ..models.tenant_metadata import TenantMetadata
    from ..models.trace_metadata import TraceMetadata


T = TypeVar("T", bound="ConnectedNode")


@_attrs_define
class ConnectedNode:
    """
    Attributes:
        trace_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        node (Node):
        relation_type (RelationType):
        tenant_metadata (TenantMetadata):
        audit_info (AuditInfo):
        outdated (bool | Unset):  Default: False.
        trace_metadata (None | TraceMetadata | Unset):
        hops_away_from_source (int | None | Unset):
    """

    trace_id: str
    node: Node
    relation_type: RelationType
    tenant_metadata: TenantMetadata
    audit_info: AuditInfo
    outdated: bool | Unset = False
    trace_metadata: None | TraceMetadata | Unset = UNSET
    hops_away_from_source: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_metadata import TraceMetadata

        trace_id = self.trace_id

        node = self.node.to_dict()

        relation_type = self.relation_type.value

        tenant_metadata = self.tenant_metadata.to_dict()

        audit_info = self.audit_info.to_dict()

        outdated = self.outdated

        trace_metadata: dict[str, Any] | None | Unset
        if isinstance(self.trace_metadata, Unset):
            trace_metadata = UNSET
        elif isinstance(self.trace_metadata, TraceMetadata):
            trace_metadata = self.trace_metadata.to_dict()
        else:
            trace_metadata = self.trace_metadata

        hops_away_from_source: int | None | Unset
        if isinstance(self.hops_away_from_source, Unset):
            hops_away_from_source = UNSET
        else:
            hops_away_from_source = self.hops_away_from_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trace_id": trace_id,
                "node": node,
                "relation_type": relation_type,
                "tenant_metadata": tenant_metadata,
                "audit_info": audit_info,
            }
        )
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if trace_metadata is not UNSET:
            field_dict["trace_metadata"] = trace_metadata
        if hops_away_from_source is not UNSET:
            field_dict["hopsAwayFromSource"] = hops_away_from_source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.node import Node
        from ..models.tenant_metadata import TenantMetadata
        from ..models.trace_metadata import TraceMetadata

        d = dict(src_dict)
        trace_id = d.pop("trace_id")

        node = Node.from_dict(d.pop("node"))

        relation_type = RelationType(d.pop("relation_type"))

        tenant_metadata = TenantMetadata.from_dict(d.pop("tenant_metadata"))

        audit_info = AuditInfo.from_dict(d.pop("audit_info"))

        outdated = d.pop("outdated", UNSET)

        def _parse_trace_metadata(data: object) -> None | TraceMetadata | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trace_metadata_type_0 = TraceMetadata.from_dict(data)

                return trace_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TraceMetadata | Unset, data)

        trace_metadata = _parse_trace_metadata(d.pop("trace_metadata", UNSET))

        def _parse_hops_away_from_source(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hops_away_from_source = _parse_hops_away_from_source(
            d.pop("hopsAwayFromSource", UNSET)
        )

        connected_node = cls(
            trace_id=trace_id,
            node=node,
            relation_type=relation_type,
            tenant_metadata=tenant_metadata,
            audit_info=audit_info,
            outdated=outdated,
            trace_metadata=trace_metadata,
            hops_away_from_source=hops_away_from_source,
        )

        connected_node.additional_properties = d
        return connected_node

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
