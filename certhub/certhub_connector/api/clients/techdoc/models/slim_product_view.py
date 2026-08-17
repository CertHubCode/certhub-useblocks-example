from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.issuing_entity_type_enum import IssuingEntityTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.product_context_question import ProductContextQuestion
    from ..models.product_properties import ProductProperties
    from ..models.slim_knowledge_unit_ref import SlimKnowledgeUnitRef
    from ..models.slim_product_family_ref import SlimProductFamilyRef
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="SlimProductView")


@_attrs_define
class SlimProductView:
    """Lightweight product view for list endpoints.

    knowledge_units are returned as id-only stubs so callers can determine the
    count without fetching full KU/KT data.
    product_families are returned as shallow refs (id + history id only).

        Attributes:
            name (str):
            product_properties (ProductProperties):
            product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
            major_version (int):
            minor_version (int):
            is_latest_approved (bool):
            read_only (bool):
            metadata (TenantMetadata):
            audit_info (AuditInfo):
            field_id (None | str | Unset): MongoDB document ObjectID
            udi (None | str | Unset):
            udi_issuer (IssuingEntityTypeEnum | None | Unset):
            udi_di (None | str | Unset):  Default: 'N/A'.
            lot_number (None | str | Unset):
            serial_number (None | str | Unset):
            notified_body (None | str | Unset):
            ce_certificate_number (None | str | Unset):
            regulatory_status (None | str | Unset):
            product_context (list[ProductContextQuestion] | None | Unset):
            product_website (None | str | Unset):
            product_families (list[SlimProductFamilyRef] | Unset):
            knowledge_units (list[SlimKnowledgeUnitRef] | Unset):
            commit_message (None | str | Unset):
    """

    name: str
    product_properties: ProductProperties
    product_history_id: str
    major_version: int
    minor_version: int
    is_latest_approved: bool
    read_only: bool
    metadata: TenantMetadata
    audit_info: AuditInfo
    field_id: None | str | Unset = UNSET
    udi: None | str | Unset = UNSET
    udi_issuer: IssuingEntityTypeEnum | None | Unset = UNSET
    udi_di: None | str | Unset = "N/A"
    lot_number: None | str | Unset = UNSET
    serial_number: None | str | Unset = UNSET
    notified_body: None | str | Unset = UNSET
    ce_certificate_number: None | str | Unset = UNSET
    regulatory_status: None | str | Unset = UNSET
    product_context: list[ProductContextQuestion] | None | Unset = UNSET
    product_website: None | str | Unset = UNSET
    product_families: list[SlimProductFamilyRef] | Unset = UNSET
    knowledge_units: list[SlimKnowledgeUnitRef] | Unset = UNSET
    commit_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        product_properties = self.product_properties.to_dict()

        product_history_id = self.product_history_id

        major_version = self.major_version

        minor_version = self.minor_version

        is_latest_approved = self.is_latest_approved

        read_only = self.read_only

        metadata = self.metadata.to_dict()

        audit_info = self.audit_info.to_dict()

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

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

        product_families: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_families, Unset):
            product_families = []
            for product_families_item_data in self.product_families:
                product_families_item = product_families_item_data.to_dict()
                product_families.append(product_families_item)

        knowledge_units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.knowledge_units, Unset):
            knowledge_units = []
            for knowledge_units_item_data in self.knowledge_units:
                knowledge_units_item = knowledge_units_item_data.to_dict()
                knowledge_units.append(knowledge_units_item)

        commit_message: None | str | Unset
        if isinstance(self.commit_message, Unset):
            commit_message = UNSET
        else:
            commit_message = self.commit_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "product_properties": product_properties,
                "product_history_id": product_history_id,
                "major_version": major_version,
                "minor_version": minor_version,
                "is_latest_approved": is_latest_approved,
                "read_only": read_only,
                "metadata": metadata,
                "audit_info": audit_info,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
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
        if product_context is not UNSET:
            field_dict["product_context"] = product_context
        if product_website is not UNSET:
            field_dict["product_website"] = product_website
        if product_families is not UNSET:
            field_dict["product_families"] = product_families
        if knowledge_units is not UNSET:
            field_dict["knowledge_units"] = knowledge_units
        if commit_message is not UNSET:
            field_dict["commit_message"] = commit_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.product_context_question import ProductContextQuestion
        from ..models.product_properties import ProductProperties
        from ..models.slim_knowledge_unit_ref import SlimKnowledgeUnitRef
        from ..models.slim_product_family_ref import SlimProductFamilyRef
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        name = d.pop("name")

        product_properties = ProductProperties.from_dict(d.pop("product_properties"))

        product_history_id = d.pop("product_history_id")

        major_version = d.pop("major_version")

        minor_version = d.pop("minor_version")

        is_latest_approved = d.pop("is_latest_approved")

        read_only = d.pop("read_only")

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        audit_info = AuditInfo.from_dict(d.pop("audit_info"))

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

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

        _product_families = d.pop("product_families", UNSET)
        product_families: list[SlimProductFamilyRef] | Unset = UNSET
        if _product_families is not UNSET:
            product_families = []
            for product_families_item_data in _product_families:
                product_families_item = SlimProductFamilyRef.from_dict(
                    product_families_item_data
                )

                product_families.append(product_families_item)

        _knowledge_units = d.pop("knowledge_units", UNSET)
        knowledge_units: list[SlimKnowledgeUnitRef] | Unset = UNSET
        if _knowledge_units is not UNSET:
            knowledge_units = []
            for knowledge_units_item_data in _knowledge_units:
                knowledge_units_item = SlimKnowledgeUnitRef.from_dict(
                    knowledge_units_item_data
                )

                knowledge_units.append(knowledge_units_item)

        def _parse_commit_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_message = _parse_commit_message(d.pop("commit_message", UNSET))

        slim_product_view = cls(
            name=name,
            product_properties=product_properties,
            product_history_id=product_history_id,
            major_version=major_version,
            minor_version=minor_version,
            is_latest_approved=is_latest_approved,
            read_only=read_only,
            metadata=metadata,
            audit_info=audit_info,
            field_id=field_id,
            udi=udi,
            udi_issuer=udi_issuer,
            udi_di=udi_di,
            lot_number=lot_number,
            serial_number=serial_number,
            notified_body=notified_body,
            ce_certificate_number=ce_certificate_number,
            regulatory_status=regulatory_status,
            product_context=product_context,
            product_website=product_website,
            product_families=product_families,
            knowledge_units=knowledge_units,
            commit_message=commit_message,
        )

        slim_product_view.additional_properties = d
        return slim_product_view

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
