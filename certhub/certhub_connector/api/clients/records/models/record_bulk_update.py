from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_bulk_update_form_type_0 import RecordBulkUpdateFormType0


T = TypeVar("T", bound="RecordBulkUpdate")


@_attrs_define
class RecordBulkUpdate:
    """Bulk update payload for updating a bulk of records by ids.
    Currently only `form` can be updated.

        Attributes:
            ids (list[str]):
            form (None | RecordBulkUpdateFormType0 | Unset):
    """

    ids: list[str]
    form: None | RecordBulkUpdateFormType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.record_bulk_update_form_type_0 import RecordBulkUpdateFormType0

        ids = self.ids

        form: dict[str, Any] | None | Unset
        if isinstance(self.form, Unset):
            form = UNSET
        elif isinstance(self.form, RecordBulkUpdateFormType0):
            form = self.form.to_dict()
        else:
            form = self.form

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if form is not UNSET:
            field_dict["form"] = form

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.record_bulk_update_form_type_0 import RecordBulkUpdateFormType0

        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        def _parse_form(data: object) -> None | RecordBulkUpdateFormType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                form_type_0 = RecordBulkUpdateFormType0.from_dict(data)

                return form_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecordBulkUpdateFormType0 | Unset, data)

        form = _parse_form(d.pop("form", UNSET))

        record_bulk_update = cls(
            ids=ids,
            form=form,
        )

        record_bulk_update.additional_properties = d
        return record_bulk_update

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
