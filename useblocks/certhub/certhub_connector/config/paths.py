"""Project path helpers."""

from __future__ import annotations

import subprocess
from pathlib import Path


def project_root() -> Path:
    """Return the Cadence project root (directory containing pyproject.toml)."""
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "pyproject.toml").is_file() and (candidate / "certhub").is_dir():
            return candidate
    raise RuntimeError("Could not locate project root (pyproject.toml + certhub/)")


def git_head_commit() -> str | None:
    """Return HEAD SHA, or None if git is unavailable / not a repo."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            cwd=project_root(),
        )
        return result.stdout.strip() or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def sphinx_generated_dir() -> Path:
    return project_root() / "sphinx" / "source" / "generated"


def sphinx_html_dir() -> Path:
    return project_root() / "sphinx" / "build" / "html"


def certhub_generated_dir() -> Path:
    return project_root() / "certhub" / "generated"


def reports_dir() -> Path:
    return project_root() / "reports"


def junit_path() -> Path:
    return reports_dir() / "junit.xml"


def codelinks_analysis_path() -> Path:
    return reports_dir() / "codelinks_analysis.json"


def normalized_snapshot_path() -> Path:
    return certhub_generated_dir() / "normalized_export.json"


def certhub_result_path() -> Path:
    return certhub_generated_dir() / "certhub_result.json"


def evidence_dir() -> Path:
    return project_root() / "evidence"
