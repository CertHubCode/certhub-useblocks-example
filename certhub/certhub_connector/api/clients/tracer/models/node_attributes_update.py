from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_attributes_update_mode import NodeAttributesUpdateMode
from ..models.node_type import NodeType
from ..models.relation_type import RelationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeAttributesUpdate")


@_attrs_define
class NodeAttributesUpdate:
    """
    Attributes:
        source_type (NodeType):
        source_id (str):
        source_version (int | str):
        new_version (int | str):
        update_mode (NodeAttributesUpdateMode):
        new_source_type (NodeType | None | Unset):
        new_source_id (None | str | Unset):
        excluded_relations (list[RelationType] | None | Unset):
        allowed_relations (list[RelationType] | None | Unset):
    """

    source_type: NodeType
    source_id: str
    source_version: int | str
    new_version: int | str
    update_mode: NodeAttributesUpdateMode
    new_source_type: NodeType | None | Unset = UNSET
    new_source_id: None | str | Unset = UNSET
    excluded_relations: list[RelationType] | None | Unset = UNSET
    allowed_relations: list[RelationType] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type.value

        source_id = self.source_id

        source_version: int | str
        source_version = self.source_version

        new_version: int | str
        new_version = self.new_version

        update_mode = self.update_mode.value

        new_source_type: None | str | Unset
        if isinstance(self.new_source_type, Unset):
            new_source_type = UNSET
        elif isinstance(self.new_source_type, NodeType):
            new_source_type = self.new_source_type.value
        else:
            new_source_type = self.new_source_type

        new_source_id: None | str | Unset
        if isinstance(self.new_source_id, Unset):
            new_source_id = UNSET
        else:
            new_source_id = self.new_source_id

        excluded_relations: list[str] | None | Unset
        if isinstance(self.excluded_relations, Unset):
            excluded_relations = UNSET
        elif isinstance(self.excluded_relations, list):
            excluded_relations = []
            for excluded_relations_type_0_item_data in self.excluded_relations:
                excluded_relations_type_0_item = (
                    excluded_relations_type_0_item_data.value
                )
                excluded_relations.append(excluded_relations_type_0_item)

        else:
            excluded_relations = self.excluded_relations

        allowed_relations: list[str] | None | Unset
        if isinstance(self.allowed_relations, Unset):
            allowed_relations = UNSET
        elif isinstance(self.allowed_relations, list):
            allowed_relations = []
            for allowed_relations_type_0_item_data in self.allowed_relations:
                allowed_relations_type_0_item = allowed_relations_type_0_item_data.value
                allowed_relations.append(allowed_relations_type_0_item)

        else:
            allowed_relations = self.allowed_relations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceType": source_type,
                "sourceId": source_id,
                "sourceVersion": source_version,
                "newVersion": new_version,
                "updateMode": update_mode,
            }
        )
        if new_source_type is not UNSET:
            field_dict["newSourceType"] = new_source_type
        if new_source_id is not UNSET:
            field_dict["newSourceId"] = new_source_id
        if excluded_relations is not UNSET:
            field_dict["excludedRelations"] = excluded_relations
        if allowed_relations is not UNSET:
            field_dict["allowedRelations"] = allowed_relations

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_type = NodeType(d.pop("sourceType"))

        source_id = d.pop("sourceId")

        def _parse_source_version(data: object) -> int | str:
            return cast(int | str, data)

        source_version = _parse_source_version(d.pop("sourceVersion"))

        def _parse_new_version(data: object) -> int | str:
            return cast(int | str, data)

        new_version = _parse_new_version(d.pop("newVersion"))

        update_mode = NodeAttributesUpdateMode(d.pop("updateMode"))

        def _parse_new_source_type(data: object) -> NodeType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                new_source_type_type_0 = NodeType(data)

                return new_source_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NodeType | None | Unset, data)

        new_source_type = _parse_new_source_type(d.pop("newSourceType", UNSET))

        def _parse_new_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_source_id = _parse_new_source_id(d.pop("newSourceId", UNSET))

        def _parse_excluded_relations(
            data: object,
        ) -> list[RelationType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_relations_type_0 = []
                _excluded_relations_type_0 = data
                for excluded_relations_type_0_item_data in _excluded_relations_type_0:
                    excluded_relations_type_0_item = RelationType(
                        excluded_relations_type_0_item_data
                    )

                    excluded_relations_type_0.append(excluded_relations_type_0_item)

                return excluded_relations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RelationType] | None | Unset, data)

        excluded_relations = _parse_excluded_relations(
            d.pop("excludedRelations", UNSET)
        )

        def _parse_allowed_relations(data: object) -> list[RelationType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_relations_type_0 = []
                _allowed_relations_type_0 = data
                for allowed_relations_type_0_item_data in _allowed_relations_type_0:
                    allowed_relations_type_0_item = RelationType(
                        allowed_relations_type_0_item_data
                    )

                    allowed_relations_type_0.append(allowed_relations_type_0_item)

                return allowed_relations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RelationType] | None | Unset, data)

        allowed_relations = _parse_allowed_relations(d.pop("allowedRelations", UNSET))

        node_attributes_update = cls(
            source_type=source_type,
            source_id=source_id,
            source_version=source_version,
            new_version=new_version,
            update_mode=update_mode,
            new_source_type=new_source_type,
            new_source_id=new_source_id,
            excluded_relations=excluded_relations,
            allowed_relations=allowed_relations,
        )

        node_attributes_update.additional_properties = d
        return node_attributes_update

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
