from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    sop_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/matching/qms/{sop_id}".format(
            sop_id=quote(str(sop_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError]:
    r"""Start Matching

     Start a SOP matching session. Returns an SSE stream with state transitions
    and suggestion events. Closes after AWAITING_DECISIONS state is emitted.

    Event types:
      state       — { state: \"FETCHING\" | \"MATCHING\" | \"AWAITING_DECISIONS\", session_id?: str }
      suggestion  — { type: str, matches: ObjectMatch[], no_match: bool }
      error       — { message: str }
      done        — stream complete

    Args:
        sop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        sop_id=sop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | None:
    r"""Start Matching

     Start a SOP matching session. Returns an SSE stream with state transitions
    and suggestion events. Closes after AWAITING_DECISIONS state is emitted.

    Event types:
      state       — { state: \"FETCHING\" | \"MATCHING\" | \"AWAITING_DECISIONS\", session_id?: str }
      suggestion  — { type: str, matches: ObjectMatch[], no_match: bool }
      error       — { message: str }
      done        — stream complete

    Args:
        sop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        sop_id=sop_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError]:
    r"""Start Matching

     Start a SOP matching session. Returns an SSE stream with state transitions
    and suggestion events. Closes after AWAITING_DECISIONS state is emitted.

    Event types:
      state       — { state: \"FETCHING\" | \"MATCHING\" | \"AWAITING_DECISIONS\", session_id?: str }
      suggestion  — { type: str, matches: ObjectMatch[], no_match: bool }
      error       — { message: str }
      done        — stream complete

    Args:
        sop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        sop_id=sop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | None:
    r"""Start Matching

     Start a SOP matching session. Returns an SSE stream with state transitions
    and suggestion events. Closes after AWAITING_DECISIONS state is emitted.

    Event types:
      state       — { state: \"FETCHING\" | \"MATCHING\" | \"AWAITING_DECISIONS\", session_id?: str }
      suggestion  — { type: str, matches: ObjectMatch[], no_match: bool }
      error       — { message: str }
      done        — stream complete

    Args:
        sop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            sop_id=sop_id,
            client=client,
        )
    ).parsed
