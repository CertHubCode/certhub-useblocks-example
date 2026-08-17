from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QmListCreate")


@_attrs_define
class QmListCreate:
    """
    Attributes:
        name (str):
        template_ids (list[str]):
        description (None | str | Unset):  Default: ''.
        filter_tag (None | str | Unset):
    """

    name: str
    template_ids: list[str]
    description: None | str | Unset = ""
    filter_tag: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        template_ids = self.template_ids

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        filter_tag: None | str | Unset
        if isinstance(self.filter_tag, Unset):
            filter_tag = UNSET
        else:
            filter_tag = self.filter_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "template_ids": template_ids,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if filter_tag is not UNSET:
            field_dict["filter_tag"] = filter_tag

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        template_ids = cast(list[str], d.pop("template_ids"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_filter_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_tag = _parse_filter_tag(d.pop("filter_tag", UNSET))

        qm_list_create = cls(
            name=name,
            template_ids=template_ids,
            description=description,
            filter_tag=filter_tag,
        )

        qm_list_create.additional_properties = d
        return qm_list_create

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
