from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_source_info import ExternalSourceInfo
    from ..models.knowledge_topic_update import KnowledgeTopicUpdate
    from ..models.no_external_source import NoExternalSource


T = TypeVar("T", bound="KnowledgeUnitUpdate")


@_attrs_define
class KnowledgeUnitUpdate:
    """
    Attributes:
        knowledge_unit_name (None | str | Unset):
        knowledge_unit_description (None | str | Unset):
        knowledge_topics (list[KnowledgeTopicUpdate] | None | Unset):
        is_not_editable_for_children (bool | None | Unset):  Default: False.
        parent_entity (None | str | Unset):
        external_source (ExternalSourceInfo | NoExternalSource | None | Unset):
    """

    knowledge_unit_name: None | str | Unset = UNSET
    knowledge_unit_description: None | str | Unset = UNSET
    knowledge_topics: list[KnowledgeTopicUpdate] | None | Unset = UNSET
    is_not_editable_for_children: bool | None | Unset = False
    parent_entity: None | str | Unset = UNSET
    external_source: ExternalSourceInfo | NoExternalSource | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.external_source_info import ExternalSourceInfo
        from ..models.no_external_source import NoExternalSource

        knowledge_unit_name: None | str | Unset
        if isinstance(self.knowledge_unit_name, Unset):
            knowledge_unit_name = UNSET
        else:
            knowledge_unit_name = self.knowledge_unit_name

        knowledge_unit_description: None | str | Unset
        if isinstance(self.knowledge_unit_description, Unset):
            knowledge_unit_description = UNSET
        else:
            knowledge_unit_description = self.knowledge_unit_description

        knowledge_topics: list[dict[str, Any]] | None | Unset
        if isinstance(self.knowledge_topics, Unset):
            knowledge_topics = UNSET
        elif isinstance(self.knowledge_topics, list):
            knowledge_topics = []
            for knowledge_topics_type_0_item_data in self.knowledge_topics:
                knowledge_topics_type_0_item = (
                    knowledge_topics_type_0_item_data.to_dict()
                )
                knowledge_topics.append(knowledge_topics_type_0_item)

        else:
            knowledge_topics = self.knowledge_topics

        is_not_editable_for_children: bool | None | Unset
        if isinstance(self.is_not_editable_for_children, Unset):
            is_not_editable_for_children = UNSET
        else:
            is_not_editable_for_children = self.is_not_editable_for_children

        parent_entity: None | str | Unset
        if isinstance(self.parent_entity, Unset):
            parent_entity = UNSET
        else:
            parent_entity = self.parent_entity

        external_source: dict[str, Any] | None | Unset
        if isinstance(self.external_source, Unset):
            external_source = UNSET
        elif isinstance(self.external_source, NoExternalSource) or isinstance(
            self.external_source, ExternalSourceInfo
        ):
            external_source = self.external_source.to_dict()
        else:
            external_source = self.external_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if knowledge_unit_name is not UNSET:
            field_dict["knowledge_unit_name"] = knowledge_unit_name
        if knowledge_unit_description is not UNSET:
            field_dict["knowledge_unit_description"] = knowledge_unit_description
        if knowledge_topics is not UNSET:
            field_dict["knowledge_topics"] = knowledge_topics
        if is_not_editable_for_children is not UNSET:
            field_dict["is_not_editable_for_children"] = is_not_editable_for_children
        if parent_entity is not UNSET:
            field_dict["parent_entity"] = parent_entity
        if external_source is not UNSET:
            field_dict["external_source"] = external_source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.external_source_info import ExternalSourceInfo
        from ..models.knowledge_topic_update import KnowledgeTopicUpdate
        from ..models.no_external_source import NoExternalSource

        d = dict(src_dict)

        def _parse_knowledge_unit_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_name = _parse_knowledge_unit_name(
            d.pop("knowledge_unit_name", UNSET)
        )

        def _parse_knowledge_unit_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_description = _parse_knowledge_unit_description(
            d.pop("knowledge_unit_description", UNSET)
        )

        def _parse_knowledge_topics(
            data: object,
        ) -> list[KnowledgeTopicUpdate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                knowledge_topics_type_0 = []
                _knowledge_topics_type_0 = data
                for knowledge_topics_type_0_item_data in _knowledge_topics_type_0:
                    knowledge_topics_type_0_item = KnowledgeTopicUpdate.from_dict(
                        knowledge_topics_type_0_item_data
                    )

                    knowledge_topics_type_0.append(knowledge_topics_type_0_item)

                return knowledge_topics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KnowledgeTopicUpdate] | None | Unset, data)

        knowledge_topics = _parse_knowledge_topics(d.pop("knowledge_topics", UNSET))

        def _parse_is_not_editable_for_children(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_not_editable_for_children = _parse_is_not_editable_for_children(
            d.pop("is_not_editable_for_children", UNSET)
        )

        def _parse_parent_entity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_entity = _parse_parent_entity(d.pop("parent_entity", UNSET))

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

        knowledge_unit_update = cls(
            knowledge_unit_name=knowledge_unit_name,
            knowledge_unit_description=knowledge_unit_description,
            knowledge_topics=knowledge_topics,
            is_not_editable_for_children=is_not_editable_for_children,
            parent_entity=parent_entity,
            external_source=external_source,
        )

        knowledge_unit_update.additional_properties = d
        return knowledge_unit_update

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
