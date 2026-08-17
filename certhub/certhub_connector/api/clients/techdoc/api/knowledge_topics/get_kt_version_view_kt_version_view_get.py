from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_topic_version_entry import KnowledgeTopicVersionEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ku_history_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ku_history_id: None | str | Unset
    if isinstance(ku_history_id, Unset):
        json_ku_history_id = UNSET
    else:
        json_ku_history_id = ku_history_id
    params["ku_history_id"] = json_ku_history_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/kt/version-view",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[KnowledgeTopicVersionEntry] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KnowledgeTopicVersionEntry.from_dict(
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
) -> Response[Any | HTTPValidationError | list[KnowledgeTopicVersionEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ku_history_id: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[KnowledgeTopicVersionEntry]]:
    """Get Kt Version View

     Returns every (KU revision, KT revision) pair for the tenant with version and
    approval status.  Optionally scoped to a single KU lineage via ku_history_id.

    Args:
        ku_history_id (None | str | Unset): Filter by KU history ID to get only KTs from that KU
            lineage

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeTopicVersionEntry]]
    """

    kwargs = _get_kwargs(
        ku_history_id=ku_history_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    ku_history_id: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | list[KnowledgeTopicVersionEntry] | None:
    """Get Kt Version View

     Returns every (KU revision, KT revision) pair for the tenant with version and
    approval status.  Optionally scoped to a single KU lineage via ku_history_id.

    Args:
        ku_history_id (None | str | Unset): Filter by KU history ID to get only KTs from that KU
            lineage

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeTopicVersionEntry]
    """

    return sync_detailed(
        client=client,
        ku_history_id=ku_history_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ku_history_id: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[KnowledgeTopicVersionEntry]]:
    """Get Kt Version View

     Returns every (KU revision, KT revision) pair for the tenant with version and
    approval status.  Optionally scoped to a single KU lineage via ku_history_id.

    Args:
        ku_history_id (None | str | Unset): Filter by KU history ID to get only KTs from that KU
            lineage

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[KnowledgeTopicVersionEntry]]
    """

    kwargs = _get_kwargs(
        ku_history_id=ku_history_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ku_history_id: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | list[KnowledgeTopicVersionEntry] | None:
    """Get Kt Version View

     Returns every (KU revision, KT revision) pair for the tenant with version and
    approval status.  Optionally scoped to a single KU lineage via ku_history_id.

    Args:
        ku_history_id (None | str | Unset): Filter by KU history ID to get only KTs from that KU
            lineage

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[KnowledgeTopicVersionEntry]
    """

    return (
        await asyncio_detailed(
            client=client,
            ku_history_id=ku_history_id,
        )
    ).parsed
