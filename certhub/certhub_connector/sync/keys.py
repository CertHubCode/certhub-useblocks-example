"""Resolve CertHub form field keys via schema ``certhub-key`` (and label fallback)."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

REQUIRED_RELEASE_EVIDENCE_KEYS: tuple[str, ...] = (
    "release-number",
    "release-id",
    "generated-at",
    "evidence-url",
    "details",
)

# Labels used when a form component has no certhub-key yet (inbound KTs today).
_LABEL_TO_SEMANTIC: dict[str, str] = {
    "name": "name",
    "description": "description",
    "description / requirement statement": "description",
    "specification": "specification",
    "requirement concerning": "concerning",
    "test under": "test_under",
    "test condition": "test_condition",
    "standard clause": "standard_clause",
    "acceptance criteria": "acceptance_criteria",
    "expected test status": "expected_test_status",
    "expected test result": "test_result",
    "validation regarding": "validation_regarding",
    "sample size": "sample_size",
    "sample size justification": "sample_size_justification",
    "relates to system requirement(s)": "relates_to_system_requirement",
    "relates to -> component req": "relates_to_component_requirement",
    "relates to -> verification": "relates_to_verification",
    "relates to risk control measure(s)": "relates_to_risk_control",
    "individual id": "individual_id",
}

# Form keys that are already stable / semantic on the CertHub form.
_SEMANTIC_PASSTHROUGH: frozenset[str] = frozenset(
    {
        "name",
        "description",
        "type",
        "priority",
        "source",
        "justification",
        "test_method",
        "test_result",
        "validation_method",
        "results",
        "status",
        "rationale",
        "relates_to_system_requirement",
        "relates_to_component_requirement",
        "relates_to_verification",
        "relates_to_risk_control",
        "individual_id",
        "specification",
    }
)

# Temporary bridge for fixture / live data before certhub-keys exist on inbound forms.
# Prefer schema certhub-key or label mapping; never put these names on domain models.
# Delete entries once every inbound KT schema exposes certhub-key for that field —
# do not expand this map for new forms.
_OPAQUE_TO_SEMANTIC: dict[str, str] = {
    "checklist_kgd0ri": "concerning",
    "textfield_u1u4nh": "standard_clause",
    "textarea_rs0jwr": "test_condition",
    "textarea_d1jh7": "acceptance_criteria",
    "select_p361sa": "expected_test_status",
    "radio_mj9zeru": "test_under",
    "textfield_82f9x4": "validation_regarding",
    "textarea_15pm9": "acceptance_criteria",
    "textfield_ftyshh": "sample_size",
    "textarea_8ohfuj": "sample_size_justification",
    "textfield_5azvqs": "name",
    "textarea_8t3kc": "description",
    "textfield_3veivb": "relates_to_verification",
}


def certhub_key_to_field(certhub_key: str) -> str:
    """``release-number`` → ``release_number``."""
    if not certhub_key or not certhub_key.strip():
        raise ValueError("Missing required field: 'certhub_key'")
    return certhub_key.strip().replace("-", "_")


class CerthubKeyMap(BaseModel):
    """Semantic certhub-key → opaque form component key."""

    model_config = ConfigDict(frozen=True)

    mapping: dict[str, str] = Field(default_factory=dict)

    def form_key(self, certhub_key: str) -> str:
        if not certhub_key:
            raise ValueError("Missing required field: 'certhub_key'")
        key = self.mapping.get(certhub_key)
        if not key:
            raise ValueError(
                f"KT schema is missing certhub-key '{certhub_key}'. "
                f"Present: {sorted(self.mapping)}"
            )
        return key

    def require_all(self, keys: tuple[str, ...] = REQUIRED_RELEASE_EVIDENCE_KEYS) -> None:
        missing = [k for k in keys if k not in self.mapping]
        if missing:
            raise ValueError(
                "KT schema missing required certhub-keys: "
                f"{missing}. Present: {sorted(self.mapping)}"
            )


def certhub_key_map_from_schema(schema: dict[str, Any]) -> CerthubKeyMap:
    """Build map from a knowledge_topic_schema dict (components list)."""
    if not schema:
        raise ValueError("Missing required field: 'schema'")
    components = schema.get("components")
    if not isinstance(components, list):
        raise ValueError(
            "knowledge_topic_schema.components must be a list "
            f"(got {type(components).__name__})"
        )
    mapping: dict[str, str] = {}
    for component in components:
        if not isinstance(component, dict):
            continue
        form_key = component.get("key")
        properties = component.get("properties")
        if not isinstance(form_key, str) or not form_key.strip():
            continue
        if not isinstance(properties, dict):
            continue
        certhub_key = properties.get("certhub-key")
        if not isinstance(certhub_key, str) or not certhub_key.strip():
            continue
        certhub_key = certhub_key.strip()
        if certhub_key in mapping:
            raise ValueError(
                f"Duplicate certhub-key '{certhub_key}' in KT schema "
                f"({mapping[certhub_key]!r} and {form_key!r})"
            )
        mapping[certhub_key] = form_key.strip()
    return CerthubKeyMap(mapping=mapping)


def semanticize_record_data(
    raw: dict[str, Any] | None,
    schema: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Map opaque form ``data`` keys → semantic field names for domain models.

    Priority per component / raw key:
    1. ``properties["certhub-key"]`` from schema (canonical)
    2. component label → known semantic name
    3. form key already semantic (passthrough)
    4. temporary opaque→semantic bridge (fixtures / pre-key forms only)
    """
    if not raw:
        return {}

    out: dict[str, Any] = {}
    consumed_form_keys: set[str] = set()

    if schema:
        components = schema.get("components")
        if isinstance(components, list):
            for component in components:
                if not isinstance(component, dict):
                    continue
                form_key = component.get("key")
                if not isinstance(form_key, str) or not form_key.strip():
                    continue
                form_key = form_key.strip()
                if form_key not in raw:
                    continue
                properties = component.get("properties")
                label = component.get("label")
                semantic: str | None = None
                if isinstance(properties, dict):
                    certhub_key = properties.get("certhub-key")
                    if isinstance(certhub_key, str) and certhub_key.strip():
                        semantic = certhub_key_to_field(certhub_key)
                if semantic is None and isinstance(label, str) and label.strip():
                    semantic = _LABEL_TO_SEMANTIC.get(label.strip().casefold())
                if semantic is None and form_key in _SEMANTIC_PASSTHROUGH:
                    semantic = form_key
                if semantic is None:
                    semantic = _OPAQUE_TO_SEMANTIC.get(form_key)
                if semantic is None:
                    continue
                out[semantic] = raw[form_key]
                consumed_form_keys.add(form_key)

    for form_key, value in raw.items():
        if form_key in consumed_form_keys:
            continue
        if form_key in _SEMANTIC_PASSTHROUGH:
            out.setdefault(form_key, value)
            continue
        bridged = _OPAQUE_TO_SEMANTIC.get(form_key)
        if bridged is not None:
            out.setdefault(bridged, value)

    return out
