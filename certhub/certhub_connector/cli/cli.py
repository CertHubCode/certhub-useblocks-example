"""CLI entry point for cadence (invoked by Makefile)."""

from __future__ import annotations

import argparse
import json
import os
import webbrowser
from pathlib import Path

from certhub_connector.config import CerthubConfig, TenantSettings, load_dotenv
from certhub_connector.config.dashboard_url import DashboardKt, dashboard_kt_url
from certhub_connector.config.paths import evidence_dir
from certhub_connector.evidence import package_evidence
from certhub_connector.evidence.push import (
    confirm_evidence,
    format_proof,
    push_evidence,
)
from certhub_connector.evidence.report import generate_report
from certhub_connector.evidence.verify import (
    format_verification_report,
    verify_certification,
)
from certhub_connector.sync import sync_from_source
from certhub_connector.sync.sources import HttpKtExportSource

from . import ui


def _open_url(url: str) -> None:
    if not url or not url.strip():
        raise ValueError("Missing required field: 'url'")
    opened = webbrowser.open(url.strip())
    if not opened:
        ui.warn(f"Could not open a browser — open this URL manually: {url.strip()}")


def cmd_sync(_args: argparse.Namespace) -> int:
    ui.banner("Synchronize requirements")
    load_dotenv()
    CerthubConfig.load(load_env_file=False)

    ui.step("Reading controlled content from CertHub")
    http_source = HttpKtExportSource()
    export = sync_from_source(http_source)
    ui.success_panel(
        "Requirements synchronized",
        [
            ("Product", f"{export.project.id}"),
            ("Version", export.project.version),
            ("Source", "CertHub (system of record)"),
            ("User Requirements", str(len(export.user_requirements))),
            ("System Requirements", str(len(export.system_requirements))),
            ("Component Requirements", str(len(export.component_requirements))),
            ("Unit Requirements", str(len(export.unit_requirements))),
            ("Design Output", str(len(export.design_outputs))),
            ("Verification", str(len(export.verifications))),
            ("Validation", str(len(export.validations))),
            ("Tracer records batched", str(http_source.trace_record_count)),
            ("Records with use-case edges", str(http_source.trace_neighbor_count)),
            ("Trace links applied", str(len(http_source.trace_assignments))),
        ],
    )
    ui.step("Tracer use-case links (sample)")
    sample = http_source.trace_assignments[:12]
    if not sample:
        ui.warn("No in-sync connected_within_use_case edges applied")
    else:
        for line in sample:
            ui.ok(line)
        remaining = len(http_source.trace_assignments) - len(sample)
        if remaining > 0:
            ui.ok(f"… and {remaining} more (see INFO logs / generated RST :links:)")
    for warning in http_source.link_warnings:
        ui.warn(warning)
    return 0


def cmd_verify(_args: argparse.Namespace) -> int:
    ui.banner("Traceability verification")
    report = verify_certification()
    print(format_verification_report(report))
    status = "VERIFIED" if report.ok else "BLOCKED"
    ui.details(
        [
            ("Gate", status),
            ("Requirements", str(len(report.requirements))),
        ],
        title="Certification status",
    )
    if report.ok:
        ui.ok("All linked requirements are verified for this baseline")
        return 0
    ui.fail("Verification incomplete — resolve gaps before release")
    return 1


def cmd_report(_args: argparse.Namespace) -> int:
    ui.banner("Certification summary")
    report = verify_certification()
    out, summary, text = generate_report(report)
    print(text)
    ui.details(
        [
            ("Result", str(out)),
            ("Summary", str(summary)),
            ("Status", "VERIFIED" if report.ok else "BLOCKED"),
        ],
        title="Written artifacts",
    )
    ui.ok("Certification summary written")
    return 0


def cmd_package_evidence(_args: argparse.Namespace) -> int:
    ui.banner("Evidence pack")
    out_dir, manifest, report = package_evidence()
    ui.success_panel(
        "Evidence pack ready",
        [
            ("Location", str(out_dir)),
            ("Commit", manifest.git_commit),
            ("Status", manifest.certification_status),
            ("Artifacts", str(len(manifest.artifact_hashes))),
        ],
    )
    if report.ok:
        return 0
    ui.fail("Pack written, but the verification gate is BLOCKED")
    return 1


def cmd_push_evidence(args: argparse.Namespace) -> int:
    load_dotenv()
    evidence_path = Path(args.from_dir) if args.from_dir else evidence_dir()
    push = os.environ.get("CERTHUB_PUSH", "").strip() == "1" or bool(args.push)
    dry_run = not push
    ui.banner(
        "Release Record (preview)"
        if dry_run
        else "Create Release Record"
    )
    result = push_evidence(
        baseline=args.baseline,
        evidence_path=evidence_path,
        dry_run=dry_run,
        evidence_url=args.evidence_url,
    )
    body = result.payload.model_dump(by_alias=True, exclude_none=True)
    print(json.dumps(body, indent=2, sort_keys=True))
    tenant = TenantSettings.load()
    records_url = dashboard_kt_url(tenant, kt="release_record")
    if dry_run:
        ui.details(
            [
                ("Baseline", args.baseline),
                ("Mode", "Preview only — nothing written to CertHub"),
                ("Next step", "Re-run with --push to create the release evidence record"),
            ],
            title="Preview",
        )
        ui.link_panel(
            "Release evidence KT in CertHub",
            records_url,
            note="Destination knowledge topic (Release Record).",
        )
        return 0
    ui.success_panel(
        "Release evidence record created",
        [
            ("Baseline", args.baseline),
            ("Record id", result.record_id or ""),
            ("Knowledge topic", "Release Record"),
        ],
    )
    ui.link_panel(
        "Open in CertHub",
        records_url,
        note="Review the controlled release evidence record for this software baseline.",
    )
    return 0


