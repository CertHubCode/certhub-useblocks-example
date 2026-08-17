"""Build CertHub dashboard KT URLs from TenantSettings (no API required)."""

from __future__ import annotations

from typing import Literal

from certhub_connector.config.settings import TenantSettings

DashboardKt = Literal["system_requirements", "release_record"]


def dashboard_kt_url(tenant: TenantSettings, *, kt: DashboardKt) -> str:
    """Build a CertHub dashboard URL for a knowledge topic.

    Format:
    ``{dashboard}/dashboard/products/{product}/{ku}?version={ver}&knowledgeTopicId={kt_history}``
    """
    if kt == "system_requirements":
        knowledge_topic_history_id = tenant.system_requirements_kt_history_id
    elif kt == "release_record":
        knowledge_topic_history_id = tenant.release_record_kt_history_id
    else:
        raise ValueError(f"Unknown dashboard KT: {kt!r}")

    if not knowledge_topic_history_id:
        raise ValueError("Missing required field: 'knowledge_topic_history_id'")

    return (
        f"{tenant.dashboard_base_url}/dashboard/products/"
        f"{tenant.product_history_id}/{tenant.ku_history_id}"
        f"?version={tenant.product_version}"
        f"&knowledgeTopicId={knowledge_topic_history_id}"
    )
