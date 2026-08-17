"""Parse CertHub API JSON into generated Pydantic models as early as possible."""

from __future__ import annotations

import json
from typing import Any, TypeVar

from pydantic import BaseModel, TypeAdapter

from certhub_connector.api.api_models.records.records_models import Record
from certhub_connector.api.api_models.techdoc.techdoc_models import (
    KnowledgeTopicDetailResponse,
)

T = TypeVar("T", bound=BaseModel)


def parse_model(model_type: type[T], payload: Any) -> T:
    """Validate ``payload`` into ``model_type`` immediately."""
    if not model_type:
        raise ValueError("Missing required field: 'model_type'")
    return model_type.model_validate(payload)


def parse_model_json(model_type: type[T], raw: bytes | str) -> T:
    """Parse JSON bytes/str into ``model_type`` immediately."""
    if not raw:
        raise ValueError("Missing required field: 'raw'")
    return parse_model(model_type, json.loads(raw))


def parse_knowledge_topic(
    raw: bytes | str | dict[str, Any],
) -> KnowledgeTopicDetailResponse:
    if isinstance(raw, dict):
        return parse_model(KnowledgeTopicDetailResponse, raw)
    return parse_model_json(KnowledgeTopicDetailResponse, raw)


def parse_records_list(raw: bytes | str | list[Any]) -> list[Record]:
    adapter = TypeAdapter(list[Record])
    if isinstance(raw, list):
        return adapter.validate_python(raw)
    payload = json.loads(raw)
    if not isinstance(payload, list):
        raise ValueError(
            f"Expected JSON array of records, got {type(payload).__name__}"
        )
    return adapter.validate_python(payload)
