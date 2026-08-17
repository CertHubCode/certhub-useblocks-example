"""Plain-text CertHub Notes (`details`) for release evidence."""

from __future__ import annotations

from certhub_connector.evidence import EvidenceManifest
from certhub_connector.evidence.push import format_release_details_text


def test_format_release_details_text_is_lean_plain_text() -> None:
    result = {
        "project": "sterilisator_20a",
        "version": "1.0.0",
        "certificationStatus": "VERIFIED",
        "totals": {
            "system_requirements": 3,
            "verified": 2,
            "passed": 4,
            "failed": 1,
            "design_outputs": 3,
            "verifications": 5,
            "implemented": 3,
        },
        "requirements": [
            {
                "id": "SYSREQ_001",
                "status": "verified",
                "specification": "DOUT_001",
                "implementation": "src/sterilisator_20a/device.py:temperature_within_range",
                "tests": [{"id": "VERIF_001", "result": "passed"}],
            },
            {
                "id": "SYSREQ_002",
                "status": "failed",
                "specification": "DOUT_002",
                "implementation": "src/sterilisator_20a/device.py:reported_cycle_duration_minutes",
                "tests": [{"id": "VERIF_002", "result": "failed"}],
            },
            {
                "id": "SYSREQ_003",
                "status": "verified",
                "specification": "DOUT_003",
                "implementation": None,
                "tests": [],
            },
        ],
    }
    manifest = EvidenceManifest(
        git_commit="deadbeef",
        generated_at="2026-08-09T12:00:00+00:00",
        certification_status="VERIFIED",
        artifact_hashes={
            "certhub_result.json": "a" * 64,
            "junit.xml": "b" * 64,
            "docs": "c" * 64,
        },
    )

    text = format_release_details_text(result, manifest)

    assert text.startswith("Certification: VERIFIED")
    assert "Project: sterilisator_20a  Version: 1.0.0" in text
    assert "System Requirements: 3" in text
    assert "Verified: 2 / 3" in text
    assert "Passed: 4  Failed: 1" in text
    assert "SYSREQ_001  verified" in text
    assert "SYSREQ_002  failed" in text
    assert "SYSREQ_003  verified" in text
    assert f"Result SHA: {'a' * 64}" in text

    assert "{" not in text
    assert "}" not in text
    assert "specification" not in text
    assert "implementation" not in text
    assert "artifact_hashes" not in text
    assert "regulatory_impact" not in text
    assert "VERIF_001" not in text
