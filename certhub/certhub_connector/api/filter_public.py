"""Filter OpenAPI specs to ``x-public: true`` operations before codegen.

Backends mark API-key routes with certhub_auth's ``@public_api`` decorator,
which emits ``x-public: true`` on the OpenAPI operation. Cadence generates
HTTP clients only from that public surface (same contract as the published
API docs).

Usage::

    python -m certhub_connector.api.filter_public schemas/techdoc.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

HTTP_METHODS = (
    "get",
    "put",
    "post",
    "delete",
    "options",
    "head",
    "patch",
    "trace",
)

_SCHEMA_REF_PREFIX = "#/components/schemas/"


def filter_to_public_operations(spec: dict[str, Any]) -> tuple[int, int]:
    """Keep only operations with ``x-public: true``. Return (kept, dropped)."""
    paths = spec.get("paths")
    if not isinstance(paths, dict):
        raise ValueError('OpenAPI spec has no "paths" object')

    kept = 0
    dropped = 0
    empty_routes: list[str] = []

    for route, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        for method in HTTP_METHODS:
            operation = path_item.get(method)
            if operation is None:
                continue
            if isinstance(operation, dict) and operation.get("x-public") is True:
                kept += 1
            else:
                del path_item[method]
                dropped += 1
        if not any(method in path_item for method in HTTP_METHODS):
            empty_routes.append(route)

    for route in empty_routes:
        del paths[route]

    return kept, dropped


def _collect_schema_refs(node: Any, found: set[str]) -> None:
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref.startswith(_SCHEMA_REF_PREFIX):
            found.add(ref[len(_SCHEMA_REF_PREFIX) :])
        for value in node.values():
            _collect_schema_refs(value, found)
    elif isinstance(node, list):
        for item in node:
            _collect_schema_refs(item, found)


def prune_unused_schemas(spec: dict[str, Any]) -> int:
    """Remove ``components.schemas`` entries not referenced by remaining ops.

    Returns the number of schemas removed.
    """
    components = spec.get("components")
    if not isinstance(components, dict):
        return 0
    schemas = components.get("schemas")
    if not isinstance(schemas, dict) or not schemas:
        return 0

    # Paths + remaining components (parameters, responses, …) except schemas
    # themselves — walk schemas transitively from path refs.
    roots: list[Any] = [spec.get("paths")]
    for key, value in components.items():
        if key != "schemas":
            roots.append(value)

    needed: set[str] = set()
    for root in roots:
        _collect_schema_refs(root, needed)

    # Transitively include nested schema refs.
    changed = True
    while changed:
        changed = False
        for name in list(needed):
            schema = schemas.get(name)
            if schema is None:
                continue
            before = len(needed)
            _collect_schema_refs(schema, needed)
            if len(needed) > before:
                changed = True

    removed = 0
    for name in list(schemas):
        if name not in needed:
            del schemas[name]
            removed += 1
    return removed


def filter_openapi_file(path: Path) -> tuple[int, int, int]:
    """Filter ``path`` in place. Return (kept, dropped, schemas_pruned)."""
    if not path.is_file():
        raise FileNotFoundError(f"OpenAPI schema not found: {path}")

    spec = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(spec, dict):
        raise ValueError(f"OpenAPI schema must be a JSON object: {path}")

    kept, dropped = filter_to_public_operations(spec)
    if kept == 0:
        raise ValueError(
            f"{path}: 0 operations marked \"x-public: true\" survived filtering "
            f"(dropped {dropped}). Annotate routes with @public_api on the "
            "source service, redeploy, re-fetch, and try again."
        )

    pruned = prune_unused_schemas(spec)
    path.write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
    return kept, dropped, pruned


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Filter an OpenAPI JSON file to x-public: true operations.",
    )
    parser.add_argument(
        "schema",
        type=Path,
        help="Path to openapi.json (filtered in place)",
    )
    args = parser.parse_args(argv)

    try:
        kept, dropped, pruned = filter_openapi_file(args.schema)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(
        f"Filtered {args.schema}: kept {kept} public operation(s), "
        f"dropped {dropped}, pruned {pruned} unused schema(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
