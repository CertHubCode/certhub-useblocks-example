from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.matrix_type import MatrixType

if TYPE_CHECKING:
    from ..models.traceability_matrix_request_records import (
        TraceabilityMatrixRequestRecords,
    )


T = TypeVar("T", bound="TraceabilityMatrixRequest")


@_attrs_define
class TraceabilityMatrixRequest:
    """
    Attributes:
        matrix_type (MatrixType):
        records (TraceabilityMatrixRequestRecords): Dictionary mapping record_id to record
    """

    matrix_type: MatrixType
    records: TraceabilityMatrixRequestRecords
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matrix_type = self.matrix_type.value

        records = self.records.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matrix_type": matrix_type,
                "records": records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.traceability_matrix_request_records import (
            TraceabilityMatrixRequestRecords,
        )

        d = dict(src_dict)
        matrix_type = MatrixType(d.pop("matrix_type"))

        records = TraceabilityMatrixRequestRecords.from_dict(d.pop("records"))

        traceability_matrix_request = cls(
            matrix_type=matrix_type,
            records=records,
        )

        traceability_matrix_request.additional_properties = d
        return traceability_matrix_request

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
