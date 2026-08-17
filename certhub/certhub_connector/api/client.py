"""Thin wrappers over generated OpenAPI clients; return Pydantic models only."""

from __future__ import annotations

import json
from typing import Any

import httpx

from certhub_connector.api.api_models.records.records_models import Record, RecordCreate
from certhub_connector.api.api_models.techdoc.techdoc_models import (
    FullKnowledgeUnitView,
    KnowledgeTopicDetailResponse,
)
from certhub_connector.api.parse import (
    parse_knowledge_topic,
    parse_model_json,
    parse_records_list,
)
from certhub_connector.api.clients.records.api.records import (
    create_new_record_records_post,
    delete_existing_record_records_id_delete,
    list_records_records_get,
    read_record_records_id_get,
)
from certhub_connector.api.clients.records.client import Client as RecordsHttpClient
from certhub_connector.api.clients.records.models.record_create import (
    RecordCreate as AttrsRecordCreate,
)
from certhub_connector.api.clients.techdoc.api.knowledge_topics import (
    get_kt_kt_knowledge_topic_id_get,
)
from certhub_connector.api.clients.techdoc.api.knowledge_units import (
    get_ku_with_topics_by_version_or_latest_ku_knowledge_unit_history_id_get as get_ku_mod,
)
from certhub_connector.api.clients.techdoc.client import Client as TechDocHttpClient
from certhub_connector.api.clients.tracer.api.default import (
    batch_retrieve_traces_traces_batch_list_post as batch_list_mod,
)
from certhub_connector.api.clients.tracer.client import Client as TracerHttpClient
from certhub_connector.api.clients.tracer.models.batch_retrieve_mode import BatchRetrieveMode
from certhub_connector.api.clients.tracer.models.batch_retrieve_node import BatchRetrieveNode
from certhub_connector.api.clients.tracer.models.batch_retrieve_request import (
    BatchRetrieveRequest,
)
from certhub_connector.api.clients.tracer.models.node_type import NodeType
from certhub_connector.config import CerthubConfig


def _x_api_key_headers(api_key: str) -> dict[str, str]:
    if not api_key:
        raise ValueError("Missing required field: 'api_key'")
    return {
        "X-API-Key": api_key,
        "Accept": "application/json",
    }


class TechDocClient:
    """Tech Doc wrapper: GET /kt/{id} and KU history → Pydantic models."""

    def __init__(self, config: CerthubConfig, *, timeout_s: float = 30.0) -> None:
        if not config:
            raise ValueError("Missing required field: 'config'")
        if not config.techdoc_base_url:
            raise ValueError("Missing required field: 'techdoc_base_url'")
        self._config = config
        self._client = TechDocHttpClient(
            base_url=config.techdoc_base_url,
            headers=_x_api_key_headers(config.api_key),
            timeout=httpx.Timeout(timeout_s),
            raise_on_unexpected_status=False,
        )

    @property
    def config(self) -> CerthubConfig:
        return self._config

    def get_kt(self, knowledge_topic_id: str) -> KnowledgeTopicDetailResponse:
        kt_id = (knowledge_topic_id or "").strip()
        if not kt_id:
            raise ValueError("Missing required field: 'knowledge_topic_id'")
        try:
            response = get_kt_kt_knowledge_topic_id_get.sync_detailed(
                kt_id,
                client=self._client,
            )
        except httpx.HTTPError as exc:
            raise RuntimeError(f"CertHub Tech Doc request failed: {exc}") from exc

        if response.status_code == 401:
            raise PermissionError(
                "CertHub Tech Doc rejected the API key (401). "
                "Check CERTHUB_API_KEY and that the key uses the X-API-Key header."
            )
        if response.status_code == 404:
            raise FileNotFoundError(f"Knowledge topic not found: {kt_id}")
        if response.status_code >= 400:
            body = response.content.decode("utf-8", errors="replace")[:500]
            raise RuntimeError(
                f"CertHub Tech Doc error {response.status_code} for /kt/{kt_id}: {body}"
            )
        return parse_knowledge_topic(response.content)

    def get_ku_latest_revision_id(self, knowledge_unit_history_id: str) -> str:
        """Resolve KU history id → latest revision id (Records ``context.knowledge_unit_id``).

        Uses ``GET /ku/{history_id}`` (API-key friendly). ``/ku/histories/{id}`` often
        returns 401 for the same key.
        """
        history_id = (knowledge_unit_history_id or "").strip()
        if not history_id:
            raise ValueError("Missing required field: 'knowledge_unit_history_id'")
        try:
            response = get_ku_mod.sync_detailed(
                history_id,
                client=self._client,
            )
        except httpx.HTTPError as exc:
            raise RuntimeError(f"CertHub Tech Doc KU request failed: {exc}") from exc

        if response.status_code == 401:
            raise PermissionError(
                "CertHub Tech Doc rejected the API key (401). "
                "Check CERTHUB_API_KEY and that the key uses the X-API-Key header."
            )
        if response.status_code == 404:
            raise FileNotFoundError(f"Knowledge unit not found: {history_id}")
        if response.status_code >= 400:
            body = response.content.decode("utf-8", errors="replace")[:500]
            raise RuntimeError(
                f"CertHub Tech Doc error {response.status_code} "
                f"for /ku/{history_id}: {body}"
            )
        ku = parse_model_json(FullKnowledgeUnitView, response.content)
        revision_id = (ku.id or "").strip()
        if not revision_id:
            raise RuntimeError(f"KU {history_id} response has no id (revision)")
        return revision_id


