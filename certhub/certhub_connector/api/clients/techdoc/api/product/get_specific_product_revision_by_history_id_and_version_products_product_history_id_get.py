from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.full_product_view import FullProductView
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_history_id: str,
    *,
    version: str | Unset = UNSET,
    combine_related_product_families_kus: bool | Unset = False,
    latest_approved: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["version"] = version

    params["combine_related_product_families_kus"] = (
        combine_related_product_families_kus
    )

    params["latest_approved"] = latest_approved

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/products/{product_history_id}".format(
            product_history_id=quote(str(product_history_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FullProductView | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FullProductView.from_dict(response.json())

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
) -> Response[Any | FullProductView | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    combine_related_product_families_kus: bool | Unset = False,
    latest_approved: bool | Unset = False,
) -> Response[Any | FullProductView | HTTPValidationError]:
    """Get product revision by history ID and version

     Returns a specific product revision or the latest one if no version is specified.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        combine_related_product_families_kus (bool | Unset): Whether to include knowledge units
            from related product families Default: False.
        latest_approved (bool | Unset): Whether to return the latest approved revision of the
            product (if available), otherwise returns the latest revision. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FullProductView | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
        version=version,
        combine_related_product_families_kus=combine_related_product_families_kus,
        latest_approved=latest_approved,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    combine_related_product_families_kus: bool | Unset = False,
    latest_approved: bool | Unset = False,
) -> Any | FullProductView | HTTPValidationError | None:
    """Get product revision by history ID and version

     Returns a specific product revision or the latest one if no version is specified.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        combine_related_product_families_kus (bool | Unset): Whether to include knowledge units
            from related product families Default: False.
        latest_approved (bool | Unset): Whether to return the latest approved revision of the
            product (if available), otherwise returns the latest revision. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FullProductView | HTTPValidationError
    """

    return sync_detailed(
        product_history_id=product_history_id,
        client=client,
        version=version,
        combine_related_product_families_kus=combine_related_product_families_kus,
        latest_approved=latest_approved,
    ).parsed


async def asyncio_detailed(
    product_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    combine_related_product_families_kus: bool | Unset = False,
    latest_approved: bool | Unset = False,
) -> Response[Any | FullProductView | HTTPValidationError]:
    """Get product revision by history ID and version

     Returns a specific product revision or the latest one if no version is specified.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        combine_related_product_families_kus (bool | Unset): Whether to include knowledge units
            from related product families Default: False.
        latest_approved (bool | Unset): Whether to return the latest approved revision of the
            product (if available), otherwise returns the latest revision. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FullProductView | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
        version=version,
        combine_related_product_families_kus=combine_related_product_families_kus,
        latest_approved=latest_approved,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    combine_related_product_families_kus: bool | Unset = False,
    latest_approved: bool | Unset = False,
) -> Any | FullProductView | HTTPValidationError | None:
    """Get product revision by history ID and version

     Returns a specific product revision or the latest one if no version is specified.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.
        combine_related_product_families_kus (bool | Unset): Whether to include knowledge units
            from related product families Default: False.
        latest_approved (bool | Unset): Whether to return the latest approved revision of the
            product (if available), otherwise returns the latest revision. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FullProductView | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            product_history_id=product_history_id,
            client=client,
            version=version,
            combine_related_product_families_kus=combine_related_product_families_kus,
            latest_approved=latest_approved,
        )
    ).parsed
