"""Mapper + Tracer use-case join tests."""

from __future__ import annotations

import json
import logging
from pathlib import Path

import pytest

from certhub_connector.api.parse import parse_knowledge_topic, parse_records_list
from certhub_connector.sync.mapper import (
    form_data_from_record,
    map_records_to_export,
)
from certhub_connector.sync.requirements_use_case import (
    TOPIC_COMPONENT,
    TOPIC_DESIGN_OUTPUT,
    TOPIC_SYSTEM,
    TOPIC_VERIFICATION,
    relation_for,
)
from certhub_connector.sync import write_generated_files
from certhub_connector.sync.trace_links import apply_usecase_links, usecase_neighbors

FIXTURES = Path(__file__).resolve().parent / "fixtures"
_PRODUCT_VERSION = "0.1"


def _load_three() -> tuple:
    kt = parse_knowledge_topic((FIXTURES / "kt_sample.json").read_text(encoding="utf-8"))
    requirements = parse_records_list(
        (FIXTURES / "requirements_sample.json").read_text(encoding="utf-8")
    )
    verification = parse_records_list(
        (FIXTURES / "verification_sample.json").read_text(encoding="utf-8")
    )
    validation = parse_records_list(
        (FIXTURES / "validation_sample.json").read_text(encoding="utf-8")
    )
    return kt, requirements, verification, validation


def _fixture_topics(requirements, verification, validation) -> dict[str, str]:
    topics: dict[str, str] = {}
    for record in requirements:
        topics[record.field_id] = TOPIC_SYSTEM
    for record in verification:
        topics[record.field_id] = TOPIC_VERIFICATION
    for record in validation:
        topics[record.field_id] = "Validation"
    return topics


def test_parse_requirements_fixture_into_pydantic() -> None:
    records = parse_records_list(
        (FIXTURES / "requirements_sample.json").read_text(encoding="utf-8")
    )
    assert len(records) == 4
    assert records[0].field_id == "6a7701ffcd5640b4bf28b05e"
    form = form_data_from_record(records[0])
    assert "Sterilization temperature range is better" in form.name
    assert form.priority == "high"


def test_relation_for_topic_pairs() -> None:
    assert relation_for(TOPIC_SYSTEM, TOPIC_VERIFICATION) == "Verified By"
    assert relation_for(TOPIC_VERIFICATION, TOPIC_SYSTEM) == "Verifies SR"
    assert relation_for(TOPIC_DESIGN_OUTPUT, TOPIC_SYSTEM) == "Relates to SR"
    assert relation_for(TOPIC_VERIFICATION, TOPIC_DESIGN_OUTPUT) == "Verifies DO"
    assert relation_for(TOPIC_DESIGN_OUTPUT, TOPIC_COMPONENT) == "Relates to CR"
    assert relation_for(TOPIC_SYSTEM, TOPIC_DESIGN_OUTPUT) is None


def test_usecase_neighbors_undirected_and_filters() -> None:
    known = {"sys-1", "ver-1", "other"}
    results = {
        "Record:sys-1:": {
            "edges": [
                {
                    "relation_type": ["connected_within_use_case"],
                    "source_node": {"node_id": "sys-1"},
                    "target_node": {"node_id": "ver-1"},
                },
                {
                    "relation_type": ["connected_within_use_case"],
                    "source_node": {"node_id": "sys-1"},
                    "target_node": {"node_id": "sys-1"},
                },
                {
                    "relation_type": ["is_related"],
                    "source_node": {"node_id": "sys-1"},
                    "target_node": {"node_id": "other"},
                },
                {
                    "relation_type": ["connected_within_use_case"],
                    "source_node": {"node_id": "sys-1"},
                    "target_node": {"node_id": "unknown"},
                },
            ]
        }
    }
    neighbors = usecase_neighbors(results, known)
    assert neighbors["sys-1"] == {"ver-1"}
    assert neighbors["ver-1"] == {"sys-1"}
    assert neighbors["other"] == set()


def test_apply_usecase_links_sets_verifies_and_logs(caplog: pytest.LogCaptureFixture) -> None:
    from certhub_connector.sync.models import SystemRequirement, Verification

    sysreq = SystemRequirement(
        id="SYSREQ_001",
        title="Temp",
        description="d",
        external_id="sys-1",
    )
    verif = Verification(
        id="VERIF_001",
        title="Test",
        description="d",
        external_id="ver-1",
    )
    need_by = {"sys-1": sysreq, "ver-1": verif}
    topics = {"sys-1": TOPIC_SYSTEM, "ver-1": TOPIC_VERIFICATION}
    neighbors = {"sys-1": {"ver-1"}, "ver-1": {"sys-1"}}
    with caplog.at_level(logging.INFO, logger="certhub_connector.sync.trace_links"):
        lines = apply_usecase_links(need_by, topics, neighbors)
    assert "VERIF_001" in sysreq.links
    assert "SYSREQ_001" in verif.links
    assert verif.verifies == ["SYSREQ_001"]
    assert any("Verified By" in line for line in lines)
    assert any("Verifies SR" in line for line in lines)
    assert any("Verified By" in r.message for r in caplog.records)


