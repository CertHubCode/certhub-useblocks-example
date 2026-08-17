from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.base_library_response import BaseLibraryResponse
    from ..models.knowledge_topic_schema_detail_response import (
        KnowledgeTopicSchemaDetailResponse,
    )
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="SchemaWithLibraries")


@_attrs_define
class SchemaWithLibraries:
    """
    Attributes:
        id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_name (str):
        metadata (TenantMetadata):
        knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        major_version (int):
        minor_version (int):
        is_latest_approved (bool):
        read_only (bool):
        knowledge_unit_description (None | str | Unset):
        is_not_editable_for_children (bool | None | Unset):  Default: False.
        audit_info (AuditInfo | None | Unset):
        knowledge_topic_schemas (list[KnowledgeTopicSchemaDetailResponse] | None | Unset):
        commit_message (None | str | Unset):
        libraries (list[BaseLibraryResponse] | Unset):
    """

    id: str
    knowledge_unit_name: str
    metadata: TenantMetadata
    knowledge_unit_schema_history_id: str
    major_version: int
    minor_version: int
    is_latest_approved: bool
    read_only: bool
    knowledge_unit_description: None | str | Unset = UNSET
    is_not_editable_for_children: bool | None | Unset = False
    audit_info: AuditInfo | None | Unset = UNSET
    knowledge_topic_schemas: list[KnowledgeTopicSchemaDetailResponse] | None | Unset = (
        UNSET
    )
    commit_message: None | str | Unset = UNSET
    libraries: list[BaseLibraryResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_info import AuditInfo

        id = self.id

        knowledge_unit_name = self.knowledge_unit_name

        metadata = self.metadata.to_dict()

        knowledge_unit_schema_history_id = self.knowledge_unit_schema_history_id

        major_version = self.major_version

        minor_version = self.minor_version

        is_latest_approved = self.is_latest_approved

        read_only = self.read_only

        knowledge_unit_description: None | str | Unset
        if isinstance(self.knowledge_unit_description, Unset):
            knowledge_unit_description = UNSET
        else:
            knowledge_unit_description = self.knowledge_unit_description

        is_not_editable_for_children: bool | None | Unset
        if isinstance(self.is_not_editable_for_children, Unset):
            is_not_editable_for_children = UNSET
        else:
            is_not_editable_for_children = self.is_not_editable_for_children

        audit_info: dict[str, Any] | None | Unset
        if isinstance(self.audit_info, Unset):
            audit_info = UNSET
        elif isinstance(self.audit_info, AuditInfo):
            audit_info = self.audit_info.to_dict()
        else:
            audit_info = self.audit_info

        knowledge_topic_schemas: list[dict[str, Any]] | None | Unset
        if isinstance(self.knowledge_topic_schemas, Unset):
            knowledge_topic_schemas = UNSET
        elif isinstance(self.knowledge_topic_schemas, list):
            knowledge_topic_schemas = []
            for (
                knowledge_topic_schemas_type_0_item_data
            ) in self.knowledge_topic_schemas:
                knowledge_topic_schemas_type_0_item = (
                    knowledge_topic_schemas_type_0_item_data.to_dict()
                )
                knowledge_topic_schemas.append(knowledge_topic_schemas_type_0_item)

        else:
            knowledge_topic_schemas = self.knowledge_topic_schemas

        commit_message: None | str | Unset
        if isinstance(self.commit_message, Unset):
            commit_message = UNSET
        else:
            commit_message = self.commit_message

        libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()
                libraries.append(libraries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "knowledge_unit_name": knowledge_unit_name,
                "metadata": metadata,
                "knowledge_unit_schema_history_id": knowledge_unit_schema_history_id,
                "major_version": major_version,
                "minor_version": minor_version,
                "is_latest_approved": is_latest_approved,
                "read_only": read_only,
            }
        )
        if knowledge_unit_description is not UNSET:
            field_dict["knowledge_unit_description"] = knowledge_unit_description
        if is_not_editable_for_children is not UNSET:
            field_dict["is_not_editable_for_children"] = is_not_editable_for_children
        if audit_info is not UNSET:
            field_dict["audit_info"] = audit_info
        if knowledge_topic_schemas is not UNSET:
            field_dict["knowledge_topic_schemas"] = knowledge_topic_schemas
        if commit_message is not UNSET:
            field_dict["commit_message"] = commit_message
        if libraries is not UNSET:
            field_dict["libraries"] = libraries

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.base_library_response import BaseLibraryResponse
        from ..models.knowledge_topic_schema_detail_response import (
            KnowledgeTopicSchemaDetailResponse,
        )
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        id = d.pop("id")

        knowledge_unit_name = d.pop("knowledge_unit_name")

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        knowledge_unit_schema_history_id = d.pop("knowledge_unit_schema_history_id")

        major_version = d.pop("major_version")

        minor_version = d.pop("minor_version")

        is_latest_approved = d.pop("is_latest_approved")

        read_only = d.pop("read_only")

        def _parse_knowledge_unit_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_description = _parse_knowledge_unit_description(
            d.pop("knowledge_unit_description", UNSET)
        )

        def _parse_is_not_editable_for_children(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_not_editable_for_children = _parse_is_not_editable_for_children(
            d.pop("is_not_editable_for_children", UNSET)
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

        def _parse_knowledge_topic_schemas(
            data: object,
        ) -> list[KnowledgeTopicSchemaDetailResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                knowledge_topic_schemas_type_0 = []
                _knowledge_topic_schemas_type_0 = data
                for (
                    knowledge_topic_schemas_type_0_item_data
                ) in _knowledge_topic_schemas_type_0:
                    knowledge_topic_schemas_type_0_item = (
                        KnowledgeTopicSchemaDetailResponse.from_dict(
                            knowledge_topic_schemas_type_0_item_data
                        )
                    )

                    knowledge_topic_schemas_type_0.append(
                        knowledge_topic_schemas_type_0_item
                    )

                return knowledge_topic_schemas_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KnowledgeTopicSchemaDetailResponse] | None | Unset, data)

        knowledge_topic_schemas = _parse_knowledge_topic_schemas(
            d.pop("knowledge_topic_schemas", UNSET)
        )

        def _parse_commit_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_message = _parse_commit_message(d.pop("commit_message", UNSET))

        _libraries = d.pop("libraries", UNSET)
        libraries: list[BaseLibraryResponse] | Unset = UNSET
        if _libraries is not UNSET:
            libraries = []
            for libraries_item_data in _libraries:
                libraries_item = BaseLibraryResponse.from_dict(libraries_item_data)

                libraries.append(libraries_item)

        schema_with_libraries = cls(
            id=id,
            knowledge_unit_name=knowledge_unit_name,
            metadata=metadata,
            knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
            major_version=major_version,
            minor_version=minor_version,
            is_latest_approved=is_latest_approved,
            read_only=read_only,
            knowledge_unit_description=knowledge_unit_description,
            is_not_editable_for_children=is_not_editable_for_children,
            audit_info=audit_info,
            knowledge_topic_schemas=knowledge_topic_schemas,
            commit_message=commit_message,
            libraries=libraries,
        )

        schema_with_libraries.additional_properties = d
        return schema_with_libraries

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
