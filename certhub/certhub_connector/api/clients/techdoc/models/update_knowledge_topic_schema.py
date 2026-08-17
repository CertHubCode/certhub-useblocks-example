from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_knowledge_topic_schema_component_schema_type_0 import (
        UpdateKnowledgeTopicSchemaComponentSchemaType0,
    )
    from ..models.update_knowledge_topic_schema_data_type_0 import (
        UpdateKnowledgeTopicSchemaDataType0,
    )


T = TypeVar("T", bound="UpdateKnowledgeTopicSchema")


@_attrs_define
class UpdateKnowledgeTopicSchema:
    """Model for updating a knowledge topic schema

    Attributes:
        knowledge_topic_name (None | str | Unset):
        component_schema (None | Unset | UpdateKnowledgeTopicSchemaComponentSchemaType0):
        data (None | Unset | UpdateKnowledgeTopicSchemaDataType0):
        knowledge_unit_schema_history_id (None | str | Unset):
    """

    knowledge_topic_name: None | str | Unset = UNSET
    component_schema: None | Unset | UpdateKnowledgeTopicSchemaComponentSchemaType0 = (
        UNSET
    )
    data: None | Unset | UpdateKnowledgeTopicSchemaDataType0 = UNSET
    knowledge_unit_schema_history_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_knowledge_topic_schema_component_schema_type_0 import (
            UpdateKnowledgeTopicSchemaComponentSchemaType0,
        )
        from ..models.update_knowledge_topic_schema_data_type_0 import (
            UpdateKnowledgeTopicSchemaDataType0,
        )

        knowledge_topic_name: None | str | Unset
        if isinstance(self.knowledge_topic_name, Unset):
            knowledge_topic_name = UNSET
        else:
            knowledge_topic_name = self.knowledge_topic_name

        component_schema: dict[str, Any] | None | Unset
        if isinstance(self.component_schema, Unset):
            component_schema = UNSET
        elif isinstance(
            self.component_schema, UpdateKnowledgeTopicSchemaComponentSchemaType0
        ):
            component_schema = self.component_schema.to_dict()
        else:
            component_schema = self.component_schema

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, UpdateKnowledgeTopicSchemaDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        knowledge_unit_schema_history_id: None | str | Unset
        if isinstance(self.knowledge_unit_schema_history_id, Unset):
            knowledge_unit_schema_history_id = UNSET
        else:
            knowledge_unit_schema_history_id = self.knowledge_unit_schema_history_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if knowledge_topic_name is not UNSET:
            field_dict["knowledge_topic_name"] = knowledge_topic_name
        if component_schema is not UNSET:
            field_dict["component_schema"] = component_schema
        if data is not UNSET:
            field_dict["data"] = data
        if knowledge_unit_schema_history_id is not UNSET:
            field_dict["knowledge_unit_schema_history_id"] = (
                knowledge_unit_schema_history_id
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_knowledge_topic_schema_component_schema_type_0 import (
            UpdateKnowledgeTopicSchemaComponentSchemaType0,
        )
        from ..models.update_knowledge_topic_schema_data_type_0 import (
            UpdateKnowledgeTopicSchemaDataType0,
        )

        d = dict(src_dict)

        def _parse_knowledge_topic_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_topic_name = _parse_knowledge_topic_name(
            d.pop("knowledge_topic_name", UNSET)
        )

        def _parse_component_schema(
            data: object,
        ) -> None | Unset | UpdateKnowledgeTopicSchemaComponentSchemaType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_schema_type_0 = (
                    UpdateKnowledgeTopicSchemaComponentSchemaType0.from_dict(data)
                )

                return component_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | Unset | UpdateKnowledgeTopicSchemaComponentSchemaType0, data
            )

        component_schema = _parse_component_schema(d.pop("component_schema", UNSET))

        def _parse_data(
            data: object,
        ) -> None | Unset | UpdateKnowledgeTopicSchemaDataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = UpdateKnowledgeTopicSchemaDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateKnowledgeTopicSchemaDataType0, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_knowledge_unit_schema_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_schema_history_id = _parse_knowledge_unit_schema_history_id(
            d.pop("knowledge_unit_schema_history_id", UNSET)
        )

        update_knowledge_topic_schema = cls(
            knowledge_topic_name=knowledge_topic_name,
            component_schema=component_schema,
            data=data,
            knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
        )

        update_knowledge_topic_schema.additional_properties = d
        return update_knowledge_topic_schema

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
