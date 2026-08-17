from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.guidance_phase_response import GuidancePhaseResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: str | Unset = "en",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/guidance/template",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[GuidancePhaseResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GuidancePhaseResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | HTTPValidationError | list[GuidancePhaseResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: str | Unset = "en",
) -> Response[Any | HTTPValidationError | list[GuidancePhaseResponse]]:
    """Get Guidance Template Endpoint

     Return guidance phases from DB in the requested language (en / de).

    Args:
        lang (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[GuidancePhaseResponse]]
    """

    kwargs = _get_kwargs(
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lang: str | Unset = "en",
) -> Any | HTTPValidationError | list[GuidancePhaseResponse] | None:
    """Get Guidance Template Endpoint

     Return guidance phases from DB in the requested language (en / de).

    Args:
        lang (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[GuidancePhaseResponse]
    """

    return sync_detailed(
        client=client,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: str | Unset = "en",
) -> Response[Any | HTTPValidationError | list[GuidancePhaseResponse]]:
    """Get Guidance Template Endpoint

     Return guidance phases from DB in the requested language (en / de).

    Args:
        lang (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[GuidancePhaseResponse]]
    """

    kwargs = _get_kwargs(
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lang: str | Unset = "en",
) -> Any | HTTPValidationError | list[GuidancePhaseResponse] | None:
    """Get Guidance Template Endpoint

     Return guidance phases from DB in the requested language (en / de).

    Args:
        lang (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[GuidancePhaseResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
        )
    ).parsed
