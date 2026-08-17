from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connected_nodes_response import ConnectedNodesResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.node_type import NodeType
from ...models.query_type import QueryType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    node_id: str,
    node_type: NodeType,
    version: str,
    n_hops: int | Unset = 1,
    query_type: QueryType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["node_id"] = node_id

    json_node_type = node_type.value
    params["node_type"] = json_node_type

    params["version"] = version

    params["n_hops"] = n_hops

    json_query_type: str | Unset = UNSET
    if not isinstance(query_type, Unset):
        json_query_type = query_type.value

    params["query_type"] = json_query_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/traces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectedNodesResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ConnectedNodesResponse.from_dict(response.json())

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
) -> Response[ConnectedNodesResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    node_id: str,
    node_type: NodeType,
    version: str,
    n_hops: int | Unset = 1,
    query_type: QueryType | Unset = UNSET,
) -> Response[ConnectedNodesResponse | HTTPValidationError]:
    r"""Get Node Links

     Retrieves all traces (links) associated with a node up to `n_hops` distance.

    Args:
        query_type: Determines the type of query:
            - \"traces_list\": (default) use for traces entity display
            - \"traces_list_with_reference_traces\": traces list plus
              auto-reference traces (have no version)
            - \"graph\": use for trace entity graph display

    Args:
        node_id (str):
        node_type (NodeType):
        version (str):
        n_hops (int | Unset):  Default: 1.
        query_type (QueryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedNodesResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        node_type=node_type,
        version=version,
        n_hops=n_hops,
        query_type=query_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    node_id: str,
    node_type: NodeType,
    version: str,
    n_hops: int | Unset = 1,
    query_type: QueryType | Unset = UNSET,
) -> ConnectedNodesResponse | HTTPValidationError | None:
    r"""Get Node Links

     Retrieves all traces (links) associated with a node up to `n_hops` distance.

    Args:
        query_type: Determines the type of query:
            - \"traces_list\": (default) use for traces entity display
            - \"traces_list_with_reference_traces\": traces list plus
              auto-reference traces (have no version)
            - \"graph\": use for trace entity graph display

    Args:
        node_id (str):
        node_type (NodeType):
        version (str):
        n_hops (int | Unset):  Default: 1.
        query_type (QueryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedNodesResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        node_id=node_id,
        node_type=node_type,
        version=version,
        n_hops=n_hops,
        query_type=query_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    node_id: str,
    node_type: NodeType,
    version: str,
    n_hops: int | Unset = 1,
    query_type: QueryType | Unset = UNSET,
) -> Response[ConnectedNodesResponse | HTTPValidationError]:
    r"""Get Node Links

     Retrieves all traces (links) associated with a node up to `n_hops` distance.

    Args:
        query_type: Determines the type of query:
            - \"traces_list\": (default) use for traces entity display
            - \"traces_list_with_reference_traces\": traces list plus
              auto-reference traces (have no version)
            - \"graph\": use for trace entity graph display

    Args:
        node_id (str):
        node_type (NodeType):
        version (str):
        n_hops (int | Unset):  Default: 1.
        query_type (QueryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedNodesResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        node_type=node_type,
        version=version,
        n_hops=n_hops,
        query_type=query_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    node_id: str,
    node_type: NodeType,
    version: str,
    n_hops: int | Unset = 1,
    query_type: QueryType | Unset = UNSET,
) -> ConnectedNodesResponse | HTTPValidationError | None:
    r"""Get Node Links

     Retrieves all traces (links) associated with a node up to `n_hops` distance.

    Args:
        query_type: Determines the type of query:
            - \"traces_list\": (default) use for traces entity display
            - \"traces_list_with_reference_traces\": traces list plus
              auto-reference traces (have no version)
            - \"graph\": use for trace entity graph display

    Args:
        node_id (str):
        node_type (NodeType):
        version (str):
        n_hops (int | Unset):  Default: 1.
        query_type (QueryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedNodesResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            node_id=node_id,
            node_type=node_type,
            version=version,
            n_hops=n_hops,
            query_type=query_type,
        )
    ).parsed
