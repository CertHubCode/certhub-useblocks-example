from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_update_data_type_0 import RecordUpdateDataType0
    from ..models.record_update_form_type_0 import RecordUpdateFormType0
    from ..models.update_record_context import UpdateRecordContext


T = TypeVar("T", bound="RecordUpdate")


@_attrs_define
class RecordUpdate:
    """
    Attributes:
        name (None | str | Unset):
        form (None | RecordUpdateFormType0 | Unset):
        data (None | RecordUpdateDataType0 | Unset):
        context (None | Unset | UpdateRecordContext):
        read_only (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    form: None | RecordUpdateFormType0 | Unset = UNSET
    data: None | RecordUpdateDataType0 | Unset = UNSET
    context: None | Unset | UpdateRecordContext = UNSET
    read_only: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.record_update_data_type_0 import RecordUpdateDataType0
        from ..models.record_update_form_type_0 import RecordUpdateFormType0
        from ..models.update_record_context import UpdateRecordContext

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        form: dict[str, Any] | None | Unset
        if isinstance(self.form, Unset):
            form = UNSET
        elif isinstance(self.form, RecordUpdateFormType0):
            form = self.form.to_dict()
        else:
            form = self.form

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, RecordUpdateDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        context: dict[str, Any] | None | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, UpdateRecordContext):
            context = self.context.to_dict()
        else:
            context = self.context

        read_only: bool | None | Unset
        if isinstance(self.read_only, Unset):
            read_only = UNSET
        else:
            read_only = self.read_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if form is not UNSET:
            field_dict["form"] = form
        if data is not UNSET:
            field_dict["data"] = data
        if context is not UNSET:
            field_dict["context"] = context
        if read_only is not UNSET:
            field_dict["read_only"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.record_update_data_type_0 import RecordUpdateDataType0
        from ..models.record_update_form_type_0 import RecordUpdateFormType0
        from ..models.update_record_context import UpdateRecordContext

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_form(data: object) -> None | RecordUpdateFormType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                form_type_0 = RecordUpdateFormType0.from_dict(data)

                return form_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecordUpdateFormType0 | Unset, data)

        form = _parse_form(d.pop("form", UNSET))

        def _parse_data(data: object) -> None | RecordUpdateDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = RecordUpdateDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecordUpdateDataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_context(data: object) -> None | Unset | UpdateRecordContext:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = UpdateRecordContext.from_dict(data)

                return context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateRecordContext, data)

        context = _parse_context(d.pop("context", UNSET))

        def _parse_read_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read_only = _parse_read_only(d.pop("read_only", UNSET))

        record_update = cls(
            name=name,
            form=form,
            data=data,
            context=context,
            read_only=read_only,
        )

        record_update.additional_properties = d
        return record_update

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
