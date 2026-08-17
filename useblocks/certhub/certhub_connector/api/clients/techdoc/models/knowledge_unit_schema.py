from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.knowledge_unit_schema_knowledge_topic_schemas_item import (
        KnowledgeUnitSchemaKnowledgeTopicSchemasItem,
    )
    from ..models.knowledge_unit_schema_libraries_item import (
        KnowledgeUnitSchemaLibrariesItem,
    )
    from ..models.ordered_knowledge_topic_schema import OrderedKnowledgeTopicSchema
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="KnowledgeUnitSchema")


@_attrs_define
class KnowledgeUnitSchema:
    """
    Attributes:
        knowledge_unit_name (str):
        knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        major_version (int):
        minor_version (int):
        is_latest_approved (bool):
        read_only (bool):
        metadata (TenantMetadata):
        field_id (None | str | Unset): MongoDB document ObjectID
        knowledge_unit_description (None | str | Unset):
        knowledge_topic_schemas (list[KnowledgeUnitSchemaKnowledgeTopicSchemasItem] | Unset):
        ordered_knowledge_topic_schemas (list[OrderedKnowledgeTopicSchema] | Unset):
        libraries (list[KnowledgeUnitSchemaLibrariesItem] | Unset):
        is_not_editable_for_children (bool | None | Unset):  Default: False.
        commit_message (None | str | Unset):
        audit_info (AuditInfo | None | Unset):
    """

    knowledge_unit_name: str
    knowledge_unit_schema_history_id: str
    major_version: int
    minor_version: int
    is_latest_approved: bool
    read_only: bool
    metadata: TenantMetadata
    field_id: None | str | Unset = UNSET
    knowledge_unit_description: None | str | Unset = UNSET
    knowledge_topic_schemas: (
        list[KnowledgeUnitSchemaKnowledgeTopicSchemasItem] | Unset
    ) = UNSET
    ordered_knowledge_topic_schemas: list[OrderedKnowledgeTopicSchema] | Unset = UNSET
    libraries: list[KnowledgeUnitSchemaLibrariesItem] | Unset = UNSET
    is_not_editable_for_children: bool | None | Unset = False
    commit_message: None | str | Unset = UNSET
    audit_info: AuditInfo | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_info import AuditInfo

        knowledge_unit_name = self.knowledge_unit_name

        knowledge_unit_schema_history_id = self.knowledge_unit_schema_history_id

        major_version = self.major_version

        minor_version = self.minor_version

        is_latest_approved = self.is_latest_approved

        read_only = self.read_only

        metadata = self.metadata.to_dict()

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        knowledge_unit_description: None | str | Unset
        if isinstance(self.knowledge_unit_description, Unset):
            knowledge_unit_description = UNSET
        else:
            knowledge_unit_description = self.knowledge_unit_description

        knowledge_topic_schemas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.knowledge_topic_schemas, Unset):
            knowledge_topic_schemas = []
            for knowledge_topic_schemas_item_data in self.knowledge_topic_schemas:
                knowledge_topic_schemas_item = (
                    knowledge_topic_schemas_item_data.to_dict()
                )
                knowledge_topic_schemas.append(knowledge_topic_schemas_item)

        ordered_knowledge_topic_schemas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ordered_knowledge_topic_schemas, Unset):
            ordered_knowledge_topic_schemas = []
            for (
                ordered_knowledge_topic_schemas_item_data
            ) in self.ordered_knowledge_topic_schemas:
                ordered_knowledge_topic_schemas_item = (
                    ordered_knowledge_topic_schemas_item_data.to_dict()
                )
                ordered_knowledge_topic_schemas.append(
                    ordered_knowledge_topic_schemas_item
                )

        libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()
                libraries.append(libraries_item)

        is_not_editable_for_children: bool | None | Unset
        if isinstance(self.is_not_editable_for_children, Unset):
            is_not_editable_for_children = UNSET
        else:
            is_not_editable_for_children = self.is_not_editable_for_children

        commit_message: None | str | Unset
        if isinstance(self.commit_message, Unset):
            commit_message = UNSET
        else:
            commit_message = self.commit_message

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
                "knowledge_unit_name": knowledge_unit_name,
                "knowledge_unit_schema_history_id": knowledge_unit_schema_history_id,
                "major_version": major_version,
                "minor_version": minor_version,
                "is_latest_approved": is_latest_approved,
                "read_only": read_only,
                "metadata": metadata,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if knowledge_unit_description is not UNSET:
            field_dict["knowledge_unit_description"] = knowledge_unit_description
        if knowledge_topic_schemas is not UNSET:
            field_dict["knowledge_topic_schemas"] = knowledge_topic_schemas
        if ordered_knowledge_topic_schemas is not UNSET:
            field_dict["ordered_knowledge_topic_schemas"] = (
                ordered_knowledge_topic_schemas
            )
        if libraries is not UNSET:
            field_dict["libraries"] = libraries
        if is_not_editable_for_children is not UNSET:
            field_dict["is_not_editable_for_children"] = is_not_editable_for_children
        if commit_message is not UNSET:
            field_dict["commit_message"] = commit_message
        if audit_info is not UNSET:
            field_dict["audit_info"] = audit_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.knowledge_unit_schema_knowledge_topic_schemas_item import (
            KnowledgeUnitSchemaKnowledgeTopicSchemasItem,
        )
        from ..models.knowledge_unit_schema_libraries_item import (
            KnowledgeUnitSchemaLibrariesItem,
        )
        from ..models.ordered_knowledge_topic_schema import OrderedKnowledgeTopicSchema
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        knowledge_unit_name = d.pop("knowledge_unit_name")

        knowledge_unit_schema_history_id = d.pop("knowledge_unit_schema_history_id")

        major_version = d.pop("major_version")

        minor_version = d.pop("minor_version")

        is_latest_approved = d.pop("is_latest_approved")

        read_only = d.pop("read_only")

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

        def _parse_knowledge_unit_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_description = _parse_knowledge_unit_description(
            d.pop("knowledge_unit_description", UNSET)
        )

        _knowledge_topic_schemas = d.pop("knowledge_topic_schemas", UNSET)
        knowledge_topic_schemas: (
            list[KnowledgeUnitSchemaKnowledgeTopicSchemasItem] | Unset
        ) = UNSET
        if _knowledge_topic_schemas is not UNSET:
            knowledge_topic_schemas = []
            for knowledge_topic_schemas_item_data in _knowledge_topic_schemas:
                knowledge_topic_schemas_item = (
                    KnowledgeUnitSchemaKnowledgeTopicSchemasItem.from_dict(
                        knowledge_topic_schemas_item_data
                    )
                )

                knowledge_topic_schemas.append(knowledge_topic_schemas_item)

        _ordered_knowledge_topic_schemas = d.pop(
            "ordered_knowledge_topic_schemas", UNSET
        )
        ordered_knowledge_topic_schemas: list[OrderedKnowledgeTopicSchema] | Unset = (
            UNSET
        )
        if _ordered_knowledge_topic_schemas is not UNSET:
            ordered_knowledge_topic_schemas = []
            for (
                ordered_knowledge_topic_schemas_item_data
            ) in _ordered_knowledge_topic_schemas:
                ordered_knowledge_topic_schemas_item = (
                    OrderedKnowledgeTopicSchema.from_dict(
                        ordered_knowledge_topic_schemas_item_data
                    )
                )

                ordered_knowledge_topic_schemas.append(
                    ordered_knowledge_topic_schemas_item
                )

        _libraries = d.pop("libraries", UNSET)
        libraries: list[KnowledgeUnitSchemaLibrariesItem] | Unset = UNSET
        if _libraries is not UNSET:
            libraries = []
            for libraries_item_data in _libraries:
                libraries_item = KnowledgeUnitSchemaLibrariesItem.from_dict(
                    libraries_item_data
                )

                libraries.append(libraries_item)

        def _parse_is_not_editable_for_children(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_not_editable_for_children = _parse_is_not_editable_for_children(
            d.pop("is_not_editable_for_children", UNSET)
        )

        def _parse_commit_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_message = _parse_commit_message(d.pop("commit_message", UNSET))

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

        knowledge_unit_schema = cls(
            knowledge_unit_name=knowledge_unit_name,
            knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
            major_version=major_version,
            minor_version=minor_version,
            is_latest_approved=is_latest_approved,
            read_only=read_only,
            metadata=metadata,
            field_id=field_id,
            knowledge_unit_description=knowledge_unit_description,
            knowledge_topic_schemas=knowledge_topic_schemas,
            ordered_knowledge_topic_schemas=ordered_knowledge_topic_schemas,
            libraries=libraries,
            is_not_editable_for_children=is_not_editable_for_children,
            commit_message=commit_message,
            audit_info=audit_info,
        )

        knowledge_unit_schema.additional_properties = d
        return knowledge_unit_schema

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
