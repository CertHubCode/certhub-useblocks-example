"""CertHub config: API key from env; tenant settings from committed certhub.toml."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, ValidationInfo, field_validator

from certhub_connector.config.paths import project_root


def load_dotenv(path: Path | None = None) -> None:
    """Load KEY=VALUE pairs from .env into os.environ (does not override)."""
    env_path = path or (project_root() / ".env")
    if not env_path.is_file():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


def default_config_path() -> Path:
    return project_root() / "certhub.toml"


def _require_env(key: str) -> str:
    value = os.environ.get(key, "").strip()
    if not value:
        raise ValueError(
            f"Missing required field: '{key}' "
            "(set in .env — see .env.example)"
        )
    return value


def _require_toml_str(data: dict[str, Any], key: str, *, path: Path) -> str:
    raw = data.get(key)
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError(
            f"Missing required field: '{key}' in {path} "
            "(see committed certhub.toml)"
        )
    return raw.strip()


def _read_toml_table(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ValueError(f"Missing required field: certhub.toml at {path}")
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Invalid certhub.toml: expected a table at {path}")
    return data


class TenantSettings(BaseModel):
    """Non-secret settings from certhub.toml — safe without API key."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    techdoc_base_url: str
    records_base_url: str
    tracer_base_url: str
    user_requirements_kt_id: str
    system_requirements_kt_id: str
    component_requirements_kt_id: str
    unit_requirements_kt_id: str
    design_output_kt_id: str
    verification_kt_id: str
    validation_kt_id: str
    release_record_kt_id: str
    dashboard_base_url: str
    product_history_id: str
    ku_history_id: str
    product_version: str
    user_requirements_kt_history_id: str
    system_requirements_kt_history_id: str
    component_requirements_kt_history_id: str
    unit_requirements_kt_history_id: str
    design_output_kt_history_id: str
    verification_kt_history_id: str
    validation_kt_history_id: str
    release_record_kt_history_id: str

    @field_validator("*")
    @classmethod
    def _normalize_str(cls, value: Any, info: ValidationInfo) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("must be a non-empty string")
        cleaned = value.strip()
        if info.field_name in (
            "techdoc_base_url",
            "records_base_url",
            "tracer_base_url",
            "dashboard_base_url",
        ):
            return cleaned.rstrip("/")
        return cleaned

    @classmethod
    def load(cls, path: Path | None = None) -> TenantSettings:
        """Load and validate non-secret tenant settings from certhub.toml."""
        config_path = path or default_config_path()
        data = _read_toml_table(config_path)
        payload = {
            key: _require_toml_str(data, key, path=config_path)
            for key in cls.model_fields
        }
        return cls.model_validate(payload)


class CerthubConfig(BaseModel):
    """Authenticated config: API key + tenant settings from certhub.toml.

    Access tenant fields via ``config.tenant.*`` (URLs, KT ids). The API key
    lives only on this object so Makefile ``config-get`` can read tenant
    settings without a secret.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    api_key: str = Field(..., min_length=1)
    tenant: TenantSettings

    @classmethod
    def load(
        cls,
        *,
        load_env_file: bool = True,
        config_path: Path | None = None,
    ) -> CerthubConfig:
        """Load API key from env and tenant settings from certhub.toml."""
        if load_env_file:
            load_dotenv()
        return cls(
            api_key=_require_env("CERTHUB_API_KEY"),
            tenant=TenantSettings.load(config_path),
        )
