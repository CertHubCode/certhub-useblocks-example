from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paginated_trace_list import PaginatedTraceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    json_relation_type_in: None | str | Unset
    if isinstance(relation_type_in, Unset):
        json_relation_type_in = UNSET
    else:
        json_relation_type_in = relation_type_in
    params["relation_type__in"] = json_relation_type_in

    json_source: None | str | Unset
    if isinstance(source, Unset):
        json_source = UNSET
    else:
        json_source = source
    params["source"] = json_source

    json_target: None | str | Unset
    if isinstance(target, Unset):
        json_target = UNSET
    else:
        json_target = target
    params["target"] = json_target

    json_order_by: None | str | Unset
    if isinstance(order_by, Unset):
        json_order_by = UNSET
    else:
        json_order_by = order_by
    params["order_by"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/traces/all",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PaginatedTraceList | None:
    if response.status_code == 200:
        response_200 = PaginatedTraceList.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | PaginatedTraceList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PaginatedTraceList]:
    """Get All Traces Paginated

     Retrieves traces for the tenant as a paginated list with total count.

    Example: /traces/all?relation_type__in=is_related,mentions
    Example: /traces/all?source=node_type:node_id:version&skip=0&limit=50

    Args:
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        relation_type_in (None | str | Unset):
        source (None | str | Unset):
        target (None | str | Unset):
        order_by (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PaginatedTraceList]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        relation_type_in=relation_type_in,
        source=source,
        target=target,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> HTTPValidationError | PaginatedTraceList | None:
    """Get All Traces Paginated

     Retrieves traces for the tenant as a paginated list with total count.

    Example: /traces/all?relation_type__in=is_related,mentions
    Example: /traces/all?source=node_type:node_id:version&skip=0&limit=50

    Args:
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        relation_type_in (None | str | Unset):
        source (None | str | Unset):
        target (None | str | Unset):
        order_by (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PaginatedTraceList
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
        relation_type_in=relation_type_in,
        source=source,
        target=target,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PaginatedTraceList]:
    """Get All Traces Paginated

     Retrieves traces for the tenant as a paginated list with total count.

    Example: /traces/all?relation_type__in=is_related,mentions
    Example: /traces/all?source=node_type:node_id:version&skip=0&limit=50

    Args:
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        relation_type_in (None | str | Unset):
        source (None | str | Unset):
        target (None | str | Unset):
        order_by (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PaginatedTraceList]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        relation_type_in=relation_type_in,
        source=source,
        target=target,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> HTTPValidationError | PaginatedTraceList | None:
    """Get All Traces Paginated

     Retrieves traces for the tenant as a paginated list with total count.

    Example: /traces/all?relation_type__in=is_related,mentions
    Example: /traces/all?source=node_type:node_id:version&skip=0&limit=50

    Args:
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        relation_type_in (None | str | Unset):
        source (None | str | Unset):
        target (None | str | Unset):
        order_by (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PaginatedTraceList
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
            relation_type_in=relation_type_in,
            source=source,
            target=target,
            order_by=order_by,
        )
    ).parsed
