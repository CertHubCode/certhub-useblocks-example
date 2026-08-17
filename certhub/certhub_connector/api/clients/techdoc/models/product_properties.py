from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.regulation import Regulation
from ..models.reusable import Reusable
from ..models.risk_class import RiskClass
from ..models.software import Software
from ..models.software_class import SoftwareClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductProperties")


@_attrs_define
class ProductProperties:
    """
    Attributes:
        regulation (Regulation):
        risk_class (RiskClass):
        sterile (bool | None | Unset):
        reusable (None | Reusable | Unset):
        measurement (bool | None | Unset):
        active (bool | None | Unset):
        invasive (bool | None | Unset):
        implantable (bool | None | Unset):
        medicinal_product (bool | None | Unset):
        software (None | Software | Unset):  Default: Software.NOSOFTWARE.
        software_class (None | SoftwareClass | Unset):  Default: SoftwareClass.NOSOFTWARE.
        biocompatibility (bool | None | Unset):
        clinical_evaluation (bool | None | Unset):
        performance_evaluation (bool | None | Unset):
        reprocessing (bool | None | Unset):
        reagents (bool | None | Unset):
    """

    regulation: Regulation
    risk_class: RiskClass
    sterile: bool | None | Unset = UNSET
    reusable: None | Reusable | Unset = UNSET
    measurement: bool | None | Unset = UNSET
    active: bool | None | Unset = UNSET
    invasive: bool | None | Unset = UNSET
    implantable: bool | None | Unset = UNSET
    medicinal_product: bool | None | Unset = UNSET
    software: None | Software | Unset = Software.NOSOFTWARE
    software_class: None | SoftwareClass | Unset = SoftwareClass.NOSOFTWARE
    biocompatibility: bool | None | Unset = UNSET
    clinical_evaluation: bool | None | Unset = UNSET
    performance_evaluation: bool | None | Unset = UNSET
    reprocessing: bool | None | Unset = UNSET
    reagents: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regulation = self.regulation.value

        risk_class = self.risk_class.value

        sterile: bool | None | Unset
        if isinstance(self.sterile, Unset):
            sterile = UNSET
        else:
            sterile = self.sterile

        reusable: None | str | Unset
        if isinstance(self.reusable, Unset):
            reusable = UNSET
        elif isinstance(self.reusable, Reusable):
            reusable = self.reusable.value
        else:
            reusable = self.reusable

        measurement: bool | None | Unset
        if isinstance(self.measurement, Unset):
            measurement = UNSET
        else:
            measurement = self.measurement

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        invasive: bool | None | Unset
        if isinstance(self.invasive, Unset):
            invasive = UNSET
        else:
            invasive = self.invasive

        implantable: bool | None | Unset
        if isinstance(self.implantable, Unset):
            implantable = UNSET
        else:
            implantable = self.implantable

        medicinal_product: bool | None | Unset
        if isinstance(self.medicinal_product, Unset):
            medicinal_product = UNSET
        else:
            medicinal_product = self.medicinal_product

        software: None | str | Unset
        if isinstance(self.software, Unset):
            software = UNSET
        elif isinstance(self.software, Software):
            software = self.software.value
        else:
            software = self.software

        software_class: None | str | Unset
        if isinstance(self.software_class, Unset):
            software_class = UNSET
        elif isinstance(self.software_class, SoftwareClass):
            software_class = self.software_class.value
        else:
            software_class = self.software_class

        biocompatibility: bool | None | Unset
        if isinstance(self.biocompatibility, Unset):
            biocompatibility = UNSET
        else:
            biocompatibility = self.biocompatibility

        clinical_evaluation: bool | None | Unset
        if isinstance(self.clinical_evaluation, Unset):
            clinical_evaluation = UNSET
        else:
            clinical_evaluation = self.clinical_evaluation

        performance_evaluation: bool | None | Unset
        if isinstance(self.performance_evaluation, Unset):
            performance_evaluation = UNSET
        else:
            performance_evaluation = self.performance_evaluation

        reprocessing: bool | None | Unset
        if isinstance(self.reprocessing, Unset):
            reprocessing = UNSET
        else:
            reprocessing = self.reprocessing

        reagents: bool | None | Unset
        if isinstance(self.reagents, Unset):
            reagents = UNSET
        else:
            reagents = self.reagents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regulation": regulation,
                "risk_class": risk_class,
            }
        )
        if sterile is not UNSET:
            field_dict["sterile"] = sterile
        if reusable is not UNSET:
            field_dict["reusable"] = reusable
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if active is not UNSET:
            field_dict["active"] = active
        if invasive is not UNSET:
            field_dict["invasive"] = invasive
        if implantable is not UNSET:
            field_dict["implantable"] = implantable
        if medicinal_product is not UNSET:
            field_dict["medicinal_product"] = medicinal_product
        if software is not UNSET:
            field_dict["software"] = software
        if software_class is not UNSET:
            field_dict["software_class"] = software_class
        if biocompatibility is not UNSET:
            field_dict["biocompatibility"] = biocompatibility
        if clinical_evaluation is not UNSET:
            field_dict["clinical_evaluation"] = clinical_evaluation
        if performance_evaluation is not UNSET:
            field_dict["performance_evaluation"] = performance_evaluation
        if reprocessing is not UNSET:
            field_dict["reprocessing"] = reprocessing
        if reagents is not UNSET:
            field_dict["reagents"] = reagents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        regulation = Regulation(d.pop("regulation"))

        risk_class = RiskClass(d.pop("risk_class"))

        def _parse_sterile(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sterile = _parse_sterile(d.pop("sterile", UNSET))

        def _parse_reusable(data: object) -> None | Reusable | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reusable_type_0 = Reusable(data)

                return reusable_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Reusable | Unset, data)

        reusable = _parse_reusable(d.pop("reusable", UNSET))

        def _parse_measurement(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        measurement = _parse_measurement(d.pop("measurement", UNSET))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_invasive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        invasive = _parse_invasive(d.pop("invasive", UNSET))

        def _parse_implantable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        implantable = _parse_implantable(d.pop("implantable", UNSET))

        def _parse_medicinal_product(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        medicinal_product = _parse_medicinal_product(d.pop("medicinal_product", UNSET))

        def _parse_software(data: object) -> None | Software | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                software_type_0 = Software(data)

                return software_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Software | Unset, data)

        software = _parse_software(d.pop("software", UNSET))

        def _parse_software_class(data: object) -> None | SoftwareClass | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                software_class_type_0 = SoftwareClass(data)

                return software_class_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SoftwareClass | Unset, data)

        software_class = _parse_software_class(d.pop("software_class", UNSET))

        def _parse_biocompatibility(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        biocompatibility = _parse_biocompatibility(d.pop("biocompatibility", UNSET))

        def _parse_clinical_evaluation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        clinical_evaluation = _parse_clinical_evaluation(
            d.pop("clinical_evaluation", UNSET)
        )

        def _parse_performance_evaluation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        performance_evaluation = _parse_performance_evaluation(
            d.pop("performance_evaluation", UNSET)
        )

        def _parse_reprocessing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        reprocessing = _parse_reprocessing(d.pop("reprocessing", UNSET))

        def _parse_reagents(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        reagents = _parse_reagents(d.pop("reagents", UNSET))

        product_properties = cls(
            regulation=regulation,
            risk_class=risk_class,
            sterile=sterile,
            reusable=reusable,
            measurement=measurement,
            active=active,
            invasive=invasive,
            implantable=implantable,
            medicinal_product=medicinal_product,
            software=software,
            software_class=software_class,
            biocompatibility=biocompatibility,
            clinical_evaluation=clinical_evaluation,
            performance_evaluation=performance_evaluation,
            reprocessing=reprocessing,
            reagents=reagents,
        )

        product_properties.additional_properties = d
        return product_properties

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
