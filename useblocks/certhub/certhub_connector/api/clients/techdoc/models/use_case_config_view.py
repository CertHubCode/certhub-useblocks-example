from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.use_case_column_view import UseCaseColumnView
    from ..models.use_case_status_view import UseCaseStatusView


T = TypeVar("T", bound="UseCaseConfigView")


@_attrs_define
class UseCaseConfigView:
    """Bundled use-case enrichment for one KT: the purple trace columns plus the
    completeness-banner status, grouped under a single field on the KT response.

    Grouping (rather than two sibling fields) keeps future additions — ordering,
    validation rules, etc. — from growing the top-level KT shape. Present only for
    multi_record topics that belong to a use case; None otherwise.

        Attributes:
            columns (list[UseCaseColumnView] | Unset):
            status (list[UseCaseStatusView] | Unset):
    """

    columns: list[UseCaseColumnView] | Unset = UNSET
    status: list[UseCaseStatusView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)

        status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.to_dict()
                status.append(status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.use_case_column_view import UseCaseColumnView
        from ..models.use_case_status_view import UseCaseStatusView

        d = dict(src_dict)
        _columns = d.pop("columns", UNSET)
        columns: list[UseCaseColumnView] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = UseCaseColumnView.from_dict(columns_item_data)

                columns.append(columns_item)

        _status = d.pop("status", UNSET)
        status: list[UseCaseStatusView] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = UseCaseStatusView.from_dict(status_item_data)

                status.append(status_item)

        use_case_config_view = cls(
            columns=columns,
            status=status,
        )

        use_case_config_view.additional_properties = d
        return use_case_config_view

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
