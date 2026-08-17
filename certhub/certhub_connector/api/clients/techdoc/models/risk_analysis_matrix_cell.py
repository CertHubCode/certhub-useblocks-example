from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.risk_analysis_matrix_cell_data import RiskAnalysisMatrixCellData


T = TypeVar("T", bound="RiskAnalysisMatrixCell")


@_attrs_define
class RiskAnalysisMatrixCell:
    """One resolved Record in a chain.

    Its form schema (needed alongside `data` to resolve the same "<name> -
    <data name>" display label used elsewhere — `resolveRecordDataName`/
    `formatRecordDisplayName`) is not embedded here; look it up by
    `record_id` in the response's `forms` map instead.

        Attributes:
            record_id (str):
            name (str):
            data (RiskAnalysisMatrixCellData | Unset):
    """

    record_id: str
    name: str
    data: RiskAnalysisMatrixCellData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        name = self.name

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "record_id": record_id,
                "name": name,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.risk_analysis_matrix_cell_data import RiskAnalysisMatrixCellData

        d = dict(src_dict)
        record_id = d.pop("record_id")

        name = d.pop("name")

        _data = d.pop("data", UNSET)
        data: RiskAnalysisMatrixCellData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RiskAnalysisMatrixCellData.from_dict(_data)

        risk_analysis_matrix_cell = cls(
            record_id=record_id,
            name=name,
            data=data,
        )

        risk_analysis_matrix_cell.additional_properties = d
        return risk_analysis_matrix_cell

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
