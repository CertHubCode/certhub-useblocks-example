"""Certification verification gate derived from real artifacts."""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from certhub_connector.sync.models import CertHubExport, SystemRequirement
from certhub_connector.config.paths import (
    codelinks_analysis_path,
    junit_path,
    normalized_snapshot_path,
)

SAMMD_PRODUCT_DOUT_ID = "DOUT_018"


class ReqStatus(str, Enum):
    VERIFIED = "verified"
    NOT_IMPLEMENTED = "not_implemented"
    NOT_TESTED = "not_tested"
    FAILED = "failed"
    MISSING_DOUT = "missing_dout"


class CertificationStatus(str, Enum):
    VERIFIED = "VERIFIED"
    BLOCKED = "BLOCKED"


@dataclass
class RequirementVerdict:
    requirement_id: str
    status: ReqStatus
    design_output: str | None = None
    implementation: str | None = None
    verification: str | None = None
    result: str | None = None
    messages: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return self.status == ReqStatus.VERIFIED

    @property
    def specification(self) -> str | None:
        """Backwards-compatible alias for outbound/report payloads."""
        return self.design_output


@dataclass
class VerificationReport:
    project_id: str
    project_version: str
    certification_status: CertificationStatus
    requirements: list[RequirementVerdict]
    totals: dict[str, int]

    @property
    def ok(self) -> bool:
        return self.certification_status == CertificationStatus.VERIFIED


def load_normalized_export(path: Path | None = None) -> CertHubExport:
    snapshot = path or normalized_snapshot_path()
    if not snapshot.is_file():
        raise FileNotFoundError(
            f"Normalized export missing: {snapshot}. Run sync first."
        )
    return CertHubExport.model_validate_json(snapshot.read_text(encoding="utf-8"))


def load_codelinks_need_ids(path: Path | None = None) -> dict[str, list[str]]:
    """Map need ID → list of 'file:scope' implementation locations."""
    analysis = path or codelinks_analysis_path()
    if not analysis.is_file():
        return {}
    data = json.loads(analysis.read_text(encoding="utf-8"))
    mapping: dict[str, list[str]] = {}
    records = data if isinstance(data, list) else data.get("results", data.get("items", []))
    if isinstance(data, dict) and "results" not in data and "items" not in data:
        if isinstance(data.get("need_id_refs"), list):
            records = data["need_id_refs"]
    for record in records:
        if not isinstance(record, dict):
            continue
        need_ids = record.get("need_ids") or []
        filepath = record.get("filepath") or record.get("file") or "unknown"
        scope = (record.get("tagged_scope") or "").split("\n", 1)[0].strip()
        location = f"{filepath}"
        if scope:
            location = f"{filepath}:{scope[:80]}"
        for need_id in need_ids:
            mapping.setdefault(str(need_id), []).append(location)
    return mapping


def _parse_junit_properties(testcase: ET.Element) -> dict[str, str]:
    props: dict[str, str] = {}
    for properties in testcase.findall("properties"):
        for prop in properties.findall("property"):
            name = prop.get("name")
            value = prop.get("value")
            if name and value is not None:
                props[name] = value
    for prop in testcase.findall("property"):
        name = prop.get("name")
        value = prop.get("value")
        if name and value is not None:
            props[name] = value
    return props


def load_junit_results(path: Path | None = None) -> dict[str, str]:
    """Map CertHub VERIF id → passed|failed|skipped|error."""
    xml_path = path or junit_path()
    if not xml_path.is_file():
        return {}
    root = ET.parse(xml_path).getroot()
    results: dict[str, str] = {}
    for testcase in root.iter("testcase"):
        props = _parse_junit_properties(testcase)
        if "certhub_test" not in props:
            continue
        test_id = props["certhub_test"]
        if testcase.find("failure") is not None:
            results[test_id] = "failed"
        elif testcase.find("error") is not None:
            results[test_id] = "error"
        elif testcase.find("skipped") is not None:
            results[test_id] = "skipped"
        else:
            results[test_id] = "passed"
    return results


def _douts_for_sysreq(export: CertHubExport, sysreq_id: str) -> list[str]:
    found: list[str] = []
    for dout in export.design_outputs:
        if sysreq_id in dout.links:
            found.append(dout.id)
    if SAMMD_PRODUCT_DOUT_ID not in found:
        product = next(
            (d for d in export.design_outputs if d.id == SAMMD_PRODUCT_DOUT_ID),
            None,
        )
        if product and sysreq_id in product.links:
            found.append(SAMMD_PRODUCT_DOUT_ID)
    return found


def _verifs_for_sysreq(export: CertHubExport, sysreq_id: str) -> list[str]:
    found: list[str] = []
    for verif in export.verifications:
        targets = set(verif.verifies) | set(verif.links)
        if sysreq_id in targets:
            found.append(verif.id)
    return found


def _pick_implementation(
    impl_map: dict[str, list[str]],
    dout_ids: list[str],
) -> tuple[str | None, str | None]:
    for dout_id in dout_ids:
        locations = impl_map.get(dout_id, [])
        if locations:
            return dout_id, locations[0]
    product_locations = impl_map.get(SAMMD_PRODUCT_DOUT_ID, [])
    if product_locations:
        return SAMMD_PRODUCT_DOUT_ID, product_locations[0]
    return None, None


