from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.global_element_type import GlobalElementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.global_element_bulk_response_schema_type_0 import (
        GlobalElementBulkResponseSchemaType0,
    )
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="GlobalElementBulkResponse")


@_attrs_define
class GlobalElementBulkResponse:
    """Response model for bulk fetch; schema is optional depending on include_schema.

    Attributes:
        name (str):
        metadata (TenantMetadata):
        audit_info (AuditInfo):
        type_ (GlobalElementType):
        field_id (None | str | Unset):
        schema (GlobalElementBulkResponseSchemaType0 | None | Unset):
        description (None | str | Unset):
    """

    name: str
    metadata: TenantMetadata
    audit_info: AuditInfo
    type_: GlobalElementType
    field_id: None | str | Unset = UNSET
    schema: GlobalElementBulkResponseSchemaType0 | None | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.global_element_bulk_response_schema_type_0 import (
            GlobalElementBulkResponseSchemaType0,
        )

        name = self.name

        metadata = self.metadata.to_dict()

        audit_info = self.audit_info.to_dict()

        type_ = self.type_.value

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        schema: dict[str, Any] | None | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, GlobalElementBulkResponseSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "metadata": metadata,
                "audit_info": audit_info,
                "type": type_,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if schema is not UNSET:
            field_dict["schema"] = schema
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.global_element_bulk_response_schema_type_0 import (
            GlobalElementBulkResponseSchemaType0,
        )
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        name = d.pop("name")

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        audit_info = AuditInfo.from_dict(d.pop("audit_info"))

        type_ = GlobalElementType(d.pop("type"))

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

        def _parse_schema(
            data: object,
        ) -> GlobalElementBulkResponseSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = GlobalElementBulkResponseSchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GlobalElementBulkResponseSchemaType0 | None | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        global_element_bulk_response = cls(
            name=name,
            metadata=metadata,
            audit_info=audit_info,
            type_=type_,
            field_id=field_id,
            schema=schema,
            description=description,
        )

        global_element_bulk_response.additional_properties = d
        return global_element_bulk_response

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
