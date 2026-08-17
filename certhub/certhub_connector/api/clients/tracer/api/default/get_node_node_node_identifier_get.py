from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.node import Node
from ...types import Response


def _get_kwargs(
    node_identifier: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/node/{node_identifier}".format(
            node_identifier=quote(str(node_identifier), safe=""),
        ),
    }

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
    node_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | Node]:
    """Get Node

     Retrieves a single node by its identifier.

    Args:
        request: FastAPI request object containing metadata
        node_identifier: The full node identifier (type:id:version)

    Returns:
        Node: The requested node

    Raises:
        HTTPException: If node not found or retrieval fails

    Args:
        node_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Node]
    """

    kwargs = _get_kwargs(
        node_identifier=node_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | Node | None:
    """Get Node

     Retrieves a single node by its identifier.

    Args:
        request: FastAPI request object containing metadata
        node_identifier: The full node identifier (type:id:version)

    Returns:
        Node: The requested node

    Raises:
        HTTPException: If node not found or retrieval fails

    Args:
        node_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Node
    """

    return sync_detailed(
        node_identifier=node_identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    node_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | Node]:
    """Get Node

     Retrieves a single node by its identifier.

    Args:
        request: FastAPI request object containing metadata
        node_identifier: The full node identifier (type:id:version)

    Returns:
        Node: The requested node

    Raises:
        HTTPException: If node not found or retrieval fails

    Args:
        node_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Node]
    """

    kwargs = _get_kwargs(
        node_identifier=node_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_identifier: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | Node | None:
    """Get Node

     Retrieves a single node by its identifier.

    Args:
        request: FastAPI request object containing metadata
        node_identifier: The full node identifier (type:id:version)

    Returns:
        Node: The requested node

    Raises:
        HTTPException: If node not found or retrieval fails

    Args:
        node_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Node
    """

    return (
        await asyncio_detailed(
            node_identifier=node_identifier,
            client=client,
        )
    ).parsed
