from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.global_element_type import GlobalElementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_element_create_schema import GlobalElementCreateSchema


T = TypeVar("T", bound="GlobalElementCreate")


@_attrs_define
class GlobalElementCreate:
    """
    Attributes:
        name (str):
        type_ (GlobalElementType):
        schema (GlobalElementCreateSchema | Unset):
        description (None | str | Unset):
    """

    name: str
    type_: GlobalElementType
    schema: GlobalElementCreateSchema | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.global_element_create_schema import GlobalElementCreateSchema

        d = dict(src_dict)
        name = d.pop("name")

        type_ = GlobalElementType(d.pop("type"))

        _schema = d.pop("schema", UNSET)
        schema: GlobalElementCreateSchema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = GlobalElementCreateSchema.from_dict(_schema)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        global_element_create = cls(
            name=name,
            type_=type_,
            schema=schema,
            description=description,
        )

        global_element_create.additional_properties = d
        return global_element_create

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
