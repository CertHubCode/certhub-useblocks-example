from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_family_revision_summary import ProductFamilyRevisionSummary


T = TypeVar("T", bound="ProductFamilyHistoryGroup")


@_attrs_define
class ProductFamilyHistoryGroup:
    """A group of submission revisions with the same history_id

    Attributes:
        product_family_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        name (str):
        latest_revision (ProductFamilyRevisionSummary): Summary of a submission revision for listing purposes
        latest_approved (None | ProductFamilyRevisionSummary | Unset):
        revisions (list[ProductFamilyRevisionSummary] | Unset):
        total_revisions (int | Unset):  Default: 0.
    """

    product_family_history_id: str
    name: str
    latest_revision: ProductFamilyRevisionSummary
    latest_approved: None | ProductFamilyRevisionSummary | Unset = UNSET
    revisions: list[ProductFamilyRevisionSummary] | Unset = UNSET
    total_revisions: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_family_revision_summary import (
            ProductFamilyRevisionSummary,
        )

        product_family_history_id = self.product_family_history_id

        name = self.name

        latest_revision = self.latest_revision.to_dict()

        latest_approved: dict[str, Any] | None | Unset
        if isinstance(self.latest_approved, Unset):
            latest_approved = UNSET
        elif isinstance(self.latest_approved, ProductFamilyRevisionSummary):
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_family_history_id": product_family_history_id,
                "name": name,
                "latest_revision": latest_revision,
            }
        )
        if latest_approved is not UNSET:
            field_dict["latest_approved"] = latest_approved
        if revisions is not UNSET:
            field_dict["revisions"] = revisions
        if total_revisions is not UNSET:
            field_dict["total_revisions"] = total_revisions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product_family_revision_summary import (
            ProductFamilyRevisionSummary,
        )

        d = dict(src_dict)
        product_family_history_id = d.pop("product_family_history_id")

        name = d.pop("name")

        latest_revision = ProductFamilyRevisionSummary.from_dict(
            d.pop("latest_revision")
        )

        def _parse_latest_approved(
            data: object,
        ) -> None | ProductFamilyRevisionSummary | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_approved_type_0 = ProductFamilyRevisionSummary.from_dict(data)

                return latest_approved_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductFamilyRevisionSummary | Unset, data)

        latest_approved = _parse_latest_approved(d.pop("latest_approved", UNSET))

        _revisions = d.pop("revisions", UNSET)
        revisions: list[ProductFamilyRevisionSummary] | Unset = UNSET
        if _revisions is not UNSET:
            revisions = []
            for revisions_item_data in _revisions:
                revisions_item = ProductFamilyRevisionSummary.from_dict(
                    revisions_item_data
                )

                revisions.append(revisions_item)

        total_revisions = d.pop("total_revisions", UNSET)

        product_family_history_group = cls(
            product_family_history_id=product_family_history_id,
            name=name,
            latest_revision=latest_revision,
            latest_approved=latest_approved,
            revisions=revisions,
            total_revisions=total_revisions,
        )

        product_family_history_group.additional_properties = d
        return product_family_history_group

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
