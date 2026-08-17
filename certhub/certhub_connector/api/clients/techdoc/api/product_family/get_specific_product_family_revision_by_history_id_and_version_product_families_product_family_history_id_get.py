from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.full_product_family_view import FullProductFamilyView
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_family_history_id: str,
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
        "url": "/product-families/{product_family_history_id}".format(
            product_family_history_id=quote(str(product_family_history_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FullProductFamilyView | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FullProductFamilyView.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FullProductFamilyView | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_family_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    latest_approved: bool | Unset = False,
) -> Response[Any | FullProductFamilyView | HTTPValidationError]:
    """Get product family revision by history ID and version

     Returns a specific product family revision or the latest one if no version is specified.

    Args:
        product_family_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        latest_approved (bool | Unset): Whether to return the latest revision of the product
            family Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FullProductFamilyView | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        product_family_history_id=product_family_history_id,
        version=version,
        latest_approved=latest_approved,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_family_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    latest_approved: bool | Unset = False,
) -> Any | FullProductFamilyView | HTTPValidationError | None:
    """Get product family revision by history ID and version

     Returns a specific product family revision or the latest one if no version is specified.

    Args:
        product_family_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        latest_approved (bool | Unset): Whether to return the latest revision of the product
            family Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FullProductFamilyView | HTTPValidationError
    """

    return sync_detailed(
        product_family_history_id=product_family_history_id,
        client=client,
        version=version,
        latest_approved=latest_approved,
    ).parsed


async def asyncio_detailed(
    product_family_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    latest_approved: bool | Unset = False,
) -> Response[Any | FullProductFamilyView | HTTPValidationError]:
    """Get product family revision by history ID and version

     Returns a specific product family revision or the latest one if no version is specified.

    Args:
        product_family_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        latest_approved (bool | Unset): Whether to return the latest revision of the product
            family Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FullProductFamilyView | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        product_family_history_id=product_family_history_id,
        version=version,
        latest_approved=latest_approved,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_family_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    latest_approved: bool | Unset = False,
) -> Any | FullProductFamilyView | HTTPValidationError | None:
    """Get product family revision by history ID and version

     Returns a specific product family revision or the latest one if no version is specified.

    Args:
        product_family_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        latest_approved (bool | Unset): Whether to return the latest revision of the product
            family Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FullProductFamilyView | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            product_family_history_id=product_family_history_id,
            client=client,
            version=version,
            latest_approved=latest_approved,
        )
    ).parsed
