from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_info import AuditInfo
    from ..models.grid_settings import GridSettings
    from ..models.qm_list_category_type_0 import QmListCategoryType0
    from ..models.qm_list_category_type_1 import QmListCategoryType1
    from ..models.tenant_metadata import TenantMetadata


T = TypeVar("T", bound="QmList")


@_attrs_define
class QmList:
    """
    Attributes:
        name (str):
        metadata (TenantMetadata):
        audit_info (AuditInfo):
        template_ids (list[str]):
        field_id (None | str | Unset): MongoDB document ObjectID
        description (None | str | Unset):  Default: ''.
        settings (GridSettings | None | Unset):
        category (None | QmListCategoryType0 | QmListCategoryType1 | Unset):
        filter_tag (None | str | Unset):
    """

    name: str
    metadata: TenantMetadata
    audit_info: AuditInfo
    template_ids: list[str]
    field_id: None | str | Unset = UNSET
    description: None | str | Unset = ""
    settings: GridSettings | None | Unset = UNSET
    category: None | QmListCategoryType0 | QmListCategoryType1 | Unset = UNSET
    filter_tag: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_settings import GridSettings
        from ..models.qm_list_category_type_0 import QmListCategoryType0
        from ..models.qm_list_category_type_1 import QmListCategoryType1

        name = self.name

        metadata = self.metadata.to_dict()

        audit_info = self.audit_info.to_dict()

        template_ids = self.template_ids

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, GridSettings):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, QmListCategoryType0) or isinstance(
            self.category, QmListCategoryType1
        ):
            category = self.category.to_dict()
        else:
            category = self.category

        filter_tag: None | str | Unset
        if isinstance(self.filter_tag, Unset):
            filter_tag = UNSET
        else:
            filter_tag = self.filter_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "metadata": metadata,
                "audit_info": audit_info,
                "template_ids": template_ids,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if description is not UNSET:
            field_dict["description"] = description
        if settings is not UNSET:
            field_dict["settings"] = settings
        if category is not UNSET:
            field_dict["category"] = category
        if filter_tag is not UNSET:
            field_dict["filter_tag"] = filter_tag

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_info import AuditInfo
        from ..models.grid_settings import GridSettings
        from ..models.qm_list_category_type_0 import QmListCategoryType0
        from ..models.qm_list_category_type_1 import QmListCategoryType1
        from ..models.tenant_metadata import TenantMetadata

        d = dict(src_dict)
        name = d.pop("name")

        metadata = TenantMetadata.from_dict(d.pop("metadata"))

        audit_info = AuditInfo.from_dict(d.pop("audit_info"))

        template_ids = cast(list[str], d.pop("template_ids"))

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_settings(data: object) -> GridSettings | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = GridSettings.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GridSettings | None | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        def _parse_category(
            data: object,
        ) -> None | QmListCategoryType0 | QmListCategoryType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_type_0 = QmListCategoryType0.from_dict(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_type_1 = QmListCategoryType1.from_dict(data)

                return category_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QmListCategoryType0 | QmListCategoryType1 | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_filter_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_tag = _parse_filter_tag(d.pop("filter_tag", UNSET))

        qm_list = cls(
            name=name,
            metadata=metadata,
            audit_info=audit_info,
            template_ids=template_ids,
            field_id=field_id,
            description=description,
            settings=settings,
            category=category,
            filter_tag=filter_tag,
        )

        qm_list.additional_properties = d
        return qm_list

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
