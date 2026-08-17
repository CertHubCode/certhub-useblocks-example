from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_topic_type import KnowledgeTopicType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_knowledge_topic_from_existing import (
        CreateKnowledgeTopicFromExisting,
    )
    from ..models.create_knowledge_topic_knowledge_topic_schema import (
        CreateKnowledgeTopicKnowledgeTopicSchema,
    )
    from ..models.external_source_info import ExternalSourceInfo
    from ..models.no_external_source import NoExternalSource


T = TypeVar("T", bound="CreateKnowledgeTopic")


@_attrs_define
class CreateKnowledgeTopic:
    """
    Attributes:
        knowledge_topic_name (str):
        knowledge_topic_schema (CreateKnowledgeTopicKnowledgeTopicSchema):
        related_form_id (str):
        type_ (KnowledgeTopicType):
        product_data_collection_id (None | str | Unset):
        external_source (ExternalSourceInfo | NoExternalSource | None | Unset):
        from_existing (CreateKnowledgeTopicFromExisting | None | Unset):
    """

    knowledge_topic_name: str
    knowledge_topic_schema: CreateKnowledgeTopicKnowledgeTopicSchema
    related_form_id: str
    type_: KnowledgeTopicType
    product_data_collection_id: None | str | Unset = UNSET
    external_source: ExternalSourceInfo | NoExternalSource | None | Unset = UNSET
    from_existing: CreateKnowledgeTopicFromExisting | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_knowledge_topic_from_existing import (
            CreateKnowledgeTopicFromExisting,
        )
        from ..models.external_source_info import ExternalSourceInfo
        from ..models.no_external_source import NoExternalSource

        knowledge_topic_name = self.knowledge_topic_name

        knowledge_topic_schema = self.knowledge_topic_schema.to_dict()

        related_form_id = self.related_form_id

        type_ = self.type_.value

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

        from_existing: dict[str, Any] | None | Unset
        if isinstance(self.from_existing, Unset):
            from_existing = UNSET
        elif isinstance(self.from_existing, CreateKnowledgeTopicFromExisting):
            from_existing = self.from_existing.to_dict()
        else:
            from_existing = self.from_existing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_topic_name": knowledge_topic_name,
                "knowledge_topic_schema": knowledge_topic_schema,
                "related_form_id": related_form_id,
                "type": type_,
            }
        )
        if product_data_collection_id is not UNSET:
            field_dict["product_data_collection_id"] = product_data_collection_id
        if external_source is not UNSET:
            field_dict["external_source"] = external_source
        if from_existing is not UNSET:
            field_dict["from_existing"] = from_existing

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_knowledge_topic_from_existing import (
            CreateKnowledgeTopicFromExisting,
        )
        from ..models.create_knowledge_topic_knowledge_topic_schema import (
            CreateKnowledgeTopicKnowledgeTopicSchema,
        )
        from ..models.external_source_info import ExternalSourceInfo
        from ..models.no_external_source import NoExternalSource

        d = dict(src_dict)
        knowledge_topic_name = d.pop("knowledge_topic_name")

        knowledge_topic_schema = CreateKnowledgeTopicKnowledgeTopicSchema.from_dict(
            d.pop("knowledge_topic_schema")
        )

        related_form_id = d.pop("related_form_id")

        type_ = KnowledgeTopicType(d.pop("type"))

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

        def _parse_from_existing(
            data: object,
        ) -> CreateKnowledgeTopicFromExisting | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                from_existing_type_0 = CreateKnowledgeTopicFromExisting.from_dict(data)

                return from_existing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateKnowledgeTopicFromExisting | None | Unset, data)

        from_existing = _parse_from_existing(d.pop("from_existing", UNSET))

        create_knowledge_topic = cls(
            knowledge_topic_name=knowledge_topic_name,
            knowledge_topic_schema=knowledge_topic_schema,
            related_form_id=related_form_id,
            type_=type_,
            product_data_collection_id=product_data_collection_id,
            external_source=external_source,
            from_existing=from_existing,
        )

        create_knowledge_topic.additional_properties = d
        return create_knowledge_topic

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
