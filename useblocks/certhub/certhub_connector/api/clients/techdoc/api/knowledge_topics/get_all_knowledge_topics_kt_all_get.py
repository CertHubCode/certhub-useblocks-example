from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_topic_overview_response import KnowledgeTopicOverviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    latest_or_latest_approved: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["latest_or_latest_approved"] = latest_or_latest_approved

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/kt/all",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KnowledgeTopicOverviewResponse.from_dict(
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
) -> Response[Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    latest_or_latest_approved: bool | Unset = False,
) -> Response[Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse]]:
    """Get all knowledge topics for latest revision of all products and product families

     Retrieve all knowledge topics for latest revision of all products and product families.

    Args:
        latest_or_latest_approved (bool | Unset): Return only knowledge topics from latest or
            latest approved knowledge unit revisions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse]]
    """

    kwargs = _get_kwargs(
        latest_or_latest_approved=latest_or_latest_approved,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    latest_or_latest_approved: bool | Unset = False,
) -> Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse] | None:
    """Get all knowledge topics for latest revision of all products and product families

     Retrieve all knowledge topics for latest revision of all products and product families.

    Args:
        latest_or_latest_approved (bool | Unset): Return only knowledge topics from latest or
            latest approved knowledge unit revisions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse]
    """

    return sync_detailed(
        client=client,
        latest_or_latest_approved=latest_or_latest_approved,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    latest_or_latest_approved: bool | Unset = False,
) -> Response[Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse]]:
    """Get all knowledge topics for latest revision of all products and product families

     Retrieve all knowledge topics for latest revision of all products and product families.

    Args:
        latest_or_latest_approved (bool | Unset): Return only knowledge topics from latest or
            latest approved knowledge unit revisions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse]]
    """

    kwargs = _get_kwargs(
        latest_or_latest_approved=latest_or_latest_approved,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    latest_or_latest_approved: bool | Unset = False,
) -> Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse] | None:
    """Get all knowledge topics for latest revision of all products and product families

     Retrieve all knowledge topics for latest revision of all products and product families.

    Args:
        latest_or_latest_approved (bool | Unset): Return only knowledge topics from latest or
            latest approved knowledge unit revisions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeTopicOverviewResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            latest_or_latest_approved=latest_or_latest_approved,
        )
    ).parsed
