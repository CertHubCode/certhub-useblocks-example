"""One-off export of needs_* from conf.py to ubproject.toml (ubCode migration)."""
# /// script
# dependencies = ["tomli-w"]
# ///
# uv run export_needs_toml.py

from __future__ import annotations

import sys
from pathlib import Path

import tomli_w

import conf

need_attributes: dict[str, object] = {}
for attribute in dir(conf):
    if attribute.startswith("needs_"):
        need_attributes[attribute[6:]] = getattr(conf, attribute)

output_path = Path(__file__).resolve().parent / "ubproject.toml"
payload: dict[str, object] = {
    "$schema": "https://ubcode.useblocks.com/ubproject.schema.json",
    "project": {"name": conf.project, "srcdir": "."},
    "needs": need_attributes,
}
output_path.write_text(tomli_w.dumps(payload), encoding="utf-8")
print(f"Wrote {output_path}", file=sys.stderr)
