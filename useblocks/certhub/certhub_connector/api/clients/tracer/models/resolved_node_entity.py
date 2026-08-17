from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_type import NodeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolved_node_entity_additional_data_type_0 import (
        ResolvedNodeEntityAdditionalDataType0,
    )
    from ..models.version_data import VersionData


T = TypeVar("T", bound="ResolvedNodeEntity")


@_attrs_define
class ResolvedNodeEntity:
    """
    Attributes:
        entity_id (str): the id of the entity. in case of versioned entites, this is the parent id
        entity_type (NodeType):
        name (str):
        entity_version (list[str] | None | str | Unset):  Default: ''.
        additional_data (None | ResolvedNodeEntityAdditionalDataType0 | Unset):
        versions (list[VersionData] | None | Unset):
    """

    entity_id: str
    entity_type: NodeType
    name: str
    entity_version: list[str] | None | str | Unset = ""
    additional_data: None | ResolvedNodeEntityAdditionalDataType0 | Unset = UNSET
    versions: list[VersionData] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resolved_node_entity_additional_data_type_0 import (
            ResolvedNodeEntityAdditionalDataType0,
        )

        entity_id = self.entity_id

        entity_type = self.entity_type.value

        name = self.name

        entity_version: list[str] | None | str | Unset
        if isinstance(self.entity_version, Unset):
            entity_version = UNSET
        elif isinstance(self.entity_version, list):
            entity_version = self.entity_version

        else:
            entity_version = self.entity_version

        additional_data: dict[str, Any] | None | Unset
        if isinstance(self.additional_data, Unset):
            additional_data = UNSET
        elif isinstance(self.additional_data, ResolvedNodeEntityAdditionalDataType0):
            additional_data = self.additional_data.to_dict()
        else:
            additional_data = self.additional_data

        versions: list[dict[str, Any]] | None | Unset
        if isinstance(self.versions, Unset):
            versions = UNSET
        elif isinstance(self.versions, list):
            versions = []
            for versions_type_0_item_data in self.versions:
                versions_type_0_item = versions_type_0_item_data.to_dict()
                versions.append(versions_type_0_item)

        else:
            versions = self.versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_id": entity_id,
                "entity_type": entity_type,
                "name": name,
            }
        )
        if entity_version is not UNSET:
            field_dict["entity_version"] = entity_version
        if additional_data is not UNSET:
            field_dict["additional_data"] = additional_data
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resolved_node_entity_additional_data_type_0 import (
            ResolvedNodeEntityAdditionalDataType0,
        )
        from ..models.version_data import VersionData

        d = dict(src_dict)
        entity_id = d.pop("entity_id")

        entity_type = NodeType(d.pop("entity_type"))

        name = d.pop("name")

        def _parse_entity_version(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entity_version_type_1 = cast(list[str], data)

                return entity_version_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        entity_version = _parse_entity_version(d.pop("entity_version", UNSET))

        def _parse_additional_data(
            data: object,
        ) -> None | ResolvedNodeEntityAdditionalDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_data_type_0 = (
                    ResolvedNodeEntityAdditionalDataType0.from_dict(data)
                )

                return additional_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResolvedNodeEntityAdditionalDataType0 | Unset, data)

        additional_data = _parse_additional_data(d.pop("additional_data", UNSET))

        def _parse_versions(data: object) -> list[VersionData] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                versions_type_0 = []
                _versions_type_0 = data
                for versions_type_0_item_data in _versions_type_0:
                    versions_type_0_item = VersionData.from_dict(
                        versions_type_0_item_data
                    )

                    versions_type_0.append(versions_type_0_item)

                return versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VersionData] | None | Unset, data)

        versions = _parse_versions(d.pop("versions", UNSET))

        resolved_node_entity = cls(
            entity_id=entity_id,
            entity_type=entity_type,
            name=name,
            entity_version=entity_version,
            additional_data=additional_data,
            versions=versions,
        )

        resolved_node_entity.additional_properties = d
        return resolved_node_entity

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