def test_map_with_tracer_neighbors() -> None:
    kt, requirements, verification, validation = _load_three()
    sys_ext = sorted(requirements, key=lambda r: r.field_id or "")[0].field_id
    ver_ext = sorted(verification, key=lambda r: r.field_id or "")[0].field_id
    topics = _fixture_topics(requirements, verification, validation)
    neighbors = {sys_ext: {ver_ext}, ver_ext: {sys_ext}}
    export = map_records_to_export(
        kt,
        user_records=[],
        system_records=requirements,
        component_records=[],
        unit_records=[],
        design_output_records=[],
        verification_records=verification,
        validation_records=validation,
        product_version=_PRODUCT_VERSION,
        usecase_neighbors=neighbors,
        topic_by_external_id=topics,
    )
    assert export.system_requirements[0].id == "SYSREQ_001"
    assert "VERIF_001" in export.system_requirements[0].links
    assert export.verifications[0].verifies == ["SYSREQ_001"]
    assert export.verifications[1].verifies == []


def test_map_without_neighbors_has_empty_links() -> None:
    kt, requirements, verification, validation = _load_three()
    export = map_records_to_export(
        kt,
        user_records=[],
        system_records=requirements,
        component_records=[],
        unit_records=[],
        design_output_records=[],
        verification_records=verification,
        validation_records=validation,
        product_version=_PRODUCT_VERSION,
    )
    assert export.verifications[0].verifies == []
    assert export.verifications[0].links == []
    assert export.validations[0].links == []


def test_empty_system_requirements_raises() -> None:
    kt, _, verification, validation = _load_three()
    with pytest.raises(ValueError, match="system_records"):
        map_records_to_export(
            kt,
            user_records=[],
            system_records=[],
            component_records=[],
            unit_records=[],
            design_output_records=[],
            verification_records=verification,
            validation_records=validation,
            product_version=_PRODUCT_VERSION,
        )


def test_missing_product_version_raises() -> None:
    kt, requirements, verification, validation = _load_three()
    with pytest.raises(ValueError, match="product_version"):
        map_records_to_export(
            kt,
            user_records=[],
            system_records=requirements,
            component_records=[],
            unit_records=[],
            design_output_records=[],
            verification_records=verification,
            validation_records=validation,
            product_version="  ",
        )


def test_sync_emits_external_id_and_form_fields(tmp_path: Path, monkeypatch) -> None:
    import certhub_connector.sync.sync as sync_impl

    monkeypatch.setattr(sync_impl, "sphinx_generated_dir", lambda: tmp_path / "sphinx")
    monkeypatch.setattr(sync_impl, "certhub_generated_dir", lambda: tmp_path / "certhub")
    monkeypatch.setattr(
        sync_impl,
        "normalized_snapshot_path",
        lambda: tmp_path / "certhub" / "normalized_export.json",
    )

    kt, requirements, verification, validation = _load_three()
    export = map_records_to_export(
        kt,
        user_records=[],
        system_records=requirements,
        component_records=[],
        unit_records=[],
        design_output_records=[],
        verification_records=verification,
        validation_records=validation,
        product_version=_PRODUCT_VERSION,
    )
    written = write_generated_files(export)
    req_rst = next(path for path in written if path.name == "system_requirements.rst")
    text = req_rst.read_text(encoding="utf-8")
    assert "source_system: CertHub" in text
    assert "external_id: 6a7701ffcd5640b4bf28b05e" in text
    assert "req_type: functional" in text
    assert "priority: high" in text
    assert "Sterilization temperature range is better" in text

    verif_rst = next(path for path in written if path.name == "verifications.rst")
    verif_text = verif_rst.read_text(encoding="utf-8")
    assert "external_id:" in verif_text

    snapshot = json.loads(
        (tmp_path / "certhub" / "normalized_export.json").read_text(encoding="utf-8")
    )
    assert snapshot["system_requirements"][0]["external_id"] == "6a7701ffcd5640b4bf28b05e"
    assert snapshot["verifications"][0]["id"] == "VERIF_001"
