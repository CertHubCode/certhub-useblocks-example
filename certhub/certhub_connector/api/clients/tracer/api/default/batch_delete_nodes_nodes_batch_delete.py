from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_node_delete_request import BatchNodeDeleteRequest
from ...models.batch_node_delete_response import BatchNodeDeleteResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: BatchNodeDeleteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/nodes/batch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BatchNodeDeleteResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BatchNodeDeleteResponse.from_dict(response.json())

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
) -> Response[BatchNodeDeleteResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchNodeDeleteRequest,
) -> Response[BatchNodeDeleteResponse | HTTPValidationError]:
    """Batch Delete Nodes

     Batch delete nodes by identifier and cascade to all connected edges.
    Nodes that don't exist are reported as failed, but don't prevent other deletions.

    Args:
        request: FastAPI request object containing metadata
        batch_request: Batch request containing list of node identifiers to delete

    Returns:
        BatchNodeDeleteResponse: Response containing results for each deletion

    Args:
        body (BatchNodeDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchNodeDeleteResponse | HTTPValidationError]
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
    body: BatchNodeDeleteRequest,
) -> BatchNodeDeleteResponse | HTTPValidationError | None:
    """Batch Delete Nodes

     Batch delete nodes by identifier and cascade to all connected edges.
    Nodes that don't exist are reported as failed, but don't prevent other deletions.

    Args:
        request: FastAPI request object containing metadata
        batch_request: Batch request containing list of node identifiers to delete

    Returns:
        BatchNodeDeleteResponse: Response containing results for each deletion

    Args:
        body (BatchNodeDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchNodeDeleteResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchNodeDeleteRequest,
) -> Response[BatchNodeDeleteResponse | HTTPValidationError]:
    """Batch Delete Nodes

     Batch delete nodes by identifier and cascade to all connected edges.
    Nodes that don't exist are reported as failed, but don't prevent other deletions.

    Args:
        request: FastAPI request object containing metadata
        batch_request: Batch request containing list of node identifiers to delete

    Returns:
        BatchNodeDeleteResponse: Response containing results for each deletion

    Args:
        body (BatchNodeDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchNodeDeleteResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BatchNodeDeleteRequest,
) -> BatchNodeDeleteResponse | HTTPValidationError | None:
    """Batch Delete Nodes

     Batch delete nodes by identifier and cascade to all connected edges.
    Nodes that don't exist are reported as failed, but don't prevent other deletions.

    Args:
        request: FastAPI request object containing metadata
        batch_request: Batch request containing list of node identifiers to delete

    Returns:
        BatchNodeDeleteResponse: Response containing results for each deletion

    Args:
        body (BatchNodeDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchNodeDeleteResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
