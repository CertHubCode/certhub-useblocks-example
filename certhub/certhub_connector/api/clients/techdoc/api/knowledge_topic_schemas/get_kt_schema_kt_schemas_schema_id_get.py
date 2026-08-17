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
    schema_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/kt-schemas/{schema_id}".format(
            schema_id=quote(str(schema_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | KnowledgeTopicSchemaDetailResponse | None:
    if response.status_code == 200:
        response_200 = KnowledgeTopicSchemaDetailResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | KnowledgeTopicSchemaDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schema_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | KnowledgeTopicSchemaDetailResponse]:
    """Get Kt Schema

     Retrieve a specific knowledge topic schema

    Args:
        schema_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeTopicSchemaDetailResponse]
    """

    kwargs = _get_kwargs(
        schema_id=schema_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schema_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | KnowledgeTopicSchemaDetailResponse | None:
    """Get Kt Schema

     Retrieve a specific knowledge topic schema

    Args:
        schema_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeTopicSchemaDetailResponse
    """

    return sync_detailed(
        schema_id=schema_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    schema_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | KnowledgeTopicSchemaDetailResponse]:
    """Get Kt Schema

     Retrieve a specific knowledge topic schema

    Args:
        schema_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeTopicSchemaDetailResponse]
    """

    kwargs = _get_kwargs(
        schema_id=schema_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schema_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | KnowledgeTopicSchemaDetailResponse | None:
    """Get Kt Schema

     Retrieve a specific knowledge topic schema

    Args:
        schema_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeTopicSchemaDetailResponse
    """

    return (
        await asyncio_detailed(
            schema_id=schema_id,
            client=client,
        )
    ).parsed
