from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportRequest")


@_attrs_define
class ImportRequest:
    """Request model for importing units or schemas

    Attributes:
        files (list[str]): JSON files in string format to import
        library_ids (list[str] | None | Unset): Library IDs to associate with imported schemas
    """

    files: list[str]
    library_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = self.files

        library_ids: list[str] | None | Unset
        if isinstance(self.library_ids, Unset):
            library_ids = UNSET
        elif isinstance(self.library_ids, list):
            library_ids = self.library_ids

        else:
            library_ids = self.library_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
            }
        )
        if library_ids is not UNSET:
            field_dict["library_ids"] = library_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        files = cast(list[str], d.pop("files"))

        def _parse_library_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                library_ids_type_0 = cast(list[str], data)

                return library_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        library_ids = _parse_library_ids(d.pop("library_ids", UNSET))

        import_request = cls(
            files=files,
            library_ids=library_ids,
        )

        import_request.additional_properties = d
        return import_request

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
