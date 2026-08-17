from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relation_type import RelationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.edge_source_node_type_0 import EdgeSourceNodeType0
    from ..models.edge_source_node_type_1 import EdgeSourceNodeType1
    from ..models.edge_target_node_type_0 import EdgeTargetNodeType0
    from ..models.edge_target_node_type_1 import EdgeTargetNodeType1
    from ..models.tenant_metadata import TenantMetadata
    from ..models.trace_metadata import TraceMetadata


T = TypeVar("T", bound="Edge")


@_attrs_define
class Edge:
    """
    Attributes:
        source (str):
        target (str):
        tenant_metadata (TenantMetadata):
        audit_info (AuditInfo):
        field_id (None | str | Unset): MongoDB document ObjectID
        relation_type (RelationType | Unset):
        source_node (EdgeSourceNodeType0 | EdgeSourceNodeType1 | None | Unset):
        target_node (EdgeTargetNodeType0 | EdgeTargetNodeType1 | None | Unset):
        outdated (bool | Unset):  Default: False.
        trace_metadata (None | TraceMetadata | Unset):
    """

    source: str
    target: str
    tenant_metadata: TenantMetadata
    audit_info: AuditInfo
    field_id: None | str | Unset = UNSET
    relation_type: RelationType | Unset = UNSET
    source_node: EdgeSourceNodeType0 | EdgeSourceNodeType1 | None | Unset = UNSET
    target_node: EdgeTargetNodeType0 | EdgeTargetNodeType1 | None | Unset = UNSET
    outdated: bool | Unset = False
    trace_metadata: None | TraceMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.edge_source_node_type_0 import EdgeSourceNodeType0
        from ..models.edge_source_node_type_1 import EdgeSourceNodeType1
        from ..models.edge_target_node_type_0 import EdgeTargetNodeType0
        from ..models.edge_target_node_type_1 import EdgeTargetNodeType1
        from ..models.trace_metadata import TraceMetadata

        source = self.source

        target = self.target

        tenant_metadata = self.tenant_metadata.to_dict()

        audit_info = self.audit_info.to_dict()

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        relation_type: str | Unset = UNSET
        if not isinstance(self.relation_type, Unset):
            relation_type = self.relation_type.value

        source_node: dict[str, Any] | None | Unset
        if isinstance(self.source_node, Unset):
            source_node = UNSET
        elif isinstance(self.source_node, EdgeSourceNodeType0) or isinstance(
            self.source_node, EdgeSourceNodeType1
        ):
            source_node = self.source_node.to_dict()
        else:
            source_node = self.source_node

        target_node: dict[str, Any] | None | Unset
        if isinstance(self.target_node, Unset):
            target_node = UNSET
        elif isinstance(self.target_node, EdgeTargetNodeType0) or isinstance(
            self.target_node, EdgeTargetNodeType1
        ):
            target_node = self.target_node.to_dict()
        else:
            target_node = self.target_node

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
                "source": source,
                "target": target,
                "tenant_metadata": tenant_metadata,
                "audit_info": audit_info,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if relation_type is not UNSET:
            field_dict["relation_type"] = relation_type
        if source_node is not UNSET:
            field_dict["source_node"] = source_node
        if target_node is not UNSET:
            field_dict["target_node"] = target_node
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if trace_metadata is not UNSET:
            field_dict["trace_metadata"] = trace_metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.edge_source_node_type_0 import EdgeSourceNodeType0
        from ..models.edge_source_node_type_1 import EdgeSourceNodeType1
        from ..models.edge_target_node_type_0 import EdgeTargetNodeType0
        from ..models.edge_target_node_type_1 import EdgeTargetNodeType1
        from ..models.tenant_metadata import TenantMetadata
        from ..models.trace_metadata import TraceMetadata

        d = dict(src_dict)
        source = d.pop("source")

        target = d.pop("target")

        tenant_metadata = TenantMetadata.from_dict(d.pop("tenant_metadata"))

        audit_info = AuditInfo.from_dict(d.pop("audit_info"))

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

        _relation_type = d.pop("relation_type", UNSET)
        relation_type: RelationType | Unset
        if isinstance(_relation_type, Unset):
            relation_type = UNSET
        else:
            relation_type = RelationType(_relation_type)

        def _parse_source_node(
            data: object,
        ) -> EdgeSourceNodeType0 | EdgeSourceNodeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_node_type_0 = EdgeSourceNodeType0.from_dict(data)

                return source_node_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_node_type_1 = EdgeSourceNodeType1.from_dict(data)

                return source_node_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EdgeSourceNodeType0 | EdgeSourceNodeType1 | None | Unset, data)

        source_node = _parse_source_node(d.pop("source_node", UNSET))

        def _parse_target_node(
            data: object,
        ) -> EdgeTargetNodeType0 | EdgeTargetNodeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_node_type_0 = EdgeTargetNodeType0.from_dict(data)

                return target_node_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_node_type_1 = EdgeTargetNodeType1.from_dict(data)

                return target_node_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EdgeTargetNodeType0 | EdgeTargetNodeType1 | None | Unset, data)

        target_node = _parse_target_node(d.pop("target_node", UNSET))

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

        edge = cls(
            source=source,
            target=target,
            tenant_metadata=tenant_metadata,
            audit_info=audit_info,
            field_id=field_id,
            relation_type=relation_type,
            source_node=source_node,
            target_node=target_node,
            outdated=outdated,
            trace_metadata=trace_metadata,
        )

        edge.additional_properties = d
        return edge

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
