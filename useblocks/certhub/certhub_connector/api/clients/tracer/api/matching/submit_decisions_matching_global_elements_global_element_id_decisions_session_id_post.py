from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.global_element_decision_result import GlobalElementDecisionResult
from ...models.global_element_match_decisions_request import (
    GlobalElementMatchDecisionsRequest,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    global_element_id: str,
    session_id: str,
    *,
    body: GlobalElementMatchDecisionsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/matching/global-elements/{global_element_id}/decisions/{session_id}".format(
            global_element_id=quote(str(global_element_id), safe=""),
            session_id=quote(str(session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GlobalElementDecisionResult | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GlobalElementDecisionResult.from_dict(response.json())

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
) -> Response[GlobalElementDecisionResult | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    global_element_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GlobalElementMatchDecisionsRequest,
) -> Response[GlobalElementDecisionResult | HTTPValidationError]:
    r"""Submit Decisions

     Submits the accepted suggestions for a completed matching session; each accepted (record, evidence)
    pair is persisted as a bidirectional \"References Global Element\" trace.

    Args:
        global_element_id (str):
        session_id (str):
        body (GlobalElementMatchDecisionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlobalElementDecisionResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        global_element_id=global_element_id,
        session_id=session_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    global_element_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GlobalElementMatchDecisionsRequest,
) -> GlobalElementDecisionResult | HTTPValidationError | None:
    r"""Submit Decisions

     Submits the accepted suggestions for a completed matching session; each accepted (record, evidence)
    pair is persisted as a bidirectional \"References Global Element\" trace.

    Args:
        global_element_id (str):
        session_id (str):
        body (GlobalElementMatchDecisionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlobalElementDecisionResult | HTTPValidationError
    """

    return sync_detailed(
        global_element_id=global_element_id,
        session_id=session_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    global_element_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GlobalElementMatchDecisionsRequest,
) -> Response[GlobalElementDecisionResult | HTTPValidationError]:
    r"""Submit Decisions

     Submits the accepted suggestions for a completed matching session; each accepted (record, evidence)
    pair is persisted as a bidirectional \"References Global Element\" trace.

    Args:
        global_element_id (str):
        session_id (str):
        body (GlobalElementMatchDecisionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlobalElementDecisionResult | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        global_element_id=global_element_id,
        session_id=session_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    global_element_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GlobalElementMatchDecisionsRequest,
) -> GlobalElementDecisionResult | HTTPValidationError | None:
    r"""Submit Decisions

     Submits the accepted suggestions for a completed matching session; each accepted (record, evidence)
    pair is persisted as a bidirectional \"References Global Element\" trace.

    Args:
        global_element_id (str):
        session_id (str):
        body (GlobalElementMatchDecisionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlobalElementDecisionResult | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            global_element_id=global_element_id,
            session_id=session_id,
            client=client,
            body=body,
        )
    ).parsed
