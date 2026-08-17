from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.global_element_type import GlobalElementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_element_update_schema_type_0 import (
        GlobalElementUpdateSchemaType0,
    )


T = TypeVar("T", bound="GlobalElementUpdate")


@_attrs_define
class GlobalElementUpdate:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        schema (GlobalElementUpdateSchemaType0 | None | Unset):
        type_ (GlobalElementType | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    schema: GlobalElementUpdateSchemaType0 | None | Unset = UNSET
    type_: GlobalElementType | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.global_element_update_schema_type_0 import (
            GlobalElementUpdateSchemaType0,
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        schema: dict[str, Any] | None | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, GlobalElementUpdateSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, GlobalElementType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if schema is not UNSET:
            field_dict["schema"] = schema
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.global_element_update_schema_type_0 import (
            GlobalElementUpdateSchemaType0,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_schema(
            data: object,
        ) -> GlobalElementUpdateSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = GlobalElementUpdateSchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GlobalElementUpdateSchemaType0 | None | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_type_(data: object) -> GlobalElementType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = GlobalElementType(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GlobalElementType | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        global_element_update = cls(
            name=name,
            description=description,
            schema=schema,
            type_=type_,
        )

        global_element_update.additional_properties = d
        return global_element_update

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
