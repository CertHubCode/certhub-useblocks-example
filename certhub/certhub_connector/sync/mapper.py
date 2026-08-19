"""Map CertHub V-Model KTs into CertHubExport (seven content types).

Cross-need ``links`` / ``verifies`` come only from Tracer ``connected_within_use_case``
edges + the Requirements use-case topic→topic table — never keywords or form-text joins.
Need ids follow ``SYSREQ_001`` style prefixes parsed from record names when present.
CertHub Mongo ``_id`` is stored as ``external_id``.

Form ``record.data`` is remapped via ``certhub-key`` / labels before domain models see it.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Any, TypeVar

from pydantic import BaseModel

from certhub_connector.api.api_models.records.records_models import Record
from certhub_connector.api.api_models.techdoc.techdoc_models import (
    KnowledgeTopicDetailResponse,
)
from certhub_connector.sync.keys import semanticize_record_data
from certhub_connector.sync.models import (
    CertHubExport,
    ComponentRequirement,
    DesignOutput,
    ProjectInfo,
    RequirementBase,
    RequirementFormData,
    SystemRequirement,
    UnitRequirement,
    UserRequirement,
    Validation,
    ValidationFormData,
    Verification,
    VerificationFormData,
)
from certhub_connector.sync.trace_links import apply_usecase_links

_NEED_PREFIXES = (
    "UREQ",
    "SYSREQ",
    "CREQ",
    "UNITREQ",
    "DOUT",
    "VERIF",
    "VALID",
    "REQ",
    "SPEC",
    "TEST",
)
_PREFIX_GROUP = "|".join(_NEED_PREFIXES)
_NAME_PREFIX_RE = re.compile(
    rf"^({_PREFIX_GROUP})_(\d+)\s*[—–-]\s*(.+)$",
    re.IGNORECASE,
)

_LEGACY_PREFIX_MAP = {
    "REQ": "SYSREQ",
    "SPEC": "DOUT",
    "TEST": "VERIF",
}

TForm = TypeVar("TForm", bound=BaseModel)
TNeed = TypeVar("TNeed")
TReq = TypeVar("TReq", bound=RequirementBase)


def _canonical_prefix(prefix: str) -> str:
    upper = prefix.upper()
    return _LEGACY_PREFIX_MAP.get(upper, upper)


def _need_id(prefix: str, num: int) -> str:
    return f"{_canonical_prefix(prefix)}_{num:03d}"


def need_id_and_title(
    record_name: str,
    *,
    default_prefix: str,
    index: int,
) -> tuple[str, str]:
    stripped = record_name.strip()
    match = _NAME_PREFIX_RE.match(stripped)
    if match:
        num = int(match.group(2))
        return _need_id(match.group(1), num), match.group(3).strip()
    return _need_id(default_prefix, index), stripped


def form_from_record(
    model_type: type[TForm],
    record: Record,
    schema: dict[str, Any] | None = None,
    *,
    fill_description_from_specification: bool = False,
) -> TForm:
    if not record:
        raise ValueError("Missing required field: 'record'")
    if not model_type:
        raise ValueError("Missing required field: 'model_type'")
    semantic = semanticize_record_data(record.data, schema)
    if "name" not in semantic and record.name.strip():
        semantic["name"] = record.name.strip()
    if fill_description_from_specification and "description" not in semantic:
        for key in ("description", "specification"):
            if semantic.get(key):
                semantic["description"] = str(semantic[key])
                break
    return model_type.model_validate(semantic)


def form_data_from_record(
    record: Record,
    schema: dict[str, Any] | None = None,
) -> RequirementFormData:
    return form_from_record(
        RequirementFormData,
        record,
        schema,
        fill_description_from_specification=True,
    )


def verification_form_from_record(
    record: Record,
    schema: dict[str, Any] | None = None,
) -> VerificationFormData:
    return form_from_record(VerificationFormData, record, schema)


def validation_form_from_record(
    record: Record,
    schema: dict[str, Any] | None = None,
) -> ValidationFormData:
    return form_from_record(ValidationFormData, record, schema)


def _concerning_text(form: RequirementFormData) -> list[str] | None:
    if not form.concerning:
        return None
    return [item for item in form.concerning if item]


def _map_records(
    records: list[Record],
    *,
    prefix: str,
    schema: dict[str, Any] | None,
    kind: str,
    build: Callable[[Record, Any, str, str, str], TNeed],
    form_fn: Callable[[Record, dict[str, Any] | None], Any],
) -> list[TNeed]:
    sorted_records = sorted(records, key=lambda item: (item.field_id or item.name or ""))
    mapped: list[TNeed] = []
    seen: set[str] = set()
    for index, record in enumerate(sorted_records, start=1):
        form = form_fn(record, schema)
        external_id = record.field_id
        if not external_id:
            raise ValueError(f"Record '{record.name}' missing required field: '_id'")
        name = getattr(form, "name", None) or record.name
        need_id, title = need_id_and_title(
            name,
            default_prefix=prefix,
            index=index,
        )
        if need_id in seen:
            raise ValueError(f"Duplicate {kind} id '{need_id}' after mapping")
        seen.add(need_id)
        mapped.append(build(record, form, need_id, title, external_id))
    return mapped


def _map_requirement_records(
    records: list[Record],
    *,
    prefix: str,
    schema: dict[str, Any] | None,
    model: type[TReq],
) -> list[TReq]:
    def build(
        _record: Record,
        form: RequirementFormData,
        need_id: str,
        title: str,
        external_id: str,
    ) -> TReq:
        return model(
            id=need_id,
            title=title,
            description=form.description,
            status="approved",
            external_id=external_id,
            req_type=form.type,
            priority=form.priority,
            source=form.source,
            justification=form.justification,
            concerning=_concerning_text(form),
        )

    return _map_records(
        records,
        prefix=prefix,
        schema=schema,
        kind="requirement",
        build=build,
        form_fn=form_data_from_record,
    )


def _map_design_outputs(
    records: list[Record],
    schema: dict[str, Any] | None,
) -> list[DesignOutput]:
    def build(
        record: Record,
        form: RequirementFormData,
        need_id: str,
        title: str,
        external_id: str,
    ) -> DesignOutput:
        description = form.description
        semantic = semanticize_record_data(record.data, schema)
        spec_body = semantic.get("specification") or semantic.get("test_method")
        if spec_body and str(spec_body).strip():
            description = f"{description}\n\n{spec_body}".strip()
        return DesignOutput(
            id=need_id,
            title=title,
            description=description,
            status="approved",
            external_id=external_id,
            links=[],
        )

    return _map_records(
        records,
        prefix="DOUT",
        schema=schema,
        kind="design output",
        build=build,
        form_fn=form_data_from_record,
    )


def _map_verifications(
    records: list[Record],
    schema: dict[str, Any] | None,
) -> list[Verification]:
    def build(
        _record: Record,
        form: VerificationFormData,
        need_id: str,
        title: str,
        external_id: str,
    ) -> Verification:
        description = (
            form.test_method
            or form.acceptance_criteria
            or form.test_result
            or title
        )
        return Verification(
            id=need_id,
            title=title,
            description=description or title,
            status="approved",
            external_id=external_id,
            links=[],
            verifies=[],
        )

    return _map_records(
        records,
        prefix="VERIF",
        schema=schema,
        kind="verification",
        build=build,
        form_fn=verification_form_from_record,
    )


def _map_validations(
    records: list[Record],
    schema: dict[str, Any] | None,
) -> list[Validation]:
    def build(
        _record: Record,
        form: ValidationFormData,
        need_id: str,
        title: str,
        external_id: str,
    ) -> Validation:
        description = (
            form.validation_method
            or form.acceptance_criteria
            or form.results
            or title
        )
        return Validation(
            id=need_id,
            title=title,
            description=description or title,
            status="approved",
            external_id=external_id,
            links=[],
        )

    return _map_records(
        records,
        prefix="VALID",
        schema=schema,
        kind="validation",
        build=build,
        form_fn=validation_form_from_record,
    )


def _index_needs_by_external_id(
    *groups: list[Any],
) -> dict[str, Any]:
    by_ext: dict[str, Any] = {}
    for group in groups:
        for need in group:
            external_id = getattr(need, "external_id", None)
            if not external_id:
                raise ValueError(f"Need '{need.id}' missing required field: 'external_id'")
            if external_id in by_ext:
                raise ValueError(f"Duplicate external_id '{external_id}' across needs")
            by_ext[external_id] = need
    return by_ext


def map_records_to_export(
    system_kt: KnowledgeTopicDetailResponse,
    *,
    user_records: list[Record],
    system_records: list[Record],
    component_records: list[Record],
    unit_records: list[Record],
    design_output_records: list[Record],
    verification_records: list[Record],
    validation_records: list[Record],
    product_version: str,
    usecase_neighbors: dict[str, set[str]] | None = None,
    topic_by_external_id: dict[str, str] | None = None,
    link_warnings: list[str] | None = None,
    trace_assignments: list[str] | None = None,
    user_schema: dict[str, Any] | None = None,
    system_schema: dict[str, Any] | None = None,
    component_schema: dict[str, Any] | None = None,
    unit_schema: dict[str, Any] | None = None,
    design_output_schema: dict[str, Any] | None = None,
    verification_schema: dict[str, Any] | None = None,
    validation_schema: dict[str, Any] | None = None,
) -> CertHubExport:
    if not system_kt:
        raise ValueError("Missing required field: 'system_kt'")
    if not system_records:
        raise ValueError("Missing required field: 'system_records' must be non-empty")
    if not verification_records:
        raise ValueError("Missing required field: 'verification_records' must be non-empty")
    if not product_version or not product_version.strip():
        raise ValueError("Missing required field: 'product_version'")

    name = system_kt.knowledge_topic_name.strip()
    if not name:
        raise ValueError("Missing required field: 'knowledge_topic_name'")
    product_history_id = system_kt.product_history_id.strip()
    if not product_history_id:
        raise ValueError("Missing required field: 'product_history_id'")

    warnings: list[str] = []
    sys_schema = system_schema or system_kt.knowledge_topic_schema

    user_requirements = _map_requirement_records(
        user_records,
        prefix="UREQ",
        schema=user_schema,
        model=UserRequirement,
    )
    system_requirements = _map_requirement_records(
        system_records,
        prefix="SYSREQ",
        schema=sys_schema,
        model=SystemRequirement,
    )
    component_requirements = _map_requirement_records(
        component_records,
        prefix="CREQ",
        schema=component_schema,
        model=ComponentRequirement,
    )
    unit_requirements = _map_requirement_records(
        unit_records,
        prefix="UNITREQ",
        schema=unit_schema,
        model=UnitRequirement,
    )
    design_outputs = _map_design_outputs(
        design_output_records,
        design_output_schema,
    )
    verifications = _map_verifications(
        verification_records,
        verification_schema,
    )
    validations = _map_validations(
        validation_records,
        validation_schema,
    )

    if not user_records:
        warnings.append("User Requirements KT returned no records")
    if not component_records:
        warnings.append("Component Requirements KT returned no records")
    if not unit_records:
        warnings.append("Unit Requirements KT returned no records")
    if not design_output_records:
        warnings.append("Design Output KT returned no records")
    if not validation_records:
        warnings.append("Validation KT returned no records")

    need_by_external_id = _index_needs_by_external_id(
        user_requirements,
        system_requirements,
        component_requirements,
        unit_requirements,
        design_outputs,
        verifications,
        validations,
    )
    neighbors = usecase_neighbors or {}
    topics = topic_by_external_id or {}
    if neighbors and not topics:
        raise ValueError(
            "Missing required field: 'topic_by_external_id' when usecase_neighbors is set"
        )
    assignments: list[str] = []
    if neighbors:
        assignments = apply_usecase_links(need_by_external_id, topics, neighbors)

    if link_warnings is not None:
        link_warnings.clear()
        link_warnings.extend(warnings)
    if trace_assignments is not None:
        trace_assignments.clear()
        trace_assignments.extend(assignments)

    return CertHubExport(
        project=ProjectInfo(
            id=product_history_id,
            name=name,
            version=product_version.strip(),
        ),
        user_requirements=user_requirements,
        system_requirements=system_requirements,
        component_requirements=component_requirements,
        unit_requirements=unit_requirements,
        design_outputs=design_outputs,
        verifications=verifications,
        validations=validations,
    )
