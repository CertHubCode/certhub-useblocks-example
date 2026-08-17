"""Certification gate picks the CodeLinks site that matches each SYSREQ's VERIF."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from certhub_connector.evidence.verify import (
    _pick_implementation,
    verify_certification,
)
from certhub_connector.sync.models import (
    CertHubExport,
    DesignOutput,
    ProjectInfo,
    SystemRequirement,
    Verification,
)
from certhub_connector.config.paths import normalized_snapshot_path, project_root

import pytest

_IMPL_MAP = {
    "DOUT_018": [
        "src/sterilisator_20a/cycle/controller.py:def temperature_within_range(peak_temperature_c: float) -> bool:",
        "src/sterilisator_20a/cycle/controller.py:def reported_cycle_duration_minutes(measured_minutes: float) -> float:",
        "src/sterilisator_20a/cycle/controller.py:def cycle_within_time_budget(duration_minutes: float) -> bool:",
        "src/sterilisator_20a/ui/messages.py:def ui_messages() -> dict[str, str]:",
        "src/sterilisator_20a/enclosure/footprint.py:def device_dimensions_cm() -> DimensionsCm:",
    ],
    "VERIF_001": [
        "src/sterilisator_20a/tests/test_sterilisator.py:def test_sterilization_temperature_accuracy() -> None:"
    ],
    "VERIF_002": [
        "src/sterilisator_20a/tests/test_sterilisator.py:def test_sterilization_cycle_time() -> None:"
    ],
    "VERIF_003": [
        "src/sterilisator_20a/tests/test_sterilisator.py:def test_user_interface_labeling() -> None:"
    ],
    "VERIF_004": [
        "src/sterilisator_20a/tests/test_sterilisator.py:def test_device_footprint() -> None:"
    ],
}


def test_pick_implementation_matches_verif_domain() -> None:
    cases = {
        "VERIF_001": "temperature_within_range",
        "VERIF_002": "reported_cycle_duration_minutes",
        "VERIF_003": "messages.py",
        "VERIF_004": "footprint.py",
    }
    for verif_id, needle in cases.items():
        _dout, impl = _pick_implementation(_IMPL_MAP, ["DOUT_018"], [verif_id])
        assert impl is not None, verif_id
        assert needle in impl, f"{verif_id}: expected {needle} in {impl}"


def test_pick_implementation_prefers_source_over_tests() -> None:
    impl_map = {
        "DOUT_018": [
            "src/sterilisator_20a/tests/test_sterilisator.py:def test_sterilization_temperature_accuracy",
            "src/sterilisator_20a/cycle/controller.py:def temperature_within_range",
        ],
        "VERIF_001": [
            "src/sterilisator_20a/tests/test_sterilisator.py:def test_sterilization_temperature_accuracy"
        ],
    }
    _dout, impl = _pick_implementation(impl_map, ["DOUT_018"], ["VERIF_001"])
    assert impl is not None
    assert "controller.py" in impl
    assert "/tests/" not in impl


def _minimal_export() -> CertHubExport:
    sysreqs = []
    verifs = []
    mapping = (
        ("SYSREQ_001", "VERIF_001", "temperature"),
        ("SYSREQ_002", "VERIF_002", "cycle time"),
        ("SYSREQ_003", "VERIF_003", "english UI"),
        ("SYSREQ_004", "VERIF_004", "footprint"),
    )
    for sys_id, ver_id, title in mapping:
        sysreqs.append(
            SystemRequirement(
                id=sys_id,
                title=title,
                description=title,
                status="approved",
            )
        )
        verifs.append(
            Verification(
                id=ver_id,
                title=title,
                description=title,
                status="approved",
                verifies=[sys_id],
            )
        )
    return CertHubExport(
        project=ProjectInfo(id="demo", name="Sterilisator 20A", version="0.1"),
        user_requirements=[],
        system_requirements=sysreqs,
        component_requirements=[],
        unit_requirements=[],
        design_outputs=[
            DesignOutput(
                id="DOUT_017",
                title="Legacy catalog device",
                description="Wrong product — no CodeLinks",
                status="approved",
                links=["SYSREQ_002"],
            ),
            DesignOutput(
                id="DOUT_018",
                title="Sterilizer 20A",
                description="SaMD product design output",
                status="approved",
                links=["SYSREQ_001", "SYSREQ_003", "SYSREQ_004"],
            ),
        ],
        verifications=verifs,
        validations=[],
    )


def test_verify_report_cites_matching_source_files(tmp_path: Path) -> None:
    junit = tmp_path / "junit.xml"
    cases = "".join(
        f'<testcase name="{vid}" classname="t">'
        f'<properties><property name="certhub_test" value="{vid}"/></properties>'
        f"</testcase>"
        for vid in ("VERIF_001", "VERIF_002", "VERIF_003", "VERIF_004")
    )
    junit.write_text(
        f'<testsuite tests="4">{cases}</testsuite>\n',
        encoding="utf-8",
    )
    analysis = tmp_path / "codelinks.json"
    records = []
    for need_id, locations in _IMPL_MAP.items():
        for loc in locations:
            filepath, _, scope = loc.partition(":")
            records.append(
                {
                    "filepath": filepath,
                    "need_ids": [need_id],
                    "tagged_scope": scope,
                }
            )
    analysis.write_text(__import__("json").dumps(records), encoding="utf-8")

    report = verify_certification(
        _minimal_export(),
        codelinks_path=analysis,
        junit=junit,
    )
    assert report.ok
    expected = {
        "SYSREQ_001": "temperature_within_range",
        "SYSREQ_002": "reported_cycle_duration_minutes",
        "SYSREQ_003": "messages.py",
        "SYSREQ_004": "footprint.py",
    }
    by_id = {v.requirement_id: v.implementation or "" for v in report.requirements}
    for sys_id, needle in expected.items():
        assert needle in by_id[sys_id], f"{sys_id}: {by_id[sys_id]}"


@pytest.mark.skipif(
    not normalized_snapshot_path().is_file(),
    reason="normalized export missing — run make sync",
)
def test_live_snapshot_sysreq_impl_files() -> None:
    from certhub_connector.config.paths import codelinks_analysis_path, junit_path

    if not codelinks_analysis_path().is_file() or not junit_path().is_file():
        pytest.skip("codelinks/junit missing — run make show")
    report = verify_certification()
    expected = {
        "SYSREQ_001": "temperature_within_range",
        "SYSREQ_002": "reported_cycle_duration",
        "SYSREQ_003": "messages.py",
        "SYSREQ_004": "footprint.py",
    }
    by_id = {v.requirement_id: v.implementation or "" for v in report.requirements}
    for sys_id, needle in expected.items():
        if sys_id not in by_id:
            continue
        assert needle in by_id[sys_id], f"{sys_id}: {by_id[sys_id]}"


def test_needextend_emits_all_locations(tmp_path: Path, monkeypatch) -> None:
    script = project_root() / "scripts" / "run_codelinks.py"
    spec = importlib.util.spec_from_file_location("run_codelinks", script)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    generated = tmp_path / "generated"
    monkeypatch.setattr(mod, "GENERATED", generated)
    monkeypatch.setattr(mod, "NEEDEXTEND_RST", generated / "codelinks_needextend.rst")
    records = [
        {
            "filepath": "src/sterilisator_20a/cycle/controller.py",
            "need_ids": ["DOUT_018"],
            "source_map": {"start": {"row": 22}},
            "remote_url": "https://example.com/controller.py#L23",
        },
        {
            "filepath": "src/sterilisator_20a/ui/messages.py",
            "need_ids": ["DOUT_018"],
            "source_map": {"start": {"row": 7}},
            "remote_url": "https://example.com/messages.py#L8",
        },
        {
            "filepath": "src/sterilisator_20a/cycle/controller.py",
            "need_ids": ["DOUT_018"],
            "source_map": {"start": {"row": 22}},
            "remote_url": "https://example.com/controller.py#L23",
        },
    ]
    mod._write_needextend(records)
    text = (generated / "codelinks_needextend.rst").read_text(encoding="utf-8")
    assert "controller.py#L23" in text
    assert "messages.py#L8" in text
    assert "controller.py; src/sterilisator_20a/ui/messages.py" in text
