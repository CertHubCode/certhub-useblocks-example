from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_knowledge_unit_ku_post import BodyCreateKnowledgeUnitKuPost
from ...models.full_knowledge_unit_view import FullKnowledgeUnitView
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: BodyCreateKnowledgeUnitKuPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ku/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FullKnowledgeUnitView | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = FullKnowledgeUnitView.from_dict(response.json())

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
) -> Response[Any | FullKnowledgeUnitView | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyCreateKnowledgeUnitKuPost,
) -> Response[Any | FullKnowledgeUnitView | HTTPValidationError]:
    """Create Knowledge Unit

     Insert a new knowledge unit.
    A unique `id` will be created and provided in the response.
    We always require a product history id to add a new knowledge unit

    Args:
        body (BodyCreateKnowledgeUnitKuPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FullKnowledgeUnitView | HTTPValidationError]
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
    body: BodyCreateKnowledgeUnitKuPost,
) -> Any | FullKnowledgeUnitView | HTTPValidationError | None:
    """Create Knowledge Unit

     Insert a new knowledge unit.
    A unique `id` will be created and provided in the response.
    We always require a product history id to add a new knowledge unit

    Args:
        body (BodyCreateKnowledgeUnitKuPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FullKnowledgeUnitView | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyCreateKnowledgeUnitKuPost,
) -> Response[Any | FullKnowledgeUnitView | HTTPValidationError]:
    """Create Knowledge Unit

     Insert a new knowledge unit.
    A unique `id` will be created and provided in the response.
    We always require a product history id to add a new knowledge unit

    Args:
        body (BodyCreateKnowledgeUnitKuPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FullKnowledgeUnitView | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BodyCreateKnowledgeUnitKuPost,
) -> Any | FullKnowledgeUnitView | HTTPValidationError | None:
    """Create Knowledge Unit

     Insert a new knowledge unit.
    A unique `id` will be created and provided in the response.
    We always require a product history id to add a new knowledge unit

    Args:
        body (BodyCreateKnowledgeUnitKuPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FullKnowledgeUnitView | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
