from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_family import ProductFamily


T = TypeVar("T", bound="PublishProductFamilyResponse")


@_attrs_define
class PublishProductFamilyResponse:
    """Response for product family publish operation

    Attributes:
        success (bool):
        commit_message (str):
        product_family (None | ProductFamily | Unset):
    """

    success: bool
    commit_message: str
    product_family: None | ProductFamily | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_family import ProductFamily

        success = self.success

        commit_message = self.commit_message

        product_family: dict[str, Any] | None | Unset
        if isinstance(self.product_family, Unset):
            product_family = UNSET
        elif isinstance(self.product_family, ProductFamily):
            product_family = self.product_family.to_dict()
        else:
            product_family = self.product_family

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "commit_message": commit_message,
            }
        )
        if product_family is not UNSET:
            field_dict["product_family"] = product_family

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product_family import ProductFamily

        d = dict(src_dict)
        success = d.pop("success")

        commit_message = d.pop("commit_message")

        def _parse_product_family(data: object) -> None | ProductFamily | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                product_family_type_0 = ProductFamily.from_dict(data)

                return product_family_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductFamily | Unset, data)

        product_family = _parse_product_family(d.pop("product_family", UNSET))

        publish_product_family_response = cls(
            success=success,
            commit_message=commit_message,
            product_family=product_family,
        )

        publish_product_family_response.additional_properties = d
        return publish_product_family_response

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
