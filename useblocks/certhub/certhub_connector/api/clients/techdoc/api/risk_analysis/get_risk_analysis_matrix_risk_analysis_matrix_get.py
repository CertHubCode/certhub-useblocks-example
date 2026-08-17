from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.risk_analysis_matrix_response import RiskAnalysisMatrixResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    product_history_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["product_history_id"] = product_history_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/risk-analysis/matrix",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | RiskAnalysisMatrixResponse | None:
    if response.status_code == 200:
        response_200 = RiskAnalysisMatrixResponse.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | RiskAnalysisMatrixResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_history_id: str,
) -> Response[Any | HTTPValidationError | RiskAnalysisMatrixResponse]:
    r"""Get Risk Analysis Matrix

     Compute the Risk Analysis matrix for every \"Risks\" record in a product.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | RiskAnalysisMatrixResponse]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product_history_id: str,
) -> Any | HTTPValidationError | RiskAnalysisMatrixResponse | None:
    r"""Get Risk Analysis Matrix

     Compute the Risk Analysis matrix for every \"Risks\" record in a product.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | RiskAnalysisMatrixResponse
    """

    return sync_detailed(
        client=client,
        product_history_id=product_history_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_history_id: str,
) -> Response[Any | HTTPValidationError | RiskAnalysisMatrixResponse]:
    r"""Get Risk Analysis Matrix

     Compute the Risk Analysis matrix for every \"Risks\" record in a product.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | RiskAnalysisMatrixResponse]
    """

    kwargs = _get_kwargs(
        product_history_id=product_history_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product_history_id: str,
) -> Any | HTTPValidationError | RiskAnalysisMatrixResponse | None:
    r"""Get Risk Analysis Matrix

     Compute the Risk Analysis matrix for every \"Risks\" record in a product.

    Args:
        product_history_id (str):  Example: 5eb7cf5a86d9755df3a6c593.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | RiskAnalysisMatrixResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            product_history_id=product_history_id,
        )
    ).parsed
