from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.guidance_task_response import GuidanceTaskResponse


T = TypeVar("T", bound="GuidancePhaseResponse")


@_attrs_define
class GuidancePhaseResponse:
    """
    Attributes:
        id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        title (str):
        goal (str):
        tasks (list[GuidanceTaskResponse]):
    """

    id: str
    title: str
    goal: str
    tasks: list[GuidanceTaskResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        goal = self.goal

        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()
            tasks.append(tasks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "goal": goal,
                "tasks": tasks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.guidance_task_response import GuidanceTaskResponse

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        goal = d.pop("goal")

        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in _tasks:
            tasks_item = GuidanceTaskResponse.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        guidance_phase_response = cls(
            id=id,
            title=title,
            goal=goal,
            tasks=tasks,
        )

        guidance_phase_response.additional_properties = d
        return guidance_phase_response

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
