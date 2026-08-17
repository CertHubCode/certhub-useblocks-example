import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.record import Record
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    products: list[str] | None | Unset = UNSET,
    templates: list[str] | None | Unset = UNSET,
    id_in: None | str | Unset = UNSET,
    context_linked_product: None | str | Unset = UNSET,
    context_form_id: None | str | Unset = UNSET,
    context_knowledge_unit_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id_in: None | str | Unset = UNSET,
    context_global_element_id: None | str | Unset = UNSET,
    context_linked_document_document_id: None | str | Unset = UNSET,
    context_linked_document_document_version: None | str | Unset = UNSET,
    context_linked_document_template_id: None | str | Unset = UNSET,
    context_linked_sop: None | str | Unset = UNSET,
    context_filter_tag: None | str | Unset = UNSET,
    audit_info_user_id_created: None | str | Unset = UNSET,
    audit_info_start_date: datetime.datetime | None | Unset = UNSET,
    audit_info_end_date: datetime.datetime | None | Unset = UNSET,
    audit_info_include_updated: bool | None | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_products: list[str] | None | Unset
    if isinstance(products, Unset):
        json_products = UNSET
    elif isinstance(products, list):
        json_products = products

    else:
        json_products = products
    params["products"] = json_products

    json_templates: list[str] | None | Unset
    if isinstance(templates, Unset):
        json_templates = UNSET
    elif isinstance(templates, list):
        json_templates = templates

    else:
        json_templates = templates
    params["templates"] = json_templates

    json_id_in: None | str | Unset
    if isinstance(id_in, Unset):
        json_id_in = UNSET
    else:
        json_id_in = id_in
    params["id__in"] = json_id_in

    json_context_linked_product: None | str | Unset
    if isinstance(context_linked_product, Unset):
        json_context_linked_product = UNSET
    else:
        json_context_linked_product = context_linked_product
    params["context__linked_product"] = json_context_linked_product

    json_context_form_id: None | str | Unset
    if isinstance(context_form_id, Unset):
        json_context_form_id = UNSET
    else:
        json_context_form_id = context_form_id
    params["context__form_id"] = json_context_form_id

    json_context_knowledge_unit_id: None | str | Unset
    if isinstance(context_knowledge_unit_id, Unset):
        json_context_knowledge_unit_id = UNSET
    else:
        json_context_knowledge_unit_id = context_knowledge_unit_id
    params["context__knowledge_unit_id"] = json_context_knowledge_unit_id

    json_context_knowledge_unit_topic_id: None | str | Unset
    if isinstance(context_knowledge_unit_topic_id, Unset):
        json_context_knowledge_unit_topic_id = UNSET
    else:
        json_context_knowledge_unit_topic_id = context_knowledge_unit_topic_id
    params["context__knowledge_unit_topic_id"] = json_context_knowledge_unit_topic_id

    json_context_knowledge_unit_topic_id_in: None | str | Unset
    if isinstance(context_knowledge_unit_topic_id_in, Unset):
        json_context_knowledge_unit_topic_id_in = UNSET
    else:
        json_context_knowledge_unit_topic_id_in = context_knowledge_unit_topic_id_in
    params["context__knowledge_unit_topic_id__in"] = (
        json_context_knowledge_unit_topic_id_in
    )

    json_context_global_element_id: None | str | Unset
    if isinstance(context_global_element_id, Unset):
        json_context_global_element_id = UNSET
    else:
        json_context_global_element_id = context_global_element_id
    params["context__global_element_id"] = json_context_global_element_id

    json_context_linked_document_document_id: None | str | Unset
    if isinstance(context_linked_document_document_id, Unset):
        json_context_linked_document_document_id = UNSET
    else:
        json_context_linked_document_document_id = context_linked_document_document_id
    params["context__linked_document__document_id"] = (
        json_context_linked_document_document_id
    )

    json_context_linked_document_document_version: None | str | Unset
    if isinstance(context_linked_document_document_version, Unset):
        json_context_linked_document_document_version = UNSET
    else:
        json_context_linked_document_document_version = (
            context_linked_document_document_version
        )
    params["context__linked_document__document_version"] = (
        json_context_linked_document_document_version
    )

    json_context_linked_document_template_id: None | str | Unset
    if isinstance(context_linked_document_template_id, Unset):
        json_context_linked_document_template_id = UNSET
    else:
        json_context_linked_document_template_id = context_linked_document_template_id
    params["context__linked_document__template_id"] = (
        json_context_linked_document_template_id
    )

    json_context_linked_sop: None | str | Unset
    if isinstance(context_linked_sop, Unset):
        json_context_linked_sop = UNSET
    else:
        json_context_linked_sop = context_linked_sop
    params["context__linked_sop"] = json_context_linked_sop

    json_context_filter_tag: None | str | Unset
    if isinstance(context_filter_tag, Unset):
        json_context_filter_tag = UNSET
    else:
        json_context_filter_tag = context_filter_tag
    params["context__filter_tag"] = json_context_filter_tag

    json_audit_info_user_id_created: None | str | Unset
    if isinstance(audit_info_user_id_created, Unset):
        json_audit_info_user_id_created = UNSET
    else:
        json_audit_info_user_id_created = audit_info_user_id_created
    params["audit_info__user_id_created"] = json_audit_info_user_id_created

    json_audit_info_start_date: None | str | Unset
    if isinstance(audit_info_start_date, Unset):
        json_audit_info_start_date = UNSET
    elif isinstance(audit_info_start_date, datetime.datetime):
        json_audit_info_start_date = audit_info_start_date.isoformat()
    else:
        json_audit_info_start_date = audit_info_start_date
    params["audit_info__start_date"] = json_audit_info_start_date

    json_audit_info_end_date: None | str | Unset
    if isinstance(audit_info_end_date, Unset):
        json_audit_info_end_date = UNSET
    elif isinstance(audit_info_end_date, datetime.datetime):
        json_audit_info_end_date = audit_info_end_date.isoformat()
    else:
        json_audit_info_end_date = audit_info_end_date
    params["audit_info__end_date"] = json_audit_info_end_date

    json_audit_info_include_updated: bool | None | Unset
    if isinstance(audit_info_include_updated, Unset):
        json_audit_info_include_updated = UNSET
    else:
        json_audit_info_include_updated = audit_info_include_updated
    params["audit_info__include_updated"] = json_audit_info_include_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/records/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[Record] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Record.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | list[Record]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    products: list[str] | None | Unset = UNSET,
    templates: list[str] | None | Unset = UNSET,
    id_in: None | str | Unset = UNSET,
    context_linked_product: None | str | Unset = UNSET,
    context_form_id: None | str | Unset = UNSET,
    context_knowledge_unit_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id_in: None | str | Unset = UNSET,
    context_global_element_id: None | str | Unset = UNSET,
    context_linked_document_document_id: None | str | Unset = UNSET,
    context_linked_document_document_version: None | str | Unset = UNSET,
    context_linked_document_template_id: None | str | Unset = UNSET,
    context_linked_sop: None | str | Unset = UNSET,
    context_filter_tag: None | str | Unset = UNSET,
    audit_info_user_id_created: None | str | Unset = UNSET,
    audit_info_start_date: datetime.datetime | None | Unset = UNSET,
    audit_info_end_date: datetime.datetime | None | Unset = UNSET,
    audit_info_include_updated: bool | None | Unset = False,
) -> Response[Any | HTTPValidationError | list[Record]]:
    """List Records

     Get all Records of a tennant matching the specified filters

    Args:
        products (list[str] | None | Unset):
        templates (list[str] | None | Unset):
        id_in (None | str | Unset):
        context_linked_product (None | str | Unset):
        context_form_id (None | str | Unset):
        context_knowledge_unit_id (None | str | Unset):
        context_knowledge_unit_topic_id (None | str | Unset):
        context_knowledge_unit_topic_id_in (None | str | Unset):
        context_global_element_id (None | str | Unset):
        context_linked_document_document_id (None | str | Unset):
        context_linked_document_document_version (None | str | Unset):
        context_linked_document_template_id (None | str | Unset):
        context_linked_sop (None | str | Unset):
        context_filter_tag (None | str | Unset):
        audit_info_user_id_created (None | str | Unset):
        audit_info_start_date (datetime.datetime | None | Unset):
        audit_info_end_date (datetime.datetime | None | Unset):
        audit_info_include_updated (bool | None | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[Record]]
    """

    kwargs = _get_kwargs(
        products=products,
        templates=templates,
        id_in=id_in,
        context_linked_product=context_linked_product,
        context_form_id=context_form_id,
        context_knowledge_unit_id=context_knowledge_unit_id,
        context_knowledge_unit_topic_id=context_knowledge_unit_topic_id,
        context_knowledge_unit_topic_id_in=context_knowledge_unit_topic_id_in,
        context_global_element_id=context_global_element_id,
        context_linked_document_document_id=context_linked_document_document_id,
        context_linked_document_document_version=context_linked_document_document_version,
        context_linked_document_template_id=context_linked_document_template_id,
        context_linked_sop=context_linked_sop,
        context_filter_tag=context_filter_tag,
        audit_info_user_id_created=audit_info_user_id_created,
        audit_info_start_date=audit_info_start_date,
        audit_info_end_date=audit_info_end_date,
        audit_info_include_updated=audit_info_include_updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    products: list[str] | None | Unset = UNSET,
    templates: list[str] | None | Unset = UNSET,
    id_in: None | str | Unset = UNSET,
    context_linked_product: None | str | Unset = UNSET,
    context_form_id: None | str | Unset = UNSET,
    context_knowledge_unit_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id_in: None | str | Unset = UNSET,
    context_global_element_id: None | str | Unset = UNSET,
    context_linked_document_document_id: None | str | Unset = UNSET,
    context_linked_document_document_version: None | str | Unset = UNSET,
    context_linked_document_template_id: None | str | Unset = UNSET,
    context_linked_sop: None | str | Unset = UNSET,
    context_filter_tag: None | str | Unset = UNSET,
    audit_info_user_id_created: None | str | Unset = UNSET,
    audit_info_start_date: datetime.datetime | None | Unset = UNSET,
    audit_info_end_date: datetime.datetime | None | Unset = UNSET,
    audit_info_include_updated: bool | None | Unset = False,
) -> Any | HTTPValidationError | list[Record] | None:
    """List Records

     Get all Records of a tennant matching the specified filters

    Args:
        products (list[str] | None | Unset):
        templates (list[str] | None | Unset):
        id_in (None | str | Unset):
        context_linked_product (None | str | Unset):
        context_form_id (None | str | Unset):
        context_knowledge_unit_id (None | str | Unset):
        context_knowledge_unit_topic_id (None | str | Unset):
        context_knowledge_unit_topic_id_in (None | str | Unset):
        context_global_element_id (None | str | Unset):
        context_linked_document_document_id (None | str | Unset):
        context_linked_document_document_version (None | str | Unset):
        context_linked_document_template_id (None | str | Unset):
        context_linked_sop (None | str | Unset):
        context_filter_tag (None | str | Unset):
        audit_info_user_id_created (None | str | Unset):
        audit_info_start_date (datetime.datetime | None | Unset):
        audit_info_end_date (datetime.datetime | None | Unset):
        audit_info_include_updated (bool | None | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[Record]
    """

    return sync_detailed(
        client=client,
        products=products,
        templates=templates,
        id_in=id_in,
        context_linked_product=context_linked_product,
        context_form_id=context_form_id,
        context_knowledge_unit_id=context_knowledge_unit_id,
        context_knowledge_unit_topic_id=context_knowledge_unit_topic_id,
        context_knowledge_unit_topic_id_in=context_knowledge_unit_topic_id_in,
        context_global_element_id=context_global_element_id,
        context_linked_document_document_id=context_linked_document_document_id,
        context_linked_document_document_version=context_linked_document_document_version,
        context_linked_document_template_id=context_linked_document_template_id,
        context_linked_sop=context_linked_sop,
        context_filter_tag=context_filter_tag,
        audit_info_user_id_created=audit_info_user_id_created,
        audit_info_start_date=audit_info_start_date,
        audit_info_end_date=audit_info_end_date,
        audit_info_include_updated=audit_info_include_updated,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    products: list[str] | None | Unset = UNSET,
    templates: list[str] | None | Unset = UNSET,
    id_in: None | str | Unset = UNSET,
    context_linked_product: None | str | Unset = UNSET,
    context_form_id: None | str | Unset = UNSET,
    context_knowledge_unit_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id_in: None | str | Unset = UNSET,
    context_global_element_id: None | str | Unset = UNSET,
    context_linked_document_document_id: None | str | Unset = UNSET,
    context_linked_document_document_version: None | str | Unset = UNSET,
    context_linked_document_template_id: None | str | Unset = UNSET,
    context_linked_sop: None | str | Unset = UNSET,
    context_filter_tag: None | str | Unset = UNSET,
    audit_info_user_id_created: None | str | Unset = UNSET,
    audit_info_start_date: datetime.datetime | None | Unset = UNSET,
    audit_info_end_date: datetime.datetime | None | Unset = UNSET,
    audit_info_include_updated: bool | None | Unset = False,
) -> Response[Any | HTTPValidationError | list[Record]]:
    """List Records

     Get all Records of a tennant matching the specified filters

    Args:
        products (list[str] | None | Unset):
        templates (list[str] | None | Unset):
        id_in (None | str | Unset):
        context_linked_product (None | str | Unset):
        context_form_id (None | str | Unset):
        context_knowledge_unit_id (None | str | Unset):
        context_knowledge_unit_topic_id (None | str | Unset):
        context_knowledge_unit_topic_id_in (None | str | Unset):
        context_global_element_id (None | str | Unset):
        context_linked_document_document_id (None | str | Unset):
        context_linked_document_document_version (None | str | Unset):
        context_linked_document_template_id (None | str | Unset):
        context_linked_sop (None | str | Unset):
        context_filter_tag (None | str | Unset):
        audit_info_user_id_created (None | str | Unset):
        audit_info_start_date (datetime.datetime | None | Unset):
        audit_info_end_date (datetime.datetime | None | Unset):
        audit_info_include_updated (bool | None | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[Record]]
    """

    kwargs = _get_kwargs(
        products=products,
        templates=templates,
        id_in=id_in,
        context_linked_product=context_linked_product,
        context_form_id=context_form_id,
        context_knowledge_unit_id=context_knowledge_unit_id,
        context_knowledge_unit_topic_id=context_knowledge_unit_topic_id,
        context_knowledge_unit_topic_id_in=context_knowledge_unit_topic_id_in,
        context_global_element_id=context_global_element_id,
        context_linked_document_document_id=context_linked_document_document_id,
        context_linked_document_document_version=context_linked_document_document_version,
        context_linked_document_template_id=context_linked_document_template_id,
        context_linked_sop=context_linked_sop,
        context_filter_tag=context_filter_tag,
        audit_info_user_id_created=audit_info_user_id_created,
        audit_info_start_date=audit_info_start_date,
        audit_info_end_date=audit_info_end_date,
        audit_info_include_updated=audit_info_include_updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    products: list[str] | None | Unset = UNSET,
    templates: list[str] | None | Unset = UNSET,
    id_in: None | str | Unset = UNSET,
    context_linked_product: None | str | Unset = UNSET,
    context_form_id: None | str | Unset = UNSET,
    context_knowledge_unit_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id: None | str | Unset = UNSET,
    context_knowledge_unit_topic_id_in: None | str | Unset = UNSET,
    context_global_element_id: None | str | Unset = UNSET,
    context_linked_document_document_id: None | str | Unset = UNSET,
    context_linked_document_document_version: None | str | Unset = UNSET,
    context_linked_document_template_id: None | str | Unset = UNSET,
    context_linked_sop: None | str | Unset = UNSET,
    context_filter_tag: None | str | Unset = UNSET,
    audit_info_user_id_created: None | str | Unset = UNSET,
    audit_info_start_date: datetime.datetime | None | Unset = UNSET,
    audit_info_end_date: datetime.datetime | None | Unset = UNSET,
    audit_info_include_updated: bool | None | Unset = False,
) -> Any | HTTPValidationError | list[Record] | None:
    """List Records

     Get all Records of a tennant matching the specified filters

    Args:
        products (list[str] | None | Unset):
        templates (list[str] | None | Unset):
        id_in (None | str | Unset):
        context_linked_product (None | str | Unset):
        context_form_id (None | str | Unset):
        context_knowledge_unit_id (None | str | Unset):
        context_knowledge_unit_topic_id (None | str | Unset):
        context_knowledge_unit_topic_id_in (None | str | Unset):
        context_global_element_id (None | str | Unset):
        context_linked_document_document_id (None | str | Unset):
        context_linked_document_document_version (None | str | Unset):
        context_linked_document_template_id (None | str | Unset):
        context_linked_sop (None | str | Unset):
        context_filter_tag (None | str | Unset):
        audit_info_user_id_created (None | str | Unset):
        audit_info_start_date (datetime.datetime | None | Unset):
        audit_info_end_date (datetime.datetime | None | Unset):
        audit_info_include_updated (bool | None | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[Record]
    """

    return (
        await asyncio_detailed(
            client=client,
            products=products,
            templates=templates,
            id_in=id_in,
            context_linked_product=context_linked_product,
            context_form_id=context_form_id,
            context_knowledge_unit_id=context_knowledge_unit_id,
            context_knowledge_unit_topic_id=context_knowledge_unit_topic_id,
            context_knowledge_unit_topic_id_in=context_knowledge_unit_topic_id_in,
            context_global_element_id=context_global_element_id,
            context_linked_document_document_id=context_linked_document_document_id,
            context_linked_document_document_version=context_linked_document_document_version,
            context_linked_document_template_id=context_linked_document_template_id,
            context_linked_sop=context_linked_sop,
            context_filter_tag=context_filter_tag,
            audit_info_user_id_created=audit_info_user_id_created,
            audit_info_start_date=audit_info_start_date,
            audit_info_end_date=audit_info_end_date,
            audit_info_include_updated=audit_info_include_updated,
        )
    ).parsed
