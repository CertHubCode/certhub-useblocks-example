from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.guidance_task_state import GuidanceTaskState

T = TypeVar("T", bound="UpdateGuidanceTaskStatePayload")


@_attrs_define
class UpdateGuidanceTaskStatePayload:
    """
    Attributes:
        task_id (str):
        state (GuidanceTaskState):
    """

    task_id: str
    state: GuidanceTaskState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        task_id = d.pop("task_id")

        state = GuidanceTaskState(d.pop("state"))

        update_guidance_task_state_payload = cls(
            task_id=task_id,
            state=state,
        )

        update_guidance_task_state_payload.additional_properties = d
        return update_guidance_task_state_payload

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
