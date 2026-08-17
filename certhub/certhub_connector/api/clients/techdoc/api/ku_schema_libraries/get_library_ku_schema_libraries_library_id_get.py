from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.full_library_response import FullLibraryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    library_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ku-schema-libraries/{library_id}".format(
            library_id=quote(str(library_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FullLibraryResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FullLibraryResponse.from_dict(response.json())

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
) -> Response[FullLibraryResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FullLibraryResponse | HTTPValidationError]:
    """Get Library

     Get a specific KU Schema Library

    Args:
        library_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FullLibraryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> FullLibraryResponse | HTTPValidationError | None:
    """Get Library

     Get a specific KU Schema Library

    Args:
        library_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FullLibraryResponse | HTTPValidationError
    """

    return sync_detailed(
        library_id=library_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FullLibraryResponse | HTTPValidationError]:
    """Get Library

     Get a specific KU Schema Library

    Args:
        library_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FullLibraryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> FullLibraryResponse | HTTPValidationError | None:
    """Get Library

     Get a specific KU Schema Library

    Args:
        library_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FullLibraryResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            library_id=library_id,
            client=client,
        )
    ).parsed
