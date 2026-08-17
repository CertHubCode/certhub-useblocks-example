from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knowledge_topic_type import KnowledgeTopicType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_topic_overview_response_knowledge_topic_schema_type_0 import (
        KnowledgeTopicOverviewResponseKnowledgeTopicSchemaType0,
    )
    from ..models.trace_info import TraceInfo


T = TypeVar("T", bound="KnowledgeTopicOverviewResponse")


@_attrs_define
class KnowledgeTopicOverviewResponse:
    """
    Attributes:
        id (str):
        type_ (KnowledgeTopicType):
        knowledge_topic_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_name (str):
        knowledge_topic_name (str):
        knowledge_unit_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_version (str):
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        from_family (bool):
        knowledge_topic_schema (KnowledgeTopicOverviewResponseKnowledgeTopicSchemaType0 | None | Unset):
        knowledge_unit_revision_id (None | str | Unset):
        product_revision_id (None | str | Unset):
        product_version (None | str | Unset):
        product_name (None | str | Unset):
        latest_revision_id (None | str | Unset):
        latest_or_latest_approved_revision_id (None | str | Unset):
        traces (list[TraceInfo] | Unset):
    """

    id: str
    type_: KnowledgeTopicType
    knowledge_topic_history_id: str
    knowledge_unit_name: str
    knowledge_topic_name: str
    knowledge_unit_history_id: str
    knowledge_unit_version: str
    product_history_id: str
    from_family: bool
    knowledge_topic_schema: (
        KnowledgeTopicOverviewResponseKnowledgeTopicSchemaType0 | None | Unset
    ) = UNSET
    knowledge_unit_revision_id: None | str | Unset = UNSET
    product_revision_id: None | str | Unset = UNSET
    product_version: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    latest_revision_id: None | str | Unset = UNSET
    latest_or_latest_approved_revision_id: None | str | Unset = UNSET
    traces: list[TraceInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.knowledge_topic_overview_response_knowledge_topic_schema_type_0 import (
            KnowledgeTopicOverviewResponseKnowledgeTopicSchemaType0,
        )

        id = self.id

        type_ = self.type_.value

        knowledge_topic_history_id = self.knowledge_topic_history_id

        knowledge_unit_name = self.knowledge_unit_name

        knowledge_topic_name = self.knowledge_topic_name

        knowledge_unit_history_id = self.knowledge_unit_history_id

        knowledge_unit_version = self.knowledge_unit_version

        product_history_id = self.product_history_id

        from_family = self.from_family

        knowledge_topic_schema: dict[str, Any] | None | Unset
        if isinstance(self.knowledge_topic_schema, Unset):
            knowledge_topic_schema = UNSET
        elif isinstance(
            self.knowledge_topic_schema,
            KnowledgeTopicOverviewResponseKnowledgeTopicSchemaType0,
        ):
            knowledge_topic_schema = self.knowledge_topic_schema.to_dict()
        else:
            knowledge_topic_schema = self.knowledge_topic_schema

        knowledge_unit_revision_id: None | str | Unset
        if isinstance(self.knowledge_unit_revision_id, Unset):
            knowledge_unit_revision_id = UNSET
        else:
            knowledge_unit_revision_id = self.knowledge_unit_revision_id

        product_revision_id: None | str | Unset
        if isinstance(self.product_revision_id, Unset):
            product_revision_id = UNSET
        else:
            product_revision_id = self.product_revision_id

        product_version: None | str | Unset
        if isinstance(self.product_version, Unset):
            product_version = UNSET
        else:
            product_version = self.product_version

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        latest_revision_id: None | str | Unset
        if isinstance(self.latest_revision_id, Unset):
            latest_revision_id = UNSET
        else:
            latest_revision_id = self.latest_revision_id

        latest_or_latest_approved_revision_id: None | str | Unset
        if isinstance(self.latest_or_latest_approved_revision_id, Unset):
            latest_or_latest_approved_revision_id = UNSET
        else:
            latest_or_latest_approved_revision_id = (
                self.latest_or_latest_approved_revision_id
            )

        traces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.traces, Unset):
            traces = []
            for traces_item_data in self.traces:
                traces_item = traces_item_data.to_dict()
                traces.append(traces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "knowledge_topic_history_id": knowledge_topic_history_id,
                "knowledge_unit_name": knowledge_unit_name,
                "knowledge_topic_name": knowledge_topic_name,
                "knowledge_unit_history_id": knowledge_unit_history_id,
                "knowledge_unit_version": knowledge_unit_version,
                "product_history_id": product_history_id,
                "from_family": from_family,
            }
        )
        if knowledge_topic_schema is not UNSET:
            field_dict["knowledge_topic_schema"] = knowledge_topic_schema
        if knowledge_unit_revision_id is not UNSET:
            field_dict["knowledge_unit_revision_id"] = knowledge_unit_revision_id
        if product_revision_id is not UNSET:
            field_dict["product_revision_id"] = product_revision_id
        if product_version is not UNSET:
            field_dict["product_version"] = product_version
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if latest_revision_id is not UNSET:
            field_dict["latest_revision_id"] = latest_revision_id
        if latest_or_latest_approved_revision_id is not UNSET:
            field_dict["latest_or_latest_approved_revision_id"] = (
                latest_or_latest_approved_revision_id
            )
        if traces is not UNSET:
            field_dict["traces"] = traces

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_topic_overview_response_knowledge_topic_schema_type_0 import (
            KnowledgeTopicOverviewResponseKnowledgeTopicSchemaType0,
        )
        from ..models.trace_info import TraceInfo

        d = dict(src_dict)
        id = d.pop("id")

        type_ = KnowledgeTopicType(d.pop("type"))

        knowledge_topic_history_id = d.pop("knowledge_topic_history_id")

        knowledge_unit_name = d.pop("knowledge_unit_name")

        knowledge_topic_name = d.pop("knowledge_topic_name")

        knowledge_unit_history_id = d.pop("knowledge_unit_history_id")

        knowledge_unit_version = d.pop("knowledge_unit_version")

        product_history_id = d.pop("product_history_id")

        from_family = d.pop("from_family")

        def _parse_knowledge_topic_schema(
            data: object,
        ) -> KnowledgeTopicOverviewResponseKnowledgeTopicSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                knowledge_topic_schema_type_0 = (
                    KnowledgeTopicOverviewResponseKnowledgeTopicSchemaType0.from_dict(
                        data
                    )
                )

                return knowledge_topic_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KnowledgeTopicOverviewResponseKnowledgeTopicSchemaType0 | None | Unset,
                data,
            )

        knowledge_topic_schema = _parse_knowledge_topic_schema(
            d.pop("knowledge_topic_schema", UNSET)
        )

        def _parse_knowledge_unit_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_revision_id = _parse_knowledge_unit_revision_id(
            d.pop("knowledge_unit_revision_id", UNSET)
        )

        def _parse_product_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_revision_id = _parse_product_revision_id(
            d.pop("product_revision_id", UNSET)
        )

        def _parse_product_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_version = _parse_product_version(d.pop("product_version", UNSET))

        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("product_name", UNSET))

        def _parse_latest_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_revision_id = _parse_latest_revision_id(
            d.pop("latest_revision_id", UNSET)
        )

        def _parse_latest_or_latest_approved_revision_id(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_or_latest_approved_revision_id = (
            _parse_latest_or_latest_approved_revision_id(
                d.pop("latest_or_latest_approved_revision_id", UNSET)
            )
        )

        _traces = d.pop("traces", UNSET)
        traces: list[TraceInfo] | Unset = UNSET
        if _traces is not UNSET:
            traces = []
            for traces_item_data in _traces:
                traces_item = TraceInfo.from_dict(traces_item_data)

                traces.append(traces_item)

        knowledge_topic_overview_response = cls(
            id=id,
            type_=type_,
            knowledge_topic_history_id=knowledge_topic_history_id,
            knowledge_unit_name=knowledge_unit_name,
            knowledge_topic_name=knowledge_topic_name,
            knowledge_unit_history_id=knowledge_unit_history_id,
            knowledge_unit_version=knowledge_unit_version,
            product_history_id=product_history_id,
            from_family=from_family,
            knowledge_topic_schema=knowledge_topic_schema,
            knowledge_unit_revision_id=knowledge_unit_revision_id,
            product_revision_id=product_revision_id,
            product_version=product_version,
            product_name=product_name,
            latest_revision_id=latest_revision_id,
            latest_or_latest_approved_revision_id=latest_or_latest_approved_revision_id,
            traces=traces,
        )

        knowledge_topic_overview_response.additional_properties = d
        return knowledge_topic_overview_response

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
