from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    Self,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_source_info_metadata import ExternalSourceInfoMetadata


T = TypeVar("T", bound="ExternalSourceInfo")


@_attrs_define
class ExternalSourceInfo:
    """
    Attributes:
        is_external (Literal['true']):
        external_source_type (str):
        external_source_id (str):
        metadata (ExternalSourceInfoMetadata | Unset):
    """

    is_external: Literal["true"]
    external_source_type: str
    external_source_id: str
    metadata: ExternalSourceInfoMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_external = self.is_external

        external_source_type = self.external_source_type

        external_source_id = self.external_source_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_external": is_external,
                "external_source_type": external_source_type,
                "external_source_id": external_source_id,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.external_source_info_metadata import ExternalSourceInfoMetadata

        d = dict(src_dict)
        is_external = cast(Literal["true"], d.pop("is_external"))
        if is_external != "true":
            raise ValueError(
                f"is_external must match const 'true', got '{is_external}'"
            )

        external_source_type = d.pop("external_source_type")

        external_source_id = d.pop("external_source_id")

        _metadata = d.pop("metadata", UNSET)
        metadata: ExternalSourceInfoMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ExternalSourceInfoMetadata.from_dict(_metadata)

        external_source_info = cls(
            is_external=is_external,
            external_source_type=external_source_type,
            external_source_id=external_source_id,
            metadata=metadata,
        )

        external_source_info.additional_properties = d
        return external_source_info

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
