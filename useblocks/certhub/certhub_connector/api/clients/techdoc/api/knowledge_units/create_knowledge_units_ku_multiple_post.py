from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_knowledge_units_from_existing import (
    CreateKnowledgeUnitsFromExisting,
)
from ...models.full_knowledge_unit_view import FullKnowledgeUnitView
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: CreateKnowledgeUnitsFromExisting,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ku/multiple",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[FullKnowledgeUnitView] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = FullKnowledgeUnitView.from_dict(response_201_item_data)

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
) -> Response[Any | HTTPValidationError | list[FullKnowledgeUnitView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeUnitsFromExisting,
) -> Response[Any | HTTPValidationError | list[FullKnowledgeUnitView]]:
    """Create Knowledge Units

     Create knowledge units from existing knowledge unit schemas or knowledge units.
    Knowledge unit schemas are always created from the latest approved schema revision.
    A unique `id` will be created and provided in the response.
    We always require a product history id to add a new knowledge unit.

    Args:
        body (CreateKnowledgeUnitsFromExisting): Model for creating a KU from existing KU schema
            or KU

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[FullKnowledgeUnitView]]
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
    body: CreateKnowledgeUnitsFromExisting,
) -> Any | HTTPValidationError | list[FullKnowledgeUnitView] | None:
    """Create Knowledge Units

     Create knowledge units from existing knowledge unit schemas or knowledge units.
    Knowledge unit schemas are always created from the latest approved schema revision.
    A unique `id` will be created and provided in the response.
    We always require a product history id to add a new knowledge unit.

    Args:
        body (CreateKnowledgeUnitsFromExisting): Model for creating a KU from existing KU schema
            or KU

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[FullKnowledgeUnitView]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeUnitsFromExisting,
) -> Response[Any | HTTPValidationError | list[FullKnowledgeUnitView]]:
    """Create Knowledge Units

     Create knowledge units from existing knowledge unit schemas or knowledge units.
    Knowledge unit schemas are always created from the latest approved schema revision.
    A unique `id` will be created and provided in the response.
    We always require a product history id to add a new knowledge unit.

    Args:
        body (CreateKnowledgeUnitsFromExisting): Model for creating a KU from existing KU schema
            or KU

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[FullKnowledgeUnitView]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateKnowledgeUnitsFromExisting,
) -> Any | HTTPValidationError | list[FullKnowledgeUnitView] | None:
    """Create Knowledge Units

     Create knowledge units from existing knowledge unit schemas or knowledge units.
    Knowledge unit schemas are always created from the latest approved schema revision.
    A unique `id` will be created and provided in the response.
    We always require a product history id to add a new knowledge unit.

    Args:
        body (CreateKnowledgeUnitsFromExisting): Model for creating a KU from existing KU schema
            or KU

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[FullKnowledgeUnitView]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
