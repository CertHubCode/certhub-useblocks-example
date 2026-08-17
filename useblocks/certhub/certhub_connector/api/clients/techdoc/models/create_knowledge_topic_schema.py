from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_topic_type import KnowledgeTopicType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_knowledge_topic_schema_component_schema_type_0 import (
        CreateKnowledgeTopicSchemaComponentSchemaType0,
    )
    from ..models.create_knowledge_topic_schema_data_type_0 import (
        CreateKnowledgeTopicSchemaDataType0,
    )
    from ..models.create_knowledge_topic_schema_from_existing import (
        CreateKnowledgeTopicSchemaFromExisting,
    )


T = TypeVar("T", bound="CreateKnowledgeTopicSchema")


@_attrs_define
class CreateKnowledgeTopicSchema:
    """Model for creating a new knowledge topic schema

    Attributes:
        knowledge_topic_name (str):
        type_ (KnowledgeTopicType):
        knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        component_schema (CreateKnowledgeTopicSchemaComponentSchemaType0 | None | Unset):
        product_data_collection_id (None | str | Unset):
        data (CreateKnowledgeTopicSchemaDataType0 | None | Unset):
        from_existing (CreateKnowledgeTopicSchemaFromExisting | None | Unset):
    """

    knowledge_topic_name: str
    type_: KnowledgeTopicType
    knowledge_unit_schema_history_id: str
    component_schema: CreateKnowledgeTopicSchemaComponentSchemaType0 | None | Unset = (
        UNSET
    )
    product_data_collection_id: None | str | Unset = UNSET
    data: CreateKnowledgeTopicSchemaDataType0 | None | Unset = UNSET
    from_existing: CreateKnowledgeTopicSchemaFromExisting | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_knowledge_topic_schema_component_schema_type_0 import (
            CreateKnowledgeTopicSchemaComponentSchemaType0,
        )
        from ..models.create_knowledge_topic_schema_data_type_0 import (
            CreateKnowledgeTopicSchemaDataType0,
        )
        from ..models.create_knowledge_topic_schema_from_existing import (
            CreateKnowledgeTopicSchemaFromExisting,
        )

        knowledge_topic_name = self.knowledge_topic_name

        type_ = self.type_.value

        knowledge_unit_schema_history_id = self.knowledge_unit_schema_history_id

        component_schema: dict[str, Any] | None | Unset
        if isinstance(self.component_schema, Unset):
            component_schema = UNSET
        elif isinstance(
            self.component_schema, CreateKnowledgeTopicSchemaComponentSchemaType0
        ):
            component_schema = self.component_schema.to_dict()
        else:
            component_schema = self.component_schema

        product_data_collection_id: None | str | Unset
        if isinstance(self.product_data_collection_id, Unset):
            product_data_collection_id = UNSET
        else:
            product_data_collection_id = self.product_data_collection_id

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, CreateKnowledgeTopicSchemaDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        from_existing: dict[str, Any] | None | Unset
        if isinstance(self.from_existing, Unset):
            from_existing = UNSET
        elif isinstance(self.from_existing, CreateKnowledgeTopicSchemaFromExisting):
            from_existing = self.from_existing.to_dict()
        else:
            from_existing = self.from_existing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_topic_name": knowledge_topic_name,
                "type": type_,
                "knowledge_unit_schema_history_id": knowledge_unit_schema_history_id,
            }
        )
        if component_schema is not UNSET:
            field_dict["component_schema"] = component_schema
        if product_data_collection_id is not UNSET:
            field_dict["product_data_collection_id"] = product_data_collection_id
        if data is not UNSET:
            field_dict["data"] = data
        if from_existing is not UNSET:
            field_dict["from_existing"] = from_existing

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_knowledge_topic_schema_component_schema_type_0 import (
            CreateKnowledgeTopicSchemaComponentSchemaType0,
        )
        from ..models.create_knowledge_topic_schema_data_type_0 import (
            CreateKnowledgeTopicSchemaDataType0,
        )
        from ..models.create_knowledge_topic_schema_from_existing import (
            CreateKnowledgeTopicSchemaFromExisting,
        )

        d = dict(src_dict)
        knowledge_topic_name = d.pop("knowledge_topic_name")

        type_ = KnowledgeTopicType(d.pop("type"))

        knowledge_unit_schema_history_id = d.pop("knowledge_unit_schema_history_id")

        def _parse_component_schema(
            data: object,
        ) -> CreateKnowledgeTopicSchemaComponentSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_schema_type_0 = (
                    CreateKnowledgeTopicSchemaComponentSchemaType0.from_dict(data)
                )

                return component_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateKnowledgeTopicSchemaComponentSchemaType0 | None | Unset, data
            )

        component_schema = _parse_component_schema(d.pop("component_schema", UNSET))

        def _parse_product_data_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_data_collection_id = _parse_product_data_collection_id(
            d.pop("product_data_collection_id", UNSET)
        )

        def _parse_data(
            data: object,
        ) -> CreateKnowledgeTopicSchemaDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = CreateKnowledgeTopicSchemaDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateKnowledgeTopicSchemaDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_from_existing(
            data: object,
        ) -> CreateKnowledgeTopicSchemaFromExisting | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                from_existing_type_0 = CreateKnowledgeTopicSchemaFromExisting.from_dict(
                    data
                )

                return from_existing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateKnowledgeTopicSchemaFromExisting | None | Unset, data)

        from_existing = _parse_from_existing(d.pop("from_existing", UNSET))

        create_knowledge_topic_schema = cls(
            knowledge_topic_name=knowledge_topic_name,
            type_=type_,
            knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
            component_schema=component_schema,
            product_data_collection_id=product_data_collection_id,
            data=data,
            from_existing=from_existing,
        )

        create_knowledge_topic_schema.additional_properties = d
        return create_knowledge_topic_schema

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