class RecordsClient:
    """Records wrapper: list/create/get/delete → Pydantic Record models."""

    def __init__(self, config: CerthubConfig, *, timeout_s: float = 30.0) -> None:
        if not config:
            raise ValueError("Missing required field: 'config'")
        if not config.records_base_url:
            raise ValueError("Missing required field: 'records_base_url'")
        self._config = config
        self._client = RecordsHttpClient(
            base_url=config.records_base_url,
            headers=_x_api_key_headers(config.api_key),
            timeout=httpx.Timeout(timeout_s),
            raise_on_unexpected_status=False,
        )

    @property
    def config(self) -> CerthubConfig:
        return self._config

    def list_records_for_kt(self, knowledge_topic_id: str) -> list[Record]:
        kt_id = (knowledge_topic_id or "").strip()
        if not kt_id:
            raise ValueError("Missing required field: 'knowledge_topic_id'")
        try:
            response = list_records_records_get.sync_detailed(
                client=self._client,
                context_knowledge_unit_topic_id=kt_id,
            )
        except httpx.HTTPError as exc:
            raise RuntimeError(f"CertHub Records request failed: {exc}") from exc

        if response.status_code == 401:
            raise PermissionError(
                "CertHub Records rejected the API key (401). "
                "Check CERTHUB_API_KEY and that the key uses the X-API-Key header."
            )
        if response.status_code >= 400:
            body = response.content.decode("utf-8", errors="replace")[:500]
            raise RuntimeError(
                f"CertHub Records error {response.status_code} listing KT {kt_id}: {body}"
            )
        return parse_records_list(response.content)

    def create_record(self, record: RecordCreate) -> Record:
        if not record:
            raise ValueError("Missing required field: 'record'")
        body = AttrsRecordCreate.from_dict(
            record.model_dump(by_alias=True, exclude_none=True)
        )
        try:
            response = create_new_record_records_post.sync_detailed(
                client=self._client,
                body=body,
            )
        except httpx.HTTPError as exc:
            raise RuntimeError(f"CertHub Records create failed: {exc}") from exc

        if response.status_code == 401:
            raise PermissionError(
                "CertHub Records rejected the API key (401). "
                "Check CERTHUB_API_KEY and that the key uses the X-API-Key header."
            )
        if response.status_code >= 400:
            body_text = response.content.decode("utf-8", errors="replace")[:800]
            raise RuntimeError(
                f"CertHub Records create error {response.status_code}: {body_text}"
            )
        return parse_model_json(Record, response.content)

    def get_record(self, record_id: str) -> Record:
        if not record_id or not record_id.strip():
            raise ValueError("Missing required field: 'record_id'")
        rid = record_id.strip()
        try:
            response = read_record_records_id_get.sync_detailed(
                rid,
                client=self._client,
            )
        except httpx.HTTPError as exc:
            raise RuntimeError(f"CertHub Records get failed: {exc}") from exc

        if response.status_code == 401:
            raise PermissionError(
                "CertHub Records rejected the API key (401). "
                "Check CERTHUB_API_KEY and that the key uses the X-API-Key header."
            )
        if response.status_code == 404:
            raise FileNotFoundError(f"Record not found: {rid}")
        if response.status_code >= 400:
            body_text = response.content.decode("utf-8", errors="replace")[:500]
            raise RuntimeError(
                f"CertHub Records get error {response.status_code}: {body_text}"
            )
        return parse_model_json(Record, response.content)

    def delete_record(self, record_id: str) -> None:
        if not record_id or not record_id.strip():
            raise ValueError("Missing required field: 'record_id'")
        rid = record_id.strip()
        try:
            response = delete_existing_record_records_id_delete.sync_detailed(
                rid,
                client=self._client,
            )
        except httpx.HTTPError as exc:
            raise RuntimeError(f"CertHub Records delete failed: {exc}") from exc

        if response.status_code == 401:
            raise PermissionError(
                "CertHub Records rejected the API key (401). "
                "Check CERTHUB_API_KEY and that the key uses the X-API-Key header."
            )
        if response.status_code == 404:
            raise FileNotFoundError(f"Record not found: {rid}")
        if response.status_code >= 400:
            body_text = response.content.decode("utf-8", errors="replace")[:500]
            raise RuntimeError(
                f"CertHub Records delete error {response.status_code}: {body_text}"
            )


