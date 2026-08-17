"""TenantSettings / dashboard URL / config-get reader tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from certhub_connector.config.dashboard_url import dashboard_kt_url
from certhub_connector.config.settings import TenantSettings


def test_tenant_settings_load_committed_toml() -> None:
    tenant = TenantSettings.load()
    assert tenant.dashboard_base_url
    assert tenant.product_history_id
    assert tenant.ku_history_id
    assert tenant.product_version
    assert tenant.system_requirements_kt_id
    assert tenant.system_requirements_kt_history_id
    assert tenant.verification_kt_id
    assert tenant.release_record_kt_id
    assert tenant.release_record_kt_history_id
    assert not tenant.techdoc_base_url.endswith("/")
    assert not tenant.records_base_url.endswith("/")
    assert not tenant.tracer_base_url.endswith("/")
    assert tenant.techdoc_base_url.startswith("https://")
    assert tenant.tracer_base_url.startswith("https://")


def test_dashboard_kt_urls_from_tenant() -> None:
    tenant = TenantSettings.load()
    req = dashboard_kt_url(tenant, kt="system_requirements")
    vr = dashboard_kt_url(tenant, kt="release_record")
    assert req.startswith(f"{tenant.dashboard_base_url}/dashboard/products/")
    assert f"knowledgeTopicId={tenant.system_requirements_kt_history_id}" in req
    assert f"knowledgeTopicId={tenant.release_record_kt_history_id}" in vr
    assert f"version={tenant.product_version}" in vr
    assert tenant.product_history_id in vr
    assert tenant.ku_history_id in vr


def test_tenant_settings_rejects_missing_key(tmp_path: Path) -> None:
    path = tmp_path / "certhub.toml"
    path.write_text(
        'techdoc_base_url = "https://example.com"\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Missing required field"):
        TenantSettings.load(path)
