from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_retrieve_request import BatchRetrieveRequest
from ...models.batch_retrieve_response import BatchRetrieveResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: BatchRetrieveRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/traces/batch/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BatchRetrieveResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BatchRetrieveResponse.from_dict(response.json())

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
) -> Response[BatchRetrieveResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchRetrieveRequest,
) -> Response[BatchRetrieveResponse | HTTPValidationError]:
    """Batch Retrieve Traces

     Retrieve traces for multiple nodes in a single request.
    Each node's traces are retrieved independently and returned in a dictionary
    keyed by the node identifier.

    Nodes are processed concurrently. Downstream fan-out is rate-limited by
    the module-level semaphore in NodeDataService.bulk_resolve, so parallel
    processing here does not multiply the upstream load on QMS / TechDoc.

    Args:
        body (BatchRetrieveRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchRetrieveResponse | HTTPValidationError]
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
    body: BatchRetrieveRequest,
) -> BatchRetrieveResponse | HTTPValidationError | None:
    """Batch Retrieve Traces

     Retrieve traces for multiple nodes in a single request.
    Each node's traces are retrieved independently and returned in a dictionary
    keyed by the node identifier.

    Nodes are processed concurrently. Downstream fan-out is rate-limited by
    the module-level semaphore in NodeDataService.bulk_resolve, so parallel
    processing here does not multiply the upstream load on QMS / TechDoc.

    Args:
        body (BatchRetrieveRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchRetrieveResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchRetrieveRequest,
) -> Response[BatchRetrieveResponse | HTTPValidationError]:
    """Batch Retrieve Traces

     Retrieve traces for multiple nodes in a single request.
    Each node's traces are retrieved independently and returned in a dictionary
    keyed by the node identifier.

    Nodes are processed concurrently. Downstream fan-out is rate-limited by
    the module-level semaphore in NodeDataService.bulk_resolve, so parallel
    processing here does not multiply the upstream load on QMS / TechDoc.

    Args:
        body (BatchRetrieveRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchRetrieveResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BatchRetrieveRequest,
) -> BatchRetrieveResponse | HTTPValidationError | None:
    """Batch Retrieve Traces

     Retrieve traces for multiple nodes in a single request.
    Each node's traces are retrieved independently and returned in a dictionary
    keyed by the node identifier.

    Nodes are processed concurrently. Downstream fan-out is rate-limited by
    the module-level semaphore in NodeDataService.bulk_resolve, so parallel
    processing here does not multiply the upstream load on QMS / TechDoc.

    Args:
        body (BatchRetrieveRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchRetrieveResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
