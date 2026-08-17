from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product import Product


T = TypeVar("T", bound="PublishProductResponse")


@_attrs_define
class PublishProductResponse:
    """Response for product publish operation

    Attributes:
        success (bool):
        commit_message (str):
        product (None | Product | Unset):
    """

    success: bool
    commit_message: str
    product: None | Product | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product import Product

        success = self.success

        commit_message = self.commit_message

        product: dict[str, Any] | None | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        elif isinstance(self.product, Product):
            product = self.product.to_dict()
        else:
            product = self.product

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "commit_message": commit_message,
            }
        )
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product import Product

        d = dict(src_dict)
        success = d.pop("success")

        commit_message = d.pop("commit_message")

        def _parse_product(data: object) -> None | Product | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                product_type_0 = Product.from_dict(data)

                return product_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Product | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        publish_product_response = cls(
            success=success,
            commit_message=commit_message,
            product=product,
        )

        publish_product_response.additional_properties = d
        return publish_product_response

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
