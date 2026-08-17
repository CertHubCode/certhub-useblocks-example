from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_node_attributes_update_request import (
    BatchNodeAttributesUpdateRequest,
)
from ...models.batch_node_attributes_update_response import (
    BatchNodeAttributesUpdateResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: BatchNodeAttributesUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/nodes/version/batch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BatchNodeAttributesUpdateResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BatchNodeAttributesUpdateResponse.from_dict(response.json())

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
) -> Response[BatchNodeAttributesUpdateResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchNodeAttributesUpdateRequest,
) -> Response[BatchNodeAttributesUpdateResponse | HTTPValidationError]:
    """Batch Update Node Attributes And Associated Traces

     Batch updates node attributes and associated traces using vectorized reads and bulk writes.
    Processes multiple node updates in a single transaction for high performance.

    Args:
        request: FastAPI request object containing metadata
        batch_request: Batch request containing list of node attribute updates

    Returns:
        BatchNodeAttributesUpdateResponse: Response containing results for each update

    Raises:
        HTTPException: If validation fails or update fails

    Args:
        body (BatchNodeAttributesUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchNodeAttributesUpdateResponse | HTTPValidationError]
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
    body: BatchNodeAttributesUpdateRequest,
) -> BatchNodeAttributesUpdateResponse | HTTPValidationError | None:
    """Batch Update Node Attributes And Associated Traces

     Batch updates node attributes and associated traces using vectorized reads and bulk writes.
    Processes multiple node updates in a single transaction for high performance.

    Args:
        request: FastAPI request object containing metadata
        batch_request: Batch request containing list of node attribute updates

    Returns:
        BatchNodeAttributesUpdateResponse: Response containing results for each update

    Raises:
        HTTPException: If validation fails or update fails

    Args:
        body (BatchNodeAttributesUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchNodeAttributesUpdateResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchNodeAttributesUpdateRequest,
) -> Response[BatchNodeAttributesUpdateResponse | HTTPValidationError]:
    """Batch Update Node Attributes And Associated Traces

     Batch updates node attributes and associated traces using vectorized reads and bulk writes.
    Processes multiple node updates in a single transaction for high performance.

    Args:
        request: FastAPI request object containing metadata
        batch_request: Batch request containing list of node attribute updates

    Returns:
        BatchNodeAttributesUpdateResponse: Response containing results for each update

    Raises:
        HTTPException: If validation fails or update fails

    Args:
        body (BatchNodeAttributesUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchNodeAttributesUpdateResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BatchNodeAttributesUpdateRequest,
) -> BatchNodeAttributesUpdateResponse | HTTPValidationError | None:
    """Batch Update Node Attributes And Associated Traces

     Batch updates node attributes and associated traces using vectorized reads and bulk writes.
    Processes multiple node updates in a single transaction for high performance.

    Args:
        request: FastAPI request object containing metadata
        batch_request: Batch request containing list of node attribute updates

    Returns:
        BatchNodeAttributesUpdateResponse: Response containing results for each update

    Raises:
        HTTPException: If validation fails or update fails

    Args:
        body (BatchNodeAttributesUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchNodeAttributesUpdateResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
