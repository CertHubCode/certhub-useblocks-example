"""Join Sphinx needs from Tracer ``connected_within_use_case`` edges + topic rules."""

from __future__ import annotations

import logging
from collections.abc import Mapping
from typing import Any, Protocol

from certhub_connector.sync.requirements_use_case import relation_for

logger = logging.getLogger(__name__)

_USECASE_RELATION = "connected_within_use_case"
_REQ_ID_PREFIXES = ("UREQ_", "SYSREQ_", "CREQ_", "UNITREQ_")


class _LinkableNeed(Protocol):
    id: str
    external_id: str | None
    links: list[str]


def usecase_neighbors(
    results: Mapping[str, Any],
    known: set[str],
    *,
    relation: str = _USECASE_RELATION,
) -> dict[str, set[str]]:
    """known external_id → neighbor external_ids (undirected); both ends must be known."""
    if not known:
        return {}
    out: dict[str, set[str]] = {eid: set() for eid in known}
    for payload in results.values():
        if not isinstance(payload, Mapping):
            continue
        for edge in payload.get("edges") or []:
            if not isinstance(edge, Mapping):
                continue
            relation_types = edge.get("relation_type") or []
            if relation not in relation_types:
                continue
            src = (edge.get("source_node") or {}).get("node_id")
            tgt = (edge.get("target_node") or {}).get("node_id")
            if not src or not tgt or src == tgt:
                continue
            if src in known and tgt in known:
                out[src].add(tgt)
                out[tgt].add(src)
            else:
                logger.debug(
                    "trace-skip unknown endpoint src=%s tgt=%s (known=%s/%s)",
                    src,
                    tgt,
                    src in known,
                    tgt in known,
                )
    return out


def _append_unique(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def _attach_link(need: Any, target_need_id: str, relation_name: str) -> None:
    _append_unique(need.links, target_need_id)
    if relation_name.startswith("Verifies") and hasattr(need, "verifies"):
        if target_need_id.startswith(_REQ_ID_PREFIXES):
            _append_unique(need.verifies, target_need_id)


def apply_usecase_links(
    need_by_external_id: Mapping[str, _LinkableNeed],
    topic_by_external_id: Mapping[str, str],
    neighbors: Mapping[str, set[str]],
) -> list[str]:
    """Apply directed topic-pair relations onto need.links / Verification.verifies.

    Returns human-readable assignment lines for CLI display.
    """
    if not need_by_external_id:
        raise ValueError("Missing required field: 'need_by_external_id'")
    if topic_by_external_id is None:
        raise ValueError("Missing required field: 'topic_by_external_id'")

    assignments: list[str] = []
    for src_ext, targets in neighbors.items():
        src_need = need_by_external_id.get(src_ext)
        src_topic = topic_by_external_id.get(src_ext)
        if src_need is None or not src_topic:
            continue
        for tgt_ext in sorted(targets):
            tgt_need = need_by_external_id.get(tgt_ext)
            tgt_topic = topic_by_external_id.get(tgt_ext)
            if tgt_need is None or not tgt_topic:
                logger.debug(
                    "trace-skip missing target need/topic src=%s tgt=%s",
                    src_ext,
                    tgt_ext,
                )
                continue
            relation_name = relation_for(src_topic, tgt_topic)
            if relation_name is None:
                logger.debug(
                    "trace-skip no relation rule %s -> %s (%s -> %s)",
                    src_topic,
                    tgt_topic,
                    src_need.id,
                    tgt_need.id,
                )
                continue
            _attach_link(src_need, tgt_need.id, relation_name)
            line = (
                f"{src_need.id} ({src_ext}) --{relation_name}--> "
                f"{tgt_need.id} ({tgt_ext})"
            )
            assignments.append(line)
            logger.info("trace-link %s", line)
    return assignments
