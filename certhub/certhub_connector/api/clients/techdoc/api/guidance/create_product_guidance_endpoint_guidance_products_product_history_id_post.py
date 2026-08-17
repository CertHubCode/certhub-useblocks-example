from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.product_guidance_response import ProductGuidanceResponse
from ...types import Response


def _get_kwargs(
    product_history_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/guidance/products/{product_history_id}".format(
            product_history_id=quote(str(product_history_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | ProductGuidanceResponse | None:
    if response.status_code == 201:
        response_201 = ProductGuidanceResponse.from_dict(response.json())

        return response_201

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
) -> Response[Any | HTTPValidationError | ProductGuidanceResponse]:
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
) -> Response[Any | HTTPValidationError | ProductGuidanceResponse]:
    """Create Product Guidance Endpoint

     Initialise guidance for a product. Returns 409 if it already exists.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ProductGuidanceResponse]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_history_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | ProductGuidanceResponse | None:
    """Create Product Guidance Endpoint

     Initialise guidance for a product. Returns 409 if it already exists.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ProductGuidanceResponse
    """

    return sync_detailed(
        product_history_id=product_history_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_history_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError | ProductGuidanceResponse]:
    """Create Product Guidance Endpoint

     Initialise guidance for a product. Returns 409 if it already exists.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ProductGuidanceResponse]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_history_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | ProductGuidanceResponse | None:
    """Create Product Guidance Endpoint

     Initialise guidance for a product. Returns 409 if it already exists.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ProductGuidanceResponse
    """

    return (
        await asyncio_detailed(
            product_history_id=product_history_id,
            client=client,
        )
    ).parsed
