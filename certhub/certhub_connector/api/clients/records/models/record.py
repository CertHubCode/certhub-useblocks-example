from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.record_context import RecordContext
    from ..models.record_data import RecordData
    from ..models.record_form import RecordForm
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        name (str):
        form (RecordForm):
        version (str):
        data (RecordData):
        metadata (TenantMetadata):
        context (None | RecordContext):
        audit_info (AuditInfo):
        field_id (None | str | Unset): MongoDB document ObjectID
        read_only (bool | None | Unset):  Default: False.
    """

    name: str
    form: RecordForm
    version: str
    data: RecordData
    metadata: TenantMetadata
    context: None | RecordContext
    audit_info: AuditInfo
    field_id: None | str | Unset = UNSET
    read_only: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.record_context import RecordContext

        name = self.name

        form = self.form.to_dict()

        version = self.version

        data = self.data.to_dict()

        metadata = self.metadata.to_dict()

        context: dict[str, Any] | None
        if isinstance(self.context, RecordContext):
            context = self.context.to_dict()
        else:
            context = self.context

        audit_info = self.audit_info.to_dict()

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        read_only: bool | None | Unset
        if isinstance(self.read_only, Unset):
            read_only = UNSET
        else:
            read_only = self.read_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "form": form,
                "version": version,
                "data": data,
                "metadata": metadata,
                "context": context,
                "audit_info": audit_info,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if read_only is not UNSET:
            field_dict["read_only"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.record_context import RecordContext
        from ..models.record_data import RecordData
        from ..models.record_form import RecordForm
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        name = d.pop("name")

        form = RecordForm.from_dict(d.pop("form"))

        version = d.pop("version")

        data = RecordData.from_dict(d.pop("data"))

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        def _parse_context(data: object) -> None | RecordContext:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = RecordContext.from_dict(data)

                return context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecordContext, data)

        context = _parse_context(d.pop("context"))

        audit_info = AuditInfo.from_dict(d.pop("audit_info"))

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

        def _parse_read_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read_only = _parse_read_only(d.pop("read_only", UNSET))

        record = cls(
            name=name,
            form=form,
            version=version,
            data=data,
            metadata=metadata,
            context=context,
            audit_info=audit_info,
            field_id=field_id,
            read_only=read_only,
        )

        record.additional_properties = d
        return record

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
