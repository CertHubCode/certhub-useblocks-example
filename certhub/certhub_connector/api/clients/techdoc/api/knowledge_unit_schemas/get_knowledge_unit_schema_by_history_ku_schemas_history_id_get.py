from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.schema_with_libraries import SchemaWithLibraries
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    *,
    version: str | Unset = UNSET,
    latest_approved: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["version"] = version

    params["latest_approved"] = latest_approved

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ku-schemas/{history_id}".format(
            history_id=quote(str(history_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SchemaWithLibraries | None:
    if response.status_code == 200:
        response_200 = SchemaWithLibraries.from_dict(response.json())

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
) -> Response[HTTPValidationError | SchemaWithLibraries]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    latest_approved: bool | Unset = False,
) -> Response[HTTPValidationError | SchemaWithLibraries]:
    """Get Knowledge Unit Schema by History ID

     Get a knowledge unit schema by history ID with optional version specification.

    - **history_id**: The knowledge unit schema history ID
    - **version**: Optional version string in format 'major.minor' (e.g., '1.2'). If not provided,
    returns the latest revision.

    Args:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        latest_approved (bool | Unset): Whether to return the latest approved revision of the
            knowledge unit schema Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SchemaWithLibraries]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        version=version,
        latest_approved=latest_approved,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    latest_approved: bool | Unset = False,
) -> HTTPValidationError | SchemaWithLibraries | None:
    """Get Knowledge Unit Schema by History ID

     Get a knowledge unit schema by history ID with optional version specification.

    - **history_id**: The knowledge unit schema history ID
    - **version**: Optional version string in format 'major.minor' (e.g., '1.2'). If not provided,
    returns the latest revision.

    Args:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        latest_approved (bool | Unset): Whether to return the latest approved revision of the
            knowledge unit schema Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SchemaWithLibraries
    """

    return sync_detailed(
        history_id=history_id,
        client=client,
        version=version,
        latest_approved=latest_approved,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    latest_approved: bool | Unset = False,
) -> Response[HTTPValidationError | SchemaWithLibraries]:
    """Get Knowledge Unit Schema by History ID

     Get a knowledge unit schema by history ID with optional version specification.

    - **history_id**: The knowledge unit schema history ID
    - **version**: Optional version string in format 'major.minor' (e.g., '1.2'). If not provided,
    returns the latest revision.

    Args:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        latest_approved (bool | Unset): Whether to return the latest approved revision of the
            knowledge unit schema Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SchemaWithLibraries]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        version=version,
        latest_approved=latest_approved,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    latest_approved: bool | Unset = False,
) -> HTTPValidationError | SchemaWithLibraries | None:
    """Get Knowledge Unit Schema by History ID

     Get a knowledge unit schema by history ID with optional version specification.

    - **history_id**: The knowledge unit schema history ID
    - **version**: Optional version string in format 'major.minor' (e.g., '1.2'). If not provided,
    returns the latest revision.

    Args:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        latest_approved (bool | Unset): Whether to return the latest approved revision of the
            knowledge unit schema Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SchemaWithLibraries
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            version=version,
            latest_approved=latest_approved,
        )
    ).parsed
