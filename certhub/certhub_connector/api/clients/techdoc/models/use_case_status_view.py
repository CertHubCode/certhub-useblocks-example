from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.use_case_status_view_status import UseCaseStatusViewStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.use_case_available_relation import UseCaseAvailableRelation
    from ..models.use_case_duplicate_topic import UseCaseDuplicateTopic


T = TypeVar("T", bound="UseCaseStatusView")


@_attrs_define
class UseCaseStatusView:
    """Pre-computed completeness banner for one use case the topic belongs to.

    Attributes:
        use_case_name (str):
        status (UseCaseStatusViewStatus):
        is_valid (bool):
        show_banner (bool):
        missing_topics (list[str] | Unset):
        duplicate_topics (list[UseCaseDuplicateTopic] | Unset):
        available_topics (list[str] | Unset):
        required_topics (list[str] | Unset):
        available_relations (list[UseCaseAvailableRelation] | Unset):
    """

    use_case_name: str
    status: UseCaseStatusViewStatus
    is_valid: bool
    show_banner: bool
    missing_topics: list[str] | Unset = UNSET
    duplicate_topics: list[UseCaseDuplicateTopic] | Unset = UNSET
    available_topics: list[str] | Unset = UNSET
    required_topics: list[str] | Unset = UNSET
    available_relations: list[UseCaseAvailableRelation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_case_name = self.use_case_name

        status = self.status.value

        is_valid = self.is_valid

        show_banner = self.show_banner

        missing_topics: list[str] | Unset = UNSET
        if not isinstance(self.missing_topics, Unset):
            missing_topics = self.missing_topics

        duplicate_topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.duplicate_topics, Unset):
            duplicate_topics = []
            for duplicate_topics_item_data in self.duplicate_topics:
                duplicate_topics_item = duplicate_topics_item_data.to_dict()
                duplicate_topics.append(duplicate_topics_item)

        available_topics: list[str] | Unset = UNSET
        if not isinstance(self.available_topics, Unset):
            available_topics = self.available_topics

        required_topics: list[str] | Unset = UNSET
        if not isinstance(self.required_topics, Unset):
            required_topics = self.required_topics

        available_relations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_relations, Unset):
            available_relations = []
            for available_relations_item_data in self.available_relations:
                available_relations_item = available_relations_item_data.to_dict()
                available_relations.append(available_relations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "use_case_name": use_case_name,
                "status": status,
                "is_valid": is_valid,
                "show_banner": show_banner,
            }
        )
        if missing_topics is not UNSET:
            field_dict["missing_topics"] = missing_topics
        if duplicate_topics is not UNSET:
            field_dict["duplicate_topics"] = duplicate_topics
        if available_topics is not UNSET:
            field_dict["available_topics"] = available_topics
        if required_topics is not UNSET:
            field_dict["required_topics"] = required_topics
        if available_relations is not UNSET:
            field_dict["available_relations"] = available_relations

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.use_case_available_relation import UseCaseAvailableRelation
        from ..models.use_case_duplicate_topic import UseCaseDuplicateTopic

        d = dict(src_dict)
        use_case_name = d.pop("use_case_name")

        status = UseCaseStatusViewStatus(d.pop("status"))

        is_valid = d.pop("is_valid")

        show_banner = d.pop("show_banner")

        missing_topics = cast(list[str], d.pop("missing_topics", UNSET))

        _duplicate_topics = d.pop("duplicate_topics", UNSET)
        duplicate_topics: list[UseCaseDuplicateTopic] | Unset = UNSET
        if _duplicate_topics is not UNSET:
            duplicate_topics = []
            for duplicate_topics_item_data in _duplicate_topics:
                duplicate_topics_item = UseCaseDuplicateTopic.from_dict(
                    duplicate_topics_item_data
                )

                duplicate_topics.append(duplicate_topics_item)

        available_topics = cast(list[str], d.pop("available_topics", UNSET))

        required_topics = cast(list[str], d.pop("required_topics", UNSET))

        _available_relations = d.pop("available_relations", UNSET)
        available_relations: list[UseCaseAvailableRelation] | Unset = UNSET
        if _available_relations is not UNSET:
            available_relations = []
            for available_relations_item_data in _available_relations:
                available_relations_item = UseCaseAvailableRelation.from_dict(
                    available_relations_item_data
                )

                available_relations.append(available_relations_item)

        use_case_status_view = cls(
            use_case_name=use_case_name,
            status=status,
            is_valid=is_valid,
            show_banner=show_banner,
            missing_topics=missing_topics,
            duplicate_topics=duplicate_topics,
            available_topics=available_topics,
            required_topics=required_topics,
            available_relations=available_relations,
        )

        use_case_status_view.additional_properties = d
        return use_case_status_view

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
