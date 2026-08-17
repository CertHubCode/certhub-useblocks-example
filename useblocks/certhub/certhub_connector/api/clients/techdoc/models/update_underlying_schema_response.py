from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kt_sync_result import KtSyncResult


T = TypeVar("T", bound="UpdateUnderlyingSchemaResponse")


@_attrs_define
class UpdateUnderlyingSchemaResponse:
    """Response for the 'Update Underlying Schema' action on a Product KU.

    Pushes the Product KU's current name/description/KT forms into a new
    draft revision of the Schema Library schema it was "auto based on".
    new_ku_schema_history_id/new_ku_schema_id/new_ku_schema_version identify
    that freshly created draft revision.

        Attributes:
            success (bool):
            message (str):
            new_ku_schema_history_id (None | str | Unset):
            new_ku_schema_id (None | str | Unset):
            new_ku_schema_version (None | str | Unset):
            kt_results (list[KtSyncResult] | Unset):
    """

    success: bool
    message: str
    new_ku_schema_history_id: None | str | Unset = UNSET
    new_ku_schema_id: None | str | Unset = UNSET
    new_ku_schema_version: None | str | Unset = UNSET
    kt_results: list[KtSyncResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        new_ku_schema_history_id: None | str | Unset
        if isinstance(self.new_ku_schema_history_id, Unset):
            new_ku_schema_history_id = UNSET
        else:
            new_ku_schema_history_id = self.new_ku_schema_history_id

        new_ku_schema_id: None | str | Unset
        if isinstance(self.new_ku_schema_id, Unset):
            new_ku_schema_id = UNSET
        else:
            new_ku_schema_id = self.new_ku_schema_id

        new_ku_schema_version: None | str | Unset
        if isinstance(self.new_ku_schema_version, Unset):
            new_ku_schema_version = UNSET
        else:
            new_ku_schema_version = self.new_ku_schema_version

        kt_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.kt_results, Unset):
            kt_results = []
            for kt_results_item_data in self.kt_results:
                kt_results_item = kt_results_item_data.to_dict()
                kt_results.append(kt_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
            }
        )
        if new_ku_schema_history_id is not UNSET:
            field_dict["new_ku_schema_history_id"] = new_ku_schema_history_id
        if new_ku_schema_id is not UNSET:
            field_dict["new_ku_schema_id"] = new_ku_schema_id
        if new_ku_schema_version is not UNSET:
            field_dict["new_ku_schema_version"] = new_ku_schema_version
        if kt_results is not UNSET:
            field_dict["kt_results"] = kt_results

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kt_sync_result import KtSyncResult

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        def _parse_new_ku_schema_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_ku_schema_history_id = _parse_new_ku_schema_history_id(
            d.pop("new_ku_schema_history_id", UNSET)
        )

        def _parse_new_ku_schema_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_ku_schema_id = _parse_new_ku_schema_id(d.pop("new_ku_schema_id", UNSET))

        def _parse_new_ku_schema_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_ku_schema_version = _parse_new_ku_schema_version(
            d.pop("new_ku_schema_version", UNSET)
        )

        _kt_results = d.pop("kt_results", UNSET)
        kt_results: list[KtSyncResult] | Unset = UNSET
        if _kt_results is not UNSET:
            kt_results = []
            for kt_results_item_data in _kt_results:
                kt_results_item = KtSyncResult.from_dict(kt_results_item_data)

                kt_results.append(kt_results_item)

        update_underlying_schema_response = cls(
            success=success,
            message=message,
            new_ku_schema_history_id=new_ku_schema_history_id,
            new_ku_schema_id=new_ku_schema_id,
            new_ku_schema_version=new_ku_schema_version,
            kt_results=kt_results,
        )

        update_underlying_schema_response.additional_properties = d
        return update_underlying_schema_response

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
