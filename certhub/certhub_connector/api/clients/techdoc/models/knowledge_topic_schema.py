from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_topic_type import KnowledgeTopicType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.knowledge_topic_schema_component_schema import (
        KnowledgeTopicSchemaComponentSchema,
    )
    from ..models.knowledge_topic_schema_data import KnowledgeTopicSchemaData
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="KnowledgeTopicSchema")


@_attrs_define
class KnowledgeTopicSchema:
    """
    Attributes:
        knowledge_topic_name (str):
        type_ (KnowledgeTopicType):
        knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_schema_name (str):
        knowledge_unit_schema_version (str):
        metadata (TenantMetadata):
        field_id (None | str | Unset): MongoDB document ObjectID
        component_schema (KnowledgeTopicSchemaComponentSchema | Unset):
        knowledge_topic_schema_history_id (str | Unset):  Example: 5eb7cf5a86d9755df3a6c593.
        data (KnowledgeTopicSchemaData | Unset):
        product_data_collection_id (None | str | Unset):
        audit_info (AuditInfo | None | Unset):
    """

    knowledge_topic_name: str
    type_: KnowledgeTopicType
    knowledge_unit_schema_history_id: str
    knowledge_unit_schema_name: str
    knowledge_unit_schema_version: str
    metadata: TenantMetadata
    field_id: None | str | Unset = UNSET
    component_schema: KnowledgeTopicSchemaComponentSchema | Unset = UNSET
    knowledge_topic_schema_history_id: str | Unset = UNSET
    data: KnowledgeTopicSchemaData | Unset = UNSET
    product_data_collection_id: None | str | Unset = UNSET
    audit_info: AuditInfo | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_info import AuditInfo

        knowledge_topic_name = self.knowledge_topic_name

        type_ = self.type_.value

        knowledge_unit_schema_history_id = self.knowledge_unit_schema_history_id

        knowledge_unit_schema_name = self.knowledge_unit_schema_name

        knowledge_unit_schema_version = self.knowledge_unit_schema_version

        metadata = self.metadata.to_dict()

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        component_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component_schema, Unset):
            component_schema = self.component_schema.to_dict()

        knowledge_topic_schema_history_id = self.knowledge_topic_schema_history_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        product_data_collection_id: None | str | Unset
        if isinstance(self.product_data_collection_id, Unset):
            product_data_collection_id = UNSET
        else:
            product_data_collection_id = self.product_data_collection_id

        audit_info: dict[str, Any] | None | Unset
        if isinstance(self.audit_info, Unset):
            audit_info = UNSET
        elif isinstance(self.audit_info, AuditInfo):
            audit_info = self.audit_info.to_dict()
        else:
            audit_info = self.audit_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_topic_name": knowledge_topic_name,
                "type": type_,
                "knowledge_unit_schema_history_id": knowledge_unit_schema_history_id,
                "knowledge_unit_schema_name": knowledge_unit_schema_name,
                "knowledge_unit_schema_version": knowledge_unit_schema_version,
                "metadata": metadata,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if component_schema is not UNSET:
            field_dict["component_schema"] = component_schema
        if knowledge_topic_schema_history_id is not UNSET:
            field_dict["knowledge_topic_schema_history_id"] = (
                knowledge_topic_schema_history_id
            )
        if data is not UNSET:
            field_dict["data"] = data
        if product_data_collection_id is not UNSET:
            field_dict["product_data_collection_id"] = product_data_collection_id
        if audit_info is not UNSET:
            field_dict["audit_info"] = audit_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.knowledge_topic_schema_component_schema import (
            KnowledgeTopicSchemaComponentSchema,
        )
        from ..models.knowledge_topic_schema_data import KnowledgeTopicSchemaData
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        knowledge_topic_name = d.pop("knowledge_topic_name")

        type_ = KnowledgeTopicType(d.pop("type"))

        knowledge_unit_schema_history_id = d.pop("knowledge_unit_schema_history_id")

        knowledge_unit_schema_name = d.pop("knowledge_unit_schema_name")

        knowledge_unit_schema_version = d.pop("knowledge_unit_schema_version")

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

        _component_schema = d.pop("component_schema", UNSET)
        component_schema: KnowledgeTopicSchemaComponentSchema | Unset
        if isinstance(_component_schema, Unset):
            component_schema = UNSET
        else:
            component_schema = KnowledgeTopicSchemaComponentSchema.from_dict(
                _component_schema
            )

        knowledge_topic_schema_history_id = d.pop(
            "knowledge_topic_schema_history_id", UNSET
        )

        _data = d.pop("data", UNSET)
        data: KnowledgeTopicSchemaData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = KnowledgeTopicSchemaData.from_dict(_data)

        def _parse_product_data_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_data_collection_id = _parse_product_data_collection_id(
            d.pop("product_data_collection_id", UNSET)
        )

        def _parse_audit_info(data: object) -> AuditInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                audit_info_type_0 = AuditInfo.from_dict(data)

                return audit_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditInfo | None | Unset, data)

        audit_info = _parse_audit_info(d.pop("audit_info", UNSET))

        knowledge_topic_schema = cls(
            knowledge_topic_name=knowledge_topic_name,
            type_=type_,
            knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
            knowledge_unit_schema_name=knowledge_unit_schema_name,
            knowledge_unit_schema_version=knowledge_unit_schema_version,
            metadata=metadata,
            field_id=field_id,
            component_schema=component_schema,
            knowledge_topic_schema_history_id=knowledge_topic_schema_history_id,
            data=data,
            product_data_collection_id=product_data_collection_id,
            audit_info=audit_info,
        )

        knowledge_topic_schema.additional_properties = d
        return knowledge_topic_schema

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
