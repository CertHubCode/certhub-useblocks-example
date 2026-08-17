from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.issuing_entity_type_enum import IssuingEntityTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_context_question import ProductContextQuestion
    from ..models.product_properties import ProductProperties


T = TypeVar("T", bound="UpdateProduct")


@_attrs_define
class UpdateProduct:
    """
    Attributes:
        name (None | str | Unset):
        udi (None | str | Unset):
        udi_issuer (IssuingEntityTypeEnum | None | Unset):
        udi_di (None | str | Unset):
        lot_number (None | str | Unset):
        serial_number (None | str | Unset):
        notified_body (None | str | Unset):
        ce_certificate_number (None | str | Unset):
        regulatory_status (None | str | Unset):
        product_properties (None | ProductProperties | Unset):
        product_families (list[str] | None | Unset):
        product_context (list[ProductContextQuestion] | None | Unset):
        product_website (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    udi: None | str | Unset = UNSET
    udi_issuer: IssuingEntityTypeEnum | None | Unset = UNSET
    udi_di: None | str | Unset = UNSET
    lot_number: None | str | Unset = UNSET
    serial_number: None | str | Unset = UNSET
    notified_body: None | str | Unset = UNSET
    ce_certificate_number: None | str | Unset = UNSET
    regulatory_status: None | str | Unset = UNSET
    product_properties: None | ProductProperties | Unset = UNSET
    product_families: list[str] | None | Unset = UNSET
    product_context: list[ProductContextQuestion] | None | Unset = UNSET
    product_website: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_properties import ProductProperties

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        udi: None | str | Unset
        if isinstance(self.udi, Unset):
            udi = UNSET
        else:
            udi = self.udi

        udi_issuer: None | str | Unset
        if isinstance(self.udi_issuer, Unset):
            udi_issuer = UNSET
        elif isinstance(self.udi_issuer, IssuingEntityTypeEnum):
            udi_issuer = self.udi_issuer.value
        else:
            udi_issuer = self.udi_issuer

        udi_di: None | str | Unset
        if isinstance(self.udi_di, Unset):
            udi_di = UNSET
        else:
            udi_di = self.udi_di

        lot_number: None | str | Unset
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        serial_number: None | str | Unset
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        notified_body: None | str | Unset
        if isinstance(self.notified_body, Unset):
            notified_body = UNSET
        else:
            notified_body = self.notified_body

        ce_certificate_number: None | str | Unset
        if isinstance(self.ce_certificate_number, Unset):
            ce_certificate_number = UNSET
        else:
            ce_certificate_number = self.ce_certificate_number

        regulatory_status: None | str | Unset
        if isinstance(self.regulatory_status, Unset):
            regulatory_status = UNSET
        else:
            regulatory_status = self.regulatory_status

        product_properties: dict[str, Any] | None | Unset
        if isinstance(self.product_properties, Unset):
            product_properties = UNSET
        elif isinstance(self.product_properties, ProductProperties):
            product_properties = self.product_properties.to_dict()
        else:
            product_properties = self.product_properties

        product_families: list[str] | None | Unset
        if isinstance(self.product_families, Unset):
            product_families = UNSET
        elif isinstance(self.product_families, list):
            product_families = self.product_families

        else:
            product_families = self.product_families

        product_context: list[dict[str, Any]] | None | Unset
        if isinstance(self.product_context, Unset):
            product_context = UNSET
        elif isinstance(self.product_context, list):
            product_context = []
            for product_context_type_0_item_data in self.product_context:
                product_context_type_0_item = product_context_type_0_item_data.to_dict()
                product_context.append(product_context_type_0_item)

        else:
            product_context = self.product_context

        product_website: None | str | Unset
        if isinstance(self.product_website, Unset):
            product_website = UNSET
        else:
            product_website = self.product_website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if udi is not UNSET:
            field_dict["udi"] = udi
        if udi_issuer is not UNSET:
            field_dict["udi_issuer"] = udi_issuer
        if udi_di is not UNSET:
            field_dict["udi_di"] = udi_di
        if lot_number is not UNSET:
            field_dict["lot_number"] = lot_number
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if notified_body is not UNSET:
            field_dict["notified_body"] = notified_body
        if ce_certificate_number is not UNSET:
            field_dict["ce_certificate_number"] = ce_certificate_number
        if regulatory_status is not UNSET:
            field_dict["regulatory_status"] = regulatory_status
        if product_properties is not UNSET:
            field_dict["product_properties"] = product_properties
        if product_families is not UNSET:
            field_dict["product_families"] = product_families
        if product_context is not UNSET:
            field_dict["product_context"] = product_context
        if product_website is not UNSET:
            field_dict["product_website"] = product_website

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.product_context_question import ProductContextQuestion
        from ..models.product_properties import ProductProperties

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_udi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        udi = _parse_udi(d.pop("udi", UNSET))

        def _parse_udi_issuer(data: object) -> IssuingEntityTypeEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                udi_issuer_type_0 = IssuingEntityTypeEnum(data)

                return udi_issuer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IssuingEntityTypeEnum | None | Unset, data)

        udi_issuer = _parse_udi_issuer(d.pop("udi_issuer", UNSET))

        def _parse_udi_di(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        udi_di = _parse_udi_di(d.pop("udi_di", UNSET))

        def _parse_lot_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_number = _parse_lot_number(d.pop("lot_number", UNSET))

        def _parse_serial_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial_number = _parse_serial_number(d.pop("serial_number", UNSET))

        def _parse_notified_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notified_body = _parse_notified_body(d.pop("notified_body", UNSET))

        def _parse_ce_certificate_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ce_certificate_number = _parse_ce_certificate_number(
            d.pop("ce_certificate_number", UNSET)
        )

        def _parse_regulatory_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        regulatory_status = _parse_regulatory_status(d.pop("regulatory_status", UNSET))

        def _parse_product_properties(data: object) -> None | ProductProperties | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                product_properties_type_0 = ProductProperties.from_dict(data)

                return product_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductProperties | Unset, data)

        product_properties = _parse_product_properties(
            d.pop("product_properties", UNSET)
        )

        def _parse_product_families(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                product_families_type_0 = cast(list[str], data)

                return product_families_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        product_families = _parse_product_families(d.pop("product_families", UNSET))

        def _parse_product_context(
            data: object,
        ) -> list[ProductContextQuestion] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                product_context_type_0 = []
                _product_context_type_0 = data
                for product_context_type_0_item_data in _product_context_type_0:
                    product_context_type_0_item = ProductContextQuestion.from_dict(
                        product_context_type_0_item_data
                    )

                    product_context_type_0.append(product_context_type_0_item)

                return product_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductContextQuestion] | None | Unset, data)

        product_context = _parse_product_context(d.pop("product_context", UNSET))

        def _parse_product_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_website = _parse_product_website(d.pop("product_website", UNSET))

        update_product = cls(
            name=name,
            udi=udi,
            udi_issuer=udi_issuer,
            udi_di=udi_di,
            lot_number=lot_number,
            serial_number=serial_number,
            notified_body=notified_body,
            ce_certificate_number=ce_certificate_number,
            regulatory_status=regulatory_status,
            product_properties=product_properties,
            product_families=product_families,
            product_context=product_context,
            product_website=product_website,
        )

        update_product.additional_properties = d
        return update_product

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
