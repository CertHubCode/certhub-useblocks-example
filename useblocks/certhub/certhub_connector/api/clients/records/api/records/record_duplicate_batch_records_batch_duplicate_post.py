from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.record_duplicate_batch import RecordDuplicateBatch
from ...models.record_duplicate_batch_response import RecordDuplicateBatchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[RecordDuplicateBatch],
    copy_traces: bool | Unset = True,
    copy_use_case_traces: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["copy_traces"] = copy_traces

    params["copy_use_case_traces"] = copy_use_case_traces

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/records/batch-duplicate",
        "params": params,
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | RecordDuplicateBatchResponse | None:
    if response.status_code == 201:
        response_201 = RecordDuplicateBatchResponse.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | RecordDuplicateBatchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[RecordDuplicateBatch],
    copy_traces: bool | Unset = True,
    copy_use_case_traces: bool | Unset = False,
) -> Response[Any | HTTPValidationError | RecordDuplicateBatchResponse]:
    """Record Duplicate Batch

    Args:
        copy_traces (bool | Unset): Whether to copy traces for duplicated records in Tracer. Set
            to false to skip trace duplication. Default: True.
        copy_use_case_traces (bool | Unset): Whether to copy use case traces for duplicated
            records in Tracer. Set to false to skip use case trace duplication. Default: False.
        body (list[RecordDuplicateBatch]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | RecordDuplicateBatchResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        copy_traces=copy_traces,
        copy_use_case_traces=copy_use_case_traces,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: list[RecordDuplicateBatch],
    copy_traces: bool | Unset = True,
    copy_use_case_traces: bool | Unset = False,
) -> Any | HTTPValidationError | RecordDuplicateBatchResponse | None:
    """Record Duplicate Batch

    Args:
        copy_traces (bool | Unset): Whether to copy traces for duplicated records in Tracer. Set
            to false to skip trace duplication. Default: True.
        copy_use_case_traces (bool | Unset): Whether to copy use case traces for duplicated
            records in Tracer. Set to false to skip use case trace duplication. Default: False.
        body (list[RecordDuplicateBatch]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | RecordDuplicateBatchResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        copy_traces=copy_traces,
        copy_use_case_traces=copy_use_case_traces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[RecordDuplicateBatch],
    copy_traces: bool | Unset = True,
    copy_use_case_traces: bool | Unset = False,
) -> Response[Any | HTTPValidationError | RecordDuplicateBatchResponse]:
    """Record Duplicate Batch

    Args:
        copy_traces (bool | Unset): Whether to copy traces for duplicated records in Tracer. Set
            to false to skip trace duplication. Default: True.
        copy_use_case_traces (bool | Unset): Whether to copy use case traces for duplicated
            records in Tracer. Set to false to skip use case trace duplication. Default: False.
        body (list[RecordDuplicateBatch]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | RecordDuplicateBatchResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        copy_traces=copy_traces,
        copy_use_case_traces=copy_use_case_traces,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[RecordDuplicateBatch],
    copy_traces: bool | Unset = True,
    copy_use_case_traces: bool | Unset = False,
) -> Any | HTTPValidationError | RecordDuplicateBatchResponse | None:
    """Record Duplicate Batch

    Args:
        copy_traces (bool | Unset): Whether to copy traces for duplicated records in Tracer. Set
            to false to skip trace duplication. Default: True.
        copy_use_case_traces (bool | Unset): Whether to copy use case traces for duplicated
            records in Tracer. Set to false to skip use case trace duplication. Default: False.
        body (list[RecordDuplicateBatch]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | RecordDuplicateBatchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            copy_traces=copy_traces,
            copy_use_case_traces=copy_use_case_traces,
        )
    ).parsed
