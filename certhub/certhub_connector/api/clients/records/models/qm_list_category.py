from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="QmListCategory")


@_attrs_define
class QmListCategory:
    """
    Attributes:
        name (str):
        metadata (TenantMetadata):
        audit_info (AuditInfo):
        field_id (None | str | Unset): MongoDB document ObjectID
    """

    name: str
    metadata: TenantMetadata
    audit_info: AuditInfo
    field_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        metadata = self.metadata.to_dict()

        audit_info = self.audit_info.to_dict()

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "metadata": metadata,
                "audit_info": audit_info,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        name = d.pop("name")

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        audit_info = AuditInfo.from_dict(d.pop("audit_info"))

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

        qm_list_category = cls(
            name=name,
            metadata=metadata,
            audit_info=audit_info,
            field_id=field_id,
        )

        qm_list_category.additional_properties = d
        return qm_list_category

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
