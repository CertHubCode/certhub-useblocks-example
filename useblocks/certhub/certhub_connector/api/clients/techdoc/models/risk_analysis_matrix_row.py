from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.risk_analysis_matrix_cell import RiskAnalysisMatrixCell


T = TypeVar("T", bound="RiskAnalysisMatrixRow")


@_attrs_define
class RiskAnalysisMatrixRow:
    """One resolved (possibly partial) chain, rooted at `risk`.

    Attributes:
        risk (RiskAnalysisMatrixCell): One resolved Record in a chain.

            Its form schema (needed alongside `data` to resolve the same "<name> -
            <data name>" display label used elsewhere — `resolveRecordDataName`/
            `formatRecordDisplayName`) is not embedded here; look it up by
            `record_id` in the response's `forms` map instead.
        system_misbehaviour (None | RiskAnalysisMatrixCell | Unset):
        hazard (None | RiskAnalysisMatrixCell | Unset):
        hazardous_situation (None | RiskAnalysisMatrixCell | Unset):
        harm (None | RiskAnalysisMatrixCell | Unset):
        risk_control_measure (None | RiskAnalysisMatrixCell | Unset):
        risk_management_team (None | RiskAnalysisMatrixCell | Unset):
    """

    risk: RiskAnalysisMatrixCell
    system_misbehaviour: None | RiskAnalysisMatrixCell | Unset = UNSET
    hazard: None | RiskAnalysisMatrixCell | Unset = UNSET
    hazardous_situation: None | RiskAnalysisMatrixCell | Unset = UNSET
    harm: None | RiskAnalysisMatrixCell | Unset = UNSET
    risk_control_measure: None | RiskAnalysisMatrixCell | Unset = UNSET
    risk_management_team: None | RiskAnalysisMatrixCell | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.risk_analysis_matrix_cell import RiskAnalysisMatrixCell

        risk = self.risk.to_dict()

        system_misbehaviour: dict[str, Any] | None | Unset
        if isinstance(self.system_misbehaviour, Unset):
            system_misbehaviour = UNSET
        elif isinstance(self.system_misbehaviour, RiskAnalysisMatrixCell):
            system_misbehaviour = self.system_misbehaviour.to_dict()
        else:
            system_misbehaviour = self.system_misbehaviour

        hazard: dict[str, Any] | None | Unset
        if isinstance(self.hazard, Unset):
            hazard = UNSET
        elif isinstance(self.hazard, RiskAnalysisMatrixCell):
            hazard = self.hazard.to_dict()
        else:
            hazard = self.hazard

        hazardous_situation: dict[str, Any] | None | Unset
        if isinstance(self.hazardous_situation, Unset):
            hazardous_situation = UNSET
        elif isinstance(self.hazardous_situation, RiskAnalysisMatrixCell):
            hazardous_situation = self.hazardous_situation.to_dict()
        else:
            hazardous_situation = self.hazardous_situation

        harm: dict[str, Any] | None | Unset
        if isinstance(self.harm, Unset):
            harm = UNSET
        elif isinstance(self.harm, RiskAnalysisMatrixCell):
            harm = self.harm.to_dict()
        else:
            harm = self.harm

        risk_control_measure: dict[str, Any] | None | Unset
        if isinstance(self.risk_control_measure, Unset):
            risk_control_measure = UNSET
        elif isinstance(self.risk_control_measure, RiskAnalysisMatrixCell):
            risk_control_measure = self.risk_control_measure.to_dict()
        else:
            risk_control_measure = self.risk_control_measure

        risk_management_team: dict[str, Any] | None | Unset
        if isinstance(self.risk_management_team, Unset):
            risk_management_team = UNSET
        elif isinstance(self.risk_management_team, RiskAnalysisMatrixCell):
            risk_management_team = self.risk_management_team.to_dict()
        else:
            risk_management_team = self.risk_management_team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "risk": risk,
            }
        )
        if system_misbehaviour is not UNSET:
            field_dict["system_misbehaviour"] = system_misbehaviour
        if hazard is not UNSET:
            field_dict["hazard"] = hazard
        if hazardous_situation is not UNSET:
            field_dict["hazardous_situation"] = hazardous_situation
        if harm is not UNSET:
            field_dict["harm"] = harm
        if risk_control_measure is not UNSET:
            field_dict["risk_control_measure"] = risk_control_measure
        if risk_management_team is not UNSET:
            field_dict["risk_management_team"] = risk_management_team

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.risk_analysis_matrix_cell import RiskAnalysisMatrixCell

        d = dict(src_dict)
        risk = RiskAnalysisMatrixCell.from_dict(d.pop("risk"))

        def _parse_system_misbehaviour(
            data: object,
        ) -> None | RiskAnalysisMatrixCell | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                system_misbehaviour_type_0 = RiskAnalysisMatrixCell.from_dict(data)

                return system_misbehaviour_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RiskAnalysisMatrixCell | Unset, data)

        system_misbehaviour = _parse_system_misbehaviour(
            d.pop("system_misbehaviour", UNSET)
        )

        def _parse_hazard(data: object) -> None | RiskAnalysisMatrixCell | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hazard_type_0 = RiskAnalysisMatrixCell.from_dict(data)

                return hazard_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RiskAnalysisMatrixCell | Unset, data)

        hazard = _parse_hazard(d.pop("hazard", UNSET))

        def _parse_hazardous_situation(
            data: object,
        ) -> None | RiskAnalysisMatrixCell | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hazardous_situation_type_0 = RiskAnalysisMatrixCell.from_dict(data)

                return hazardous_situation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RiskAnalysisMatrixCell | Unset, data)

        hazardous_situation = _parse_hazardous_situation(
            d.pop("hazardous_situation", UNSET)
        )

        def _parse_harm(data: object) -> None | RiskAnalysisMatrixCell | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                harm_type_0 = RiskAnalysisMatrixCell.from_dict(data)

                return harm_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RiskAnalysisMatrixCell | Unset, data)

        harm = _parse_harm(d.pop("harm", UNSET))

        def _parse_risk_control_measure(
            data: object,
        ) -> None | RiskAnalysisMatrixCell | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                risk_control_measure_type_0 = RiskAnalysisMatrixCell.from_dict(data)

                return risk_control_measure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RiskAnalysisMatrixCell | Unset, data)

        risk_control_measure = _parse_risk_control_measure(
            d.pop("risk_control_measure", UNSET)
        )

        def _parse_risk_management_team(
            data: object,
        ) -> None | RiskAnalysisMatrixCell | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                risk_management_team_type_0 = RiskAnalysisMatrixCell.from_dict(data)

                return risk_management_team_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RiskAnalysisMatrixCell | Unset, data)

        risk_management_team = _parse_risk_management_team(
            d.pop("risk_management_team", UNSET)
        )

        risk_analysis_matrix_row = cls(
            risk=risk,
            system_misbehaviour=system_misbehaviour,
            hazard=hazard,
            hazardous_situation=hazardous_situation,
            harm=harm,
            risk_control_measure=risk_control_measure,
            risk_management_team=risk_management_team,
        )

        risk_analysis_matrix_row.additional_properties = d
        return risk_analysis_matrix_row

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
