"""Build the local evidence pack consumed by CI artifacts and CertHub push."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, field_validator

from certhub_connector.config.paths import (
    certhub_result_path,
    codelinks_analysis_path,
    evidence_dir,
    git_head_commit,
    junit_path,
    sphinx_html_dir,
)
from certhub_connector.evidence.report import generate_report
from certhub_connector.evidence.verify import VerificationReport, verify_certification


class EvidenceManifest(BaseModel):
    """Immutable summary of one evidence pack."""

    model_config = ConfigDict(frozen=True)

    git_commit: str
    generated_at: str
    certification_status: str
    run_id: str | None = None
    evidence_url: str | None = None
    artifact_hashes: dict[str, str] = Field(default_factory=dict)
    totals: dict[str, int] = Field(default_factory=dict)

    @field_validator("git_commit", "generated_at", "certification_status")
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Manifest required fields must be non-empty")
        return value.strip()


def _git_commit() -> str:
    commit = git_head_commit()
    if not commit:
        raise RuntimeError("Unable to resolve git commit for evidence pack")
    return commit


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sha256_tree(root: Path) -> str:
    """Deterministic digest of a directory (sorted relative paths + file hashes)."""
    if not root.is_dir():
        raise FileNotFoundError(f"Missing directory for tree hash: {root}")
    digest = hashlib.sha256()
    files = sorted(path for path in root.rglob("*") if path.is_file())
    for path in files:
        relative = path.relative_to(root).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(_sha256_file(path).encode("ascii"))
        digest.update(b"\0")
    return digest.hexdigest()


def _copy_if_exists(src: Path, dest: Path) -> bool:
    if not src.is_file():
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return True


def _copy_sphinx_docs(dest_docs: Path) -> None:
    """Copy Sphinx HTML build into ``evidence/docs/``."""
    src = sphinx_html_dir()
    index = src / "index.html"
    if not src.is_dir() or not index.is_file():
        raise FileNotFoundError(
            f"Missing Sphinx HTML at {src} (expected index.html) — "
            "run sphinx-build or make evidence first"
        )
    if dest_docs.exists():
        shutil.rmtree(dest_docs)
    shutil.copytree(src, dest_docs)


def resolve_evidence_url() -> str | None:
    """Prefer GitHub Actions run URL when running in CI."""
    server = os.environ.get("GITHUB_SERVER_URL", "").strip().rstrip("/")
    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()
    run_id = os.environ.get("GITHUB_RUN_ID", "").strip()
    if server and repo and run_id:
        return f"{server}/{repo}/actions/runs/{run_id}"
    explicit = os.environ.get("CERTHUB_EVIDENCE_URL", "").strip()
    return explicit or None


def package_evidence(
    report: VerificationReport | None = None,
    *,
    write_report: bool = True,
) -> tuple[Path, EvidenceManifest, VerificationReport]:
    """Write ``evidence/`` pack from current verify/report outputs."""
    report = report or verify_certification()
    if write_report:
        generate_report(report)

    out_dir = evidence_dir()
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    copied: list[str] = []
    pairs = (
        (certhub_result_path(), out_dir / "certhub_result.json"),
        (junit_path(), out_dir / "junit.xml"),
        (codelinks_analysis_path(), out_dir / "codelinks_analysis.json"),
    )
    for src, dest in pairs:
        if _copy_if_exists(src, dest):
            copied.append(dest.name)

    if "certhub_result.json" not in copied:
        raise FileNotFoundError(
            f"Missing certhub_result.json at {certhub_result_path()} — run report first"
        )

    docs_dir = out_dir / "docs"
    _copy_sphinx_docs(docs_dir)

    hashes = {
        name: _sha256_file(out_dir / name)
        for name in copied
    }
    hashes["docs"] = _sha256_tree(docs_dir)
    generated_at = datetime.now(timezone.utc).isoformat()
    run_id = os.environ.get("GITHUB_RUN_ID", "").strip() or None
    evidence_url = resolve_evidence_url()
    manifest = EvidenceManifest(
        git_commit=_git_commit(),
        generated_at=generated_at,
        certification_status=report.certification_status.value,
        run_id=run_id,
        evidence_url=evidence_url,
        artifact_hashes=hashes,
        totals=dict(report.totals),
    )
    manifest_path = out_dir / "MANIFEST.json"
    manifest_path.write_text(
        manifest.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    # Include manifest hash of itself after writing other files only.
    # Hash of MANIFEST content excluding its own hash entry is unnecessary;
    # callers hash the file for provenance separately if needed.
    return out_dir, manifest, report


def load_evidence_result(evidence_path: Path | None = None) -> dict[str, object]:
    """Load ``certhub_result.json`` from an evidence pack (typed as object JSON)."""
    base = evidence_path or evidence_dir()
    result_path = base / "certhub_result.json"
    if not result_path.is_file():
        raise FileNotFoundError(f"Missing evidence result: {result_path}")
    payload = json.loads(result_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("certhub_result.json must be a JSON object")
    return payload


def load_evidence_manifest(evidence_path: Path | None = None) -> EvidenceManifest:
    base = evidence_path or evidence_dir()
    path = base / "MANIFEST.json"
    if not path.is_file():
        raise FileNotFoundError(f"Missing evidence MANIFEST: {path}")
    return EvidenceManifest.model_validate_json(path.read_text(encoding="utf-8"))
