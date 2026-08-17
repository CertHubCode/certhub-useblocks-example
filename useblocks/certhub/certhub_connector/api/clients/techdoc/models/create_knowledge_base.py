from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parent_entity import ParentEntity
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKnowledgeBase")


@_attrs_define
class CreateKnowledgeBase:
    """
    Attributes:
        knowledge_unit_name (str):
        parent_entity (ParentEntity):
        is_not_editable_for_children (bool | None | Unset):  Default: False.
    """

    knowledge_unit_name: str
    parent_entity: ParentEntity
    is_not_editable_for_children: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_unit_name = self.knowledge_unit_name

        parent_entity = self.parent_entity.value

        is_not_editable_for_children: bool | None | Unset
        if isinstance(self.is_not_editable_for_children, Unset):
            is_not_editable_for_children = UNSET
        else:
            is_not_editable_for_children = self.is_not_editable_for_children

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_unit_name": knowledge_unit_name,
                "parent_entity": parent_entity,
            }
        )
        if is_not_editable_for_children is not UNSET:
            field_dict["is_not_editable_for_children"] = is_not_editable_for_children

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        knowledge_unit_name = d.pop("knowledge_unit_name")

        parent_entity = ParentEntity(d.pop("parent_entity"))

        def _parse_is_not_editable_for_children(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_not_editable_for_children = _parse_is_not_editable_for_children(
            d.pop("is_not_editable_for_children", UNSET)
        )

        create_knowledge_base = cls(
            knowledge_unit_name=knowledge_unit_name,
            parent_entity=parent_entity,
            is_not_editable_for_children=is_not_editable_for_children,
        )

        create_knowledge_base.additional_properties = d
        return create_knowledge_base

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