def verify_certification(
    export: CertHubExport | None = None,
    *,
    codelinks_path: Path | None = None,
    junit: Path | None = None,
) -> VerificationReport:
    export = export or load_normalized_export()
    impl_map = load_codelinks_need_ids(codelinks_path)
    junit_results = load_junit_results(junit)

    gate_requirements: list[SystemRequirement] = export.system_requirements
    verdicts: list[RequirementVerdict] = []

    for sysreq in gate_requirements:
        dout_ids = _douts_for_sysreq(export, sysreq.id)
        verif_ids = _verifs_for_sysreq(export, sysreq.id)

        if not dout_ids:
            verdicts.append(
                RequirementVerdict(
                    requirement_id=sysreq.id,
                    status=ReqStatus.MISSING_DOUT,
                    messages=["design_output: MISSING"],
                )
            )
            continue

        dout_id, implementation = _pick_implementation(impl_map, dout_ids)
        if not implementation:
            verdicts.append(
                RequirementVerdict(
                    requirement_id=sysreq.id,
                    status=ReqStatus.NOT_IMPLEMENTED,
                    design_output=dout_ids[0],
                    messages=["implementation: MISSING (CodeLinks on Design Output)"],
                )
            )
            continue

        if not verif_ids:
            verdicts.append(
                RequirementVerdict(
                    requirement_id=sysreq.id,
                    status=ReqStatus.NOT_TESTED,
                    design_output=dout_id,
                    implementation=implementation,
                    messages=["verification: MISSING"],
                )
            )
            continue

        primary_verif = verif_ids[0]
        result = junit_results.get(primary_verif)
        if result is None:
            for vid in verif_ids:
                if vid in junit_results:
                    primary_verif = vid
                    result = junit_results[vid]
                    break

        if result is None:
            verdicts.append(
                RequirementVerdict(
                    requirement_id=sysreq.id,
                    status=ReqStatus.NOT_TESTED,
                    design_output=dout_id,
                    implementation=implementation,
                    verification=primary_verif,
                    messages=[f"result: MISSING for {primary_verif}"],
                )
            )
            continue

        if result != "passed":
            verdicts.append(
                RequirementVerdict(
                    requirement_id=sysreq.id,
                    status=ReqStatus.FAILED,
                    design_output=dout_id,
                    implementation=implementation,
                    verification=primary_verif,
                    result=result.upper(),
                    messages=[f"result: {result.upper()}"],
                )
            )
            continue

        verdicts.append(
            RequirementVerdict(
                requirement_id=sysreq.id,
                status=ReqStatus.VERIFIED,
                design_output=dout_id,
                implementation=implementation,
                verification=", ".join(verif_ids),
                result="PASSED",
            )
        )

    blocked = any(not v.passed for v in verdicts)
    status = CertificationStatus.BLOCKED if blocked else CertificationStatus.VERIFIED

    implemented = sum(1 for v in verdicts if v.implementation)
    verified = sum(1 for v in verdicts if v.passed)
    passed_tests = sum(1 for r in junit_results.values() if r == "passed")
    failed_tests = sum(1 for r in junit_results.values() if r in {"failed", "error"})

    totals = {
        "system_requirements": len(gate_requirements),
        "design_outputs": len(export.design_outputs),
        "verifications": len(export.verifications),
        "validations": len(export.validations),
        "implemented": implemented,
        "verified": verified,
        "passed": passed_tests,
        "failed": failed_tests,
    }

    return VerificationReport(
        project_id=export.project.id,
        project_version=export.project.version,
        certification_status=status,
        requirements=verdicts,
        totals=totals,
    )


def format_verification_report(report: VerificationReport) -> str:
    lines = [
        "Certification Verification",
        "==========================",
        "",
    ]
    for verdict in report.requirements:
        label = "PASS" if verdict.passed else "FAIL"
        lines.append(f"{verdict.requirement_id}  {label}")
        lines.append(f"  design_output: {verdict.design_output or 'MISSING'}")
        lines.append(f"  implementation: {verdict.implementation or 'MISSING'}")
        lines.append(f"  verification: {verdict.verification or 'MISSING'}")
        lines.append(f"  result: {verdict.result or 'N/A'}")
        for msg in verdict.messages:
            lines.append(f"  note: {msg}")
        lines.append("")

    lines.append("--------------------------------")
    lines.append(f"Certification status: {report.certification_status.value}")
    lines.append("")
    t = report.totals
    lines.append(f"System Requirements           {t['system_requirements']}")
    lines.append(f"Design Outputs                {t['design_outputs']}")
    lines.append(f"Verifications                 {t['verifications']}")
    lines.append(f"Validations                   {t['validations']}")
    lines.append("")
    lines.append(
        f"Implemented                   {t['implemented']} / {t['system_requirements']}"
    )
    lines.append(
        f"Verified                      {t['verified']} / {t['system_requirements']}"
    )
    lines.append("")
    lines.append(f"Passed                        {t['passed']}")
    lines.append(f"Failed                        {t['failed']}")
    lines.append("")
    return "\n".join(lines)
