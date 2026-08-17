from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph_traversal_options import GraphTraversalOptions
    from ..models.node_ai_analysis_request_changed_object_type_0 import (
        NodeAIAnalysisRequestChangedObjectType0,
    )
    from ..models.product_context_question import ProductContextQuestion


T = TypeVar("T", bound="NodeAIAnalysisRequest")


@_attrs_define
class NodeAIAnalysisRequest:
    """
    Attributes:
        filter_ (GraphTraversalOptions | Unset):
        changed_object (NodeAIAnalysisRequestChangedObjectType0 | None | Unset):
        product_context (list[ProductContextQuestion] | Unset):
        user_query (None | str | Unset):
    """

    filter_: GraphTraversalOptions | Unset = UNSET
    changed_object: NodeAIAnalysisRequestChangedObjectType0 | None | Unset = UNSET
    product_context: list[ProductContextQuestion] | Unset = UNSET
    user_query: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.node_ai_analysis_request_changed_object_type_0 import (
            NodeAIAnalysisRequestChangedObjectType0,
        )

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        changed_object: dict[str, Any] | None | Unset
        if isinstance(self.changed_object, Unset):
            changed_object = UNSET
        elif isinstance(self.changed_object, NodeAIAnalysisRequestChangedObjectType0):
            changed_object = self.changed_object.to_dict()
        else:
            changed_object = self.changed_object

        product_context: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_context, Unset):
            product_context = []
            for product_context_item_data in self.product_context:
                product_context_item = product_context_item_data.to_dict()
                product_context.append(product_context_item)

        user_query: None | str | Unset
        if isinstance(self.user_query, Unset):
            user_query = UNSET
        else:
            user_query = self.user_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if changed_object is not UNSET:
            field_dict["changed_object"] = changed_object
        if product_context is not UNSET:
            field_dict["product_context"] = product_context
        if user_query is not UNSET:
            field_dict["user_query"] = user_query

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.graph_traversal_options import GraphTraversalOptions
        from ..models.node_ai_analysis_request_changed_object_type_0 import (
            NodeAIAnalysisRequestChangedObjectType0,
        )
        from ..models.product_context_question import ProductContextQuestion

        d = dict(src_dict)
        _filter_ = d.pop("filter", UNSET)
        filter_: GraphTraversalOptions | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = GraphTraversalOptions.from_dict(_filter_)

        def _parse_changed_object(
            data: object,
        ) -> NodeAIAnalysisRequestChangedObjectType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                changed_object_type_0 = (
                    NodeAIAnalysisRequestChangedObjectType0.from_dict(data)
                )

                return changed_object_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NodeAIAnalysisRequestChangedObjectType0 | None | Unset, data)

        changed_object = _parse_changed_object(d.pop("changed_object", UNSET))

        _product_context = d.pop("product_context", UNSET)
        product_context: list[ProductContextQuestion] | Unset = UNSET
        if _product_context is not UNSET:
            product_context = []
            for product_context_item_data in _product_context:
                product_context_item = ProductContextQuestion.from_dict(
                    product_context_item_data
                )

                product_context.append(product_context_item)

        def _parse_user_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_query = _parse_user_query(d.pop("user_query", UNSET))

        node_ai_analysis_request = cls(
            filter_=filter_,
            changed_object=changed_object,
            product_context=product_context,
            user_query=user_query,
        )

        node_ai_analysis_request.additional_properties = d
        return node_ai_analysis_request

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
