from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.trace_list import TraceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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
        "url": "/traces/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TraceList | None:
    if response.status_code == 200:
        response_200 = TraceList.from_dict(response.json())

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
) -> Response[HTTPValidationError | TraceList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TraceList]:
    """Get All Traces

     Retrieves all traces for the tenant as a simple list.

    Supports filtering by relation_type using query parameters.
    Example: /traces/list?relation_type__in=is_related,mentions

    You can also filter by a source node:
    Example: /traces/list?source=node_type:node_id:version

    Combine filters to get traces from a specific node with specific relation types:
    Example: /traces/list?source=node_type:node_id:version&relation_type__in=is_related,mentions

    Args:
        relation_type_in (None | str | Unset):
        source (None | str | Unset):
        target (None | str | Unset):
        order_by (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TraceList]
    """

    kwargs = _get_kwargs(
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
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> HTTPValidationError | TraceList | None:
    """Get All Traces

     Retrieves all traces for the tenant as a simple list.

    Supports filtering by relation_type using query parameters.
    Example: /traces/list?relation_type__in=is_related,mentions

    You can also filter by a source node:
    Example: /traces/list?source=node_type:node_id:version

    Combine filters to get traces from a specific node with specific relation types:
    Example: /traces/list?source=node_type:node_id:version&relation_type__in=is_related,mentions

    Args:
        relation_type_in (None | str | Unset):
        source (None | str | Unset):
        target (None | str | Unset):
        order_by (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TraceList
    """

    return sync_detailed(
        client=client,
        relation_type_in=relation_type_in,
        source=source,
        target=target,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TraceList]:
    """Get All Traces

     Retrieves all traces for the tenant as a simple list.

    Supports filtering by relation_type using query parameters.
    Example: /traces/list?relation_type__in=is_related,mentions

    You can also filter by a source node:
    Example: /traces/list?source=node_type:node_id:version

    Combine filters to get traces from a specific node with specific relation types:
    Example: /traces/list?source=node_type:node_id:version&relation_type__in=is_related,mentions

    Args:
        relation_type_in (None | str | Unset):
        source (None | str | Unset):
        target (None | str | Unset):
        order_by (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TraceList]
    """

    kwargs = _get_kwargs(
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
    relation_type_in: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    target: None | str | Unset = UNSET,
    order_by: None | str | Unset = UNSET,
) -> HTTPValidationError | TraceList | None:
    """Get All Traces

     Retrieves all traces for the tenant as a simple list.

    Supports filtering by relation_type using query parameters.
    Example: /traces/list?relation_type__in=is_related,mentions

    You can also filter by a source node:
    Example: /traces/list?source=node_type:node_id:version

    Combine filters to get traces from a specific node with specific relation types:
    Example: /traces/list?source=node_type:node_id:version&relation_type__in=is_related,mentions

    Args:
        relation_type_in (None | str | Unset):
        source (None | str | Unset):
        target (None | str | Unset):
        order_by (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TraceList
    """

    return (
        await asyncio_detailed(
            client=client,
            relation_type_in=relation_type_in,
            source=source,
            target=target,
            order_by=order_by,
        )
    ).parsed
