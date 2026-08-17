from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    entity_type: str,
    entity_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/matching/qms/{entity_type}/{entity_id}/steps".format(
            entity_type=quote(str(entity_type), safe=""),
            entity_id=quote(str(entity_id), safe=""),
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
    entity_type: str,
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError]:
    r"""Start Step Matching

     Start a BPMN step-level matching session for a SOP draft or a Work Instruction.
    Streams SSE events:
      state           — { state: \"FETCHING\" | \"MATCHING\" }
      step_suggestion — { step_id, step_name, step_type, catalogue_type, matches }
      error           — { message: str }
      done            — stream complete

    UserTask steps are matched against templates + QM lists.
    CallActivity steps are matched against SOPs + work instructions.
    Returns top-1 match per catalogue type per step.

    entity_type ∈ {\"sop\", \"workinstruction\"} — selects which QMS resource to read/patch.

    Args:
        entity_type (str):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_id=entity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_type: str,
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | None:
    r"""Start Step Matching

     Start a BPMN step-level matching session for a SOP draft or a Work Instruction.
    Streams SSE events:
      state           — { state: \"FETCHING\" | \"MATCHING\" }
      step_suggestion — { step_id, step_name, step_type, catalogue_type, matches }
      error           — { message: str }
      done            — stream complete

    UserTask steps are matched against templates + QM lists.
    CallActivity steps are matched against SOPs + work instructions.
    Returns top-1 match per catalogue type per step.

    entity_type ∈ {\"sop\", \"workinstruction\"} — selects which QMS resource to read/patch.

    Args:
        entity_type (str):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        entity_type=entity_type,
        entity_id=entity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    entity_type: str,
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError]:
    r"""Start Step Matching

     Start a BPMN step-level matching session for a SOP draft or a Work Instruction.
    Streams SSE events:
      state           — { state: \"FETCHING\" | \"MATCHING\" }
      step_suggestion — { step_id, step_name, step_type, catalogue_type, matches }
      error           — { message: str }
      done            — stream complete

    UserTask steps are matched against templates + QM lists.
    CallActivity steps are matched against SOPs + work instructions.
    Returns top-1 match per catalogue type per step.

    entity_type ∈ {\"sop\", \"workinstruction\"} — selects which QMS resource to read/patch.

    Args:
        entity_type (str):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        entity_id=entity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_type: str,
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | None:
    r"""Start Step Matching

     Start a BPMN step-level matching session for a SOP draft or a Work Instruction.
    Streams SSE events:
      state           — { state: \"FETCHING\" | \"MATCHING\" }
      step_suggestion — { step_id, step_name, step_type, catalogue_type, matches }
      error           — { message: str }
      done            — stream complete

    UserTask steps are matched against templates + QM lists.
    CallActivity steps are matched against SOPs + work instructions.
    Returns top-1 match per catalogue type per step.

    entity_type ∈ {\"sop\", \"workinstruction\"} — selects which QMS resource to read/patch.

    Args:
        entity_type (str):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            entity_type=entity_type,
            entity_id=entity_id,
            client=client,
        )
    ).parsed
