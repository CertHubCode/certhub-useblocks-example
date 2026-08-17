from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.duplicate_knowledge_topic import DuplicateKnowledgeTopic
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_topic import KnowledgeTopic
from ...types import Response


def _get_kwargs(
    *,
    body: DuplicateKnowledgeTopic,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/kt/duplicate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | KnowledgeTopic | None:
    if response.status_code == 201:
        response_201 = KnowledgeTopic.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | KnowledgeTopic]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DuplicateKnowledgeTopic,
) -> Response[Any | HTTPValidationError | KnowledgeTopic]:
    """Knowledge Topic Duplicate

     Duplicate knowledge topic

    Args:
        body (DuplicateKnowledgeTopic):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | KnowledgeTopic]
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
    body: DuplicateKnowledgeTopic,
) -> Any | HTTPValidationError | KnowledgeTopic | None:
    """Knowledge Topic Duplicate

     Duplicate knowledge topic

    Args:
        body (DuplicateKnowledgeTopic):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | KnowledgeTopic
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DuplicateKnowledgeTopic,
) -> Response[Any | HTTPValidationError | KnowledgeTopic]:
    """Knowledge Topic Duplicate

     Duplicate knowledge topic

    Args:
        body (DuplicateKnowledgeTopic):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | KnowledgeTopic]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DuplicateKnowledgeTopic,
) -> Any | HTTPValidationError | KnowledgeTopic | None:
    """Knowledge Topic Duplicate

     Duplicate knowledge topic

    Args:
        body (DuplicateKnowledgeTopic):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | KnowledgeTopic
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
