from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_knowledge_topic_fetch_request import BulkKnowledgeTopicFetchRequest
from ...models.bulk_knowledge_topic_fetch_result import BulkKnowledgeTopicFetchResult
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: BulkKnowledgeTopicFetchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/kt/bulk-fetch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BulkKnowledgeTopicFetchResult.from_dict(
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
) -> Response[Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkKnowledgeTopicFetchRequest,
) -> Response[Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult]]:
    """Bulk fetch knowledge topics, each resolved to its latest-or-latest-approved revision

     Resolve many knowledge topics in one call. Each requested id may point to any revision; it is
    resolved server-side to its latest-or-latest-approved revision and returned in the same shape as GET
    /kt/{id}. Results are in request order; a missing/cross-tenant id does not fail the batch.

    Args:
        body (BulkKnowledgeTopicFetchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult]]
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
    body: BulkKnowledgeTopicFetchRequest,
) -> Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult] | None:
    """Bulk fetch knowledge topics, each resolved to its latest-or-latest-approved revision

     Resolve many knowledge topics in one call. Each requested id may point to any revision; it is
    resolved server-side to its latest-or-latest-approved revision and returned in the same shape as GET
    /kt/{id}. Results are in request order; a missing/cross-tenant id does not fail the batch.

    Args:
        body (BulkKnowledgeTopicFetchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkKnowledgeTopicFetchRequest,
) -> Response[Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult]]:
    """Bulk fetch knowledge topics, each resolved to its latest-or-latest-approved revision

     Resolve many knowledge topics in one call. Each requested id may point to any revision; it is
    resolved server-side to its latest-or-latest-approved revision and returned in the same shape as GET
    /kt/{id}. Results are in request order; a missing/cross-tenant id does not fail the batch.

    Args:
        body (BulkKnowledgeTopicFetchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkKnowledgeTopicFetchRequest,
) -> Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult] | None:
    """Bulk fetch knowledge topics, each resolved to its latest-or-latest-approved revision

     Resolve many knowledge topics in one call. Each requested id may point to any revision; it is
    resolved server-side to its latest-or-latest-approved revision and returned in the same shape as GET
    /kt/{id}. Results are in request order; a missing/cross-tenant id does not fail the batch.

    Args:
        body (BulkKnowledgeTopicFetchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[BulkKnowledgeTopicFetchResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
