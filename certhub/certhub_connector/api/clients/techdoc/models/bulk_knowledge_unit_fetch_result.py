from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.full_knowledge_unit_view import FullKnowledgeUnitView
    from ..models.knowledge_unit_history_group import KnowledgeUnitHistoryGroup


T = TypeVar("T", bound="BulkKnowledgeUnitFetchResult")


@_attrs_define
class BulkKnowledgeUnitFetchResult:
    """Per-item result, returned in request order. One failure does not fail the batch.

    Attributes:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        success (bool):
        revision (FullKnowledgeUnitView | None | Unset):
        history (KnowledgeUnitHistoryGroup | None | Unset):
        error (None | str | Unset):
    """

    history_id: str
    success: bool
    revision: FullKnowledgeUnitView | None | Unset = UNSET
    history: KnowledgeUnitHistoryGroup | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.full_knowledge_unit_view import FullKnowledgeUnitView
        from ..models.knowledge_unit_history_group import KnowledgeUnitHistoryGroup

        history_id = self.history_id

        success = self.success

        revision: dict[str, Any] | None | Unset
        if isinstance(self.revision, Unset):
            revision = UNSET
        elif isinstance(self.revision, FullKnowledgeUnitView):
            revision = self.revision.to_dict()
        else:
            revision = self.revision

        history: dict[str, Any] | None | Unset
        if isinstance(self.history, Unset):
            history = UNSET
        elif isinstance(self.history, KnowledgeUnitHistoryGroup):
            history = self.history.to_dict()
        else:
            history = self.history

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history_id": history_id,
                "success": success,
            }
        )
        if revision is not UNSET:
            field_dict["revision"] = revision
        if history is not UNSET:
            field_dict["history"] = history
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.full_knowledge_unit_view import FullKnowledgeUnitView
        from ..models.knowledge_unit_history_group import KnowledgeUnitHistoryGroup

        d = dict(src_dict)
        history_id = d.pop("history_id")

        success = d.pop("success")

        def _parse_revision(data: object) -> FullKnowledgeUnitView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revision_type_0 = FullKnowledgeUnitView.from_dict(data)

                return revision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FullKnowledgeUnitView | None | Unset, data)

        revision = _parse_revision(d.pop("revision", UNSET))

        def _parse_history(data: object) -> KnowledgeUnitHistoryGroup | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                history_type_0 = KnowledgeUnitHistoryGroup.from_dict(data)

                return history_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KnowledgeUnitHistoryGroup | None | Unset, data)

        history = _parse_history(d.pop("history", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        bulk_knowledge_unit_fetch_result = cls(
            history_id=history_id,
            success=success,
            revision=revision,
            history=history,
            error=error,
        )

        bulk_knowledge_unit_fetch_result.additional_properties = d
        return bulk_knowledge_unit_fetch_result

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
