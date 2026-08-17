from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.underlying_schema_sync_topic import UnderlyingSchemaSyncTopic


T = TypeVar("T", bound="UnderlyingSchemaSyncStatus")


@_attrs_define
class UnderlyingSchemaSyncStatus:
    """Whether the Product KU's current name/description/KT forms differ from
    the COMPARISON revision of its underlying Schema Library schema - the
    latest approved version (e.g. 2.0, 3.0) when one exists, otherwise (for
    schemas still under 1.0) the latest revision - i.e. whether 'Update
    Underlying Schema' would actually change anything, and precisely which
    KU/KT-level changes it would make. Drives whether the FE shows the update
    button, and lets the confirm dialog list only the entities that will
    actually change instead of everything unconditionally. A content diff,
    not a version comparison.

        Attributes:
            eligible (bool | Unset):  Default: False.
            out_of_sync (bool | Unset):  Default: False.
            ku_changed (bool | Unset):  Default: False.
            topics (list[UnderlyingSchemaSyncTopic] | Unset):
            compared_schema_version (None | str | Unset):
    """

    eligible: bool | Unset = False
    out_of_sync: bool | Unset = False
    ku_changed: bool | Unset = False
    topics: list[UnderlyingSchemaSyncTopic] | Unset = UNSET
    compared_schema_version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eligible = self.eligible

        out_of_sync = self.out_of_sync

        ku_changed = self.ku_changed

        topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        compared_schema_version: None | str | Unset
        if isinstance(self.compared_schema_version, Unset):
            compared_schema_version = UNSET
        else:
            compared_schema_version = self.compared_schema_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eligible is not UNSET:
            field_dict["eligible"] = eligible
        if out_of_sync is not UNSET:
            field_dict["out_of_sync"] = out_of_sync
        if ku_changed is not UNSET:
            field_dict["ku_changed"] = ku_changed
        if topics is not UNSET:
            field_dict["topics"] = topics
        if compared_schema_version is not UNSET:
            field_dict["compared_schema_version"] = compared_schema_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.underlying_schema_sync_topic import UnderlyingSchemaSyncTopic

        d = dict(src_dict)
        eligible = d.pop("eligible", UNSET)

        out_of_sync = d.pop("out_of_sync", UNSET)

        ku_changed = d.pop("ku_changed", UNSET)

        _topics = d.pop("topics", UNSET)
        topics: list[UnderlyingSchemaSyncTopic] | Unset = UNSET
        if _topics is not UNSET:
            topics = []
            for topics_item_data in _topics:
                topics_item = UnderlyingSchemaSyncTopic.from_dict(topics_item_data)

                topics.append(topics_item)

        def _parse_compared_schema_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compared_schema_version = _parse_compared_schema_version(
            d.pop("compared_schema_version", UNSET)
        )

        underlying_schema_sync_status = cls(
            eligible=eligible,
            out_of_sync=out_of_sync,
            ku_changed=ku_changed,
            topics=topics,
            compared_schema_version=compared_schema_version,
        )

        underlying_schema_sync_status.additional_properties = d
        return underlying_schema_sync_status

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
