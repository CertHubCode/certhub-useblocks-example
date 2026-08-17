"""Evidence pack includes Sphinx HTML under docs/."""

from __future__ import annotations

from pathlib import Path

import pytest

import certhub_connector.evidence.pack as evidence_mod
from certhub_connector.evidence import package_evidence
from certhub_connector.evidence.verify import CertificationStatus, VerificationReport


def _stub_report() -> VerificationReport:
    return VerificationReport(
        project_id="demo",
        project_version="0.0.0",
        certification_status=CertificationStatus.VERIFIED,
        requirements=[],
        totals={"verified": 0, "failed": 0, "total": 0},
    )


def test_package_evidence_includes_sphinx_docs(
    tmp_path: Path, monkeypatch
) -> None:
    result_path = tmp_path / "certhub_result.json"
    result_path.write_text('{"ok": true}\n', encoding="utf-8")

    html_src = tmp_path / "sphinx_html"
    html_src.mkdir()
    (html_src / "index.html").write_text("<html>index</html>\n", encoding="utf-8")
    (html_src / "dashboard.html").write_text(
        "<html>dashboard</html>\n", encoding="utf-8"
    )
    static = html_src / "_static"
    static.mkdir()
    (static / "custom.css").write_text("body {}\n", encoding="utf-8")

    out = tmp_path / "evidence"
    monkeypatch.setattr(evidence_mod, "evidence_dir", lambda: out)
    monkeypatch.setattr(evidence_mod, "certhub_result_path", lambda: result_path)
    monkeypatch.setattr(evidence_mod, "junit_path", lambda: tmp_path / "missing.xml")
    monkeypatch.setattr(
        evidence_mod,
        "codelinks_analysis_path",
        lambda: tmp_path / "missing.json",
    )
    monkeypatch.setattr(evidence_mod, "sphinx_html_dir", lambda: html_src)
    monkeypatch.setattr(evidence_mod, "_git_commit", lambda: "abc123deadbeef")

    pack_dir, manifest, report = package_evidence(
        _stub_report(),
        write_report=False,
    )

    assert pack_dir == out
    assert report.ok
    assert (out / "docs" / "index.html").is_file()
    assert (out / "docs" / "dashboard.html").is_file()
    assert (out / "docs" / "_static" / "custom.css").is_file()
    assert "docs" in manifest.artifact_hashes
    assert len(manifest.artifact_hashes["docs"]) == 64
    assert "certhub_result.json" in manifest.artifact_hashes


def test_package_evidence_requires_sphinx_html(
    tmp_path: Path, monkeypatch
) -> None:
    result_path = tmp_path / "certhub_result.json"
    result_path.write_text("{}\n", encoding="utf-8")
    empty_html = tmp_path / "empty_html"
    empty_html.mkdir()

    monkeypatch.setattr(evidence_mod, "evidence_dir", lambda: tmp_path / "evidence")
    monkeypatch.setattr(evidence_mod, "certhub_result_path", lambda: result_path)
    monkeypatch.setattr(evidence_mod, "junit_path", lambda: tmp_path / "missing.xml")
    monkeypatch.setattr(
        evidence_mod,
        "codelinks_analysis_path",
        lambda: tmp_path / "missing.json",
    )
    monkeypatch.setattr(evidence_mod, "sphinx_html_dir", lambda: empty_html)
    monkeypatch.setattr(evidence_mod, "_git_commit", lambda: "abc123")

    with pytest.raises(FileNotFoundError, match="Sphinx HTML"):
        package_evidence(_stub_report(), write_report=False)
