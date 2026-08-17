from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kt_sync_result import KtSyncResult


T = TypeVar("T", bound="ApplyUnderlyingSchemaResponse")


@_attrs_define
class ApplyUnderlyingSchemaResponse:
    """Response for the 'Apply Underlying Schema' action on a Product KU.

    Pulls the LATEST APPROVED revision of the Schema Library schema this
    Product KU is "auto based on" down onto the Product KU: existing
    Knowledge Topics that still match a schema topic get their
    name/form updated in place (their data is never touched), and schema
    topics with no existing match get created as brand new Knowledge
    Topics. Product Knowledge Topics that no longer have any counterpart in
    the schema's latest approved revision are left untouched - this action
    never removes content from the Product KU. A draft (unapproved) schema
    revision is never eligible, no matter how new.

    applied_ku_schema_history_id/applied_ku_schema_id/applied_ku_schema_version
    identify the approved schema revision that was applied.

        Attributes:
            success (bool):
            message (str):
            applied_ku_schema_history_id (None | str | Unset):
            applied_ku_schema_id (None | str | Unset):
            applied_ku_schema_version (None | str | Unset):
            kt_results (list[KtSyncResult] | Unset):
    """

    success: bool
    message: str
    applied_ku_schema_history_id: None | str | Unset = UNSET
    applied_ku_schema_id: None | str | Unset = UNSET
    applied_ku_schema_version: None | str | Unset = UNSET
    kt_results: list[KtSyncResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        applied_ku_schema_history_id: None | str | Unset
        if isinstance(self.applied_ku_schema_history_id, Unset):
            applied_ku_schema_history_id = UNSET
        else:
            applied_ku_schema_history_id = self.applied_ku_schema_history_id

        applied_ku_schema_id: None | str | Unset
        if isinstance(self.applied_ku_schema_id, Unset):
            applied_ku_schema_id = UNSET
        else:
            applied_ku_schema_id = self.applied_ku_schema_id

        applied_ku_schema_version: None | str | Unset
        if isinstance(self.applied_ku_schema_version, Unset):
            applied_ku_schema_version = UNSET
        else:
            applied_ku_schema_version = self.applied_ku_schema_version

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
        if applied_ku_schema_history_id is not UNSET:
            field_dict["applied_ku_schema_history_id"] = applied_ku_schema_history_id
        if applied_ku_schema_id is not UNSET:
            field_dict["applied_ku_schema_id"] = applied_ku_schema_id
        if applied_ku_schema_version is not UNSET:
            field_dict["applied_ku_schema_version"] = applied_ku_schema_version
        if kt_results is not UNSET:
            field_dict["kt_results"] = kt_results

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kt_sync_result import KtSyncResult

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        def _parse_applied_ku_schema_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applied_ku_schema_history_id = _parse_applied_ku_schema_history_id(
            d.pop("applied_ku_schema_history_id", UNSET)
        )

        def _parse_applied_ku_schema_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applied_ku_schema_id = _parse_applied_ku_schema_id(
            d.pop("applied_ku_schema_id", UNSET)
        )

        def _parse_applied_ku_schema_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applied_ku_schema_version = _parse_applied_ku_schema_version(
            d.pop("applied_ku_schema_version", UNSET)
        )

        _kt_results = d.pop("kt_results", UNSET)
        kt_results: list[KtSyncResult] | Unset = UNSET
        if _kt_results is not UNSET:
            kt_results = []
            for kt_results_item_data in _kt_results:
                kt_results_item = KtSyncResult.from_dict(kt_results_item_data)

                kt_results.append(kt_results_item)

        apply_underlying_schema_response = cls(
            success=success,
            message=message,
            applied_ku_schema_history_id=applied_ku_schema_history_id,
            applied_ku_schema_id=applied_ku_schema_id,
            applied_ku_schema_version=applied_ku_schema_version,
            kt_results=kt_results,
        )

        apply_underlying_schema_response.additional_properties = d
        return apply_underlying_schema_response

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
