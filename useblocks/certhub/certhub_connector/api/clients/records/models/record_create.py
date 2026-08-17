from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_context import RecordContext
    from ..models.record_create_data_type_0 import RecordCreateDataType0
    from ..models.record_create_form import RecordCreateForm


T = TypeVar("T", bound="RecordCreate")


@_attrs_define
class RecordCreate:
    """
    Attributes:
        name (str):
        form (RecordCreateForm):
        context (RecordContext):
        data (None | RecordCreateDataType0 | Unset):
        auto_number (bool | None | Unset):  Default: False.
        read_only (bool | None | Unset):
    """

    name: str
    form: RecordCreateForm
    context: RecordContext
    data: None | RecordCreateDataType0 | Unset = UNSET
    auto_number: bool | None | Unset = False
    read_only: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.record_create_data_type_0 import RecordCreateDataType0

        name = self.name

        form = self.form.to_dict()

        context = self.context.to_dict()

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, RecordCreateDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        auto_number: bool | None | Unset
        if isinstance(self.auto_number, Unset):
            auto_number = UNSET
        else:
            auto_number = self.auto_number

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
                "context": context,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if auto_number is not UNSET:
            field_dict["auto_number"] = auto_number
        if read_only is not UNSET:
            field_dict["read_only"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.record_context import RecordContext
        from ..models.record_create_data_type_0 import RecordCreateDataType0
        from ..models.record_create_form import RecordCreateForm

        d = dict(src_dict)
        name = d.pop("name")

        form = RecordCreateForm.from_dict(d.pop("form"))

        context = RecordContext.from_dict(d.pop("context"))

        def _parse_data(data: object) -> None | RecordCreateDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = RecordCreateDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecordCreateDataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_auto_number(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_number = _parse_auto_number(d.pop("auto_number", UNSET))

        def _parse_read_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read_only = _parse_read_only(d.pop("read_only", UNSET))

        record_create = cls(
            name=name,
            form=form,
            context=context,
            data=data,
            auto_number=auto_number,
            read_only=read_only,
        )

        record_create.additional_properties = d
        return record_create

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
