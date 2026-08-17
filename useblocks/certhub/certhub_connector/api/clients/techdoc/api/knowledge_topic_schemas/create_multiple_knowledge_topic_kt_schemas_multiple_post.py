from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_knowledge_topic_schemas_from_existing import (
    CreateKnowledgeTopicSchemasFromExisting,
)
from ...models.create_knowledge_topic_schemas_response import (
    CreateKnowledgeTopicSchemasResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: CreateKnowledgeTopicSchemasFromExisting,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/kt-schemas/multiple",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateKnowledgeTopicSchemasResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = CreateKnowledgeTopicSchemasResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateKnowledgeTopicSchemasResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeTopicSchemasFromExisting,
) -> Response[CreateKnowledgeTopicSchemasResponse | HTTPValidationError]:
    """Create Multiple Knowledge Topic

     Insert multiple knowledge topic schemas from existing KT schemas or KTs.
    Returns created schemas and any skipped knowledge topics.

    Args:
        body (CreateKnowledgeTopicSchemasFromExisting): Model for creating a KT from existing KT
            schema or KT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateKnowledgeTopicSchemasResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeTopicSchemasFromExisting,
) -> CreateKnowledgeTopicSchemasResponse | HTTPValidationError | None:
    """Create Multiple Knowledge Topic

     Insert multiple knowledge topic schemas from existing KT schemas or KTs.
    Returns created schemas and any skipped knowledge topics.

    Args:
        body (CreateKnowledgeTopicSchemasFromExisting): Model for creating a KT from existing KT
            schema or KT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateKnowledgeTopicSchemasResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeTopicSchemasFromExisting,
) -> Response[CreateKnowledgeTopicSchemasResponse | HTTPValidationError]:
    """Create Multiple Knowledge Topic

     Insert multiple knowledge topic schemas from existing KT schemas or KTs.
    Returns created schemas and any skipped knowledge topics.

    Args:
        body (CreateKnowledgeTopicSchemasFromExisting): Model for creating a KT from existing KT
            schema or KT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateKnowledgeTopicSchemasResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeTopicSchemasFromExisting,
) -> CreateKnowledgeTopicSchemasResponse | HTTPValidationError | None:
    """Create Multiple Knowledge Topic

     Insert multiple knowledge topic schemas from existing KT schemas or KTs.
    Returns created schemas and any skipped knowledge topics.

    Args:
        body (CreateKnowledgeTopicSchemasFromExisting): Model for creating a KT from existing KT
            schema or KT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateKnowledgeTopicSchemasResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
