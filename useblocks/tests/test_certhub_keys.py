"""Unit tests for certhub-key → form key mapping (no network)."""

from __future__ import annotations

import pytest

from certhub_connector.sync.keys import (
    REQUIRED_RELEASE_EVIDENCE_KEYS,
    certhub_key_map_from_schema,
)


VALIDATION_RECORDS_SCHEMA = {
    "components": [
        {
            "label": "Release Number",
            "key": "textfield_xd6x5",
            "properties": {"certhub-key": "release-number"},
        },
        {
            "label": "Commit-Id",
            "key": "textfield_7qosf",
            "properties": {"certhub-key": "release-id"},
        },
        {
            "label": "Generated at",
            "key": "datetime_qp65ok",
            "properties": {"certhub-key": "generated-at"},
        },
        {
            "label": "Evidence Url",
            "key": "textfield_pikby9",
            "properties": {"certhub-key": "evidence-url"},
        },
        {
            "label": "Notes",
            "key": "textfield_bw3z2q",
            "properties": {"certhub-key": "details"},
        },
    ],
    "id": "form_1",
    "type": "default",
}


def test_certhub_key_map_from_release_record_schema() -> None:
    key_map = certhub_key_map_from_schema(VALIDATION_RECORDS_SCHEMA)
    key_map.require_all(REQUIRED_RELEASE_EVIDENCE_KEYS)
    assert key_map.form_key("release-number") == "textfield_xd6x5"
    assert key_map.form_key("release-id") == "textfield_7qosf"
    assert key_map.form_key("generated-at") == "datetime_qp65ok"
    assert key_map.form_key("evidence-url") == "textfield_pikby9"
    assert key_map.form_key("details") == "textfield_bw3z2q"


def test_certhub_key_map_fails_loud_on_missing_key() -> None:
    key_map = certhub_key_map_from_schema(
        {"components": [{"key": "a", "properties": {"certhub-key": "release-number"}}]}
    )
    with pytest.raises(ValueError, match="missing required certhub-keys"):
        key_map.require_all(REQUIRED_RELEASE_EVIDENCE_KEYS)


def test_normalize_release_baseline() -> None:
    from certhub_connector.evidence.push import normalize_release_baseline

    assert normalize_release_baseline("v1.2.3") == "1.2.3"
    assert normalize_release_baseline("1.2.3") == "1.2.3"
    with pytest.raises(ValueError, match="main"):
        normalize_release_baseline("main")
    with pytest.raises(ValueError, match="RC"):
        normalize_release_baseline("v1.2.3-rc.1")


def test_build_record_create_uses_ku_revision_not_history() -> None:
    from certhub_connector.api.api_models.techdoc.techdoc_models import (
        KnowledgeTopicDetailResponse,
        KnowledgeTopicType,
    )
    from certhub_connector.sync.keys import certhub_key_map_from_schema
    from certhub_connector.evidence.push import (
        ReleaseEvidenceFields,
        build_record_create,
    )

    kt = KnowledgeTopicDetailResponse.model_validate(
        {
            "_id": "6a79c7cca446feb63f8cb3a4",
            "knowledge_topic_name": "Release Record",
            "type": KnowledgeTopicType.multi_record,
            "knowledge_topic_history_id": "6a79c7cca446feb63f8cb3a3",
            "product_history_id": "69b9899f4252b7481003afaa",
            "product_version": "0.1",
            "knowledge_unit_history_id": "69b989a14252b7481003afe5",
            "knowledge_unit_version": "0.1",
            "knowledge_topic_schema": VALIDATION_RECORDS_SCHEMA,
            "metadata": {"tenant_id": "bd71306e-90ea-43e5-af42-9239b7e7920b"},
        }
    )
    ku_revision_id = "69b989a14252b7481003afe6"
    fields = ReleaseEvidenceFields(
        release_number="1.0.0",
        release_id="abc123",
        generated_at="2026-08-08T12:00:00+00:00",
        evidence_url="https://example.test/evidence",
        details=(
            "Certification: VERIFIED\n"
            "Project: demo  Version: 1.0.0\n"
            "\n"
            "Requirements: 1\n"
            "Verified: 1 / 1\n"
            "Passed: 1  Failed: 0\n"
            "\n"
            "REQ_001  verified\n"
            "\n"
            "Result SHA: abc"
        ),
    )
    payload = build_record_create(
        fields=fields,
        key_map=certhub_key_map_from_schema(VALIDATION_RECORDS_SCHEMA),
        kt=kt,
        knowledge_unit_id=ku_revision_id,
    )
    assert payload.context.linked_product == "69b9899f4252b7481003afaa"
    assert payload.context.knowledge_unit_topic_id == "6a79c7cca446feb63f8cb3a4"
    assert payload.context.knowledge_unit_id == ku_revision_id
    assert payload.context.knowledge_unit_id != kt.knowledge_unit_history_id

    with pytest.raises(ValueError, match="knowledge_unit_id"):
        build_record_create(
            fields=fields,
            key_map=certhub_key_map_from_schema(VALIDATION_RECORDS_SCHEMA),
            kt=kt,
            knowledge_unit_id="",
        )


def test_semanticize_removes_opaque_keys_from_model() -> None:
    from certhub_connector.sync.keys import semanticize_record_data
    from certhub_connector.sync.models import VerificationFormData

    raw = {
        "name": "TEST_001",
        "test_method": "unit",
        "textfield_u1u4nh": "REQ_001, SPEC_001",
        "textarea_d1jh7": "accepted",
    }
    form = VerificationFormData.model_validate(semanticize_record_data(raw))
    assert form.standard_clause == "REQ_001, SPEC_001"
    assert form.acceptance_criteria == "accepted"
    dumped = form.model_dump()
    assert "textfield_u1u4nh" not in dumped
    assert "textarea_d1jh7" not in dumped
