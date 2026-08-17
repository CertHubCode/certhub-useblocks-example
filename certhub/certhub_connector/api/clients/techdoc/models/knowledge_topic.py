from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_topic_type import KnowledgeTopicType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.external_source_info import ExternalSourceInfo
    from ..models.knowledge_topic_data import KnowledgeTopicData
    from ..models.knowledge_topic_knowledge_topic_schema import (
        KnowledgeTopicKnowledgeTopicSchema,
    )
    from ..models.no_external_source import NoExternalSource
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="KnowledgeTopic")


@_attrs_define
class KnowledgeTopic:
    """
    Attributes:
        knowledge_topic_name (str):
        type_ (KnowledgeTopicType):
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_version (str):
        knowledge_topic_schema (KnowledgeTopicKnowledgeTopicSchema):
        metadata (TenantMetadata):
        field_id (None | str | Unset): MongoDB document ObjectID
        knowledge_topic_history_id (str | Unset):  Example: 5eb7cf5a86d9755df3a6c593.
        product_version (str | Unset):  Default: '0.1'.
        source_schema_id (None | str | Unset):
        data (KnowledgeTopicData | Unset):
        product_data_collection_id (None | str | Unset):
        external_source (ExternalSourceInfo | NoExternalSource | None | Unset):
        audit_info (AuditInfo | None | Unset):
    """

    knowledge_topic_name: str
    type_: KnowledgeTopicType
    product_history_id: str
    knowledge_unit_history_id: str
    knowledge_unit_version: str
    knowledge_topic_schema: KnowledgeTopicKnowledgeTopicSchema
    metadata: TenantMetadata
    field_id: None | str | Unset = UNSET
    knowledge_topic_history_id: str | Unset = UNSET
    product_version: str | Unset = "0.1"
    source_schema_id: None | str | Unset = UNSET
    data: KnowledgeTopicData | Unset = UNSET
    product_data_collection_id: None | str | Unset = UNSET
    external_source: ExternalSourceInfo | NoExternalSource | None | Unset = UNSET
    audit_info: AuditInfo | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_info import AuditInfo
        from ..models.external_source_info import ExternalSourceInfo
        from ..models.no_external_source import NoExternalSource

        knowledge_topic_name = self.knowledge_topic_name

        type_ = self.type_.value

        product_history_id = self.product_history_id

        knowledge_unit_history_id = self.knowledge_unit_history_id

        knowledge_unit_version = self.knowledge_unit_version

        knowledge_topic_schema = self.knowledge_topic_schema.to_dict()

        metadata = self.metadata.to_dict()

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        knowledge_topic_history_id = self.knowledge_topic_history_id

        product_version = self.product_version

        source_schema_id: None | str | Unset
        if isinstance(self.source_schema_id, Unset):
            source_schema_id = UNSET
        else:
            source_schema_id = self.source_schema_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        product_data_collection_id: None | str | Unset
        if isinstance(self.product_data_collection_id, Unset):
            product_data_collection_id = UNSET
        else:
            product_data_collection_id = self.product_data_collection_id

        external_source: dict[str, Any] | None | Unset
        if isinstance(self.external_source, Unset):
            external_source = UNSET
        elif isinstance(self.external_source, NoExternalSource) or isinstance(
            self.external_source, ExternalSourceInfo
        ):
            external_source = self.external_source.to_dict()
        else:
            external_source = self.external_source

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
                "product_history_id": product_history_id,
                "knowledge_unit_history_id": knowledge_unit_history_id,
                "knowledge_unit_version": knowledge_unit_version,
                "knowledge_topic_schema": knowledge_topic_schema,
                "metadata": metadata,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if knowledge_topic_history_id is not UNSET:
            field_dict["knowledge_topic_history_id"] = knowledge_topic_history_id
        if product_version is not UNSET:
            field_dict["product_version"] = product_version
        if source_schema_id is not UNSET:
            field_dict["source_schema_id"] = source_schema_id
        if data is not UNSET:
            field_dict["data"] = data
        if product_data_collection_id is not UNSET:
            field_dict["product_data_collection_id"] = product_data_collection_id
        if external_source is not UNSET:
            field_dict["external_source"] = external_source
        if audit_info is not UNSET:
            field_dict["audit_info"] = audit_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.external_source_info import ExternalSourceInfo
        from ..models.knowledge_topic_data import KnowledgeTopicData
        from ..models.knowledge_topic_knowledge_topic_schema import (
            KnowledgeTopicKnowledgeTopicSchema,
        )
        from ..models.no_external_source import NoExternalSource
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        knowledge_topic_name = d.pop("knowledge_topic_name")

        type_ = KnowledgeTopicType(d.pop("type"))

        product_history_id = d.pop("product_history_id")

        knowledge_unit_history_id = d.pop("knowledge_unit_history_id")

        knowledge_unit_version = d.pop("knowledge_unit_version")

        knowledge_topic_schema = KnowledgeTopicKnowledgeTopicSchema.from_dict(
            d.pop("knowledge_topic_schema")
        )

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

        knowledge_topic_history_id = d.pop("knowledge_topic_history_id", UNSET)

        product_version = d.pop("product_version", UNSET)

        def _parse_source_schema_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_schema_id = _parse_source_schema_id(d.pop("source_schema_id", UNSET))

        _data = d.pop("data", UNSET)
        data: KnowledgeTopicData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = KnowledgeTopicData.from_dict(_data)

        def _parse_product_data_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_data_collection_id = _parse_product_data_collection_id(
            d.pop("product_data_collection_id", UNSET)
        )

        def _parse_external_source(
            data: object,
        ) -> ExternalSourceInfo | NoExternalSource | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_source_type_0_type_0 = NoExternalSource.from_dict(data)

                return external_source_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_source_type_0_type_1 = ExternalSourceInfo.from_dict(data)

                return external_source_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalSourceInfo | NoExternalSource | None | Unset, data)

        external_source = _parse_external_source(d.pop("external_source", UNSET))

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

        knowledge_topic = cls(
            knowledge_topic_name=knowledge_topic_name,
            type_=type_,
            product_history_id=product_history_id,
            knowledge_unit_history_id=knowledge_unit_history_id,
            knowledge_unit_version=knowledge_unit_version,
            knowledge_topic_schema=knowledge_topic_schema,
            metadata=metadata,
            field_id=field_id,
            knowledge_topic_history_id=knowledge_topic_history_id,
            product_version=product_version,
            source_schema_id=source_schema_id,
            data=data,
            product_data_collection_id=product_data_collection_id,
            external_source=external_source,
            audit_info=audit_info,
        )

        knowledge_topic.additional_properties = d
        return knowledge_topic

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
