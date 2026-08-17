from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edge import Edge
from ...models.edge_update import EdgeUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    edge_id: str,
    *,
    body: EdgeUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/trace/{edge_id}".format(
            edge_id=quote(str(edge_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Edge | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = Edge.from_dict(response.json())

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
) -> Response[Edge | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    edge_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EdgeUpdate,
) -> Response[Edge | HTTPValidationError]:
    """Update Edge

     Update an existing edge's source or target.

    Args:
        edge_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (EdgeUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Edge | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        edge_id=edge_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    edge_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EdgeUpdate,
) -> Edge | HTTPValidationError | None:
    """Update Edge

     Update an existing edge's source or target.

    Args:
        edge_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (EdgeUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Edge | HTTPValidationError
    """

    return sync_detailed(
        edge_id=edge_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    edge_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EdgeUpdate,
) -> Response[Edge | HTTPValidationError]:
    """Update Edge

     Update an existing edge's source or target.

    Args:
        edge_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (EdgeUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Edge | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        edge_id=edge_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    edge_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EdgeUpdate,
) -> Edge | HTTPValidationError | None:
    """Update Edge

     Update an existing edge's source or target.

    Args:
        edge_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (EdgeUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Edge | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            edge_id=edge_id,
            client=client,
            body=body,
        )
    ).parsed
