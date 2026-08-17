from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_library_mode import DeleteLibraryMode
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    library_id: str,
    *,
    delete_mode: DeleteLibraryMode | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_delete_mode: str | Unset = UNSET
    if not isinstance(delete_mode, Unset):
        json_delete_mode = delete_mode.value

    params["delete_mode"] = json_delete_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/ku-schema-libraries/{library_id}".format(
            library_id=quote(str(library_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
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
    delete_mode: DeleteLibraryMode | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Delete Library

     Delete a KU Schema Library

    Args:
        library_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        delete_mode (DeleteLibraryMode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        delete_mode=delete_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_mode: DeleteLibraryMode | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Delete Library

     Delete a KU Schema Library

    Args:
        library_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        delete_mode (DeleteLibraryMode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        library_id=library_id,
        client=client,
        delete_mode=delete_mode,
    ).parsed


async def asyncio_detailed(
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_mode: DeleteLibraryMode | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Delete Library

     Delete a KU Schema Library

    Args:
        library_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        delete_mode (DeleteLibraryMode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        delete_mode=delete_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
    delete_mode: DeleteLibraryMode | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Delete Library

     Delete a KU Schema Library

    Args:
        library_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        delete_mode (DeleteLibraryMode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            library_id=library_id,
            client=client,
            delete_mode=delete_mode,
        )
    ).parsed
