from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="BaseLibraryResponse")


@_attrs_define
class BaseLibraryResponse:
    """
    Attributes:
        id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        name (str):
        metadata (TenantMetadata):
        audit_info (AuditInfo):
        description (None | str | Unset):
    """

    id: str
    name: str
    metadata: TenantMetadata
    audit_info: AuditInfo
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        metadata = self.metadata.to_dict()

        audit_info = self.audit_info.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "metadata": metadata,
                "audit_info": audit_info,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        audit_info = AuditInfo.from_dict(d.pop("audit_info"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        base_library_response = cls(
            id=id,
            name=name,
            metadata=metadata,
            audit_info=audit_info,
            description=description,
        )

        base_library_response.additional_properties = d
        return base_library_response

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
