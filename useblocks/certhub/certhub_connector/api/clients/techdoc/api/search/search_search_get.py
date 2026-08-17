from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.search_entity_type import SearchEntityType
from ...models.search_results import SearchResults
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    entity_types: list[SearchEntityType] | None | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    json_entity_types: list[str] | None | Unset
    if isinstance(entity_types, Unset):
        json_entity_types = UNSET
    elif isinstance(entity_types, list):
        json_entity_types = []
        for entity_types_type_0_item_data in entity_types:
            entity_types_type_0_item = entity_types_type_0_item_data.value
            json_entity_types.append(entity_types_type_0_item)

    else:
        json_entity_types = entity_types
    params["entity_types"] = json_entity_types

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | SearchResults | None:
    if response.status_code == 200:
        response_200 = SearchResults.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | SearchResults]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    entity_types: list[SearchEntityType] | None | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[Any | HTTPValidationError | SearchResults]:
    """Prefix search across products, knowledge units and knowledge topics

     Autocomplete-style search. Matches latest-approved entities whose name starts with the query (case-
    insensitive). Returns only the entity id and the ids needed to build a link: a KT result carries its
    parent KU and product, a KU result carries its parent product.

    Args:
        query (str): Text the entity name should start with.
        entity_types (list[SearchEntityType] | None | Unset): Optional filter — restrict results
            to these entity types.
        limit (int | Unset): Maximum number of results. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | SearchResults]
    """

    kwargs = _get_kwargs(
        query=query,
        entity_types=entity_types,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    entity_types: list[SearchEntityType] | None | Unset = UNSET,
    limit: int | Unset = 20,
) -> Any | HTTPValidationError | SearchResults | None:
    """Prefix search across products, knowledge units and knowledge topics

     Autocomplete-style search. Matches latest-approved entities whose name starts with the query (case-
    insensitive). Returns only the entity id and the ids needed to build a link: a KT result carries its
    parent KU and product, a KU result carries its parent product.

    Args:
        query (str): Text the entity name should start with.
        entity_types (list[SearchEntityType] | None | Unset): Optional filter — restrict results
            to these entity types.
        limit (int | Unset): Maximum number of results. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | SearchResults
    """

    return sync_detailed(
        client=client,
        query=query,
        entity_types=entity_types,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    entity_types: list[SearchEntityType] | None | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[Any | HTTPValidationError | SearchResults]:
    """Prefix search across products, knowledge units and knowledge topics

     Autocomplete-style search. Matches latest-approved entities whose name starts with the query (case-
    insensitive). Returns only the entity id and the ids needed to build a link: a KT result carries its
    parent KU and product, a KU result carries its parent product.

    Args:
        query (str): Text the entity name should start with.
        entity_types (list[SearchEntityType] | None | Unset): Optional filter — restrict results
            to these entity types.
        limit (int | Unset): Maximum number of results. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | SearchResults]
    """

    kwargs = _get_kwargs(
        query=query,
        entity_types=entity_types,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    entity_types: list[SearchEntityType] | None | Unset = UNSET,
    limit: int | Unset = 20,
) -> Any | HTTPValidationError | SearchResults | None:
    """Prefix search across products, knowledge units and knowledge topics

     Autocomplete-style search. Matches latest-approved entities whose name starts with the query (case-
    insensitive). Returns only the entity id and the ids needed to build a link: a KT result carries its
    parent KU and product, a KU result carries its parent product.

    Args:
        query (str): Text the entity name should start with.
        entity_types (list[SearchEntityType] | None | Unset): Optional filter — restrict results
            to these entity types.
        limit (int | Unset): Maximum number of results. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | SearchResults
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            entity_types=entity_types,
            limit=limit,
        )
    ).parsed
