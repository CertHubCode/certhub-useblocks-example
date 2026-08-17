"""Push release evidence into CertHub Release Record KT
(``release_record_kt_id`` in certhub.toml).
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from certhub_connector.api.api_models.records.records_models import RecordContext, RecordCreate
from certhub_connector.api.api_models.techdoc.techdoc_models import (
    KnowledgeTopicDetailResponse,
)
from certhub_connector.sync.keys import (
    REQUIRED_RELEASE_EVIDENCE_KEYS,
    CerthubKeyMap,
    certhub_key_map_from_schema,
)
from certhub_connector.api.client import RecordsClient, TechDocClient
from certhub_connector.config import CerthubConfig
from certhub_connector.evidence.pack import (
    EvidenceManifest,
    load_evidence_manifest,
    load_evidence_result,
    resolve_evidence_url,
)

_RELEASE_VERSION_RE = re.compile(
    r"^v?(?P<version>\d+\.\d+\.\d+)$",
    re.IGNORECASE,
)
_DETAILS_PREVIEW_CHARS = 200


class ReleaseEvidenceFields(BaseModel):
    """Semantic field values before mapping onto opaque form keys."""

    model_config = ConfigDict(frozen=True)

    release_number: str
    release_id: str
    generated_at: str
    evidence_url: str
    details: str

    @field_validator(
        "release_number",
        "release_id",
        "generated_at",
        "evidence_url",
        "details",
    )
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Release evidence fields must be non-empty")
        return value.strip()


class PushEvidenceResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    dry_run: bool
    record_id: str | None = None
    payload: RecordCreate
    fields: ReleaseEvidenceFields
    key_map: dict[str, str] = Field(default_factory=dict)


class ConfirmProof(BaseModel):
    model_config = ConfigDict(frozen=True)

    record_id: str
    kt_id: str
    release_number: str
    release_id: str
    generated_at: str
    evidence_url: str
    details_preview: str
    matched: bool


def normalize_release_baseline(baseline: str) -> str:
    """Accept ``1.0.0`` or ``v1.0.0``; reject branches / RC tags."""
    if not baseline or not baseline.strip():
        raise ValueError("Missing required field: 'baseline'")
    raw = baseline.strip()
    if raw.lower() in {"main", "master", "head"}:
        raise ValueError(
            f"Refusing baseline {raw!r}: use an explicit release version, not a branch"
        )
    if "rc" in raw.lower():
        raise ValueError(
            f"Refusing baseline {raw!r}: RC tags do not sync to CertHub "
            "(artifact-only). Use a full release vX.Y.Z."
        )
    match = _RELEASE_VERSION_RE.fullmatch(raw)
    if not match:
        raise ValueError(
            f"Invalid release baseline {raw!r}; expected vX.Y.Z or X.Y.Z"
        )
    return match.group("version")


def format_release_details_text(
    result: dict[str, object],
    manifest: EvidenceManifest,
) -> str:
    """Short plain-text Notes body for CertHub Release Record."""
    status = result.get("certificationStatus") or manifest.certification_status
    project = result.get("project") or "unknown"
    version = result.get("version") or "unknown"
    totals_raw = result.get("totals")
    totals: dict[str, object] = totals_raw if isinstance(totals_raw, dict) else {}
    requirements_count = totals.get("system_requirements", totals.get("requirements", 0))
    verified = totals.get("verified", 0)
    passed = totals.get("passed", 0)
    failed = totals.get("failed", 0)

    lines = [
        f"Certification: {status}",
        f"Project: {project}  Version: {version}",
        "",
        f"System Requirements: {requirements_count}",
        f"Verified: {verified} / {requirements_count}",
        f"Passed: {passed}  Failed: {failed}",
        "",
    ]

    requirements = result.get("requirements")
    if isinstance(requirements, list):
        for item in requirements:
            if not isinstance(item, dict):
                continue
            req_id = item.get("id")
            req_status = item.get("status")
            if not isinstance(req_id, str) or not req_id.strip():
                continue
            status_label = (
                req_status.strip()
                if isinstance(req_status, str) and req_status.strip()
                else "unknown"
            )
            lines.append(f"{req_id.strip()}  {status_label}")

    result_sha = manifest.artifact_hashes.get("certhub_result.json") or "unknown"
    lines.append("")
    lines.append(f"Result SHA: {result_sha}")
    text = "\n".join(lines).strip()
    if not text:
        raise ValueError("Release details text must be non-empty")
    return text


def build_release_fields(
    *,
    baseline: str,
    evidence_path: Path,
    evidence_url: str | None = None,
) -> tuple[ReleaseEvidenceFields, EvidenceManifest]:
    version = normalize_release_baseline(baseline)
    result = load_evidence_result(evidence_path)
    manifest = load_evidence_manifest(evidence_path)
    url = (evidence_url or manifest.evidence_url or resolve_evidence_url() or "").strip()
    if not url:
        url = f"local://evidence/{version}/{manifest.git_commit}"
    details = format_release_details_text(result, manifest)
    commit = manifest.git_commit
    result_commit = result.get("commit")
    if isinstance(result_commit, str) and result_commit.strip():
        commit = result_commit.strip()
    generated_at = manifest.generated_at
    result_generated = result.get("generatedAt")
    if isinstance(result_generated, str) and result_generated.strip():
        generated_at = result_generated.strip()
    fields = ReleaseEvidenceFields(
        release_number=version,
        release_id=commit,
        generated_at=generated_at,
        evidence_url=url,
        details=details,
    )
    return fields, manifest


def map_fields_to_form_data(
    fields: ReleaseEvidenceFields,
    key_map: CerthubKeyMap,
) -> dict[str, Any]:
    key_map.require_all(REQUIRED_RELEASE_EVIDENCE_KEYS)
    return {
        key_map.form_key("release-number"): fields.release_number,
        key_map.form_key("release-id"): fields.release_id,
        key_map.form_key("generated-at"): fields.generated_at,
        key_map.form_key("evidence-url"): fields.evidence_url,
        key_map.form_key("details"): fields.details,
    }


def build_record_create(
    *,
    fields: ReleaseEvidenceFields,
    key_map: CerthubKeyMap,
    kt: KnowledgeTopicDetailResponse,
    knowledge_unit_id: str,
) -> RecordCreate:
    """Build create payload; ``knowledge_unit_id`` must be KU *revision* id (not history)."""
    if not knowledge_unit_id or not knowledge_unit_id.strip():
        raise ValueError("Missing required field: 'knowledge_unit_id'")
    data = map_fields_to_form_data(fields, key_map)
    return RecordCreate(
        name=f"Release Evidence {fields.release_number}",
        form={},
        data=data,
        context=RecordContext(
            knowledge_unit_topic_id=kt.field_id,
            knowledge_unit_id=knowledge_unit_id.strip(),
            linked_product=kt.product_history_id,
        ),
        read_only=True,
    )


def push_evidence(
    *,
    baseline: str,
    evidence_path: Path,
    config: CerthubConfig | None = None,
    dry_run: bool = True,
    evidence_url: str | None = None,
) -> PushEvidenceResult:
    config = config or CerthubConfig.load()
    fields, _manifest = build_release_fields(
        baseline=baseline,
        evidence_path=evidence_path,
        evidence_url=evidence_url,
    )
    techdoc = TechDocClient(config)
    kt = techdoc.get_kt(config.release_record_kt_id)
    ku_revision_id = techdoc.get_ku_latest_revision_id(kt.knowledge_unit_history_id)
    key_map = certhub_key_map_from_schema(kt.knowledge_topic_schema)
    payload = build_record_create(
        fields=fields,
        key_map=key_map,
        kt=kt,
        knowledge_unit_id=ku_revision_id,
    )

    if dry_run:
        return PushEvidenceResult(
            dry_run=True,
            record_id=None,
            payload=payload,
            fields=fields,
            key_map=dict(key_map.mapping),
        )

    records = RecordsClient(config)
    created = records.create_record(payload)
    record_id = created.field_id
    if not record_id:
        raise RuntimeError("CertHub create_record returned no _id")
    return PushEvidenceResult(
        dry_run=False,
        record_id=record_id,
        payload=payload,
        fields=fields,
        key_map=dict(key_map.mapping),
    )


def _values_match(certhub_key: str, expected: object, actual: object) -> bool:
    if expected == actual:
        return True
    if certhub_key != "generated-at":
        return False
    if not isinstance(expected, str) or not isinstance(actual, str):
        return False

    def _parse(value: str) -> datetime:
        normalized = value.strip().replace("Z", "+00:00")
        parsed = datetime.fromisoformat(normalized)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=timezone.utc)
        return parsed

    try:
        return abs((_parse(expected) - _parse(actual)).total_seconds()) < 2
    except ValueError:
        return expected.replace("+00:00", "Z") == actual.replace("+00:00", "Z")

def confirm_evidence(
    *,
    baseline: str,
    evidence_path: Path,
    config: CerthubConfig | None = None,
    cleanup: bool = False,
    evidence_url: str | None = None,
) -> ConfirmProof:
    """POST → GET → assert fields match; print-ready proof object."""
    config = config or CerthubConfig.load()
    pushed = push_evidence(
        baseline=baseline,
        evidence_path=evidence_path,
        config=config,
        dry_run=False,
        evidence_url=evidence_url,
    )
    if not pushed.record_id:
        raise RuntimeError("push_evidence did not return a record id")

    records = RecordsClient(config)
    fetched = records.get_record(pushed.record_id)
    key_map = CerthubKeyMap(mapping=pushed.key_map)
    data = fetched.data or {}

    expected = {
        "release-number": pushed.fields.release_number,
        "release-id": pushed.fields.release_id,
        "generated-at": pushed.fields.generated_at,
        "evidence-url": pushed.fields.evidence_url,
        "details": pushed.fields.details,
    }
    mismatches: list[str] = []
    for certhub_key, expected_value in expected.items():
        form_key = key_map.form_key(certhub_key)
        actual = data.get(form_key)
        if not _values_match(certhub_key, expected_value, actual):
            mismatches.append(
                f"{certhub_key} ({form_key}): expected {expected_value!r}, got {actual!r}"
            )

    details = pushed.fields.details
    if not details.strip():
        mismatches.append("details text is empty")
    elif not details.startswith("Certification:"):
        mismatches.append("details missing Certification status line")
    if "Result SHA:" not in details:
        mismatches.append("details missing Result SHA line")

    matched = not mismatches
    preview = details[:_DETAILS_PREVIEW_CHARS]
    if len(details) > _DETAILS_PREVIEW_CHARS:
        preview = preview.rstrip() + "…"
    proof = ConfirmProof(
        record_id=pushed.record_id,
        kt_id=config.release_record_kt_id,
        release_number=pushed.fields.release_number,
        release_id=pushed.fields.release_id,
        generated_at=pushed.fields.generated_at,
        evidence_url=pushed.fields.evidence_url,
        details_preview=preview,
        matched=matched,
    )

    if cleanup:
        records.delete_record(pushed.record_id)

    if mismatches:
        raise AssertionError(
            "Confirm round-trip failed:\n  - " + "\n  - ".join(mismatches)
        )
    return proof


def format_proof(proof: ConfirmProof) -> str:
    lines = [
        "PROOF",
        "=====",
        f"record_id:        {proof.record_id}",
        f"kt_id:            {proof.kt_id}",
        f"release_number:   {proof.release_number}",
        f"release_id:       {proof.release_id}",
        f"generated_at:     {proof.generated_at}",
        f"evidence_url:     {proof.evidence_url}",
        f"details_preview:  {proof.details_preview!r}",
        f"matched:          {proof.matched}",
        f"confirmed_at:     {datetime.now(timezone.utc).isoformat()}",
    ]
    return "\n".join(lines)
