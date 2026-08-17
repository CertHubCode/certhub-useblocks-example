from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_topic_update_data_type_0 import (
        KnowledgeTopicUpdateDataType0,
    )
    from ..models.knowledge_topic_update_knowledge_topic_schema_type_0 import (
        KnowledgeTopicUpdateKnowledgeTopicSchemaType0,
    )


T = TypeVar("T", bound="KnowledgeTopicUpdate")


@_attrs_define
class KnowledgeTopicUpdate:
    """Model for updating a Knowledge Topic.

    Only allows updating:
    - knowledge_topic_name: The name of the knowledge topic
    - knowledge_topic_schema: The schema definition (form structure)
    - data: The actual data stored in the topic

    Excluded fields (immutable/system-managed):
    - knowledge_unit_history_id: Ownership relationship (immutable)
    - product_history_id: Ownership relationship (immutable)
    - type: Fundamental characteristic (immutable)
    - product_data_collection_id: Tied to type and relationships (immutable)
    - source_schema_id: Historical reference (immutable)
    - metadata: System-managed tenant metadata (immutable)
    - audit_info: System-managed audit trail (auto-updated by service)

        Attributes:
            data (KnowledgeTopicUpdateDataType0 | None | Unset):
            knowledge_topic_name (None | str | Unset):
            knowledge_topic_schema (KnowledgeTopicUpdateKnowledgeTopicSchemaType0 | None | Unset):
    """

    data: KnowledgeTopicUpdateDataType0 | None | Unset = UNSET
    knowledge_topic_name: None | str | Unset = UNSET
    knowledge_topic_schema: (
        KnowledgeTopicUpdateKnowledgeTopicSchemaType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.knowledge_topic_update_data_type_0 import (
            KnowledgeTopicUpdateDataType0,
        )
        from ..models.knowledge_topic_update_knowledge_topic_schema_type_0 import (
            KnowledgeTopicUpdateKnowledgeTopicSchemaType0,
        )

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, KnowledgeTopicUpdateDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        knowledge_topic_name: None | str | Unset
        if isinstance(self.knowledge_topic_name, Unset):
            knowledge_topic_name = UNSET
        else:
            knowledge_topic_name = self.knowledge_topic_name

        knowledge_topic_schema: dict[str, Any] | None | Unset
        if isinstance(self.knowledge_topic_schema, Unset):
            knowledge_topic_schema = UNSET
        elif isinstance(
            self.knowledge_topic_schema, KnowledgeTopicUpdateKnowledgeTopicSchemaType0
        ):
            knowledge_topic_schema = self.knowledge_topic_schema.to_dict()
        else:
            knowledge_topic_schema = self.knowledge_topic_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if knowledge_topic_name is not UNSET:
            field_dict["knowledge_topic_name"] = knowledge_topic_name
        if knowledge_topic_schema is not UNSET:
            field_dict["knowledge_topic_schema"] = knowledge_topic_schema

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_topic_update_data_type_0 import (
            KnowledgeTopicUpdateDataType0,
        )
        from ..models.knowledge_topic_update_knowledge_topic_schema_type_0 import (
            KnowledgeTopicUpdateKnowledgeTopicSchemaType0,
        )

        d = dict(src_dict)

        def _parse_data(data: object) -> KnowledgeTopicUpdateDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = KnowledgeTopicUpdateDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KnowledgeTopicUpdateDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_knowledge_topic_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_topic_name = _parse_knowledge_topic_name(
            d.pop("knowledge_topic_name", UNSET)
        )

        def _parse_knowledge_topic_schema(
            data: object,
        ) -> KnowledgeTopicUpdateKnowledgeTopicSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                knowledge_topic_schema_type_0 = (
                    KnowledgeTopicUpdateKnowledgeTopicSchemaType0.from_dict(data)
                )

                return knowledge_topic_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KnowledgeTopicUpdateKnowledgeTopicSchemaType0 | None | Unset, data
            )

        knowledge_topic_schema = _parse_knowledge_topic_schema(
            d.pop("knowledge_topic_schema", UNSET)
        )

        knowledge_topic_update = cls(
            data=data,
            knowledge_topic_name=knowledge_topic_name,
            knowledge_topic_schema=knowledge_topic_schema,
        )

        knowledge_topic_update.additional_properties = d
        return knowledge_topic_update

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
