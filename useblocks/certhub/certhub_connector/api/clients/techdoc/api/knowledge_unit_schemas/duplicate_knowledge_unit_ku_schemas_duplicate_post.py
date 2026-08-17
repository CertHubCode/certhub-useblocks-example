from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_knowledge_unit_schema_from_existing import (
    CreateKnowledgeUnitSchemaFromExisting,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_unit_schema import KnowledgeUnitSchema
from ...types import Response


def _get_kwargs(
    *,
    body: CreateKnowledgeUnitSchemaFromExisting,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ku-schemas/duplicate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | KnowledgeUnitSchema | None:
    if response.status_code == 201:
        response_201 = KnowledgeUnitSchema.from_dict(response.json())

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
) -> Response[HTTPValidationError | KnowledgeUnitSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeUnitSchemaFromExisting,
) -> Response[HTTPValidationError | KnowledgeUnitSchema]:
    """Duplicate Knowledge Unit

     Duplicate a knowledge unit schema including its library associations.
    The new schema will be associated with the same libraries as the source schema.

    Args:
        body (CreateKnowledgeUnitSchemaFromExisting): Model for creating a schema from existing KU
            schema or KU

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeUnitSchema]
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
    body: CreateKnowledgeUnitSchemaFromExisting,
) -> HTTPValidationError | KnowledgeUnitSchema | None:
    """Duplicate Knowledge Unit

     Duplicate a knowledge unit schema including its library associations.
    The new schema will be associated with the same libraries as the source schema.

    Args:
        body (CreateKnowledgeUnitSchemaFromExisting): Model for creating a schema from existing KU
            schema or KU

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeUnitSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeUnitSchemaFromExisting,
) -> Response[HTTPValidationError | KnowledgeUnitSchema]:
    """Duplicate Knowledge Unit

     Duplicate a knowledge unit schema including its library associations.
    The new schema will be associated with the same libraries as the source schema.

    Args:
        body (CreateKnowledgeUnitSchemaFromExisting): Model for creating a schema from existing KU
            schema or KU

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeUnitSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeUnitSchemaFromExisting,
) -> HTTPValidationError | KnowledgeUnitSchema | None:
    """Duplicate Knowledge Unit

     Duplicate a knowledge unit schema including its library associations.
    The new schema will be associated with the same libraries as the source schema.

    Args:
        body (CreateKnowledgeUnitSchemaFromExisting): Model for creating a schema from existing KU
            schema or KU

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeUnitSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
