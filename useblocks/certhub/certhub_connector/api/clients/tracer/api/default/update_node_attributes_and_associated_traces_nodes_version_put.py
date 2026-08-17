from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.node import Node
from ...models.node_attributes_update import NodeAttributesUpdate
from ...types import Response


def _get_kwargs(
    *,
    body: NodeAttributesUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/nodes/version",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Node | None:
    if response.status_code == 200:
        response_200 = Node.from_dict(response.json())

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
) -> Response[HTTPValidationError | Node]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NodeAttributesUpdate,
) -> Response[HTTPValidationError | Node]:
    """Update Node Attributes And Associated Traces

     Updates a node's version either in-place or by creating a new version with duplicated relationships.

    Args:
        request: FastAPI request object containing metadata
        update: The version update parameters

    Returns:
        Node: The updated/new node

    Raises:
        HTTPException: If node not found or update fails

    Args:
        body (NodeAttributesUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Node]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: NodeAttributesUpdate,
) -> HTTPValidationError | Node | None:
    """Update Node Attributes And Associated Traces

     Updates a node's version either in-place or by creating a new version with duplicated relationships.

    Args:
        request: FastAPI request object containing metadata
        update: The version update parameters

    Returns:
        Node: The updated/new node

    Raises:
        HTTPException: If node not found or update fails

    Args:
        body (NodeAttributesUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Node
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NodeAttributesUpdate,
) -> Response[HTTPValidationError | Node]:
    """Update Node Attributes And Associated Traces

     Updates a node's version either in-place or by creating a new version with duplicated relationships.

    Args:
        request: FastAPI request object containing metadata
        update: The version update parameters

    Returns:
        Node: The updated/new node

    Raises:
        HTTPException: If node not found or update fails

    Args:
        body (NodeAttributesUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Node]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NodeAttributesUpdate,
) -> HTTPValidationError | Node | None:
    """Update Node Attributes And Associated Traces

     Updates a node's version either in-place or by creating a new version with duplicated relationships.

    Args:
        request: FastAPI request object containing metadata
        update: The version update parameters

    Returns:
        Node: The updated/new node

    Raises:
        HTTPException: If node not found or update fails

    Args:
        body (NodeAttributesUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Node
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
