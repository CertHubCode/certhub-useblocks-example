"""Tests for public-only OpenAPI filtering before codegen."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from certhub_connector.api.filter_public import (
    filter_openapi_file,
    filter_to_public_operations,
    prune_unused_schemas,
)


def _mini_spec() -> dict:
    return {
        "openapi": "3.0.0",
        "info": {"title": "Test", "version": "1.0.0"},
        "paths": {
            "/public": {
                "get": {
                    "operationId": "public_get",
                    "x-public": True,
                    "responses": {
                        "200": {
                            "description": "ok",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/PublicModel"
                                    }
                                }
                            },
                        }
                    },
                }
            },
            "/internal": {
                "get": {
                    "operationId": "internal_get",
                    "responses": {
                        "200": {
                            "description": "ok",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/InternalModel"
                                    }
                                }
                            },
                        }
                    },
                }
            },
        },
        "components": {
            "schemas": {
                "PublicModel": {
                    "type": "object",
                    "properties": {
                        "nested": {"$ref": "#/components/schemas/NestedModel"}
                    },
                },
                "NestedModel": {"type": "object", "properties": {"id": {"type": "string"}}},
                "InternalModel": {"type": "object"},
                "UnusedModel": {"type": "object"},
            }
        },
    }


def test_filter_keeps_only_x_public() -> None:
    spec = _mini_spec()
    kept, dropped = filter_to_public_operations(spec)
    assert kept == 1
    assert dropped == 1
    assert "/public" in spec["paths"]
    assert "/internal" not in spec["paths"]
    assert "get" in spec["paths"]["/public"]


def test_prune_unused_schemas_keeps_transitive_refs() -> None:
    spec = _mini_spec()
    filter_to_public_operations(spec)
    removed = prune_unused_schemas(spec)
    schemas = spec["components"]["schemas"]
    assert removed == 2
    assert "PublicModel" in schemas
    assert "NestedModel" in schemas
    assert "InternalModel" not in schemas
    assert "UnusedModel" not in schemas


def test_filter_openapi_file_writes_and_rejects_empty(tmp_path: Path) -> None:
    path = tmp_path / "api.json"
    path.write_text(json.dumps(_mini_spec()), encoding="utf-8")

    kept, dropped, pruned = filter_openapi_file(path)
    assert kept == 1
    assert dropped == 1
    assert pruned == 2

    written = json.loads(path.read_text(encoding="utf-8"))
    assert list(written["paths"]) == ["/public"]
    assert set(written["components"]["schemas"]) == {"PublicModel", "NestedModel"}

    empty = tmp_path / "empty.json"
    empty.write_text(
        json.dumps(
            {
                "openapi": "3.0.0",
                "info": {"title": "Empty", "version": "1"},
                "paths": {
                    "/x": {"get": {"operationId": "nope", "responses": {"200": {}}}}
                },
            }
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="x-public"):
        filter_openapi_file(empty)
