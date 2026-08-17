from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_unit_schema import KnowledgeUnitSchema
from ...models.update_knowledge_unit_schema import UpdateKnowledgeUnitSchema
from ...types import Response


def _get_kwargs(
    schema_history_id: str,
    *,
    body: UpdateKnowledgeUnitSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/ku-schemas/{schema_history_id}".format(
            schema_history_id=quote(str(schema_history_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | KnowledgeUnitSchema | None:
    if response.status_code == 200:
        response_200 = KnowledgeUnitSchema.from_dict(response.json())

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
) -> Response[HTTPValidationError | KnowledgeUnitSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schema_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateKnowledgeUnitSchema,
) -> Response[HTTPValidationError | KnowledgeUnitSchema]:
    """Update Ku Schema

     Update a knowledge unit schema

    Args:
        schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (UpdateKnowledgeUnitSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeUnitSchema]
    """

    kwargs = _get_kwargs(
        schema_history_id=schema_history_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schema_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateKnowledgeUnitSchema,
) -> HTTPValidationError | KnowledgeUnitSchema | None:
    """Update Ku Schema

     Update a knowledge unit schema

    Args:
        schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (UpdateKnowledgeUnitSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeUnitSchema
    """

    return sync_detailed(
        schema_history_id=schema_history_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    schema_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateKnowledgeUnitSchema,
) -> Response[HTTPValidationError | KnowledgeUnitSchema]:
    """Update Ku Schema

     Update a knowledge unit schema

    Args:
        schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (UpdateKnowledgeUnitSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeUnitSchema]
    """

    kwargs = _get_kwargs(
        schema_history_id=schema_history_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schema_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateKnowledgeUnitSchema,
) -> HTTPValidationError | KnowledgeUnitSchema | None:
    """Update Ku Schema

     Update a knowledge unit schema

    Args:
        schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (UpdateKnowledgeUnitSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeUnitSchema
    """

    return (
        await asyncio_detailed(
            schema_history_id=schema_history_id,
            client=client,
            body=body,
        )
    ).parsed
