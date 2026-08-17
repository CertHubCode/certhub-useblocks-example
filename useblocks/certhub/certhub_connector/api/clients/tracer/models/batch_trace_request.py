from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch_trace_create_operation import BatchTraceCreateOperation
    from ..models.batch_trace_delete_by_id_operation import (
        BatchTraceDeleteByIdOperation,
    )
    from ..models.batch_trace_delete_by_target_operation import (
        BatchTraceDeleteByTargetOperation,
    )


T = TypeVar("T", bound="BatchTraceRequest")


@_attrs_define
class BatchTraceRequest:
    """
    Attributes:
        operations (list[BatchTraceCreateOperation | BatchTraceDeleteByIdOperation |
            BatchTraceDeleteByTargetOperation]):
    """

    operations: list[
        BatchTraceCreateOperation
        | BatchTraceDeleteByIdOperation
        | BatchTraceDeleteByTargetOperation
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_trace_create_operation import BatchTraceCreateOperation
        from ..models.batch_trace_delete_by_id_operation import (
            BatchTraceDeleteByIdOperation,
        )

        operations = []
        for operations_item_data in self.operations:
            operations_item: dict[str, Any]
            if isinstance(
                operations_item_data, BatchTraceCreateOperation
            ) or isinstance(operations_item_data, BatchTraceDeleteByIdOperation):
                operations_item = operations_item_data.to_dict()
            else:
                operations_item = operations_item_data.to_dict()

            operations.append(operations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operations": operations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_trace_create_operation import BatchTraceCreateOperation
        from ..models.batch_trace_delete_by_id_operation import (
            BatchTraceDeleteByIdOperation,
        )
        from ..models.batch_trace_delete_by_target_operation import (
            BatchTraceDeleteByTargetOperation,
        )

        d = dict(src_dict)
        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:

            def _parse_operations_item(
                data: object,
            ) -> (
                BatchTraceCreateOperation
                | BatchTraceDeleteByIdOperation
                | BatchTraceDeleteByTargetOperation
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_0 = BatchTraceCreateOperation.from_dict(data)

                    return operations_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_1 = BatchTraceDeleteByIdOperation.from_dict(
                        data
                    )

                    return operations_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                operations_item_type_2 = BatchTraceDeleteByTargetOperation.from_dict(
                    data
                )

                return operations_item_type_2

            operations_item = _parse_operations_item(operations_item_data)

            operations.append(operations_item)

        batch_trace_request = cls(
            operations=operations,
        )

        batch_trace_request.additional_properties = d
        return batch_trace_request

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
