from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.publish_knowledge_unit_response import PublishKnowledgeUnitResponse
from ...models.publish_knowledge_unit_revision_request import (
    PublishKnowledgeUnitRevisionRequest,
)
from ...types import Response


def _get_kwargs(
    history_id: str,
    *,
    body: PublishKnowledgeUnitRevisionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ku/publish/{history_id}".format(
            history_id=quote(str(history_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | PublishKnowledgeUnitResponse | None:
    if response.status_code == 200:
        response_200 = PublishKnowledgeUnitResponse.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | PublishKnowledgeUnitResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublishKnowledgeUnitRevisionRequest,
) -> Response[Any | HTTPValidationError | PublishKnowledgeUnitResponse]:
    """Publish Knowledge Unit

     Release a major version of a knowledge unit

    Args:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (PublishKnowledgeUnitRevisionRequest): Request to publish a revision (morph to next
            major version)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | PublishKnowledgeUnitResponse]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublishKnowledgeUnitRevisionRequest,
) -> Any | HTTPValidationError | PublishKnowledgeUnitResponse | None:
    """Publish Knowledge Unit

     Release a major version of a knowledge unit

    Args:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (PublishKnowledgeUnitRevisionRequest): Request to publish a revision (morph to next
            major version)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | PublishKnowledgeUnitResponse
    """

    return sync_detailed(
        history_id=history_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublishKnowledgeUnitRevisionRequest,
) -> Response[Any | HTTPValidationError | PublishKnowledgeUnitResponse]:
    """Publish Knowledge Unit

     Release a major version of a knowledge unit

    Args:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (PublishKnowledgeUnitRevisionRequest): Request to publish a revision (morph to next
            major version)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | PublishKnowledgeUnitResponse]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublishKnowledgeUnitRevisionRequest,
) -> Any | HTTPValidationError | PublishKnowledgeUnitResponse | None:
    """Publish Knowledge Unit

     Release a major version of a knowledge unit

    Args:
        history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (PublishKnowledgeUnitRevisionRequest): Request to publish a revision (morph to next
            major version)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | PublishKnowledgeUnitResponse
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            body=body,
        )
    ).parsed
