from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_status import BatchStatus

if TYPE_CHECKING:
    from ..models.batch_node_delete_result import BatchNodeDeleteResult


T = TypeVar("T", bound="BatchNodeDeleteResponse")


@_attrs_define
class BatchNodeDeleteResponse:
    """
    Attributes:
        results (list[BatchNodeDeleteResult]):
        status (BatchStatus):
        total_count (int):
        success_count (int):
        failure_count (int):
    """

    results: list[BatchNodeDeleteResult]
    status: BatchStatus
    total_count: int
    success_count: int
    failure_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        status = self.status.value

        total_count = self.total_count

        success_count = self.success_count

        failure_count = self.failure_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
                "total_count": total_count,
                "success_count": success_count,
                "failure_count": failure_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_node_delete_result import BatchNodeDeleteResult

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = BatchNodeDeleteResult.from_dict(results_item_data)

            results.append(results_item)

        status = BatchStatus(d.pop("status"))

        total_count = d.pop("total_count")

        success_count = d.pop("success_count")

        failure_count = d.pop("failure_count")

        batch_node_delete_response = cls(
            results=results,
            status=status,
            total_count=total_count,
            success_count=success_count,
            failure_count=failure_count,
        )

        batch_node_delete_response.additional_properties = d
        return batch_node_delete_response

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
