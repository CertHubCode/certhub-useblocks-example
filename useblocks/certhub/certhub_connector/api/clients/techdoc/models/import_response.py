from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_response_error_details_item import (
        ImportResponseErrorDetailsItem,
    )


T = TypeVar("T", bound="ImportResponse")


@_attrs_define
class ImportResponse:
    """Response model for import operations

    Attributes:
        successful_imports (int | Unset): Number of successfully imported units Default: 0.
        failed_imports (int | Unset): Number of failed imports Default: 0.
        error_details (list[ImportResponseErrorDetailsItem] | Unset): Details of any failed imports
    """

    successful_imports: int | Unset = 0
    failed_imports: int | Unset = 0
    error_details: list[ImportResponseErrorDetailsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        successful_imports = self.successful_imports

        failed_imports = self.failed_imports

        error_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.error_details, Unset):
            error_details = []
            for error_details_item_data in self.error_details:
                error_details_item = error_details_item_data.to_dict()
                error_details.append(error_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if successful_imports is not UNSET:
            field_dict["successful_imports"] = successful_imports
        if failed_imports is not UNSET:
            field_dict["failed_imports"] = failed_imports
        if error_details is not UNSET:
            field_dict["error_details"] = error_details

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.import_response_error_details_item import (
            ImportResponseErrorDetailsItem,
        )

        d = dict(src_dict)
        successful_imports = d.pop("successful_imports", UNSET)

        failed_imports = d.pop("failed_imports", UNSET)

        _error_details = d.pop("error_details", UNSET)
        error_details: list[ImportResponseErrorDetailsItem] | Unset = UNSET
        if _error_details is not UNSET:
            error_details = []
            for error_details_item_data in _error_details:
                error_details_item = ImportResponseErrorDetailsItem.from_dict(
                    error_details_item_data
                )

                error_details.append(error_details_item)

        import_response = cls(
            successful_imports=successful_imports,
            failed_imports=failed_imports,
            error_details=error_details,
        )

        import_response.additional_properties = d
        return import_response

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
