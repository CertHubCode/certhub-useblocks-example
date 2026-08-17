#!/usr/bin/env python3
"""Thin bridge: official CodeLinks analyse → verify-gate JSON + needextend RST.

1. Invokes ``codelinks analyse``
2. Normalizes marked_content.json into reports/codelinks_analysis.json for verify
3. Writes needextend RST with local-url, impl-file, and remote-url
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOML = ROOT / "codelinks.toml"
REPORTS = ROOT / "reports"
RAW_DIR = REPORTS / "codelinks_raw"
MARKED_JSON = RAW_DIR / "marked_content.json"
ANALYSIS_JSON = REPORTS / "codelinks_analysis.json"
GENERATED = ROOT / "sphinx" / "source" / "generated"
NEEDEXTEND_RST = GENERATED / "codelinks_needextend.rst"


def _run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=ROOT)


def _normalize_records(raw: object) -> list[dict]:
    """Flatten CodeLinks marked_content.json into verify-friendly need-id-refs."""
    records: list[dict] = []

    def consume(item: object) -> None:
        if isinstance(item, list):
            for entry in item:
                consume(entry)
            return
        if not isinstance(item, dict):
            return
        # Direct need-id-refs record
        need_ids = item.get("need_ids")
        if need_ids:
            filepath = item.get("filepath") or item.get("file") or ""
            if isinstance(filepath, Path):
                filepath = str(filepath)
            try:
                rel = str(Path(str(filepath)).resolve().relative_to(ROOT))
            except Exception:  # noqa: BLE001
                rel = str(filepath)
            scope = item.get("tagged_scope") or ""
            if not isinstance(scope, str):
                scope = str(scope)[:120]
            source_map = item.get("source_map") or {}
            records.append(
                {
                    "filepath": rel,
                    "need_ids": list(need_ids),
                    "tagged_scope": scope.split("\n", 1)[0][:120],
                    "marker": item.get("marker", "@need-ids:"),
                    "type": "need-id-refs",
                    "source_map": source_map,
                    "remote_url": item.get("remote_url") or item.get("remote-url") or "",
                }
            )
            return
        # Nested project dumps
        for key in ("need_id_refs", "results", "items", "projects", "marked_content"):
            if key in item:
                consume(item[key])
        for value in item.values():
            if isinstance(value, (list, dict)):
                consume(value)

    consume(raw)
    return records


def _fallback_grep() -> list[dict]:
    records: list[dict] = []
    for path in (ROOT / "src" / "sterilisator_20a").rglob("*.py"):
        if not path.is_file():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines):
            if "@need-ids:" not in line:
                continue
            ids_part = line.split("@need-ids:", 1)[1].strip()
            need_ids = [part.strip() for part in ids_part.split(",") if part.strip()]
            scope = ""
            for follow in lines[idx + 1 : idx + 8]:
                stripped = follow.strip()
                if stripped.startswith("def "):
                    scope = stripped
                    break
            records.append(
                {
                    "filepath": str(path.relative_to(ROOT)),
                    "need_ids": need_ids,
                    "tagged_scope": scope,
                    "marker": "@need-ids:",
                    "type": "need-id-refs",
                    "source_map": {"start": {"row": idx, "column": 0}},
                }
            )
    return records


def _write_needextend(records: list[dict]) -> None:
    GENERATED.mkdir(parents=True, exist_ok=True)
    by_need: dict[str, list[dict]] = {}
    for record in records:
        for need_id in record.get("need_ids", []):
            by_need.setdefault(need_id, []).append(record)

    lines = [
        ".. GENERATED via official CodeLinks analyse + write bridge — DO NOT EDIT",
        "",
        "Source markers from ``@need-ids:`` (Sphinx-CodeLinks).",
        "",
    ]
    for need_id in sorted(by_need):
        rec = by_need[need_id][0]
        filepath = rec.get("filepath", "")
        row = 1
        start = (rec.get("source_map") or {}).get("start") or {}
        if isinstance(start, dict) and "row" in start:
            row = int(start["row"]) + 1
        remote = str(rec.get("remote_url") or "").strip()
        block = [
            f".. needextend:: {need_id}",
            f"   :local-url: ../../{filepath}#L{row}",
            f"   :impl-file: {filepath}",
        ]
        if remote:
            block.append(f"   :remote-url: {remote}")
        block.append("")
        lines.extend(block)
    NEEDEXTEND_RST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    REPORTS.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED.mkdir(parents=True, exist_ok=True)

    try:
        _run(["codelinks", "analyse", str(TOML), "-o", str(RAW_DIR)])
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"Official codelinks analyse failed ({exc}); using marker fallback", file=sys.stderr)

    records: list[dict] = []
    if MARKED_JSON.is_file():
        raw = json.loads(MARKED_JSON.read_text(encoding="utf-8"))
        records = _normalize_records(raw)

    if not records:
        records = _fallback_grep()

    ANALYSIS_JSON.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    if records:
        _write_needextend(records)

    print(f"Wrote {ANALYSIS_JSON} ({len(records)} marker records)")
    print(f"Wrote {NEEDEXTEND_RST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
