from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parent_entity import ParentEntity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.knowledge_unit_knowledge_topics_item import (
        KnowledgeUnitKnowledgeTopicsItem,
    )
    from ..models.ordered_knowledge_topic import OrderedKnowledgeTopic
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="KnowledgeUnit")


@_attrs_define
class KnowledgeUnit:
    """
    Attributes:
        knowledge_unit_name (str):
        parent_entity (ParentEntity):
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        major_version (int):
        minor_version (int):
        is_latest_approved (bool):
        read_only (bool):
        metadata (TenantMetadata):
        field_id (None | str | Unset): MongoDB document ObjectID
        knowledge_unit_description (str | Unset):  Default: ''.
        product_version (str | Unset):  Default: '0.1'.
        source_schema_id (None | str | Unset):
        knowledge_topics (list[KnowledgeUnitKnowledgeTopicsItem] | Unset):
        ordered_knowledge_topics (list[OrderedKnowledgeTopic] | Unset):
        is_not_editable_for_children (bool | None | Unset):  Default: False.
        commit_message (None | str | Unset):
        audit_info (AuditInfo | None | Unset):
    """

    knowledge_unit_name: str
    parent_entity: ParentEntity
    product_history_id: str
    knowledge_unit_history_id: str
    major_version: int
    minor_version: int
    is_latest_approved: bool
    read_only: bool
    metadata: TenantMetadata
    field_id: None | str | Unset = UNSET
    knowledge_unit_description: str | Unset = ""
    product_version: str | Unset = "0.1"
    source_schema_id: None | str | Unset = UNSET
    knowledge_topics: list[KnowledgeUnitKnowledgeTopicsItem] | Unset = UNSET
    ordered_knowledge_topics: list[OrderedKnowledgeTopic] | Unset = UNSET
    is_not_editable_for_children: bool | None | Unset = False
    commit_message: None | str | Unset = UNSET
    audit_info: AuditInfo | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_info import AuditInfo

        knowledge_unit_name = self.knowledge_unit_name

        parent_entity = self.parent_entity.value

        product_history_id = self.product_history_id

        knowledge_unit_history_id = self.knowledge_unit_history_id

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

        knowledge_unit_description = self.knowledge_unit_description

        product_version = self.product_version

        source_schema_id: None | str | Unset
        if isinstance(self.source_schema_id, Unset):
            source_schema_id = UNSET
        else:
            source_schema_id = self.source_schema_id

        knowledge_topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.knowledge_topics, Unset):
            knowledge_topics = []
            for knowledge_topics_item_data in self.knowledge_topics:
                knowledge_topics_item = knowledge_topics_item_data.to_dict()
                knowledge_topics.append(knowledge_topics_item)

        ordered_knowledge_topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ordered_knowledge_topics, Unset):
            ordered_knowledge_topics = []
            for ordered_knowledge_topics_item_data in self.ordered_knowledge_topics:
                ordered_knowledge_topics_item = (
                    ordered_knowledge_topics_item_data.to_dict()
                )
                ordered_knowledge_topics.append(ordered_knowledge_topics_item)

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
                "parent_entity": parent_entity,
                "product_history_id": product_history_id,
                "knowledge_unit_history_id": knowledge_unit_history_id,
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
        if product_version is not UNSET:
            field_dict["product_version"] = product_version
        if source_schema_id is not UNSET:
            field_dict["source_schema_id"] = source_schema_id
        if knowledge_topics is not UNSET:
            field_dict["knowledge_topics"] = knowledge_topics
        if ordered_knowledge_topics is not UNSET:
            field_dict["ordered_knowledge_topics"] = ordered_knowledge_topics
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
        from ..models.knowledge_unit_knowledge_topics_item import (
            KnowledgeUnitKnowledgeTopicsItem,
        )
        from ..models.ordered_knowledge_topic import OrderedKnowledgeTopic
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        knowledge_unit_name = d.pop("knowledge_unit_name")

        parent_entity = ParentEntity(d.pop("parent_entity"))

        product_history_id = d.pop("product_history_id")

        knowledge_unit_history_id = d.pop("knowledge_unit_history_id")

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

        knowledge_unit_description = d.pop("knowledge_unit_description", UNSET)

        product_version = d.pop("product_version", UNSET)

        def _parse_source_schema_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_schema_id = _parse_source_schema_id(d.pop("source_schema_id", UNSET))

        _knowledge_topics = d.pop("knowledge_topics", UNSET)
        knowledge_topics: list[KnowledgeUnitKnowledgeTopicsItem] | Unset = UNSET
        if _knowledge_topics is not UNSET:
            knowledge_topics = []
            for knowledge_topics_item_data in _knowledge_topics:
                knowledge_topics_item = KnowledgeUnitKnowledgeTopicsItem.from_dict(
                    knowledge_topics_item_data
                )

                knowledge_topics.append(knowledge_topics_item)

        _ordered_knowledge_topics = d.pop("ordered_knowledge_topics", UNSET)
        ordered_knowledge_topics: list[OrderedKnowledgeTopic] | Unset = UNSET
        if _ordered_knowledge_topics is not UNSET:
            ordered_knowledge_topics = []
            for ordered_knowledge_topics_item_data in _ordered_knowledge_topics:
                ordered_knowledge_topics_item = OrderedKnowledgeTopic.from_dict(
                    ordered_knowledge_topics_item_data
                )

                ordered_knowledge_topics.append(ordered_knowledge_topics_item)

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

        knowledge_unit = cls(
            knowledge_unit_name=knowledge_unit_name,
            parent_entity=parent_entity,
            product_history_id=product_history_id,
            knowledge_unit_history_id=knowledge_unit_history_id,
            major_version=major_version,
            minor_version=minor_version,
            is_latest_approved=is_latest_approved,
            read_only=read_only,
            metadata=metadata,
            field_id=field_id,
            knowledge_unit_description=knowledge_unit_description,
            product_version=product_version,
            source_schema_id=source_schema_id,
            knowledge_topics=knowledge_topics,
            ordered_knowledge_topics=ordered_knowledge_topics,
            is_not_editable_for_children=is_not_editable_for_children,
            commit_message=commit_message,
            audit_info=audit_info,
        )

        knowledge_unit.additional_properties = d
        return knowledge_unit

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
