from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolved_node_entity import ResolvedNodeEntity


T = TypeVar("T", bound="ResolvedNodeEntityWithLinkedEntities")


@_attrs_define
class ResolvedNodeEntityWithLinkedEntities:
    """Resolved entity plus optional linked entities (traces resolved and grouped by type).

    Attributes:
        entity (ResolvedNodeEntity):
        linked_sops (list[ResolvedNodeEntity] | Unset):
        linked_work_instructions (list[ResolvedNodeEntity] | Unset):
        linked_products (list[ResolvedNodeEntity] | Unset):
        linked_files (list[ResolvedNodeEntity] | Unset):
        linked_documents (list[ResolvedNodeEntity] | Unset):
        linked_forms (list[ResolvedNodeEntity] | Unset):
        linked_knowledge_topics (list[ResolvedNodeEntity] | Unset):
        linked_knowledge_units (list[ResolvedNodeEntity] | Unset):
        linked_templates (list[ResolvedNodeEntity] | Unset):
        linked_submissions (list[ResolvedNodeEntity] | Unset):
        linked_records (list[ResolvedNodeEntity] | Unset):
        linked_global_elements (list[ResolvedNodeEntity] | Unset):
        linked_global_element_entries (list[ResolvedNodeEntity] | Unset):
    """

    entity: ResolvedNodeEntity
    linked_sops: list[ResolvedNodeEntity] | Unset = UNSET
    linked_work_instructions: list[ResolvedNodeEntity] | Unset = UNSET
    linked_products: list[ResolvedNodeEntity] | Unset = UNSET
    linked_files: list[ResolvedNodeEntity] | Unset = UNSET
    linked_documents: list[ResolvedNodeEntity] | Unset = UNSET
    linked_forms: list[ResolvedNodeEntity] | Unset = UNSET
    linked_knowledge_topics: list[ResolvedNodeEntity] | Unset = UNSET
    linked_knowledge_units: list[ResolvedNodeEntity] | Unset = UNSET
    linked_templates: list[ResolvedNodeEntity] | Unset = UNSET
    linked_submissions: list[ResolvedNodeEntity] | Unset = UNSET
    linked_records: list[ResolvedNodeEntity] | Unset = UNSET
    linked_global_elements: list[ResolvedNodeEntity] | Unset = UNSET
    linked_global_element_entries: list[ResolvedNodeEntity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity = self.entity.to_dict()

        linked_sops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_sops, Unset):
            linked_sops = []
            for linked_sops_item_data in self.linked_sops:
                linked_sops_item = linked_sops_item_data.to_dict()
                linked_sops.append(linked_sops_item)

        linked_work_instructions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_work_instructions, Unset):
            linked_work_instructions = []
            for linked_work_instructions_item_data in self.linked_work_instructions:
                linked_work_instructions_item = (
                    linked_work_instructions_item_data.to_dict()
                )
                linked_work_instructions.append(linked_work_instructions_item)

        linked_products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_products, Unset):
            linked_products = []
            for linked_products_item_data in self.linked_products:
                linked_products_item = linked_products_item_data.to_dict()
                linked_products.append(linked_products_item)

        linked_files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_files, Unset):
            linked_files = []
            for linked_files_item_data in self.linked_files:
                linked_files_item = linked_files_item_data.to_dict()
                linked_files.append(linked_files_item)

        linked_documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_documents, Unset):
            linked_documents = []
            for linked_documents_item_data in self.linked_documents:
                linked_documents_item = linked_documents_item_data.to_dict()
                linked_documents.append(linked_documents_item)

        linked_forms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_forms, Unset):
            linked_forms = []
            for linked_forms_item_data in self.linked_forms:
                linked_forms_item = linked_forms_item_data.to_dict()
                linked_forms.append(linked_forms_item)

        linked_knowledge_topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_knowledge_topics, Unset):
            linked_knowledge_topics = []
            for linked_knowledge_topics_item_data in self.linked_knowledge_topics:
                linked_knowledge_topics_item = (
                    linked_knowledge_topics_item_data.to_dict()
                )
                linked_knowledge_topics.append(linked_knowledge_topics_item)

        linked_knowledge_units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_knowledge_units, Unset):
            linked_knowledge_units = []
            for linked_knowledge_units_item_data in self.linked_knowledge_units:
                linked_knowledge_units_item = linked_knowledge_units_item_data.to_dict()
                linked_knowledge_units.append(linked_knowledge_units_item)

        linked_templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_templates, Unset):
            linked_templates = []
            for linked_templates_item_data in self.linked_templates:
                linked_templates_item = linked_templates_item_data.to_dict()
                linked_templates.append(linked_templates_item)

        linked_submissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_submissions, Unset):
            linked_submissions = []
            for linked_submissions_item_data in self.linked_submissions:
                linked_submissions_item = linked_submissions_item_data.to_dict()
                linked_submissions.append(linked_submissions_item)

        linked_records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_records, Unset):
            linked_records = []
            for linked_records_item_data in self.linked_records:
                linked_records_item = linked_records_item_data.to_dict()
                linked_records.append(linked_records_item)

        linked_global_elements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_global_elements, Unset):
            linked_global_elements = []
            for linked_global_elements_item_data in self.linked_global_elements:
                linked_global_elements_item = linked_global_elements_item_data.to_dict()
                linked_global_elements.append(linked_global_elements_item)

        linked_global_element_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_global_element_entries, Unset):
            linked_global_element_entries = []
            for (
                linked_global_element_entries_item_data
            ) in self.linked_global_element_entries:
                linked_global_element_entries_item = (
                    linked_global_element_entries_item_data.to_dict()
                )
                linked_global_element_entries.append(linked_global_element_entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity": entity,
            }
        )
        if linked_sops is not UNSET:
            field_dict["linked_sops"] = linked_sops
        if linked_work_instructions is not UNSET:
            field_dict["linked_work_instructions"] = linked_work_instructions
        if linked_products is not UNSET:
            field_dict["linked_products"] = linked_products
        if linked_files is not UNSET:
            field_dict["linked_files"] = linked_files
        if linked_documents is not UNSET:
            field_dict["linked_documents"] = linked_documents
        if linked_forms is not UNSET:
            field_dict["linked_forms"] = linked_forms
        if linked_knowledge_topics is not UNSET:
            field_dict["linked_knowledge_topics"] = linked_knowledge_topics
        if linked_knowledge_units is not UNSET:
            field_dict["linked_knowledge_units"] = linked_knowledge_units
        if linked_templates is not UNSET:
            field_dict["linked_templates"] = linked_templates
        if linked_submissions is not UNSET:
            field_dict["linked_submissions"] = linked_submissions
        if linked_records is not UNSET:
            field_dict["linked_records"] = linked_records
        if linked_global_elements is not UNSET:
            field_dict["linked_global_elements"] = linked_global_elements
        if linked_global_element_entries is not UNSET:
            field_dict["linked_global_element_entries"] = linked_global_element_entries

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resolved_node_entity import ResolvedNodeEntity

        d = dict(src_dict)
        entity = ResolvedNodeEntity.from_dict(d.pop("entity"))

        _linked_sops = d.pop("linked_sops", UNSET)
        linked_sops: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_sops is not UNSET:
            linked_sops = []
            for linked_sops_item_data in _linked_sops:
                linked_sops_item = ResolvedNodeEntity.from_dict(linked_sops_item_data)

                linked_sops.append(linked_sops_item)

        _linked_work_instructions = d.pop("linked_work_instructions", UNSET)
        linked_work_instructions: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_work_instructions is not UNSET:
            linked_work_instructions = []
            for linked_work_instructions_item_data in _linked_work_instructions:
                linked_work_instructions_item = ResolvedNodeEntity.from_dict(
                    linked_work_instructions_item_data
                )

                linked_work_instructions.append(linked_work_instructions_item)

        _linked_products = d.pop("linked_products", UNSET)
        linked_products: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_products is not UNSET:
            linked_products = []
            for linked_products_item_data in _linked_products:
                linked_products_item = ResolvedNodeEntity.from_dict(
                    linked_products_item_data
                )

                linked_products.append(linked_products_item)

        _linked_files = d.pop("linked_files", UNSET)
        linked_files: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_files is not UNSET:
            linked_files = []
            for linked_files_item_data in _linked_files:
                linked_files_item = ResolvedNodeEntity.from_dict(linked_files_item_data)

                linked_files.append(linked_files_item)

        _linked_documents = d.pop("linked_documents", UNSET)
        linked_documents: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_documents is not UNSET:
            linked_documents = []
            for linked_documents_item_data in _linked_documents:
                linked_documents_item = ResolvedNodeEntity.from_dict(
                    linked_documents_item_data
                )

                linked_documents.append(linked_documents_item)

        _linked_forms = d.pop("linked_forms", UNSET)
        linked_forms: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_forms is not UNSET:
            linked_forms = []
            for linked_forms_item_data in _linked_forms:
                linked_forms_item = ResolvedNodeEntity.from_dict(linked_forms_item_data)

                linked_forms.append(linked_forms_item)

        _linked_knowledge_topics = d.pop("linked_knowledge_topics", UNSET)
        linked_knowledge_topics: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_knowledge_topics is not UNSET:
            linked_knowledge_topics = []
            for linked_knowledge_topics_item_data in _linked_knowledge_topics:
                linked_knowledge_topics_item = ResolvedNodeEntity.from_dict(
                    linked_knowledge_topics_item_data
                )

                linked_knowledge_topics.append(linked_knowledge_topics_item)

        _linked_knowledge_units = d.pop("linked_knowledge_units", UNSET)
        linked_knowledge_units: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_knowledge_units is not UNSET:
            linked_knowledge_units = []
            for linked_knowledge_units_item_data in _linked_knowledge_units:
                linked_knowledge_units_item = ResolvedNodeEntity.from_dict(
                    linked_knowledge_units_item_data
                )

                linked_knowledge_units.append(linked_knowledge_units_item)

        _linked_templates = d.pop("linked_templates", UNSET)
        linked_templates: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_templates is not UNSET:
            linked_templates = []
            for linked_templates_item_data in _linked_templates:
                linked_templates_item = ResolvedNodeEntity.from_dict(
                    linked_templates_item_data
                )

                linked_templates.append(linked_templates_item)

        _linked_submissions = d.pop("linked_submissions", UNSET)
        linked_submissions: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_submissions is not UNSET:
            linked_submissions = []
            for linked_submissions_item_data in _linked_submissions:
                linked_submissions_item = ResolvedNodeEntity.from_dict(
                    linked_submissions_item_data
                )

                linked_submissions.append(linked_submissions_item)

        _linked_records = d.pop("linked_records", UNSET)
        linked_records: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_records is not UNSET:
            linked_records = []
            for linked_records_item_data in _linked_records:
                linked_records_item = ResolvedNodeEntity.from_dict(
                    linked_records_item_data
                )

                linked_records.append(linked_records_item)

        _linked_global_elements = d.pop("linked_global_elements", UNSET)
        linked_global_elements: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_global_elements is not UNSET:
            linked_global_elements = []
            for linked_global_elements_item_data in _linked_global_elements:
                linked_global_elements_item = ResolvedNodeEntity.from_dict(
                    linked_global_elements_item_data
                )

                linked_global_elements.append(linked_global_elements_item)

        _linked_global_element_entries = d.pop("linked_global_element_entries", UNSET)
        linked_global_element_entries: list[ResolvedNodeEntity] | Unset = UNSET
        if _linked_global_element_entries is not UNSET:
            linked_global_element_entries = []
            for (
                linked_global_element_entries_item_data
            ) in _linked_global_element_entries:
                linked_global_element_entries_item = ResolvedNodeEntity.from_dict(
                    linked_global_element_entries_item_data
                )

                linked_global_element_entries.append(linked_global_element_entries_item)

        resolved_node_entity_with_linked_entities = cls(
            entity=entity,
            linked_sops=linked_sops,
            linked_work_instructions=linked_work_instructions,
            linked_products=linked_products,
            linked_files=linked_files,
            linked_documents=linked_documents,
            linked_forms=linked_forms,
            linked_knowledge_topics=linked_knowledge_topics,
            linked_knowledge_units=linked_knowledge_units,
            linked_templates=linked_templates,
            linked_submissions=linked_submissions,
            linked_records=linked_records,
            linked_global_elements=linked_global_elements,
            linked_global_element_entries=linked_global_element_entries,
        )

        resolved_node_entity_with_linked_entities.additional_properties = d
        return resolved_node_entity_with_linked_entities

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
