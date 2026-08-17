from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resolved_trace import ResolvedTrace


T = TypeVar("T", bound="BatchRetrieveResponseResolvedResultsType0")


@_attrs_define
class BatchRetrieveResponseResolvedResultsType0:
    """ """

    additional_properties: dict[str, list[None | ResolvedTrace]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.resolved_trace import ResolvedTrace

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item: dict[str, Any] | None
                if isinstance(additional_property_item_data, ResolvedTrace):
                    additional_property_item = additional_property_item_data.to_dict()
                else:
                    additional_property_item = additional_property_item_data
                field_dict[prop_name].append(additional_property_item)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resolved_trace import ResolvedTrace

        d = dict(src_dict)
        batch_retrieve_response_resolved_results_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:

                def _parse_additional_property_item(
                    data: object,
                ) -> None | ResolvedTrace:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        additional_property_item_type_0 = ResolvedTrace.from_dict(data)

                        return additional_property_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | ResolvedTrace, data)

                additional_property_item = _parse_additional_property_item(
                    additional_property_item_data
                )

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        batch_retrieve_response_resolved_results_type_0.additional_properties = (
            additional_properties
        )
        return batch_retrieve_response_resolved_results_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[None | ResolvedTrace]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[None | ResolvedTrace]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
