from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchNodeDeleteResult")


@_attrs_define
class BatchNodeDeleteResult:
    """
    Attributes:
        success (bool):
        node_identifier (str):
        edges_deleted (int | Unset):  Default: 0.
        error (None | str | Unset):
    """

    success: bool
    node_identifier: str
    edges_deleted: int | Unset = 0
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        node_identifier = self.node_identifier

        edges_deleted = self.edges_deleted

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "node_identifier": node_identifier,
            }
        )
        if edges_deleted is not UNSET:
            field_dict["edges_deleted"] = edges_deleted
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        success = d.pop("success")

        node_identifier = d.pop("node_identifier")

        edges_deleted = d.pop("edges_deleted", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        batch_node_delete_result = cls(
            success=success,
            node_identifier=node_identifier,
            edges_deleted=edges_deleted,
            error=error,
        )

        batch_node_delete_result.additional_properties = d
        return batch_node_delete_result

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
