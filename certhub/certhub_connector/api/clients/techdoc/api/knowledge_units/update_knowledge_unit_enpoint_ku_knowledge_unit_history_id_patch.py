from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.full_knowledge_unit_view import FullKnowledgeUnitView
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_unit_update import KnowledgeUnitUpdate
from ...types import Response


def _get_kwargs(
    knowledge_unit_history_id: str,
    *,
    body: KnowledgeUnitUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/ku/{knowledge_unit_history_id}".format(
            knowledge_unit_history_id=quote(str(knowledge_unit_history_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FullKnowledgeUnitView | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FullKnowledgeUnitView.from_dict(response.json())

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
) -> Response[Any | FullKnowledgeUnitView | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_unit_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KnowledgeUnitUpdate,
) -> Response[Any | FullKnowledgeUnitView | HTTPValidationError]:
    """Update Knowledge Unit Enpoint

     Update individual values of an existing knowledge unit record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.

    Args:
        knowledge_unit_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (KnowledgeUnitUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FullKnowledgeUnitView | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        knowledge_unit_history_id=knowledge_unit_history_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_unit_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KnowledgeUnitUpdate,
) -> Any | FullKnowledgeUnitView | HTTPValidationError | None:
    """Update Knowledge Unit Enpoint

     Update individual values of an existing knowledge unit record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.

    Args:
        knowledge_unit_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (KnowledgeUnitUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FullKnowledgeUnitView | HTTPValidationError
    """

    return sync_detailed(
        knowledge_unit_history_id=knowledge_unit_history_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    knowledge_unit_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KnowledgeUnitUpdate,
) -> Response[Any | FullKnowledgeUnitView | HTTPValidationError]:
    """Update Knowledge Unit Enpoint

     Update individual values of an existing knowledge unit record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.

    Args:
        knowledge_unit_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (KnowledgeUnitUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FullKnowledgeUnitView | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        knowledge_unit_history_id=knowledge_unit_history_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_unit_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KnowledgeUnitUpdate,
) -> Any | FullKnowledgeUnitView | HTTPValidationError | None:
    """Update Knowledge Unit Enpoint

     Update individual values of an existing knowledge unit record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.

    Args:
        knowledge_unit_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (KnowledgeUnitUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FullKnowledgeUnitView | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            knowledge_unit_history_id=knowledge_unit_history_id,
            client=client,
            body=body,
        )
    ).parsed
