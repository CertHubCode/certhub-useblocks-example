from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linked_document import LinkedDocument


T = TypeVar("T", bound="RecordContext")


@_attrs_define
class RecordContext:
    """
    Attributes:
        linked_product (None | str | Unset):
        linked_sop (None | str | Unset):
        form_id (None | str | Unset):
        global_element_id (None | str | Unset):
        knowledge_unit_id (None | str | Unset):
        knowledge_unit_topic_id (None | str | Unset):
        linked_document (LinkedDocument | None | Unset):
        group_id (None | str | Unset):
    """

    linked_product: None | str | Unset = UNSET
    linked_sop: None | str | Unset = UNSET
    form_id: None | str | Unset = UNSET
    global_element_id: None | str | Unset = UNSET
    knowledge_unit_id: None | str | Unset = UNSET
    knowledge_unit_topic_id: None | str | Unset = UNSET
    linked_document: LinkedDocument | None | Unset = UNSET
    group_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.linked_document import LinkedDocument

        linked_product: None | str | Unset
        if isinstance(self.linked_product, Unset):
            linked_product = UNSET
        else:
            linked_product = self.linked_product

        linked_sop: None | str | Unset
        if isinstance(self.linked_sop, Unset):
            linked_sop = UNSET
        else:
            linked_sop = self.linked_sop

        form_id: None | str | Unset
        if isinstance(self.form_id, Unset):
            form_id = UNSET
        else:
            form_id = self.form_id

        global_element_id: None | str | Unset
        if isinstance(self.global_element_id, Unset):
            global_element_id = UNSET
        else:
            global_element_id = self.global_element_id

        knowledge_unit_id: None | str | Unset
        if isinstance(self.knowledge_unit_id, Unset):
            knowledge_unit_id = UNSET
        else:
            knowledge_unit_id = self.knowledge_unit_id

        knowledge_unit_topic_id: None | str | Unset
        if isinstance(self.knowledge_unit_topic_id, Unset):
            knowledge_unit_topic_id = UNSET
        else:
            knowledge_unit_topic_id = self.knowledge_unit_topic_id

        linked_document: dict[str, Any] | None | Unset
        if isinstance(self.linked_document, Unset):
            linked_document = UNSET
        elif isinstance(self.linked_document, LinkedDocument):
            linked_document = self.linked_document.to_dict()
        else:
            linked_document = self.linked_document

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linked_product is not UNSET:
            field_dict["linked_product"] = linked_product
        if linked_sop is not UNSET:
            field_dict["linked_sop"] = linked_sop
        if form_id is not UNSET:
            field_dict["form_id"] = form_id
        if global_element_id is not UNSET:
            field_dict["global_element_id"] = global_element_id
        if knowledge_unit_id is not UNSET:
            field_dict["knowledge_unit_id"] = knowledge_unit_id
        if knowledge_unit_topic_id is not UNSET:
            field_dict["knowledge_unit_topic_id"] = knowledge_unit_topic_id
        if linked_document is not UNSET:
            field_dict["linked_document"] = linked_document
        if group_id is not UNSET:
            field_dict["group_id"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.linked_document import LinkedDocument

        d = dict(src_dict)

        def _parse_linked_product(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linked_product = _parse_linked_product(d.pop("linked_product", UNSET))

        def _parse_linked_sop(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linked_sop = _parse_linked_sop(d.pop("linked_sop", UNSET))

        def _parse_form_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_id = _parse_form_id(d.pop("form_id", UNSET))

        def _parse_global_element_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        global_element_id = _parse_global_element_id(d.pop("global_element_id", UNSET))

        def _parse_knowledge_unit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_id = _parse_knowledge_unit_id(d.pop("knowledge_unit_id", UNSET))

        def _parse_knowledge_unit_topic_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_unit_topic_id = _parse_knowledge_unit_topic_id(
            d.pop("knowledge_unit_topic_id", UNSET)
        )

        def _parse_linked_document(data: object) -> LinkedDocument | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                linked_document_type_0 = LinkedDocument.from_dict(data)

                return linked_document_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinkedDocument | None | Unset, data)

        linked_document = _parse_linked_document(d.pop("linked_document", UNSET))

        def _parse_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        record_context = cls(
            linked_product=linked_product,
            linked_sop=linked_sop,
            form_id=form_id,
            global_element_id=global_element_id,
            knowledge_unit_id=knowledge_unit_id,
            knowledge_unit_topic_id=knowledge_unit_topic_id,
            linked_document=linked_document,
            group_id=group_id,
        )

        record_context.additional_properties = d
        return record_context

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
