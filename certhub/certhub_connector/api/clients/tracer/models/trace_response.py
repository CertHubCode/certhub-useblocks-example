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


T = TypeVar("T", bound="TraceResponse")


@_attrs_define
class TraceResponse:
    """
    Attributes:
        id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        source (str):
        target (str):
        relation_type (RelationType):
        source_node (Node):
        target_node (Node):
        trace_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        tenant_metadata (TenantMetadata):
        audit_info (AuditInfo):
        outdated (bool | Unset):  Default: False.
        trace_metadata (None | TraceMetadata | Unset):
    """

    id: str
    source: str
    target: str
    relation_type: RelationType
    source_node: Node
    target_node: Node
    trace_id: str
    tenant_metadata: TenantMetadata
    audit_info: AuditInfo
    outdated: bool | Unset = False
    trace_metadata: None | TraceMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_metadata import TraceMetadata

        id = self.id

        source = self.source

        target = self.target

        relation_type = self.relation_type.value

        source_node = self.source_node.to_dict()

        target_node = self.target_node.to_dict()

        trace_id = self.trace_id

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "target": target,
                "relation_type": relation_type,
                "source_node": source_node,
                "target_node": target_node,
                "trace_id": trace_id,
                "tenant_metadata": tenant_metadata,
                "audit_info": audit_info,
            }
        )
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if trace_metadata is not UNSET:
            field_dict["trace_metadata"] = trace_metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.node import Node
        from ..models.tenant_metadata import TenantMetadata
        from ..models.trace_metadata import TraceMetadata

        d = dict(src_dict)
        id = d.pop("id")

        source = d.pop("source")

        target = d.pop("target")

        relation_type = RelationType(d.pop("relation_type"))

        source_node = Node.from_dict(d.pop("source_node"))

        target_node = Node.from_dict(d.pop("target_node"))

        trace_id = d.pop("trace_id")

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

        trace_response = cls(
            id=id,
            source=source,
            target=target,
            relation_type=relation_type,
            source_node=source_node,
            target_node=target_node,
            trace_id=trace_id,
            tenant_metadata=tenant_metadata,
            audit_info=audit_info,
            outdated=outdated,
            trace_metadata=trace_metadata,
        )

        trace_response.additional_properties = d
        return trace_response

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
