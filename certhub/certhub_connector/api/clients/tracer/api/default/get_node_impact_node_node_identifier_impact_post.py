from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.node_impact_request import NodeImpactRequest
from ...models.node_impact_response import NodeImpactResponse
from ...types import Response


def _get_kwargs(
    node_identifier: str,
    *,
    body: NodeImpactRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/node/{node_identifier}/impact".format(
            node_identifier=quote(str(node_identifier), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | NodeImpactResponse | None:
    if response.status_code == 200:
        response_200 = NodeImpactResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | NodeImpactResponse]:
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
    body: NodeImpactRequest,
) -> Response[HTTPValidationError | NodeImpactResponse]:
    """Get Node Impact

     Retrieves the impact of a node on other nodes.

    Args:
        request: FastAPI request object containing metadata
        node_identifier: The full node identifier (type:id:version)
        impact_request: The impact request parameters
    Returns:
        NodeImpactResponse: The impact response

    Args:
        node_identifier (str):
        body (NodeImpactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NodeImpactResponse]
    """

    kwargs = _get_kwargs(
        node_identifier=node_identifier,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: NodeImpactRequest,
) -> HTTPValidationError | NodeImpactResponse | None:
    """Get Node Impact

     Retrieves the impact of a node on other nodes.

    Args:
        request: FastAPI request object containing metadata
        node_identifier: The full node identifier (type:id:version)
        impact_request: The impact request parameters
    Returns:
        NodeImpactResponse: The impact response

    Args:
        node_identifier (str):
        body (NodeImpactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NodeImpactResponse
    """

    return sync_detailed(
        node_identifier=node_identifier,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    node_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: NodeImpactRequest,
) -> Response[HTTPValidationError | NodeImpactResponse]:
    """Get Node Impact

     Retrieves the impact of a node on other nodes.

    Args:
        request: FastAPI request object containing metadata
        node_identifier: The full node identifier (type:id:version)
        impact_request: The impact request parameters
    Returns:
        NodeImpactResponse: The impact response

    Args:
        node_identifier (str):
        body (NodeImpactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NodeImpactResponse]
    """

    kwargs = _get_kwargs(
        node_identifier=node_identifier,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: NodeImpactRequest,
) -> HTTPValidationError | NodeImpactResponse | None:
    """Get Node Impact

     Retrieves the impact of a node on other nodes.

    Args:
        request: FastAPI request object containing metadata
        node_identifier: The full node identifier (type:id:version)
        impact_request: The impact request parameters
    Returns:
        NodeImpactResponse: The impact response

    Args:
        node_identifier (str):
        body (NodeImpactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NodeImpactResponse
    """

    return (
        await asyncio_detailed(
            node_identifier=node_identifier,
            client=client,
            body=body,
        )
    ).parsed
