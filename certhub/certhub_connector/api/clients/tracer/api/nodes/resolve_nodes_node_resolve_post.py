from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.resolve_nodes_node_resolve_post_response_resolve_nodes_node_resolve_post import (
    ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost,
)
from ...models.resolve_nodes_request import ResolveNodesRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ResolveNodesRequest,
    include_latest_approved_and_latest_available: bool | Unset = True,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["include_latest_approved_and_latest_available"] = (
        include_latest_approved_and_latest_available
    )

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/node/resolve",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost
    | None
):
    if response.status_code == 200:
        response_200 = (
            ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost.from_dict(
                response.json()
            )
        )

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
) -> Response[
    HTTPValidationError | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveNodesRequest,
    include_latest_approved_and_latest_available: bool | Unset = True,
) -> Response[
    HTTPValidationError | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost
]:
    """Resolve Nodes

    Args:
        include_latest_approved_and_latest_available (bool | Unset): When with_linked_entities is
            True, collapse multi-version linked targets to latest major/approved and latest
            fractional/available per entity. Default: True.
        body (ResolveNodesRequest): Request body for POST /node/resolve (node_identifiers may be
            empty).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost]
    """

    kwargs = _get_kwargs(
        body=body,
        include_latest_approved_and_latest_available=include_latest_approved_and_latest_available,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveNodesRequest,
    include_latest_approved_and_latest_available: bool | Unset = True,
) -> (
    HTTPValidationError
    | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost
    | None
):
    """Resolve Nodes

    Args:
        include_latest_approved_and_latest_available (bool | Unset): When with_linked_entities is
            True, collapse multi-version linked targets to latest major/approved and latest
            fractional/available per entity. Default: True.
        body (ResolveNodesRequest): Request body for POST /node/resolve (node_identifiers may be
            empty).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost
    """

    return sync_detailed(
        client=client,
        body=body,
        include_latest_approved_and_latest_available=include_latest_approved_and_latest_available,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveNodesRequest,
    include_latest_approved_and_latest_available: bool | Unset = True,
) -> Response[
    HTTPValidationError | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost
]:
    """Resolve Nodes

    Args:
        include_latest_approved_and_latest_available (bool | Unset): When with_linked_entities is
            True, collapse multi-version linked targets to latest major/approved and latest
            fractional/available per entity. Default: True.
        body (ResolveNodesRequest): Request body for POST /node/resolve (node_identifiers may be
            empty).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost]
    """

    kwargs = _get_kwargs(
        body=body,
        include_latest_approved_and_latest_available=include_latest_approved_and_latest_available,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ResolveNodesRequest,
    include_latest_approved_and_latest_available: bool | Unset = True,
) -> (
    HTTPValidationError
    | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost
    | None
):
    """Resolve Nodes

    Args:
        include_latest_approved_and_latest_available (bool | Unset): When with_linked_entities is
            True, collapse multi-version linked targets to latest major/approved and latest
            fractional/available per entity. Default: True.
        body (ResolveNodesRequest): Request body for POST /node/resolve (node_identifiers may be
            empty).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ResolveNodesNodeResolvePostResponseResolveNodesNodeResolvePost
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            include_latest_approved_and_latest_available=include_latest_approved_and_latest_available,
        )
    ).parsed
