from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_unit_schema import KnowledgeUnitSchema


T = TypeVar("T", bound="CommitKnowledgeUnitSchemaResponse")


@_attrs_define
class CommitKnowledgeUnitSchemaResponse:
    """Response for knowledge unit schema commit operation

    Attributes:
        success (bool):
        commit_message (str):
        knowledge_unit_schema (KnowledgeUnitSchema | None | Unset):
    """

    success: bool
    commit_message: str
    knowledge_unit_schema: KnowledgeUnitSchema | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.knowledge_unit_schema import KnowledgeUnitSchema

        success = self.success

        commit_message = self.commit_message

        knowledge_unit_schema: dict[str, Any] | None | Unset
        if isinstance(self.knowledge_unit_schema, Unset):
            knowledge_unit_schema = UNSET
        elif isinstance(self.knowledge_unit_schema, KnowledgeUnitSchema):
            knowledge_unit_schema = self.knowledge_unit_schema.to_dict()
        else:
            knowledge_unit_schema = self.knowledge_unit_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "commit_message": commit_message,
            }
        )
        if knowledge_unit_schema is not UNSET:
            field_dict["knowledge_unit_schema"] = knowledge_unit_schema

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_unit_schema import KnowledgeUnitSchema

        d = dict(src_dict)
        success = d.pop("success")

        commit_message = d.pop("commit_message")

        def _parse_knowledge_unit_schema(
            data: object,
        ) -> KnowledgeUnitSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                knowledge_unit_schema_type_0 = KnowledgeUnitSchema.from_dict(data)

                return knowledge_unit_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KnowledgeUnitSchema | None | Unset, data)

        knowledge_unit_schema = _parse_knowledge_unit_schema(
            d.pop("knowledge_unit_schema", UNSET)
        )

        commit_knowledge_unit_schema_response = cls(
            success=success,
            commit_message=commit_message,
            knowledge_unit_schema=knowledge_unit_schema,
        )

        commit_knowledge_unit_schema_response.additional_properties = d
        return commit_knowledge_unit_schema_response

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
