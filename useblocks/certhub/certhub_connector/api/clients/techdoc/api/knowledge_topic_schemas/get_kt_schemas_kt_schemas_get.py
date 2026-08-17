from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_topic_schema_view import KnowledgeTopicSchemaView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    only_latest_or_latest_approved: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["onlyLatestOrLatestApproved"] = only_latest_or_latest_approved

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/kt-schemas/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[KnowledgeTopicSchemaView] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KnowledgeTopicSchemaView.from_dict(
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
) -> Response[HTTPValidationError | list[KnowledgeTopicSchemaView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    only_latest_or_latest_approved: bool | Unset = False,
) -> Response[HTTPValidationError | list[KnowledgeTopicSchemaView]]:
    """Get Kt Schemas

     Retrieve all knowledge topic schemas

    Args:
        only_latest_or_latest_approved (bool | Unset): Return only KTs from latest or latest
            approved KU schema revisions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[KnowledgeTopicSchemaView]]
    """

    kwargs = _get_kwargs(
        only_latest_or_latest_approved=only_latest_or_latest_approved,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    only_latest_or_latest_approved: bool | Unset = False,
) -> HTTPValidationError | list[KnowledgeTopicSchemaView] | None:
    """Get Kt Schemas

     Retrieve all knowledge topic schemas

    Args:
        only_latest_or_latest_approved (bool | Unset): Return only KTs from latest or latest
            approved KU schema revisions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[KnowledgeTopicSchemaView]
    """

    return sync_detailed(
        client=client,
        only_latest_or_latest_approved=only_latest_or_latest_approved,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    only_latest_or_latest_approved: bool | Unset = False,
) -> Response[HTTPValidationError | list[KnowledgeTopicSchemaView]]:
    """Get Kt Schemas

     Retrieve all knowledge topic schemas

    Args:
        only_latest_or_latest_approved (bool | Unset): Return only KTs from latest or latest
            approved KU schema revisions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[KnowledgeTopicSchemaView]]
    """

    kwargs = _get_kwargs(
        only_latest_or_latest_approved=only_latest_or_latest_approved,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    only_latest_or_latest_approved: bool | Unset = False,
) -> HTTPValidationError | list[KnowledgeTopicSchemaView] | None:
    """Get Kt Schemas

     Retrieve all knowledge topic schemas

    Args:
        only_latest_or_latest_approved (bool | Unset): Return only KTs from latest or latest
            approved KU schema revisions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[KnowledgeTopicSchemaView]
    """

    return (
        await asyncio_detailed(
            client=client,
            only_latest_or_latest_approved=only_latest_or_latest_approved,
        )
    ).parsed
