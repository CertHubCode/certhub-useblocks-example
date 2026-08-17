from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relation_type import RelationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.edge_with_depth_source_node_type_0 import EdgeWithDepthSourceNodeType0
    from ..models.edge_with_depth_source_node_type_1 import EdgeWithDepthSourceNodeType1
    from ..models.edge_with_depth_target_node_type_0 import EdgeWithDepthTargetNodeType0
    from ..models.edge_with_depth_target_node_type_1 import EdgeWithDepthTargetNodeType1
    from ..models.tenant_metadata import TenantMetadata
    from ..models.trace_metadata import TraceMetadata


T = TypeVar("T", bound="EdgeWithDepth")


@_attrs_define
class EdgeWithDepth:
    """
    Attributes:
        field_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        source (str):
        target (str):
        relation_type (list[RelationType]):
        tenant_metadata (TenantMetadata):
        audit_info (AuditInfo):
        source_node (EdgeWithDepthSourceNodeType0 | EdgeWithDepthSourceNodeType1 | None | Unset):
        target_node (EdgeWithDepthTargetNodeType0 | EdgeWithDepthTargetNodeType1 | None | Unset):
        outdated (bool | Unset):  Default: False.
        trace_metadata (None | TraceMetadata | Unset):
        depth (int | None | Unset):
    """

    field_id: str
    source: str
    target: str
    relation_type: list[RelationType]
    tenant_metadata: TenantMetadata
    audit_info: AuditInfo
    source_node: (
        EdgeWithDepthSourceNodeType0 | EdgeWithDepthSourceNodeType1 | None | Unset
    ) = UNSET
    target_node: (
        EdgeWithDepthTargetNodeType0 | EdgeWithDepthTargetNodeType1 | None | Unset
    ) = UNSET
    outdated: bool | Unset = False
    trace_metadata: None | TraceMetadata | Unset = UNSET
    depth: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.edge_with_depth_source_node_type_0 import (
            EdgeWithDepthSourceNodeType0,
        )
        from ..models.edge_with_depth_source_node_type_1 import (
            EdgeWithDepthSourceNodeType1,
        )
        from ..models.edge_with_depth_target_node_type_0 import (
            EdgeWithDepthTargetNodeType0,
        )
        from ..models.edge_with_depth_target_node_type_1 import (
            EdgeWithDepthTargetNodeType1,
        )
        from ..models.trace_metadata import TraceMetadata

        field_id = self.field_id

        source = self.source

        target = self.target

        relation_type = []
        for relation_type_item_data in self.relation_type:
            relation_type_item = relation_type_item_data.value
            relation_type.append(relation_type_item)

        tenant_metadata = self.tenant_metadata.to_dict()

        audit_info = self.audit_info.to_dict()

        source_node: dict[str, Any] | None | Unset
        if isinstance(self.source_node, Unset):
            source_node = UNSET
        elif isinstance(self.source_node, EdgeWithDepthSourceNodeType0) or isinstance(
            self.source_node, EdgeWithDepthSourceNodeType1
        ):
            source_node = self.source_node.to_dict()
        else:
            source_node = self.source_node

        target_node: dict[str, Any] | None | Unset
        if isinstance(self.target_node, Unset):
            target_node = UNSET
        elif isinstance(self.target_node, EdgeWithDepthTargetNodeType0) or isinstance(
            self.target_node, EdgeWithDepthTargetNodeType1
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

        depth: int | None | Unset
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "source": source,
                "target": target,
                "relation_type": relation_type,
                "tenant_metadata": tenant_metadata,
                "audit_info": audit_info,
            }
        )
        if source_node is not UNSET:
            field_dict["source_node"] = source_node
        if target_node is not UNSET:
            field_dict["target_node"] = target_node
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if trace_metadata is not UNSET:
            field_dict["trace_metadata"] = trace_metadata
        if depth is not UNSET:
            field_dict["depth"] = depth

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.edge_with_depth_source_node_type_0 import (
            EdgeWithDepthSourceNodeType0,
        )
        from ..models.edge_with_depth_source_node_type_1 import (
            EdgeWithDepthSourceNodeType1,
        )
        from ..models.edge_with_depth_target_node_type_0 import (
            EdgeWithDepthTargetNodeType0,
        )
        from ..models.edge_with_depth_target_node_type_1 import (
            EdgeWithDepthTargetNodeType1,
        )
        from ..models.tenant_metadata import TenantMetadata
        from ..models.trace_metadata import TraceMetadata

        d = dict(src_dict)
        field_id = d.pop("_id")

        source = d.pop("source")

        target = d.pop("target")

        relation_type = []
        _relation_type = d.pop("relation_type")
        for relation_type_item_data in _relation_type:
            relation_type_item = RelationType(relation_type_item_data)

            relation_type.append(relation_type_item)

        tenant_metadata = TenantMetadata.from_dict(d.pop("tenant_metadata"))

        audit_info = AuditInfo.from_dict(d.pop("audit_info"))

        def _parse_source_node(
            data: object,
        ) -> EdgeWithDepthSourceNodeType0 | EdgeWithDepthSourceNodeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_node_type_0 = EdgeWithDepthSourceNodeType0.from_dict(data)

                return source_node_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_node_type_1 = EdgeWithDepthSourceNodeType1.from_dict(data)

                return source_node_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EdgeWithDepthSourceNodeType0
                | EdgeWithDepthSourceNodeType1
                | None
                | Unset,
                data,
            )

        source_node = _parse_source_node(d.pop("source_node", UNSET))

        def _parse_target_node(
            data: object,
        ) -> EdgeWithDepthTargetNodeType0 | EdgeWithDepthTargetNodeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_node_type_0 = EdgeWithDepthTargetNodeType0.from_dict(data)

                return target_node_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_node_type_1 = EdgeWithDepthTargetNodeType1.from_dict(data)

                return target_node_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EdgeWithDepthTargetNodeType0
                | EdgeWithDepthTargetNodeType1
                | None
                | Unset,
                data,
            )

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

        def _parse_depth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        depth = _parse_depth(d.pop("depth", UNSET))

        edge_with_depth = cls(
            field_id=field_id,
            source=source,
            target=target,
            relation_type=relation_type,
            tenant_metadata=tenant_metadata,
            audit_info=audit_info,
            source_node=source_node,
            target_node=target_node,
            outdated=outdated,
            trace_metadata=trace_metadata,
            depth=depth,
        )

        edge_with_depth.additional_properties = d
        return edge_with_depth

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
