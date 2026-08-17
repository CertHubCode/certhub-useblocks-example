from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_retrieve_response_resolved_results_type_0 import (
        BatchRetrieveResponseResolvedResultsType0,
    )
    from ..models.batch_retrieve_response_results import BatchRetrieveResponseResults


T = TypeVar("T", bound="BatchRetrieveResponse")


@_attrs_define
class BatchRetrieveResponse:
    """
    Attributes:
        results (BatchRetrieveResponseResults):
        resolved_results (BatchRetrieveResponseResolvedResultsType0 | None | Unset):
    """

    results: BatchRetrieveResponseResults
    resolved_results: BatchRetrieveResponseResolvedResultsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_retrieve_response_resolved_results_type_0 import (
            BatchRetrieveResponseResolvedResultsType0,
        )

        results = self.results.to_dict()

        resolved_results: dict[str, Any] | None | Unset
        if isinstance(self.resolved_results, Unset):
            resolved_results = UNSET
        elif isinstance(
            self.resolved_results, BatchRetrieveResponseResolvedResultsType0
        ):
            resolved_results = self.resolved_results.to_dict()
        else:
            resolved_results = self.resolved_results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )
        if resolved_results is not UNSET:
            field_dict["resolved_results"] = resolved_results

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_retrieve_response_resolved_results_type_0 import (
            BatchRetrieveResponseResolvedResultsType0,
        )
        from ..models.batch_retrieve_response_results import (
            BatchRetrieveResponseResults,
        )

        d = dict(src_dict)
        results = BatchRetrieveResponseResults.from_dict(d.pop("results"))

        def _parse_resolved_results(
            data: object,
        ) -> BatchRetrieveResponseResolvedResultsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolved_results_type_0 = (
                    BatchRetrieveResponseResolvedResultsType0.from_dict(data)
                )

                return resolved_results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchRetrieveResponseResolvedResultsType0 | None | Unset, data)

        resolved_results = _parse_resolved_results(d.pop("resolved_results", UNSET))

        batch_retrieve_response = cls(
            results=results,
            resolved_results=resolved_results,
        )

        batch_retrieve_response.additional_properties = d
        return batch_retrieve_response

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
