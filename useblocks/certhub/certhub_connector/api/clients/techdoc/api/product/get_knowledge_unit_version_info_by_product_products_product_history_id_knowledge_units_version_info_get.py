from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_unit_history_group import KnowledgeUnitHistoryGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_history_id: str,
    *,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/products/{product_history_id}/knowledge-units/version-info".format(
            product_history_id=quote(str(product_history_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KnowledgeUnitHistoryGroup.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup]]:
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
) -> Response[Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup]]:
    """Get knowledge unit version info by product history ID

     Returns version info for all knowledge units belonging to the product at the specified revision,
    including KUs from related product families.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup]]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
        version=version,
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
) -> Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup] | None:
    """Get knowledge unit version info by product history ID

     Returns version info for all knowledge units belonging to the product at the specified revision,
    including KUs from related product families.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup]
    """

    return sync_detailed(
        product_history_id=product_history_id,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    product_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup]]:
    """Get knowledge unit version info by product history ID

     Returns version info for all knowledge units belonging to the product at the specified revision,
    including KUs from related product families.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup]]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup] | None:
    """Get knowledge unit version info by product history ID

     Returns version info for all knowledge units belonging to the product at the specified revision,
    including KUs from related product families.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        version (str | Unset): Specific version to retrieve (e.g., '1.2'). If not provided,
            returns latest revision.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeUnitHistoryGroup]
    """

    return (
        await asyncio_detailed(
            product_history_id=product_history_id,
            client=client,
            version=version,
        )
    ).parsed
