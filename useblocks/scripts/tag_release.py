#!/usr/bin/env python3
"""Create and push Cadence RC / release git tags for CertHub evidence workflows."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from certhub_connector.cli import ui
from certhub_connector.config.settings import TenantSettings
from certhub_connector.config.dashboard_url import dashboard_kt_url

_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def _run(cmd: list[str], *, cwd: Path) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=cwd)


def _run_capture(cmd: list[str], *, cwd: Path) -> str:
    result = subprocess.run(
        cmd,
        check=True,
        capture_output=True,
        text=True,
        cwd=cwd,
    )
    return result.stdout.strip()


def _repo_root() -> Path:
    return Path(_run_capture(["git", "rev-parse", "--show-toplevel"], cwd=Path.cwd()))


def _head_commit(cwd: Path) -> str:
    return _run_capture(["git", "rev-parse", "HEAD"], cwd=cwd)


def _head_short(cwd: Path) -> str:
    return _run_capture(["git", "rev-parse", "--short", "HEAD"], cwd=cwd)


def _head_subject(cwd: Path) -> str:
    return _run_capture(["git", "log", "-1", "--pretty=%s"], cwd=cwd)


def _working_tree_clean(cwd: Path) -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        check=True,
        capture_output=True,
        text=True,
        cwd=cwd,
    )
    return result.stdout.strip() == ""


def _ref_exists(cwd: Path, ref: str) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "-q", "--verify", ref],
        capture_output=True,
        text=True,
        cwd=cwd,
    )
    return result.returncode == 0


def _remote_tag_exists(cwd: Path, tag: str) -> bool:
    result = subprocess.run(
        ["git", "ls-remote", "--tags", "origin", f"refs/tags/{tag}"],
        check=True,
        capture_output=True,
        text=True,
        cwd=cwd,
    )
    return bool(result.stdout.strip())


def _validate_semver(version: str) -> None:
    if not _VERSION_RE.fullmatch(version):
        raise ValueError(f"VERSION must be X.Y.Z, got {version!r}")


def _assert_can_tag(*, root: Path, tag: str, allow_dirty: bool) -> None:
    if not allow_dirty and not _working_tree_clean(root):
        raise RuntimeError("Working tree dirty; commit/stash or pass --allow-dirty")
    _run(["git", "fetch", "origin", "--tags"], cwd=root)
    if _ref_exists(root, f"refs/tags/{tag}"):
        raise RuntimeError(f"Tag already exists locally: {tag}")
    if _remote_tag_exists(root, tag):
        raise RuntimeError(f"Tag already exists on origin: {tag}")


def _create_tag(
    *,
    root: Path,
    tag: str,
    message: str,
    push: bool,
) -> None:
    _run(["git", "tag", "-a", tag, "-m", message], cwd=root)
    if push:
        _run(["git", "push", "origin", tag], cwd=root)


def _release_facts(
    *,
    root: Path,
    version: str,
    tag: str,
    kind: str,
    pushed: bool,
) -> list[tuple[str, str]]:
    return [
        ("Version", version),
        ("Tag", tag),
        ("Type", kind),
        ("Commit", f"{_head_short(root)} ({_head_commit(root)[:12]}…)"),
        ("Subject", _head_subject(root)),
        ("Remote", "pushed to origin" if pushed else "local only"),
    ]


def cmd_tag_rc(args: argparse.Namespace) -> int:
    ui.banner("Release candidate")
    _validate_semver(args.version)
    if not args.rc or not str(args.rc).isdigit() or int(args.rc) < 1:
        raise ValueError(f"RC must be a positive integer, got {args.rc!r}")
    root = _repo_root()
    tag = f"v{args.version}-rc.{args.rc}"
    ui.step("Preparing tag")
    _assert_can_tag(root=root, tag=tag, allow_dirty=args.allow_dirty)
    _create_tag(
        root=root,
        tag=tag,
        message=f"Release candidate {tag}",
        push=args.push,
    )
    ui.success_panel(
        f"Release candidate {tag}",
        _release_facts(
            root=root,
            version=args.version,
            tag=tag,
            kind=f"Release candidate (rc.{args.rc})",
            pushed=bool(args.push),
        ),
    )
    ui.details(
        [
            ("Evidence pack", "Built and retained for this baseline"),
            (
                "Release Record",
                "Not created — reserved for the full release",
            ),
        ],
        title="What this release candidate does",
    )
    return 0


def cmd_tag_release(args: argparse.Namespace) -> int:
    ui.banner("Software release")
    _validate_semver(args.version)
    root = _repo_root()
    tag = f"v{args.version}"
    ui.step("Preparing tag")
    _assert_can_tag(root=root, tag=tag, allow_dirty=args.allow_dirty)
    _create_tag(
        root=root,
        tag=tag,
        message=f"Release {tag}",
        push=args.push,
    )
    ui.success_panel(
        f"Release {tag}",
        _release_facts(
            root=root,
            version=args.version,
            tag=tag,
            kind="Full release",
            pushed=bool(args.push),
        ),
    )
    tenant = TenantSettings.load()
    records_url = dashboard_kt_url(tenant, kt="release_record")
    ui.details(
        [
            ("Baseline", args.version),
            ("Evidence pack", "Built for this baseline"),
            (
                "Release Record",
                f"Created in CertHub for baseline {args.version}",
            ),
            ("Knowledge topic", "Release Record"),
        ],
        title="What this release records in CertHub",
    )
    ui.link_panel(
        "Release evidence KT in CertHub",
        records_url,
        note="Open this knowledge topic to review the controlled Release Record for this baseline.",
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create CertHub release and release-candidate tags"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    rc_p = sub.add_parser("rc", help="Create vX.Y.Z-rc.N tag (evidence only)")
    rc_p.add_argument("--version", required=True)
    rc_p.add_argument("--rc", required=True)
    rc_p.add_argument("--push", action="store_true")
    rc_p.add_argument("--allow-dirty", action="store_true")
    rc_p.set_defaults(func=cmd_tag_rc)

    rel_p = sub.add_parser(
        "release", help="Create vX.Y.Z tag (evidence + Release Record)"
    )
    rel_p.add_argument("--version", required=True)
    rel_p.add_argument("--push", action="store_true")
    rel_p.add_argument("--allow-dirty", action="store_true")
    rel_p.set_defaults(func=cmd_tag_release)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:  # noqa: BLE001
        ui.fail(str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
