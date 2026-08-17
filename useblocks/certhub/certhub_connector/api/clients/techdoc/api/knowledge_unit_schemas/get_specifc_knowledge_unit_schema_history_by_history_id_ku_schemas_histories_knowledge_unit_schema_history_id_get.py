from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_unit_schema_history_group import (
    KnowledgeUnitSchemaHistoryGroup,
)
from ...types import Response


def _get_kwargs(
    knowledge_unit_schema_history_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ku-schemas/histories/{knowledge_unit_schema_history_id}".format(
            knowledge_unit_schema_history_id=quote(
                str(knowledge_unit_schema_history_id), safe=""
            ),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | KnowledgeUnitSchemaHistoryGroup | None:
    if response.status_code == 200:
        response_200 = KnowledgeUnitSchemaHistoryGroup.from_dict(response.json())

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
) -> Response[HTTPValidationError | KnowledgeUnitSchemaHistoryGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_unit_schema_history_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | KnowledgeUnitSchemaHistoryGroup]:
    """Get Knowledge Unit Schema History Group by History ID

     Get a knowledge unit schema history group by history ID.

    - **history_id**: The knowledge unit schema history ID
    - Returns the full history group with all revisions for this history ID

    Args:
        knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeUnitSchemaHistoryGroup]
    """

    kwargs = _get_kwargs(
        knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_unit_schema_history_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | KnowledgeUnitSchemaHistoryGroup | None:
    """Get Knowledge Unit Schema History Group by History ID

     Get a knowledge unit schema history group by history ID.

    - **history_id**: The knowledge unit schema history ID
    - Returns the full history group with all revisions for this history ID

    Args:
        knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeUnitSchemaHistoryGroup
    """

    return sync_detailed(
        knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    knowledge_unit_schema_history_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | KnowledgeUnitSchemaHistoryGroup]:
    """Get Knowledge Unit Schema History Group by History ID

     Get a knowledge unit schema history group by history ID.

    - **history_id**: The knowledge unit schema history ID
    - Returns the full history group with all revisions for this history ID

    Args:
        knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KnowledgeUnitSchemaHistoryGroup]
    """

    kwargs = _get_kwargs(
        knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_unit_schema_history_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | KnowledgeUnitSchemaHistoryGroup | None:
    """Get Knowledge Unit Schema History Group by History ID

     Get a knowledge unit schema history group by history ID.

    - **history_id**: The knowledge unit schema history ID
    - Returns the full history group with all revisions for this history ID

    Args:
        knowledge_unit_schema_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KnowledgeUnitSchemaHistoryGroup
    """

    return (
        await asyncio_detailed(
            knowledge_unit_schema_history_id=knowledge_unit_schema_history_id,
            client=client,
        )
    ).parsed
