"""Guards and tag-only flow for scripts/tag_release.py."""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "tag_release.py"


def _load_tag_release():
    spec = importlib.util.spec_from_file_location("tag_release", _SCRIPT)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


tag_release = _load_tag_release()


def _git(cwd: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
        cwd=cwd,
    )
    return result.stdout.strip()


@pytest.fixture
def release_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    remote = tmp_path / "remote.git"
    work = tmp_path / "work"
    _git(tmp_path, "init", "--bare", str(remote))
    _git(tmp_path, "clone", str(remote), str(work))
    _git(work, "config", "user.email", "test@example.com")
    _git(work, "config", "user.name", "Test User")
    (work / "README.md").write_text("demo\n", encoding="utf-8")
    _git(work, "add", "README.md")
    _git(work, "commit", "-m", "init")
    _git(work, "push", "-u", "origin", "HEAD")
    monkeypatch.chdir(work)
    return work


def test_release_rejects_bad_version(release_repo: Path) -> None:
    assert tag_release.main(["release", "--version", "1.0"]) == 2


def test_rc_rejects_zero_rc(release_repo: Path) -> None:
    assert tag_release.main(["rc", "--version", "1.0.0", "--rc", "0"]) == 2


def test_tag_release_creates_and_pushes(release_repo: Path) -> None:
    assert tag_release.main(["release", "--version", "1.2.3", "--push"]) == 0
    assert _git(release_repo, "tag", "--points-at", "HEAD") == "v1.2.3"
    assert _git(release_repo, "ls-remote", "--tags", "origin", "refs/tags/v1.2.3")


def test_tag_rc_creates_rc_tag(release_repo: Path) -> None:
    assert tag_release.main(["rc", "--version", "2.0.0", "--rc", "1", "--push"]) == 0
    assert _git(release_repo, "tag", "--points-at", "HEAD") == "v2.0.0-rc.1"


def test_allows_head_with_other_v_tag(release_repo: Path) -> None:
    assert tag_release.main(["rc", "--version", "1.0.0", "--rc", "1", "--push"]) == 0
    assert tag_release.main(["release", "--version", "1.0.0", "--push"]) == 0
    tags = set(_git(release_repo, "tag", "--points-at", "HEAD").splitlines())
    assert tags == {"v1.0.0-rc.1", "v1.0.0"}


def test_rejects_existing_local_tag(release_repo: Path) -> None:
    _git(release_repo, "tag", "-a", "v1.0.0", "-m", "existing")
    assert tag_release.main(["release", "--version", "1.0.0", "--push"]) == 2


def test_rejects_existing_remote_tag(release_repo: Path) -> None:
    other = release_repo.parent / "other"
    subprocess.run(
        ["git", "clone", str(release_repo.parent / "remote.git"), str(other)],
        check=True,
        capture_output=True,
    )
    _git(other, "config", "user.email", "test@example.com")
    _git(other, "config", "user.name", "Test User")
    _git(other, "tag", "-a", "v9.9.9", "-m", "remote tag")
    _git(other, "push", "origin", "v9.9.9")
    assert tag_release.main(["release", "--version", "9.9.9", "--push"]) == 2


def test_rejects_dirty_tree(release_repo: Path) -> None:
    (release_repo / "dirty.txt").write_text("x\n", encoding="utf-8")
    assert tag_release.main(["release", "--version", "1.0.0", "--push"]) == 2


def test_allow_dirty_overrides_clean_check(release_repo: Path) -> None:
    (release_repo / "dirty.txt").write_text("x\n", encoding="utf-8")
    assert (
        tag_release.main(
            ["release", "--version", "1.0.0", "--push", "--allow-dirty"]
        )
        == 0
    )
    assert _git(release_repo, "tag", "--points-at", "HEAD") == "v1.0.0"
