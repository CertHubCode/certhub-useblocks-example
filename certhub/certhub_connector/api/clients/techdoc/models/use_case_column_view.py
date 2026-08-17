from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UseCaseColumnView")


@_attrs_define
class UseCaseColumnView:
    """One purple trace column, with its target topic resolved to a history_id.

    Attributes:
        relation_name (str):
        target_knowledge_topic_name (str):
        bidirection (bool):
        target_knowledge_topic_history_id (None | str | Unset):
        allow_multiple (bool | Unset):  Default: False.
        additional_field (None | str | Unset):
        description (None | str | Unset):
        field (str | Unset):  Default: ''.
        additional_field_key (None | str | Unset):
    """

    relation_name: str
    target_knowledge_topic_name: str
    bidirection: bool
    target_knowledge_topic_history_id: None | str | Unset = UNSET
    allow_multiple: bool | Unset = False
    additional_field: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    field: str | Unset = ""
    additional_field_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relation_name = self.relation_name

        target_knowledge_topic_name = self.target_knowledge_topic_name

        bidirection = self.bidirection

        target_knowledge_topic_history_id: None | str | Unset
        if isinstance(self.target_knowledge_topic_history_id, Unset):
            target_knowledge_topic_history_id = UNSET
        else:
            target_knowledge_topic_history_id = self.target_knowledge_topic_history_id

        allow_multiple = self.allow_multiple

        additional_field: None | str | Unset
        if isinstance(self.additional_field, Unset):
            additional_field = UNSET
        else:
            additional_field = self.additional_field

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field = self.field

        additional_field_key: None | str | Unset
        if isinstance(self.additional_field_key, Unset):
            additional_field_key = UNSET
        else:
            additional_field_key = self.additional_field_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relation_name": relation_name,
                "target_knowledge_topic_name": target_knowledge_topic_name,
                "bidirection": bidirection,
            }
        )
        if target_knowledge_topic_history_id is not UNSET:
            field_dict["target_knowledge_topic_history_id"] = (
                target_knowledge_topic_history_id
            )
        if allow_multiple is not UNSET:
            field_dict["allow_multiple"] = allow_multiple
        if additional_field is not UNSET:
            field_dict["additional_field"] = additional_field
        if description is not UNSET:
            field_dict["description"] = description
        if field is not UNSET:
            field_dict["field"] = field
        if additional_field_key is not UNSET:
            field_dict["additional_field_key"] = additional_field_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        relation_name = d.pop("relation_name")

        target_knowledge_topic_name = d.pop("target_knowledge_topic_name")

        bidirection = d.pop("bidirection")

        def _parse_target_knowledge_topic_history_id(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_knowledge_topic_history_id = _parse_target_knowledge_topic_history_id(
            d.pop("target_knowledge_topic_history_id", UNSET)
        )

        allow_multiple = d.pop("allow_multiple", UNSET)

        def _parse_additional_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        additional_field = _parse_additional_field(d.pop("additional_field", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        field = d.pop("field", UNSET)

        def _parse_additional_field_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        additional_field_key = _parse_additional_field_key(
            d.pop("additional_field_key", UNSET)
        )

        use_case_column_view = cls(
            relation_name=relation_name,
            target_knowledge_topic_name=target_knowledge_topic_name,
            bidirection=bidirection,
            target_knowledge_topic_history_id=target_knowledge_topic_history_id,
            allow_multiple=allow_multiple,
            additional_field=additional_field,
            description=description,
            field=field,
            additional_field_key=additional_field_key,
        )

        use_case_column_view.additional_properties = d
        return use_case_column_view

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
