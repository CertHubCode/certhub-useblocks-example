from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grid_density import GridDensity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grid_column_visibility import GridColumnVisibility
    from ..models.grid_filter_model import GridFilterModel
    from ..models.grid_sorting import GridSorting


T = TypeVar("T", bound="GridSettings")


@_attrs_define
class GridSettings:
    """
    Attributes:
        grid_filter_model (GridFilterModel | None | Unset):
        column_visibility (list[GridColumnVisibility] | None | Unset):
        grid_density (GridDensity | None | Unset):
        sorting (list[GridSorting] | None | Unset):
    """

    grid_filter_model: GridFilterModel | None | Unset = UNSET
    column_visibility: list[GridColumnVisibility] | None | Unset = UNSET
    grid_density: GridDensity | None | Unset = UNSET
    sorting: list[GridSorting] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_filter_model import GridFilterModel

        grid_filter_model: dict[str, Any] | None | Unset
        if isinstance(self.grid_filter_model, Unset):
            grid_filter_model = UNSET
        elif isinstance(self.grid_filter_model, GridFilterModel):
            grid_filter_model = self.grid_filter_model.to_dict()
        else:
            grid_filter_model = self.grid_filter_model

        column_visibility: list[dict[str, Any]] | None | Unset
        if isinstance(self.column_visibility, Unset):
            column_visibility = UNSET
        elif isinstance(self.column_visibility, list):
            column_visibility = []
            for column_visibility_type_0_item_data in self.column_visibility:
                column_visibility_type_0_item = (
                    column_visibility_type_0_item_data.to_dict()
                )
                column_visibility.append(column_visibility_type_0_item)

        else:
            column_visibility = self.column_visibility

        grid_density: None | str | Unset
        if isinstance(self.grid_density, Unset):
            grid_density = UNSET
        elif isinstance(self.grid_density, GridDensity):
            grid_density = self.grid_density.value
        else:
            grid_density = self.grid_density

        sorting: list[dict[str, Any]] | None | Unset
        if isinstance(self.sorting, Unset):
            sorting = UNSET
        elif isinstance(self.sorting, list):
            sorting = []
            for sorting_type_0_item_data in self.sorting:
                sorting_type_0_item = sorting_type_0_item_data.to_dict()
                sorting.append(sorting_type_0_item)

        else:
            sorting = self.sorting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grid_filter_model is not UNSET:
            field_dict["gridFilterModel"] = grid_filter_model
        if column_visibility is not UNSET:
            field_dict["columnVisibility"] = column_visibility
        if grid_density is not UNSET:
            field_dict["gridDensity"] = grid_density
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grid_column_visibility import GridColumnVisibility
        from ..models.grid_filter_model import GridFilterModel
        from ..models.grid_sorting import GridSorting

        d = dict(src_dict)

        def _parse_grid_filter_model(data: object) -> GridFilterModel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grid_filter_model_type_0 = GridFilterModel.from_dict(data)

                return grid_filter_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GridFilterModel | None | Unset, data)

        grid_filter_model = _parse_grid_filter_model(d.pop("gridFilterModel", UNSET))

        def _parse_column_visibility(
            data: object,
        ) -> list[GridColumnVisibility] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                column_visibility_type_0 = []
                _column_visibility_type_0 = data
                for column_visibility_type_0_item_data in _column_visibility_type_0:
                    column_visibility_type_0_item = GridColumnVisibility.from_dict(
                        column_visibility_type_0_item_data
                    )

                    column_visibility_type_0.append(column_visibility_type_0_item)

                return column_visibility_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GridColumnVisibility] | None | Unset, data)

        column_visibility = _parse_column_visibility(d.pop("columnVisibility", UNSET))

        def _parse_grid_density(data: object) -> GridDensity | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                grid_density_type_0 = GridDensity(data)

                return grid_density_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GridDensity | None | Unset, data)

        grid_density = _parse_grid_density(d.pop("gridDensity", UNSET))

        def _parse_sorting(data: object) -> list[GridSorting] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sorting_type_0 = []
                _sorting_type_0 = data
                for sorting_type_0_item_data in _sorting_type_0:
                    sorting_type_0_item = GridSorting.from_dict(
                        sorting_type_0_item_data
                    )

                    sorting_type_0.append(sorting_type_0_item)

                return sorting_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GridSorting] | None | Unset, data)

        sorting = _parse_sorting(d.pop("sorting", UNSET))

        grid_settings = cls(
            grid_filter_model=grid_filter_model,
            column_visibility=column_visibility,
            grid_density=grid_density,
            sorting=sorting,
        )

        grid_settings.additional_properties = d
        return grid_settings

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