class TracerClient:
    """Tracer wrapper: batch-list Record traces → raw ``results`` dict."""

    def __init__(self, config: CerthubConfig, *, timeout_s: float = 60.0) -> None:
        if not config:
            raise ValueError("Missing required field: 'config'")
        if not config.tracer_base_url:
            raise ValueError("Missing required field: 'tracer_base_url'")
        self._config = config
        self._client = TracerHttpClient(
            base_url=config.tracer_base_url,
            headers=_x_api_key_headers(config.api_key),
            timeout=httpx.Timeout(timeout_s),
            raise_on_unexpected_status=False,
        )

    @property
    def config(self) -> CerthubConfig:
        return self._config

    def batch_list_records(self, record_ids: list[str]) -> dict[str, Any]:
        """POST /traces/batch/list for Record nodes; return ``results`` mapping."""
        if record_ids is None:
            raise ValueError("Missing required field: 'record_ids'")
        ids = [rid.strip() for rid in record_ids if rid and rid.strip()]
        if not ids:
            return {}
        body = BatchRetrieveRequest(
            nodes=[
                BatchRetrieveNode(
                    node_id=rid,
                    node_type=NodeType.RECORD,
                    version="",
                )
                for rid in ids
            ],
            n_hops=1,
            mode=BatchRetrieveMode.LEGACY_CONNECTED_NODES,
        )
        try:
            response = batch_list_mod.sync_detailed(client=self._client, body=body)
        except httpx.HTTPError as exc:
            raise RuntimeError(f"CertHub Tracer request failed: {exc}") from exc

        if response.status_code == 401:
            raise PermissionError(
                "CertHub Tracer rejected the API key (401). "
                "Check CERTHUB_API_KEY and that the key uses the X-API-Key header."
            )
        if response.status_code >= 400:
            body_text = response.content.decode("utf-8", errors="replace")[:800]
            raise RuntimeError(
                f"CertHub Tracer error {response.status_code} for "
                f"/traces/batch/list: {body_text}"
            )
        payload = json.loads(response.content.decode("utf-8"))
        results = payload.get("results")
        if not isinstance(results, dict):
            raise RuntimeError("CertHub Tracer batch/list response missing 'results'")
        return results
