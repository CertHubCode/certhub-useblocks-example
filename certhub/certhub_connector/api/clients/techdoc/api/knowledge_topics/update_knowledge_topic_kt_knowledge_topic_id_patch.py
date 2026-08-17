from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.knowledge_topic import KnowledgeTopic
from ...models.knowledge_topic_update import KnowledgeTopicUpdate
from ...types import Response


def _get_kwargs(
    knowledge_topic_id: str,
    *,
    body: KnowledgeTopicUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/kt/{knowledge_topic_id}".format(
            knowledge_topic_id=quote(str(knowledge_topic_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | KnowledgeTopic | None:
    if response.status_code == 200:
        response_200 = KnowledgeTopic.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | KnowledgeTopic]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_topic_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KnowledgeTopicUpdate,
) -> Response[Any | HTTPValidationError | KnowledgeTopic]:
    """Update Knowledge Topic

     Update individual values of an existing knowledge topic.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.

    Args:
        knowledge_topic_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (KnowledgeTopicUpdate): Model for updating a Knowledge Topic.

            Only allows updating:
            - knowledge_topic_name: The name of the knowledge topic
            - knowledge_topic_schema: The schema definition (form structure)
            - data: The actual data stored in the topic

            Excluded fields (immutable/system-managed):
            - knowledge_unit_history_id: Ownership relationship (immutable)
            - product_history_id: Ownership relationship (immutable)
            - type: Fundamental characteristic (immutable)
            - product_data_collection_id: Tied to type and relationships (immutable)
            - source_schema_id: Historical reference (immutable)
            - metadata: System-managed tenant metadata (immutable)
            - audit_info: System-managed audit trail (auto-updated by service)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | KnowledgeTopic]
    """

    kwargs = _get_kwargs(
        knowledge_topic_id=knowledge_topic_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_topic_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KnowledgeTopicUpdate,
) -> Any | HTTPValidationError | KnowledgeTopic | None:
    """Update Knowledge Topic

     Update individual values of an existing knowledge topic.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.

    Args:
        knowledge_topic_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (KnowledgeTopicUpdate): Model for updating a Knowledge Topic.

            Only allows updating:
            - knowledge_topic_name: The name of the knowledge topic
            - knowledge_topic_schema: The schema definition (form structure)
            - data: The actual data stored in the topic

            Excluded fields (immutable/system-managed):
            - knowledge_unit_history_id: Ownership relationship (immutable)
            - product_history_id: Ownership relationship (immutable)
            - type: Fundamental characteristic (immutable)
            - product_data_collection_id: Tied to type and relationships (immutable)
            - source_schema_id: Historical reference (immutable)
            - metadata: System-managed tenant metadata (immutable)
            - audit_info: System-managed audit trail (auto-updated by service)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | KnowledgeTopic
    """

    return sync_detailed(
        knowledge_topic_id=knowledge_topic_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    knowledge_topic_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KnowledgeTopicUpdate,
) -> Response[Any | HTTPValidationError | KnowledgeTopic]:
    """Update Knowledge Topic

     Update individual values of an existing knowledge topic.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.

    Args:
        knowledge_topic_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (KnowledgeTopicUpdate): Model for updating a Knowledge Topic.

            Only allows updating:
            - knowledge_topic_name: The name of the knowledge topic
            - knowledge_topic_schema: The schema definition (form structure)
            - data: The actual data stored in the topic

            Excluded fields (immutable/system-managed):
            - knowledge_unit_history_id: Ownership relationship (immutable)
            - product_history_id: Ownership relationship (immutable)
            - type: Fundamental characteristic (immutable)
            - product_data_collection_id: Tied to type and relationships (immutable)
            - source_schema_id: Historical reference (immutable)
            - metadata: System-managed tenant metadata (immutable)
            - audit_info: System-managed audit trail (auto-updated by service)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | KnowledgeTopic]
    """

    kwargs = _get_kwargs(
        knowledge_topic_id=knowledge_topic_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_topic_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KnowledgeTopicUpdate,
) -> Any | HTTPValidationError | KnowledgeTopic | None:
    """Update Knowledge Topic

     Update individual values of an existing knowledge topic.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.

    Args:
        knowledge_topic_id (str):  Example: 5eb7cf5a86d9755df3a6c593.
        body (KnowledgeTopicUpdate): Model for updating a Knowledge Topic.

            Only allows updating:
            - knowledge_topic_name: The name of the knowledge topic
            - knowledge_topic_schema: The schema definition (form structure)
            - data: The actual data stored in the topic

            Excluded fields (immutable/system-managed):
            - knowledge_unit_history_id: Ownership relationship (immutable)
            - product_history_id: Ownership relationship (immutable)
            - type: Fundamental characteristic (immutable)
            - product_data_collection_id: Tied to type and relationships (immutable)
            - source_schema_id: Historical reference (immutable)
            - metadata: System-managed tenant metadata (immutable)
            - audit_info: System-managed audit trail (auto-updated by service)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | KnowledgeTopic
    """

    return (
        await asyncio_detailed(
            knowledge_topic_id=knowledge_topic_id,
            client=client,
            body=body,
        )
    ).parsed
