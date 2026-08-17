from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.full_library_response import FullLibraryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    latest_approved_schemas_only: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["latestApprovedSchemasOnly"] = latest_approved_schemas_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ku-schema-libraries/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[FullLibraryResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FullLibraryResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[FullLibraryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    latest_approved_schemas_only: bool | Unset = False,
) -> Response[HTTPValidationError | list[FullLibraryResponse]]:
    """Get Libraries

     Get all KU Schema Libraries

    Args:
        latest_approved_schemas_only (bool | Unset): Return only latest approved schema revisions
            Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FullLibraryResponse]]
    """

    kwargs = _get_kwargs(
        latest_approved_schemas_only=latest_approved_schemas_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    latest_approved_schemas_only: bool | Unset = False,
) -> HTTPValidationError | list[FullLibraryResponse] | None:
    """Get Libraries

     Get all KU Schema Libraries

    Args:
        latest_approved_schemas_only (bool | Unset): Return only latest approved schema revisions
            Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FullLibraryResponse]
    """

    return sync_detailed(
        client=client,
        latest_approved_schemas_only=latest_approved_schemas_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    latest_approved_schemas_only: bool | Unset = False,
) -> Response[HTTPValidationError | list[FullLibraryResponse]]:
    """Get Libraries

     Get all KU Schema Libraries

    Args:
        latest_approved_schemas_only (bool | Unset): Return only latest approved schema revisions
            Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FullLibraryResponse]]
    """

    kwargs = _get_kwargs(
        latest_approved_schemas_only=latest_approved_schemas_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    latest_approved_schemas_only: bool | Unset = False,
) -> HTTPValidationError | list[FullLibraryResponse] | None:
    """Get Libraries

     Get all KU Schema Libraries

    Args:
        latest_approved_schemas_only (bool | Unset): Return only latest approved schema revisions
            Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FullLibraryResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            latest_approved_schemas_only=latest_approved_schemas_only,
        )
    ).parsed
