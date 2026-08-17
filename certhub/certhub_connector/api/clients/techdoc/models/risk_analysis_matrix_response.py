from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.risk_analysis_matrix_response_forms import (
        RiskAnalysisMatrixResponseForms,
    )
    from ..models.risk_analysis_matrix_row import RiskAnalysisMatrixRow


T = TypeVar("T", bound="RiskAnalysisMatrixResponse")


@_attrs_define
class RiskAnalysisMatrixResponse:
    """
    Attributes:
        rows (list[RiskAnalysisMatrixRow] | Unset):
        forms (RiskAnalysisMatrixResponseForms | Unset):
    """

    rows: list[RiskAnalysisMatrixRow] | Unset = UNSET
    forms: RiskAnalysisMatrixResponseForms | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        forms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.forms, Unset):
            forms = self.forms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows
        if forms is not UNSET:
            field_dict["forms"] = forms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.risk_analysis_matrix_response_forms import (
            RiskAnalysisMatrixResponseForms,
        )
        from ..models.risk_analysis_matrix_row import RiskAnalysisMatrixRow

        d = dict(src_dict)
        _rows = d.pop("rows", UNSET)
        rows: list[RiskAnalysisMatrixRow] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = RiskAnalysisMatrixRow.from_dict(rows_item_data)

                rows.append(rows_item)

        _forms = d.pop("forms", UNSET)
        forms: RiskAnalysisMatrixResponseForms | Unset
        if isinstance(_forms, Unset):
            forms = UNSET
        else:
            forms = RiskAnalysisMatrixResponseForms.from_dict(_forms)

        risk_analysis_matrix_response = cls(
            rows=rows,
            forms=forms,
        )

        risk_analysis_matrix_response.additional_properties = d
        return risk_analysis_matrix_response

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
