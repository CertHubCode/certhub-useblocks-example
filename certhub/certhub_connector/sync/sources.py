"""Abstractions for reading CertHub exports."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Protocol

from certhub_connector.api.client import RecordsClient, TechDocClient, TracerClient
from certhub_connector.config import CerthubConfig
from certhub_connector.config.paths import certhub_generated_dir
from certhub_connector.sync.mapper import map_records_to_export
from certhub_connector.sync.models import CertHubExport
from certhub_connector.sync.requirements_use_case import (
    TOPIC_COMPONENT,
    TOPIC_DESIGN_OUTPUT,
    TOPIC_SYSTEM,
    TOPIC_UNIT,
    TOPIC_USER,
    TOPIC_VALIDATION,
    TOPIC_VERIFICATION,
)
from certhub_connector.sync.trace_links import usecase_neighbors

logger = logging.getLogger(__name__)

_LABEL_TO_TOPIC: dict[str, str] = {
    "user": TOPIC_USER,
    "system": TOPIC_SYSTEM,
    "component": TOPIC_COMPONENT,
    "unit": TOPIC_UNIT,
    "design_output": TOPIC_DESIGN_OUTPUT,
    "verification": TOPIC_VERIFICATION,
    "validation": TOPIC_VALIDATION,
}


class CertHubExportSource(Protocol):
    """Load a normalized CertHub export."""

    def load(self) -> CertHubExport:
        """Load and validate a CertHub export."""


def _write_records_snapshot(path: Path, records: list) -> None:
    path.write_text(
        json.dumps(
            [item.model_dump(mode="json", by_alias=True) for item in records],
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def _write_kt_snapshot(path: Path, kt) -> None:
    path.write_text(
        kt.model_dump_json(indent=2, by_alias=True) + "\n",
        encoding="utf-8",
    )


def _write_schema_snapshot(path: Path, schema: dict | None) -> None:
    payload = schema if isinstance(schema, dict) else {}
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


class HttpKtExportSource:
    """Load Tech Doc KT metadata + seven Records lists + Tracer → CertHubExport."""

    def __init__(
        self,
        techdoc_client: TechDocClient | None = None,
        records_client: RecordsClient | None = None,
        tracer_client: TracerClient | None = None,
        *,
        config: CerthubConfig | None = None,
    ) -> None:
        if techdoc_client is None or records_client is None:
            if config is None:
                config = CerthubConfig.load()
        self._config = config or (
            techdoc_client.config if techdoc_client is not None else None
        )
        if self._config is None and records_client is not None:
            self._config = records_client.config
        if self._config is None:
            raise ValueError("Missing required field: 'config'")
        self._techdoc = techdoc_client or TechDocClient(self._config)
        self._records = records_client or RecordsClient(self._config)
        self._tracer = tracer_client or TracerClient(self._config)
        self.link_warnings: list[str] = []
        self.trace_assignments: list[str] = []
        self.trace_record_count: int = 0
        self.trace_neighbor_count: int = 0

    def load(self) -> CertHubExport:
        tenant = self._config.tenant
        generated = certhub_generated_dir()
        generated.mkdir(parents=True, exist_ok=True)

        kt_specs = (
            ("user", tenant.user_requirements_kt_id),
            ("system", tenant.system_requirements_kt_id),
            ("component", tenant.component_requirements_kt_id),
            ("unit", tenant.unit_requirements_kt_id),
            ("design_output", tenant.design_output_kt_id),
            ("verification", tenant.verification_kt_id),
            ("validation", tenant.validation_kt_id),
        )

        kts = {}
        schemas: dict[str, dict | None] = {}
        records_by_label: dict[str, list] = {}
        topic_by_external_id: dict[str, str] = {}
        for label, kt_id in kt_specs:
            kt = self._techdoc.get_kt(kt_id)
            kts[label] = kt
            schema = kt.knowledge_topic_schema
            schemas[label] = schema
            _write_kt_snapshot(generated / f"{label}_kt_raw.json", kt)
            _write_schema_snapshot(generated / f"{label}_schema.json", schema)

            records = self._records.list_records_for_kt(kt_id)
            records_by_label[label] = records
            _write_records_snapshot(generated / f"{label}_records_raw.json", records)
            topic = _LABEL_TO_TOPIC[label]
            for record in records:
                external_id = record.field_id
                if not external_id:
                    raise ValueError(f"Record '{record.name}' missing required field: '_id'")
                topic_by_external_id[external_id] = topic

        record_ids = list(topic_by_external_id.keys())
        logger.info("tracer batch/list for %s synced Record ids", len(record_ids))
        trace_results = self._tracer.batch_list_records(record_ids)
        neighbors = usecase_neighbors(trace_results, set(record_ids))
        linked = sum(1 for targets in neighbors.values() if targets)
        logger.info(
            "tracer use-case neighbors: %s records with ≥1 in-sync edge",
            linked,
        )
        (generated / "traces_batch_list_raw.json").write_text(
            json.dumps(trace_results, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        self.trace_record_count = len(record_ids)
        self.trace_neighbor_count = linked

        warnings: list[str] = []
        assignments: list[str] = []
        export = map_records_to_export(
            kts["system"],
            user_records=records_by_label["user"],
            system_records=records_by_label["system"],
            component_records=records_by_label["component"],
            unit_records=records_by_label["unit"],
            design_output_records=records_by_label["design_output"],
            verification_records=records_by_label["verification"],
            validation_records=records_by_label["validation"],
            product_version=tenant.product_version,
            usecase_neighbors=neighbors,
            topic_by_external_id=topic_by_external_id,
            link_warnings=warnings,
            trace_assignments=assignments,
            user_schema=schemas["user"],
            system_schema=schemas["system"],
            component_schema=schemas["component"],
            unit_schema=schemas["unit"],
            design_output_schema=schemas["design_output"],
            verification_schema=schemas["verification"],
            validation_schema=schemas["validation"],
        )
        self.link_warnings = list(warnings)
        self.trace_assignments = list(assignments)
        return export
