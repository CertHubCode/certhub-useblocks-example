"""Normalized domain model for CertHub export data + requirement form payload."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class RequirementFormData(BaseModel):
    """Semantic SaMD Requirements fields (never opaque form-js keys)."""

    model_config = ConfigDict(extra="ignore")

    name: str
    description: str
    type: str | None = None
    priority: str | None = None
    source: str | None = None
    justification: str | None = None
    concerning: list[str] | None = None

    @field_validator("name", "description")
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Requirement form fields must be non-empty")
        return value.strip()


class VerificationFormData(BaseModel):
    """Semantic Verification fields (never opaque form-js keys)."""

    model_config = ConfigDict(extra="ignore")

    name: str
    test_method: str | None = None
    test_result: str | None = None
    test_under: str | None = None
    test_condition: str | None = None
    standard_clause: str | None = None
    acceptance_criteria: str | None = None
    expected_test_status: str | None = None

    @field_validator("name")
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Verification form fields must be non-empty")
        return value.strip()


class ValidationFormData(BaseModel):
    """Semantic Validation fields (never opaque form-js keys)."""

    model_config = ConfigDict(extra="ignore")

    name: str
    validation_method: str | None = None
    results: str | None = None
    status: str | None = None
    validation_regarding: str | None = None
    acceptance_criteria: str | None = None
    sample_size: str | None = None
    sample_size_justification: str | None = None

    @field_validator("name")
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Validation form fields must be non-empty")
        return value.strip()


class ProjectInfo(BaseModel):
    id: str
    name: str
    version: str

    @field_validator("id", "name", "version")
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Project fields must be non-empty")
        return value.strip()


class RequirementBase(BaseModel):
    """Shared base for the four requirement types (inputs in the V-model)."""

    id: str
    title: str
    description: str
    status: str = "approved"
    external_id: str | None = None
    links: list[str] = Field(default_factory=list)

    # Optional metadata from the requirement form; keep as plain strings.
    req_type: str | None = None
    priority: str | None = None
    source: str | None = None
    justification: str | None = None
    concerning: list[str] | None = None

    @field_validator("id", "title", "description", "status")
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Requirement fields must be non-empty")
        return value.strip()


class UserRequirement(RequirementBase):
    """User Requirements (input requirements)."""


class SystemRequirement(RequirementBase):
    """System Requirements (input requirements)."""


class ComponentRequirement(RequirementBase):
    """Component Requirements (input requirements)."""


class UnitRequirement(RequirementBase):
    """Unit Requirements (input requirements)."""


class DesignOutput(BaseModel):
    """Design Output (V-model outputs realized by software)."""

    id: str
    title: str
    description: str
    status: str = "approved"
    external_id: str | None = None

    # Links to the design inputs this output realizes.
    links: list[str] = Field(default_factory=list)

    @field_validator("id", "title", "description", "status")
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Design Output fields must be non-empty")
        return value.strip()


class Verification(BaseModel):
    """Verification (V-model right-side activities, proven by tests)."""

    id: str
    title: str
    description: str
    status: str = "approved"
    external_id: str | None = None

    # Optional semantic relations (links) and "verifies" edges.
    links: list[str] = Field(default_factory=list)
    verifies: list[str] = Field(default_factory=list)

    @field_validator("id", "title", "description", "status")
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Verification fields must be non-empty")
        return value.strip()


class Validation(BaseModel):
    """Validation (V-model right-side activities, proven by protocols)."""

    id: str
    title: str
    description: str
    status: str = "approved"
    external_id: str | None = None

    links: list[str] = Field(default_factory=list)

    @field_validator("id", "title", "description", "status")
    @classmethod
    def required_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Validation fields must be non-empty")
        return value.strip()


class CertHubExport(BaseModel):
    """Normalized CertHub export consumed by sync/verify."""

    project: ProjectInfo
    user_requirements: list[UserRequirement]
    system_requirements: list[SystemRequirement]
    component_requirements: list[ComponentRequirement]
    unit_requirements: list[UnitRequirement]
    design_outputs: list[DesignOutput]
    verifications: list[Verification]
    validations: list[Validation]

    @model_validator(mode="after")
    def validate_graph(self) -> CertHubExport:
        # Requirements layers can be sparse in the live tenant; fail only if
        # the graph would be unusable.
        for field_name in (
            "system_requirements",
            "verifications",
        ):
            if not getattr(self, field_name):
                raise ValueError(f"Missing required field: '{field_name}' must be non-empty")

        ids: dict[str, str] = {}
        for kind, items in (
            ("user_requirement", self.user_requirements),
            ("system_requirement", self.system_requirements),
            ("component_requirement", self.component_requirements),
            ("unit_requirement", self.unit_requirements),
            ("design_output", self.design_outputs),
            ("verification", self.verifications),
            ("validation", self.validations),
        ):
            for item in items:
                if item.id in ids:
                    raise ValueError(
                        f"Duplicate ID '{item.id}' found in {kind} "
                        f"(already used as {ids[item.id]})"
                    )
                ids[item.id] = kind

        known = set(ids)

        for dout in self.design_outputs:
            for target in dout.links:
                if target not in known:
                    raise ValueError(
                        f"Design Output '{dout.id}' links to unknown ID '{target}'"
                    )

        for verif in self.verifications:
            for target in [*verif.links, *verif.verifies]:
                if target not in known:
                    raise ValueError(
                        f"Verification '{verif.id}' references unknown ID '{target}'"
                    )

        for val in self.validations:
            for target in val.links:
                if target not in known:
                    raise ValueError(
                        f"Validation '{val.id}' links to unknown ID '{target}'"
                    )

        return self
