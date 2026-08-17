from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_topic_type import KnowledgeTopicType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.knowledge_topic_schema_detail_response_component_schema import (
        KnowledgeTopicSchemaDetailResponseComponentSchema,
    )
    from ..models.knowledge_topic_schema_detail_response_data import (
        KnowledgeTopicSchemaDetailResponseData,
    )
    from ..models.tenant_metadata import TenantMetadata
    from ..models.use_case_config_view import UseCaseConfigView


T = TypeVar("T", bound="KnowledgeTopicSchemaDetailResponse")


@_attrs_define
class KnowledgeTopicSchemaDetailResponse:
    """A KT schema as served to clients, plus its use-case columns.

    Mirrors every persisted ``KnowledgeTopicSchema`` field (the BackLink is
    already excluded on the document) so the wire shape is unchanged, and adds
    ``use_case_config`` so the schema-library grid can render purple columns
    without a KU/product payload to read them from.

        Attributes:
            field_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
            knowledge_topic_name (str):
            type_ (KnowledgeTopicType):
            knowledge_topic_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
            knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
            knowledge_unit_schema_name (str):
            knowledge_unit_schema_version (str):
            metadata (TenantMetadata):
            component_schema (KnowledgeTopicSchemaDetailResponseComponentSchema | Unset):
            data (KnowledgeTopicSchemaDetailResponseData | Unset):
            product_data_collection_id (None | str | Unset):
            audit_info (AuditInfo | None | Unset):
            use_case_config (None | Unset | UseCaseConfigView):
    """

    field_id: str
    knowledge_topic_name: str
    type_: KnowledgeTopicType
    knowledge_topic_schema_history_id: str
    knowledge_unit_schema_history_id: str
    knowledge_unit_schema_name: str
    knowledge_unit_schema_version: str
    metadata: TenantMetadata
    component_schema: KnowledgeTopicSchemaDetailResponseComponentSchema | Unset = UNSET
    data: KnowledgeTopicSchemaDetailResponseData | Unset = UNSET
    product_data_collection_id: None | str | Unset = UNSET
    audit_info: AuditInfo | None | Unset = UNSET
    use_case_config: None | Unset | UseCaseConfigView = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_info import AuditInfo
        from ..models.use_case_config_view import UseCaseConfigView

        field_id = self.field_id

        knowledge_topic_name = self.knowledge_topic_name

        type_ = self.type_.value

        knowledge_topic_schema_history_id = self.knowledge_topic_schema_history_id

        knowledge_unit_schema_history_id = self.knowledge_unit_schema_history_id

        knowledge_unit_schema_name = self.knowledge_unit_schema_name

        knowledge_unit_schema_version = self.knowledge_unit_schema_version

        metadata = self.metadata.to_dict()

        component_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component_schema, Unset):
            component_schema = self.component_schema.to_dict()

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

        use_case_config: dict[str, Any] | None | Unset
        if isinstance(self.use_case_config, Unset):
            use_case_config = UNSET
        elif isinstance(self.use_case_config, UseCaseConfigView):
            use_case_config = self.use_case_config.to_dict()
        else:
            use_case_config = self.use_case_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "knowledge_topic_name": knowledge_topic_name,
                "type": type_,
                "knowledge_topic_schema_history_id": knowledge_topic_schema_history_id,
                "knowledge_unit_schema_history_id": knowledge_unit_schema_history_id,
                "knowledge_unit_schema_name": knowledge_unit_schema_name,
                "knowledge_unit_schema_version": knowledge_unit_schema_version,
                "metadata": metadata,
            }
        )
        if component_schema is not UNSET:
            field_dict["component_schema"] = component_schema
        if data is not UNSET:
            field_dict["data"] = data
        if product_data_collection_id is not UNSET:
            field_dict["product_data_collection_id"] = product_data_collection_id
        if audit_info is not UNSET:
            field_dict["audit_info"] = audit_info
        if use_case_config is not UNSET:
            field_dict["use_case_config"] = use_case_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.knowledge_topic_schema_detail_response_component_schema import (
            KnowledgeTopicSchemaDetailResponseComponentSchema,
        )
        from ..models.knowledge_topic_schema_detail_response_data import (
            KnowledgeTopicSchemaDetailResponseData,
        )
        from ..models.tenant_metadata import TenantMetadata
        from ..models.use_case_config_view import UseCaseConfigView

        d = dict(src_dict)
        field_id = d.pop("_id")

        knowledge_topic_name = d.pop("knowledge_topic_name")

        type_ = KnowledgeTopicType(d.pop("type"))

        knowledge_topic_schema_history_id = d.pop("knowledge_topic_schema_history_id")

        knowledge_unit_schema_history_id = d.pop("knowledge_unit_schema_history_id")

        knowledge_unit_schema_name = d.pop("knowledge_unit_schema_name")

        knowledge_unit_schema_version = d.pop("knowledge_unit_schema_version")

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        _component_schema = d.pop("component_schema", UNSET)
        component_schema: KnowledgeTopicSchemaDetailResponseComponentSchema | Unset
        if isinstance(_component_schema, Unset):
            component_schema = UNSET
        else:
            component_schema = (
                KnowledgeTopicSchemaDetailResponseComponentSchema.from_dict(
                    _component_schema
                )
            )

        _data = d.pop("data", UNSET)
        data: KnowledgeTopicSchemaDetailResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = KnowledgeTopicSchemaDetailResponseData.from_dict(_data)

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

        def _parse_use_case_config(data: object) -> None | Unset | UseCaseConfigView:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                use_case_config_type_0 = UseCaseConfigView.from_dict(data)

                return use_case_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UseCaseConfigView, data)

        use_case_config = _parse_use_case_config(d.pop("use_case_config", UNSET))

        knowledge_topic_schema_detail_response = cls(
            field_id=field_id,
            knowledge_topic_name=knowledge_topic_name,
            type_=type_,
            knowledge_topic_schema_history_id=knowledge_topic_schema_history_id,
            knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
            knowledge_unit_schema_name=knowledge_unit_schema_name,
            knowledge_unit_schema_version=knowledge_unit_schema_version,
            metadata=metadata,
            component_schema=component_schema,
            data=data,
            product_data_collection_id=product_data_collection_id,
            audit_info=audit_info,
            use_case_config=use_case_config,
        )

        knowledge_topic_schema_detail_response.additional_properties = d
        return knowledge_topic_schema_detail_response

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