def cmd_confirm(args: argparse.Namespace) -> int:
    load_dotenv()
    ui.banner("Release Record confirmation")
    evidence_path = Path(args.from_dir) if args.from_dir else evidence_dir()
    if args.package_first:
        ui.step("Building evidence pack")
        package_evidence()
    proof = confirm_evidence(
        baseline=args.baseline,
        evidence_path=evidence_path,
        evidence_url=args.evidence_url,
    )
    print(format_proof(proof))
    tenant = TenantSettings.load()
    records_url = dashboard_kt_url(tenant, kt="release_record")
    ui.details(
        [
            ("Baseline", args.baseline),
            ("Matched", "yes" if proof.matched else "no"),
            ("Record id", proof.record_id or ""),
        ],
        title="Round-trip result",
    )
    ui.link_panel(
        "Release evidence KT in CertHub",
        records_url,
        note="Confirm the record appears under this knowledge topic.",
    )
    if proof.matched:
        ui.ok("Release Record confirmed in CertHub")
        return 0
    ui.fail("Release Record could not be confirmed")
    return 1


def cmd_open_kt(args: argparse.Namespace) -> int:
    kt: DashboardKt = args.kt
    if kt == "system_requirements":
        title = "System Requirements"
        note = "Controlled System Requirements in CertHub — edit here, then synchronize."
    else:
        title = "Release Record"
        note = "Controlled release evidence for software baselines."
    ui.banner(f"Open {title}")
    tenant = TenantSettings.load()
    url = dashboard_kt_url(tenant, kt=kt)
    ui.details(
        [
            ("Product", tenant.product_history_id),
            ("Knowledge unit", tenant.ku_history_id),
            ("Product version", tenant.product_version),
            ("Knowledge topic", title),
        ],
        title="CertHub location",
    )
    ui.link_panel(title, url, note=note)
    if not args.no_open:
        _open_url(url)
        ui.ok(f"Opened {title} in CertHub")
    else:
        ui.ok("URL ready")
    return 0


def cmd_config_get(args: argparse.Namespace) -> int:
    """Print one TenantSettings field (for Makefile / scripts; no API key)."""
    tenant = TenantSettings.load()
    key = args.key.strip()
    if not hasattr(tenant, key):
        raise ValueError(f"Unknown tenant setting: {key!r}")
    value = getattr(tenant, key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"Missing required field: '{key}'")
    print(value)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cadence",
        description=(
            "Cadence — CertHub SaMD Engineering Loop: synchronize requirements, "
            "verify traceability, and create Release Records on release"
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sync_p = sub.add_parser(
        "sync",
        help="Synchronize CertHub requirements into the engineering twin",
    )
    sync_p.set_defaults(func=cmd_sync)

    verify_p = sub.add_parser(
        "verify", help="Verify requirement → specification → implementation → test"
    )
    verify_p.set_defaults(func=cmd_verify)

    report_p = sub.add_parser("report", help="Write certification summary artifacts")
    report_p.set_defaults(func=cmd_report)

    package_p = sub.add_parser(
        "package-evidence",
        help="Build the evidence pack for a software baseline",
    )
    package_p.set_defaults(func=cmd_package_evidence)

    push_p = sub.add_parser(
        "push-evidence",
        help="Create a Release Record in CertHub (preview by default)",
    )
    push_p.add_argument(
        "--baseline",
        required=True,
        help="Release version X.Y.Z or vX.Y.Z (not main, not RC)",
    )
    push_p.add_argument(
        "--from",
        dest="from_dir",
        default=str(evidence_dir()),
        help="Evidence pack directory (default: evidence/)",
    )
    push_p.add_argument(
        "--push",
        action="store_true",
        help="Create the Release Record in CertHub (default is preview)",
    )
    push_p.add_argument(
        "--evidence-url",
        default=None,
        help="Override evidence URL (else GITHUB_* / CERTHUB_EVIDENCE_URL / local)",
    )
    push_p.set_defaults(func=cmd_push_evidence)

    confirm_p = sub.add_parser(
        "confirm",
        help="Create and confirm a Release Record round-trip in CertHub",
    )
    confirm_p.add_argument(
        "--baseline",
        required=True,
        help="Release version used for the confirm record",
    )
    confirm_p.add_argument(
        "--from",
        dest="from_dir",
        default=str(evidence_dir()),
        help="Evidence pack directory (default: evidence/)",
    )
    confirm_p.add_argument(
        "--package-first",
        action="store_true",
        help="Build the evidence pack before confirming",
    )
    confirm_p.add_argument(
        "--evidence-url",
        default=None,
        help="Override evidence URL for the confirm record",
    )
    confirm_p.set_defaults(func=cmd_confirm)

    open_req = sub.add_parser(
        "open-requirements",
        help="Open the System Requirements knowledge topic in CertHub",
    )
    open_req.add_argument(
        "--no-open",
        action="store_true",
        help="Print URL only (do not open a browser)",
    )
    open_req.set_defaults(func=cmd_open_kt, kt="system_requirements")

    open_vr = sub.add_parser(
        "open-release-record",
        help="Open the Release Record knowledge topic in CertHub",
    )
    open_vr.add_argument(
        "--no-open",
        action="store_true",
        help="Print URL only (do not open a browser)",
    )
    open_vr.set_defaults(func=cmd_open_kt, kt="release_record")

    cfg_p = sub.add_parser(
        "config-get",
        help="Print one certhub.toml tenant field (no API key)",
    )
    cfg_p.add_argument(
        "key",
        help="TenantSettings field name (e.g. techdoc_base_url)",
    )
    cfg_p.set_defaults(func=cmd_config_get)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:  # noqa: BLE001 - CLI boundary
        ui.fail(str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
