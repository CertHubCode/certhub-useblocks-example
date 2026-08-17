from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.match_decision_action import MatchDecisionAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchDecision")


@_attrs_define
class MatchDecision:
    """
    Attributes:
        type_ (str):
        object_id (str):
        action (MatchDecisionAction):
        override_id (None | str | Unset):
    """

    type_: str
    object_id: str
    action: MatchDecisionAction
    override_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        object_id = self.object_id

        action = self.action.value

        override_id: None | str | Unset
        if isinstance(self.override_id, Unset):
            override_id = UNSET
        else:
            override_id = self.override_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "object_id": object_id,
                "action": action,
            }
        )
        if override_id is not UNSET:
            field_dict["override_id"] = override_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        object_id = d.pop("object_id")

        action = MatchDecisionAction(d.pop("action"))

        def _parse_override_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_id = _parse_override_id(d.pop("override_id", UNSET))

        match_decision = cls(
            type_=type_,
            object_id=object_id,
            action=action,
            override_id=override_id,
        )

        match_decision.additional_properties = d
        return match_decision

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
