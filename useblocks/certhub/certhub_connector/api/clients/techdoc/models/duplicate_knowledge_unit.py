from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parent_entity import ParentEntity
from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateKnowledgeUnit")


@_attrs_define
class DuplicateKnowledgeUnit:
    """
    Attributes:
        product_history_id (str):
        parent_entity (ParentEntity):
        ku_schema_id (None | str | Unset): ID of existing knowledge unit schema to copy from
        ku_history_id (None | str | Unset): ID of knowledge unit to create schema from
        include_content (bool | Unset): Whether to include content in the copy Default: False.
    """

    product_history_id: str
    parent_entity: ParentEntity
    ku_schema_id: None | str | Unset = UNSET
    ku_history_id: None | str | Unset = UNSET
    include_content: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_history_id = self.product_history_id

        parent_entity = self.parent_entity.value

        ku_schema_id: None | str | Unset
        if isinstance(self.ku_schema_id, Unset):
            ku_schema_id = UNSET
        else:
            ku_schema_id = self.ku_schema_id

        ku_history_id: None | str | Unset
        if isinstance(self.ku_history_id, Unset):
            ku_history_id = UNSET
        else:
            ku_history_id = self.ku_history_id

        include_content = self.include_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_history_id": product_history_id,
                "parent_entity": parent_entity,
            }
        )
        if ku_schema_id is not UNSET:
            field_dict["ku_schema_id"] = ku_schema_id
        if ku_history_id is not UNSET:
            field_dict["ku_history_id"] = ku_history_id
        if include_content is not UNSET:
            field_dict["include_content"] = include_content

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        product_history_id = d.pop("product_history_id")

        parent_entity = ParentEntity(d.pop("parent_entity"))

        def _parse_ku_schema_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ku_schema_id = _parse_ku_schema_id(d.pop("ku_schema_id", UNSET))

        def _parse_ku_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ku_history_id = _parse_ku_history_id(d.pop("ku_history_id", UNSET))

        include_content = d.pop("include_content", UNSET)

        duplicate_knowledge_unit = cls(
            product_history_id=product_history_id,
            parent_entity=parent_entity,
            ku_schema_id=ku_schema_id,
            ku_history_id=ku_history_id,
            include_content=include_content,
        )

        duplicate_knowledge_unit.additional_properties = d
        return duplicate_knowledge_unit

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
