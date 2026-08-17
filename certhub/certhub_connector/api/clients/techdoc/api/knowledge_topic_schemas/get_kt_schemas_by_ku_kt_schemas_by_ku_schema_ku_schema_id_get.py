from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_topic_schema_detail_response import (
    KnowledgeTopicSchemaDetailResponse,
)
from ...types import Response


def _get_kwargs(
    ku_schema_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/kt-schemas/by-ku-schema/{ku_schema_id}".format(
            ku_schema_id=quote(str(ku_schema_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KnowledgeTopicSchemaDetailResponse.from_dict(
                response_200_item_data
            )

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
) -> Response[HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ku_schema_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse]]:
    """Get Kt Schemas By Ku

     Retrieve all topic schemas for a specific KU schema

    Args:
        ku_schema_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse]]
    """

    kwargs = _get_kwargs(
        ku_schema_id=ku_schema_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ku_schema_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse] | None:
    """Get Kt Schemas By Ku

     Retrieve all topic schemas for a specific KU schema

    Args:
        ku_schema_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse]
    """

    return sync_detailed(
        ku_schema_id=ku_schema_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ku_schema_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse]]:
    """Get Kt Schemas By Ku

     Retrieve all topic schemas for a specific KU schema

    Args:
        ku_schema_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse]]
    """

    kwargs = _get_kwargs(
        ku_schema_id=ku_schema_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ku_schema_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse] | None:
    """Get Kt Schemas By Ku

     Retrieve all topic schemas for a specific KU schema

    Args:
        ku_schema_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[KnowledgeTopicSchemaDetailResponse]
    """

    return (
        await asyncio_detailed(
            ku_schema_id=ku_schema_id,
            client=client,
        )
    ).parsed
