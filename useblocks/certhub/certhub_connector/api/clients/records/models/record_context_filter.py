from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordContextFilter")


@_attrs_define
class RecordContextFilter:
    """
    Attributes:
        id_in (list[str] | None | Unset):
        context_linked_product (None | str | Unset):
        context_form_id (None | str | Unset):
        context_knowledge_unit_id (None | str | Unset):
        context_knowledge_unit_topic_id (None | str | Unset):
        context_knowledge_unit_topic_id_in (list[str] | None | Unset):
        context_global_element_id (None | str | Unset):
        context_linked_document_document_id (None | str | Unset):
        context_linked_document_document_version (None | str | Unset):
        context_linked_document_template_id (None | str | Unset):
        context_linked_sop (None | str | Unset):
        context_filter_tag (None | str | Unset):
        audit_info_user_id_created (None | str | Unset):
        audit_info_start_date (datetime.datetime | None | Unset):
        audit_info_end_date (datetime.datetime | None | Unset):
        audit_info_include_updated (bool | None | Unset):  Default: False.
    """

    id_in: list[str] | None | Unset = UNSET
    context_linked_product: None | str | Unset = UNSET
    context_form_id: None | str | Unset = UNSET
    context_knowledge_unit_id: None | str | Unset = UNSET
    context_knowledge_unit_topic_id: None | str | Unset = UNSET
    context_knowledge_unit_topic_id_in: list[str] | None | Unset = UNSET
    context_global_element_id: None | str | Unset = UNSET
    context_linked_document_document_id: None | str | Unset = UNSET
    context_linked_document_document_version: None | str | Unset = UNSET
    context_linked_document_template_id: None | str | Unset = UNSET
    context_linked_sop: None | str | Unset = UNSET
    context_filter_tag: None | str | Unset = UNSET
    audit_info_user_id_created: None | str | Unset = UNSET
    audit_info_start_date: datetime.datetime | None | Unset = UNSET
    audit_info_end_date: datetime.datetime | None | Unset = UNSET
    audit_info_include_updated: bool | None | Unset = False

    def to_dict(self) -> dict[str, Any]:
        id_in: list[str] | None | Unset
        if isinstance(self.id_in, Unset):
            id_in = UNSET
        elif isinstance(self.id_in, list):
            id_in = self.id_in

        else:
            id_in = self.id_in

        context_linked_product: None | str | Unset
        if isinstance(self.context_linked_product, Unset):
            context_linked_product = UNSET
        else:
            context_linked_product = self.context_linked_product

        context_form_id: None | str | Unset
        if isinstance(self.context_form_id, Unset):
            context_form_id = UNSET
        else:
            context_form_id = self.context_form_id

        context_knowledge_unit_id: None | str | Unset
        if isinstance(self.context_knowledge_unit_id, Unset):
            context_knowledge_unit_id = UNSET
        else:
            context_knowledge_unit_id = self.context_knowledge_unit_id

        context_knowledge_unit_topic_id: None | str | Unset
        if isinstance(self.context_knowledge_unit_topic_id, Unset):
            context_knowledge_unit_topic_id = UNSET
        else:
            context_knowledge_unit_topic_id = self.context_knowledge_unit_topic_id

        context_knowledge_unit_topic_id_in: list[str] | None | Unset
        if isinstance(self.context_knowledge_unit_topic_id_in, Unset):
            context_knowledge_unit_topic_id_in = UNSET
        elif isinstance(self.context_knowledge_unit_topic_id_in, list):
            context_knowledge_unit_topic_id_in = self.context_knowledge_unit_topic_id_in

        else:
            context_knowledge_unit_topic_id_in = self.context_knowledge_unit_topic_id_in

        context_global_element_id: None | str | Unset
        if isinstance(self.context_global_element_id, Unset):
            context_global_element_id = UNSET
        else:
            context_global_element_id = self.context_global_element_id

        context_linked_document_document_id: None | str | Unset
        if isinstance(self.context_linked_document_document_id, Unset):
            context_linked_document_document_id = UNSET
        else:
            context_linked_document_document_id = (
                self.context_linked_document_document_id
            )

        context_linked_document_document_version: None | str | Unset
        if isinstance(self.context_linked_document_document_version, Unset):
            context_linked_document_document_version = UNSET
        else:
            context_linked_document_document_version = (
                self.context_linked_document_document_version
            )

        context_linked_document_template_id: None | str | Unset
        if isinstance(self.context_linked_document_template_id, Unset):
            context_linked_document_template_id = UNSET
        else:
            context_linked_document_template_id = (
                self.context_linked_document_template_id
            )

        context_linked_sop: None | str | Unset
        if isinstance(self.context_linked_sop, Unset):
            context_linked_sop = UNSET
        else:
            context_linked_sop = self.context_linked_sop

        context_filter_tag: None | str | Unset
        if isinstance(self.context_filter_tag, Unset):
            context_filter_tag = UNSET
        else:
            context_filter_tag = self.context_filter_tag

        audit_info_user_id_created: None | str | Unset
        if isinstance(self.audit_info_user_id_created, Unset):
            audit_info_user_id_created = UNSET
        else:
            audit_info_user_id_created = self.audit_info_user_id_created

        audit_info_start_date: None | str | Unset
        if isinstance(self.audit_info_start_date, Unset):
            audit_info_start_date = UNSET
        elif isinstance(self.audit_info_start_date, datetime.datetime):
            audit_info_start_date = self.audit_info_start_date.isoformat()
        else:
            audit_info_start_date = self.audit_info_start_date

        audit_info_end_date: None | str | Unset
        if isinstance(self.audit_info_end_date, Unset):
            audit_info_end_date = UNSET
        elif isinstance(self.audit_info_end_date, datetime.datetime):
            audit_info_end_date = self.audit_info_end_date.isoformat()
        else:
            audit_info_end_date = self.audit_info_end_date

        audit_info_include_updated: bool | None | Unset
        if isinstance(self.audit_info_include_updated, Unset):
            audit_info_include_updated = UNSET
        else:
            audit_info_include_updated = self.audit_info_include_updated

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id_in is not UNSET:
            field_dict["id__in"] = id_in
        if context_linked_product is not UNSET:
            field_dict["context__linked_product"] = context_linked_product
        if context_form_id is not UNSET:
            field_dict["context__form_id"] = context_form_id
        if context_knowledge_unit_id is not UNSET:
            field_dict["context__knowledge_unit_id"] = context_knowledge_unit_id
        if context_knowledge_unit_topic_id is not UNSET:
            field_dict["context__knowledge_unit_topic_id"] = (
                context_knowledge_unit_topic_id
            )
        if context_knowledge_unit_topic_id_in is not UNSET:
            field_dict["context__knowledge_unit_topic_id__in"] = (
                context_knowledge_unit_topic_id_in
            )
        if context_global_element_id is not UNSET:
            field_dict["context__global_element_id"] = context_global_element_id
        if context_linked_document_document_id is not UNSET:
            field_dict["context__linked_document__document_id"] = (
                context_linked_document_document_id
            )
        if context_linked_document_document_version is not UNSET:
            field_dict["context__linked_document__document_version"] = (
                context_linked_document_document_version
            )
        if context_linked_document_template_id is not UNSET:
            field_dict["context__linked_document__template_id"] = (
                context_linked_document_template_id
            )
        if context_linked_sop is not UNSET:
            field_dict["context__linked_sop"] = context_linked_sop
        if context_filter_tag is not UNSET:
            field_dict["context__filter_tag"] = context_filter_tag
        if audit_info_user_id_created is not UNSET:
            field_dict["audit_info__user_id_created"] = audit_info_user_id_created
        if audit_info_start_date is not UNSET:
            field_dict["audit_info__start_date"] = audit_info_start_date
        if audit_info_end_date is not UNSET:
            field_dict["audit_info__end_date"] = audit_info_end_date
        if audit_info_include_updated is not UNSET:
            field_dict["audit_info__include_updated"] = audit_info_include_updated

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_id_in(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                id_in_type_0 = cast(list[str], data)

                return id_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        id_in = _parse_id_in(d.pop("id__in", UNSET))

        def _parse_context_linked_product(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_linked_product = _parse_context_linked_product(
            d.pop("context__linked_product", UNSET)
        )

        def _parse_context_form_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_form_id = _parse_context_form_id(d.pop("context__form_id", UNSET))

        def _parse_context_knowledge_unit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_knowledge_unit_id = _parse_context_knowledge_unit_id(
            d.pop("context__knowledge_unit_id", UNSET)
        )

        def _parse_context_knowledge_unit_topic_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_knowledge_unit_topic_id = _parse_context_knowledge_unit_topic_id(
            d.pop("context__knowledge_unit_topic_id", UNSET)
        )

        def _parse_context_knowledge_unit_topic_id_in(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                context_knowledge_unit_topic_id_in_type_0 = cast(list[str], data)

                return context_knowledge_unit_topic_id_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        context_knowledge_unit_topic_id_in = _parse_context_knowledge_unit_topic_id_in(
            d.pop("context__knowledge_unit_topic_id__in", UNSET)
        )

        def _parse_context_global_element_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_global_element_id = _parse_context_global_element_id(
            d.pop("context__global_element_id", UNSET)
        )

        def _parse_context_linked_document_document_id(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_linked_document_document_id = (
            _parse_context_linked_document_document_id(
                d.pop("context__linked_document__document_id", UNSET)
            )
        )

        def _parse_context_linked_document_document_version(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_linked_document_document_version = (
            _parse_context_linked_document_document_version(
                d.pop("context__linked_document__document_version", UNSET)
            )
        )

        def _parse_context_linked_document_template_id(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_linked_document_template_id = (
            _parse_context_linked_document_template_id(
                d.pop("context__linked_document__template_id", UNSET)
            )
        )

        def _parse_context_linked_sop(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_linked_sop = _parse_context_linked_sop(
            d.pop("context__linked_sop", UNSET)
        )

        def _parse_context_filter_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_filter_tag = _parse_context_filter_tag(
            d.pop("context__filter_tag", UNSET)
        )

        def _parse_audit_info_user_id_created(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audit_info_user_id_created = _parse_audit_info_user_id_created(
            d.pop("audit_info__user_id_created", UNSET)
        )

        def _parse_audit_info_start_date(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                audit_info_start_date_type_0 = datetime.datetime.fromisoformat(data)

                return audit_info_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        audit_info_start_date = _parse_audit_info_start_date(
            d.pop("audit_info__start_date", UNSET)
        )

        def _parse_audit_info_end_date(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                audit_info_end_date_type_0 = datetime.datetime.fromisoformat(data)

                return audit_info_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        audit_info_end_date = _parse_audit_info_end_date(
            d.pop("audit_info__end_date", UNSET)
        )

        def _parse_audit_info_include_updated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        audit_info_include_updated = _parse_audit_info_include_updated(
            d.pop("audit_info__include_updated", UNSET)
        )

        record_context_filter = cls(
            id_in=id_in,
            context_linked_product=context_linked_product,
            context_form_id=context_form_id,
            context_knowledge_unit_id=context_knowledge_unit_id,
            context_knowledge_unit_topic_id=context_knowledge_unit_topic_id,
            context_knowledge_unit_topic_id_in=context_knowledge_unit_topic_id_in,
            context_global_element_id=context_global_element_id,
            context_linked_document_document_id=context_linked_document_document_id,
            context_linked_document_document_version=context_linked_document_document_version,
            context_linked_document_template_id=context_linked_document_template_id,
            context_linked_sop=context_linked_sop,
            context_filter_tag=context_filter_tag,
            audit_info_user_id_created=audit_info_user_id_created,
            audit_info_start_date=audit_info_start_date,
            audit_info_end_date=audit_info_end_date,
            audit_info_include_updated=audit_info_include_updated,
        )

        return record_context_filter
