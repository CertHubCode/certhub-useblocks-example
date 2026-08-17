from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parent_entity import ParentEntity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_unit_revision_summary import KnowledgeUnitRevisionSummary


T = TypeVar("T", bound="KnowledgeUnitHistoryGroup")


@_attrs_define
class KnowledgeUnitHistoryGroup:
    """A group of submission revisions with the same history_id

    Attributes:
        knowledge_unit_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        name (str):
        latest_revision (KnowledgeUnitRevisionSummary): Summary of a submission revision for listing purposes
        related_product_name (str):
        parent_entity (ParentEntity):
        latest_approved (KnowledgeUnitRevisionSummary | None | Unset):
        revisions (list[KnowledgeUnitRevisionSummary] | Unset):
        total_revisions (int | Unset):  Default: 0.
        product_history_id (None | str | Unset):
        product_family_history_id (None | str | Unset):
        revision_at_product_version (KnowledgeUnitRevisionSummary | None | Unset):
    """

    knowledge_unit_history_id: str
    name: str
    latest_revision: KnowledgeUnitRevisionSummary
    related_product_name: str
    parent_entity: ParentEntity
    latest_approved: KnowledgeUnitRevisionSummary | None | Unset = UNSET
    revisions: list[KnowledgeUnitRevisionSummary] | Unset = UNSET
    total_revisions: int | Unset = 0
    product_history_id: None | str | Unset = UNSET
    product_family_history_id: None | str | Unset = UNSET
    revision_at_product_version: KnowledgeUnitRevisionSummary | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.knowledge_unit_revision_summary import (
            KnowledgeUnitRevisionSummary,
        )

        knowledge_unit_history_id = self.knowledge_unit_history_id

        name = self.name

        latest_revision = self.latest_revision.to_dict()

        related_product_name = self.related_product_name

        parent_entity = self.parent_entity.value

        latest_approved: dict[str, Any] | None | Unset
        if isinstance(self.latest_approved, Unset):
            latest_approved = UNSET
        elif isinstance(self.latest_approved, KnowledgeUnitRevisionSummary):
            latest_approved = self.latest_approved.to_dict()
        else:
            latest_approved = self.latest_approved

        revisions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.revisions, Unset):
            revisions = []
            for revisions_item_data in self.revisions:
                revisions_item = revisions_item_data.to_dict()
                revisions.append(revisions_item)

        total_revisions = self.total_revisions

        product_history_id: None | str | Unset
        if isinstance(self.product_history_id, Unset):
            product_history_id = UNSET
        else:
            product_history_id = self.product_history_id

        product_family_history_id: None | str | Unset
        if isinstance(self.product_family_history_id, Unset):
            product_family_history_id = UNSET
        else:
            product_family_history_id = self.product_family_history_id

        revision_at_product_version: dict[str, Any] | None | Unset
        if isinstance(self.revision_at_product_version, Unset):
            revision_at_product_version = UNSET
        elif isinstance(self.revision_at_product_version, KnowledgeUnitRevisionSummary):
            revision_at_product_version = self.revision_at_product_version.to_dict()
        else:
            revision_at_product_version = self.revision_at_product_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_unit_history_id": knowledge_unit_history_id,
                "name": name,
                "latest_revision": latest_revision,
                "related_product_name": related_product_name,
                "parent_entity": parent_entity,
            }
        )
        if latest_approved is not UNSET:
            field_dict["latest_approved"] = latest_approved
        if revisions is not UNSET:
            field_dict["revisions"] = revisions
        if total_revisions is not UNSET:
            field_dict["total_revisions"] = total_revisions
        if product_history_id is not UNSET:
            field_dict["product_history_id"] = product_history_id
        if product_family_history_id is not UNSET:
            field_dict["product_family_history_id"] = product_family_history_id
        if revision_at_product_version is not UNSET:
            field_dict["revision_at_product_version"] = revision_at_product_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_unit_revision_summary import (
            KnowledgeUnitRevisionSummary,
        )

        d = dict(src_dict)
        knowledge_unit_history_id = d.pop("knowledge_unit_history_id")

        name = d.pop("name")

        latest_revision = KnowledgeUnitRevisionSummary.from_dict(
            d.pop("latest_revision")
        )

        related_product_name = d.pop("related_product_name")

        parent_entity = ParentEntity(d.pop("parent_entity"))

        def _parse_latest_approved(
            data: object,
        ) -> KnowledgeUnitRevisionSummary | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_approved_type_0 = KnowledgeUnitRevisionSummary.from_dict(data)

                return latest_approved_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KnowledgeUnitRevisionSummary | None | Unset, data)

        latest_approved = _parse_latest_approved(d.pop("latest_approved", UNSET))

        _revisions = d.pop("revisions", UNSET)
        revisions: list[KnowledgeUnitRevisionSummary] | Unset = UNSET
        if _revisions is not UNSET:
            revisions = []
            for revisions_item_data in _revisions:
                revisions_item = KnowledgeUnitRevisionSummary.from_dict(
                    revisions_item_data
                )

                revisions.append(revisions_item)

        total_revisions = d.pop("total_revisions", UNSET)

        def _parse_product_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_history_id = _parse_product_history_id(
            d.pop("product_history_id", UNSET)
        )

        def _parse_product_family_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_family_history_id = _parse_product_family_history_id(
            d.pop("product_family_history_id", UNSET)
        )

        def _parse_revision_at_product_version(
            data: object,
        ) -> KnowledgeUnitRevisionSummary | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revision_at_product_version_type_0 = (
                    KnowledgeUnitRevisionSummary.from_dict(data)
                )

                return revision_at_product_version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KnowledgeUnitRevisionSummary | None | Unset, data)

        revision_at_product_version = _parse_revision_at_product_version(
            d.pop("revision_at_product_version", UNSET)
        )

        knowledge_unit_history_group = cls(
            knowledge_unit_history_id=knowledge_unit_history_id,
            name=name,
            latest_revision=latest_revision,
            related_product_name=related_product_name,
            parent_entity=parent_entity,
            latest_approved=latest_approved,
            revisions=revisions,
            total_revisions=total_revisions,
            product_history_id=product_history_id,
            product_family_history_id=product_family_history_id,
            revision_at_product_version=revision_at_product_version,
        )

        knowledge_unit_history_group.additional_properties = d
        return knowledge_unit_history_group

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
