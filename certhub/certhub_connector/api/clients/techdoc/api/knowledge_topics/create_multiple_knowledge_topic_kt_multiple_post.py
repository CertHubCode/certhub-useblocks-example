from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_knowledge_topics_from_existing import (
    CreateKnowledgeTopicsFromExisting,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_topic import KnowledgeTopic
from ...types import Response


def _get_kwargs(
    *,
    body: CreateKnowledgeTopicsFromExisting,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/kt/multiple",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[KnowledgeTopic] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = KnowledgeTopic.from_dict(response_201_item_data)

            response_201.append(response_201_item)

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
    body: CreateKnowledgeTopicsFromExisting,
) -> Response[Any | HTTPValidationError | list[KnowledgeTopic]]:
    """Create Multiple Knowledge Topic

     Insert multiple knowledge topics from existing KT schemas or KTs.

    Args:
        body (CreateKnowledgeTopicsFromExisting): Model for creating a KT from existing KT schema
            or KT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeTopic]]
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
    body: CreateKnowledgeTopicsFromExisting,
) -> Any | HTTPValidationError | list[KnowledgeTopic] | None:
    """Create Multiple Knowledge Topic

     Insert multiple knowledge topics from existing KT schemas or KTs.

    Args:
        body (CreateKnowledgeTopicsFromExisting): Model for creating a KT from existing KT schema
            or KT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeTopic]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeTopicsFromExisting,
) -> Response[Any | HTTPValidationError | list[KnowledgeTopic]]:
    """Create Multiple Knowledge Topic

     Insert multiple knowledge topics from existing KT schemas or KTs.

    Args:
        body (CreateKnowledgeTopicsFromExisting): Model for creating a KT from existing KT schema
            or KT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeTopic]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeTopicsFromExisting,
) -> Any | HTTPValidationError | list[KnowledgeTopic] | None:
    """Create Multiple Knowledge Topic

     Insert multiple knowledge topics from existing KT schemas or KTs.

    Args:
        body (CreateKnowledgeTopicsFromExisting): Model for creating a KT from existing KT schema
            or KT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeTopic]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
