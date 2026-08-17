from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_topic_overview_response import KnowledgeTopicOverviewResponse
from ...types import Response


def _get_kwargs(
    knowledge_topic_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/kt/{knowledge_topic_id}/overview".format(
            knowledge_topic_id=quote(str(knowledge_topic_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | KnowledgeTopicOverviewResponse | None:
    if response.status_code == 200:
        response_200 = KnowledgeTopicOverviewResponse.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | KnowledgeTopicOverviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_topic_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError | KnowledgeTopicOverviewResponse]:
    """Get Kt Overview

    Args:
        knowledge_topic_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | KnowledgeTopicOverviewResponse]
    """

    kwargs = _get_kwargs(
        knowledge_topic_id=knowledge_topic_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_topic_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | KnowledgeTopicOverviewResponse | None:
    """Get Kt Overview

    Args:
        knowledge_topic_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | KnowledgeTopicOverviewResponse
    """

    return sync_detailed(
        knowledge_topic_id=knowledge_topic_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    knowledge_topic_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError | KnowledgeTopicOverviewResponse]:
    """Get Kt Overview

    Args:
        knowledge_topic_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | KnowledgeTopicOverviewResponse]
    """

    kwargs = _get_kwargs(
        knowledge_topic_id=knowledge_topic_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_topic_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | KnowledgeTopicOverviewResponse | None:
    """Get Kt Overview

    Args:
        knowledge_topic_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | KnowledgeTopicOverviewResponse
    """

    return (
        await asyncio_detailed(
            knowledge_topic_id=knowledge_topic_id,
            client=client,
        )
    ).parsed
