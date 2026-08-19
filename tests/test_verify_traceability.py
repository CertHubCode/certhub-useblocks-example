"""Certification gate picks the CodeLinks site that matches each SYSREQ's VERIF."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from certhub_connector.config.paths import project_root
from certhub_connector.evidence.verify import (
    CertificationStatus,
    ReqStatus,
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


def _single_sysreq_export(
    dout_links: list[str] | None = None,
    verif_verifies: list[str] | None = None,
) -> CertHubExport:
    """One SYSREQ_001 with optional DOUT and VERIF wiring."""
    douts = []
    verifs = []
    if dout_links is not None:
        douts.append(
            DesignOutput(
                id="DOUT_018",
                title="Product",
                description="d",
                status="approved",
                links=dout_links,
            )
        )
    if verif_verifies is not None:
        verifs.append(
            Verification(
                id="VERIF_001",
                title="Temp test",
                description="d",
                status="approved",
                verifies=verif_verifies,
            )
        )
    return CertHubExport(
        project=ProjectInfo(id="demo", name="Test", version="0.1"),
        user_requirements=[],
        system_requirements=[
            SystemRequirement(
                id="SYSREQ_001", title="temperature", description="d", status="approved"
            )
        ],
        component_requirements=[],
        unit_requirements=[],
        design_outputs=douts,
        verifications=verifs,
        validations=[],
    )


def _codelinks_json(tmp_path: Path, need_ids: list[str] | None = None) -> Path:
    import json as _json

    analysis = tmp_path / "codelinks.json"
    if need_ids is None:
        analysis.write_text("[]", encoding="utf-8")
        return analysis
    records = [
        {"filepath": "src/sterilisator_20a/cycle/controller.py", "need_ids": need_ids, "tagged_scope": "def temperature_within_range"}
    ]
    analysis.write_text(_json.dumps(records), encoding="utf-8")
    return analysis


def _junit_xml(tmp_path: Path, verif_id: str, result: str = "passed") -> Path:
    junit = tmp_path / "junit.xml"
    inner = ""
    if result == "passed":
        inner = ""
    elif result == "failed":
        inner = '<failure message="fail"/>'
    tc = (
        f'<testcase name="{verif_id}" classname="t">'
        f'<properties><property name="certhub_test" value="{verif_id}"/></properties>'
        f"{inner}</testcase>"
    )
    junit.write_text(f'<testsuite tests="1">{tc}</testsuite>\n', encoding="utf-8")
    return junit


def test_gate_missing_dout(tmp_path: Path) -> None:
    export = _single_sysreq_export(dout_links=None, verif_verifies=["SYSREQ_001"])
    report = verify_certification(
        export,
        codelinks_path=_codelinks_json(tmp_path, ["DOUT_018"]),
        junit=_junit_xml(tmp_path, "VERIF_001"),
    )
    assert report.certification_status == CertificationStatus.BLOCKED
    assert report.requirements[0].status == ReqStatus.MISSING_DOUT


def test_gate_not_implemented(tmp_path: Path) -> None:
    export = _single_sysreq_export(dout_links=["SYSREQ_001"], verif_verifies=["SYSREQ_001"])
    report = verify_certification(
        export,
        codelinks_path=_codelinks_json(tmp_path),
        junit=_junit_xml(tmp_path, "VERIF_001"),
    )
    assert report.certification_status == CertificationStatus.BLOCKED
    assert report.requirements[0].status == ReqStatus.NOT_IMPLEMENTED


def test_gate_not_tested(tmp_path: Path) -> None:
    export = _single_sysreq_export(dout_links=["SYSREQ_001"], verif_verifies=[])
    report = verify_certification(
        export,
        codelinks_path=_codelinks_json(tmp_path, ["DOUT_018"]),
        junit=_junit_xml(tmp_path, "VERIF_001"),
    )
    assert report.certification_status == CertificationStatus.BLOCKED
    assert report.requirements[0].status == ReqStatus.NOT_TESTED


def test_gate_failed_test(tmp_path: Path) -> None:
    export = _single_sysreq_export(dout_links=["SYSREQ_001"], verif_verifies=["SYSREQ_001"])
    report = verify_certification(
        export,
        codelinks_path=_codelinks_json(tmp_path, ["DOUT_018"]),
        junit=_junit_xml(tmp_path, "VERIF_001", result="failed"),
    )
    assert report.certification_status == CertificationStatus.BLOCKED
    assert report.requirements[0].status == ReqStatus.FAILED
    assert report.requirements[0].result == "FAILED"


def test_gate_verified(tmp_path: Path) -> None:
    export = _single_sysreq_export(dout_links=["SYSREQ_001"], verif_verifies=["SYSREQ_001"])
    report = verify_certification(
        export,
        codelinks_path=_codelinks_json(tmp_path, ["DOUT_018"]),
        junit=_junit_xml(tmp_path, "VERIF_001"),
    )
    assert report.certification_status == CertificationStatus.VERIFIED
    assert report.requirements[0].status == ReqStatus.VERIFIED


def test_gate_ignores_non_certhub_testcases(tmp_path: Path) -> None:
    """pytest cases without certhub_test property must not affect the gate."""
    export = _single_sysreq_export(dout_links=["SYSREQ_001"], verif_verifies=["SYSREQ_001"])
    junit = tmp_path / "junit.xml"
    junit.write_text(
        '<testsuite tests="2">'
        '<testcase name="test_unrelated" classname="t"/>'
        '<testcase name="VERIF_001" classname="t">'
        '<properties><property name="certhub_test" value="VERIF_001"/></properties>'
        "</testcase></testsuite>\n",
        encoding="utf-8",
    )
    report = verify_certification(
        export,
        codelinks_path=_codelinks_json(tmp_path, ["DOUT_018"]),
        junit=junit,
    )
    assert report.certification_status == CertificationStatus.VERIFIED
    assert len(report.requirements) == 1


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
