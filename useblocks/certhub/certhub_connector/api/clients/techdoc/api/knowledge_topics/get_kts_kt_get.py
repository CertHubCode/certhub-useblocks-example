from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_topic import KnowledgeTopic
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    product_history_id: str | Unset = UNSET,
    knowledge_unit_history_id: str | Unset = UNSET,
    knowledge_unit_version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["product_history_id"] = product_history_id

    params["knowledge_unit_history_id"] = knowledge_unit_history_id

    params["knowledge_unit_version"] = knowledge_unit_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/kt/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[KnowledgeTopic] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KnowledgeTopic.from_dict(response_200_item_data)

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
) -> Response[Any | HTTPValidationError | list[KnowledgeTopic]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_history_id: str | Unset = UNSET,
    knowledge_unit_history_id: str | Unset = UNSET,
    knowledge_unit_version: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[KnowledgeTopic]]:
    """Get Kts

     Retrieve knowledge topics of the latest revision of a product.
    Alternatively, provide both knowledge_unit_history_id and knowledge_unit_version
    to retrieve knowledge topics for a specific knowledge unit revision.
    Warning: Retrieving all knowledge topics is possible but not recommended. Takes 1 minute for 3500
    knowledge topics as a reference.
    Use the /all endpoint instead.

    Args:
        product_history_id (str | Unset): Filter by related product ID Example:
            5eb7cf5a86d9755df3a6c593.
        knowledge_unit_history_id (str | Unset): Knowledge unit history ID; must be provided with
            knowledge_unit_version Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_version (str | Unset): Knowledge unit version string, e.g. "1.0"; must be
            provided with knowledge_unit_history_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeTopic]]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
        knowledge_unit_history_id=knowledge_unit_history_id,
        knowledge_unit_version=knowledge_unit_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product_history_id: str | Unset = UNSET,
    knowledge_unit_history_id: str | Unset = UNSET,
    knowledge_unit_version: str | Unset = UNSET,
) -> Any | HTTPValidationError | list[KnowledgeTopic] | None:
    """Get Kts

     Retrieve knowledge topics of the latest revision of a product.
    Alternatively, provide both knowledge_unit_history_id and knowledge_unit_version
    to retrieve knowledge topics for a specific knowledge unit revision.
    Warning: Retrieving all knowledge topics is possible but not recommended. Takes 1 minute for 3500
    knowledge topics as a reference.
    Use the /all endpoint instead.

    Args:
        product_history_id (str | Unset): Filter by related product ID Example:
            5eb7cf5a86d9755df3a6c593.
        knowledge_unit_history_id (str | Unset): Knowledge unit history ID; must be provided with
            knowledge_unit_version Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_version (str | Unset): Knowledge unit version string, e.g. "1.0"; must be
            provided with knowledge_unit_history_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeTopic]
    """

    return sync_detailed(
        client=client,
        product_history_id=product_history_id,
        knowledge_unit_history_id=knowledge_unit_history_id,
        knowledge_unit_version=knowledge_unit_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_history_id: str | Unset = UNSET,
    knowledge_unit_history_id: str | Unset = UNSET,
    knowledge_unit_version: str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[KnowledgeTopic]]:
    """Get Kts

     Retrieve knowledge topics of the latest revision of a product.
    Alternatively, provide both knowledge_unit_history_id and knowledge_unit_version
    to retrieve knowledge topics for a specific knowledge unit revision.
    Warning: Retrieving all knowledge topics is possible but not recommended. Takes 1 minute for 3500
    knowledge topics as a reference.
    Use the /all endpoint instead.

    Args:
        product_history_id (str | Unset): Filter by related product ID Example:
            5eb7cf5a86d9755df3a6c593.
        knowledge_unit_history_id (str | Unset): Knowledge unit history ID; must be provided with
            knowledge_unit_version Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_version (str | Unset): Knowledge unit version string, e.g. "1.0"; must be
            provided with knowledge_unit_history_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeTopic]]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
        knowledge_unit_history_id=knowledge_unit_history_id,
        knowledge_unit_version=knowledge_unit_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product_history_id: str | Unset = UNSET,
    knowledge_unit_history_id: str | Unset = UNSET,
    knowledge_unit_version: str | Unset = UNSET,
) -> Any | HTTPValidationError | list[KnowledgeTopic] | None:
    """Get Kts

     Retrieve knowledge topics of the latest revision of a product.
    Alternatively, provide both knowledge_unit_history_id and knowledge_unit_version
    to retrieve knowledge topics for a specific knowledge unit revision.
    Warning: Retrieving all knowledge topics is possible but not recommended. Takes 1 minute for 3500
    knowledge topics as a reference.
    Use the /all endpoint instead.

    Args:
        product_history_id (str | Unset): Filter by related product ID Example:
            5eb7cf5a86d9755df3a6c593.
        knowledge_unit_history_id (str | Unset): Knowledge unit history ID; must be provided with
            knowledge_unit_version Example: 5eb7cf5a86d9755df3a6c593.
        knowledge_unit_version (str | Unset): Knowledge unit version string, e.g. "1.0"; must be
            provided with knowledge_unit_history_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeTopic]
    """

    return (
        await asyncio_detailed(
            client=client,
            product_history_id=product_history_id,
            knowledge_unit_history_id=knowledge_unit_history_id,
            knowledge_unit_version=knowledge_unit_version,
        )
    ).parsed
