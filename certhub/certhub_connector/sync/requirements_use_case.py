"""Requirements use-case topic→topic relation names (CertHub design-controls web).

Faithful port of CertHub ``use-case-configs/requirements`` / Python twin. Tracer
stores undirected ``connected_within_use_case`` edges; this table names the
V-model meaning for each (source_topic, target_topic) pair.

NOTE: ``Relates to UR `` carries a trailing space verbatim from CertHub source.
"""

from __future__ import annotations

from dataclasses import dataclass

TOPIC_USER = "User Requirements"
TOPIC_SYSTEM = "System Requirements"
TOPIC_COMPONENT = "Component Requirements"
TOPIC_UNIT = "Unit Requirements"
TOPIC_DESIGN_OUTPUT = "Design Output"
TOPIC_VERIFICATION = "Verification"
TOPIC_VALIDATION = "Validation"
TOPIC_RCM = "Risk Control Measures"
TOPIC_USE_SCENARIOS = "Use Scenarios"


@dataclass(frozen=True)
class DomainTracerRelation:
    relation_name: str
    target_knowledge_topic: str
    allow_multiple: bool
    description: str
    bidirection: bool = True


_RELATIONS_BY_TOPIC: dict[str, tuple[DomainTracerRelation, ...]] = {
    TOPIC_USER: (
        DomainTracerRelation(
            relation_name="Relates to",
            target_knowledge_topic=TOPIC_RCM,
            allow_multiple=False,
            description="Select the risk control measure that are related to this requirement",
        ),
        DomainTracerRelation(
            relation_name="Derived from",
            target_knowledge_topic=TOPIC_USE_SCENARIOS,
            allow_multiple=True,
            description="Select the use scenario that led to this requirement.",
        ),
        DomainTracerRelation(
            relation_name="Validated By",
            target_knowledge_topic=TOPIC_VALIDATION,
            allow_multiple=True,
            description="Select validation activities linked to this requirement.",
        ),
        DomainTracerRelation(
            relation_name="Leads to",
            target_knowledge_topic=TOPIC_SYSTEM,
            allow_multiple=True,
            description="Select system requirements that were derived from this user requirement.",
        ),
    ),
    TOPIC_SYSTEM: (
        DomainTracerRelation(
            relation_name="Derived from RCM",
            target_knowledge_topic=TOPIC_RCM,
            allow_multiple=False,
            description="Select the risk control measure that led to this requirement",
        ),
        DomainTracerRelation(
            relation_name="Results in",
            target_knowledge_topic=TOPIC_COMPONENT,
            allow_multiple=True,
            description="Select the component requirements that were derived from this system requirement",
        ),
        DomainTracerRelation(
            relation_name="Derived from Use Scenario",
            target_knowledge_topic=TOPIC_USE_SCENARIOS,
            allow_multiple=True,
            description="Select the use scenario that led to this requirement.",
        ),
        DomainTracerRelation(
            relation_name="Derived from User Requirement",
            target_knowledge_topic=TOPIC_USER,
            allow_multiple=True,
            description="Select the user requirement that led to this system requirement.",
        ),
        DomainTracerRelation(
            relation_name="Verified By",
            target_knowledge_topic=TOPIC_VERIFICATION,
            allow_multiple=True,
            description="Select verification activities linked to this requirement",
        ),
    ),
    TOPIC_COMPONENT: (
        DomainTracerRelation(
            relation_name="Derived from",
            target_knowledge_topic=TOPIC_SYSTEM,
            allow_multiple=True,
            description="Select the system requirements that led to this component requirement",
        ),
        DomainTracerRelation(
            relation_name="Results in",
            target_knowledge_topic=TOPIC_UNIT,
            allow_multiple=True,
            description="Select the unit requirements that were derived from this component requirement",
        ),
        DomainTracerRelation(
            relation_name="Related to",
            target_knowledge_topic=TOPIC_RCM,
            allow_multiple=False,
            description="Select the risk control measure that led to this requirement",
        ),
        DomainTracerRelation(
            relation_name="Verified By",
            target_knowledge_topic=TOPIC_VERIFICATION,
            allow_multiple=True,
            description="Select the verification activities that verified this component requirement",
        ),
    ),
    TOPIC_UNIT: (
        DomainTracerRelation(
            relation_name="Derived from Component Requirements",
            target_knowledge_topic=TOPIC_COMPONENT,
            allow_multiple=True,
            description="Select the component requirements that led to this unit requirement",
        ),
        DomainTracerRelation(
            relation_name="Derived from RCM",
            target_knowledge_topic=TOPIC_RCM,
            allow_multiple=False,
            description="Select the risk control measure that led to this requirement",
        ),
        DomainTracerRelation(
            relation_name="Verified By",
            target_knowledge_topic=TOPIC_VERIFICATION,
            allow_multiple=True,
            description="Select the verification activities that verified this component requirement",
        ),
    ),
    TOPIC_DESIGN_OUTPUT: (
        DomainTracerRelation(
            relation_name="Relates to SR",
            target_knowledge_topic=TOPIC_SYSTEM,
            allow_multiple=False,
            description="Select the system requirements that are related to this design output",
        ),
        DomainTracerRelation(
            relation_name="Relates to CR",
            target_knowledge_topic=TOPIC_COMPONENT,
            allow_multiple=False,
            description="Select the component requirements that are related to this design output",
        ),
        DomainTracerRelation(
            # Trailing space in the relation name is intentional (verbatim from source).
            relation_name="Relates to UR ",
            target_knowledge_topic=TOPIC_UNIT,
            allow_multiple=False,
            description="Select the unit requirements that are related to this design output",
        ),
        DomainTracerRelation(
            relation_name="Verified By",
            target_knowledge_topic=TOPIC_VERIFICATION,
            allow_multiple=True,
            description="Select verification activities ensuring compliance",
        ),
        DomainTracerRelation(
            relation_name="Validated By",
            target_knowledge_topic=TOPIC_VALIDATION,
            allow_multiple=True,
            description="Select validation activities ensuring compliance",
        ),
    ),
    TOPIC_VERIFICATION: (
        DomainTracerRelation(
            relation_name="Verifies SR",
            target_knowledge_topic=TOPIC_SYSTEM,
            allow_multiple=False,
            description="Select the system requirements verified by this activity",
        ),
        DomainTracerRelation(
            relation_name="Verifies CR",
            target_knowledge_topic=TOPIC_COMPONENT,
            allow_multiple=False,
            description="Select the component requirements verified by this activity",
        ),
        DomainTracerRelation(
            relation_name="Verifies UR",
            target_knowledge_topic=TOPIC_UNIT,
            allow_multiple=False,
            description="Select the unit requirements verified by this activity",
        ),
        DomainTracerRelation(
            relation_name="Verifies DO",
            target_knowledge_topic=TOPIC_DESIGN_OUTPUT,
            allow_multiple=True,
            description="Select design outputs verified by this activity",
        ),
    ),
    TOPIC_RCM: (
        DomainTracerRelation(
            relation_name="Implemented By",
            target_knowledge_topic=TOPIC_SYSTEM,
            allow_multiple=True,
            description="Select requirements that implement this control measure",
        ),
        DomainTracerRelation(
            relation_name="Verified By",
            target_knowledge_topic=TOPIC_VERIFICATION,
            allow_multiple=True,
            description="Select verification activities ensuring control measure effectiveness",
        ),
        DomainTracerRelation(
            relation_name="Validated By",
            target_knowledge_topic=TOPIC_VALIDATION,
            allow_multiple=True,
            description="Select validation activities confirming control measure suitability",
        ),
    ),
    TOPIC_VALIDATION: (
        DomainTracerRelation(
            relation_name="Validates",
            target_knowledge_topic=TOPIC_USER,
            allow_multiple=False,
            description="Select the user requirement validated by this activity",
        ),
        DomainTracerRelation(
            relation_name="Validates DO",
            target_knowledge_topic=TOPIC_DESIGN_OUTPUT,
            allow_multiple=True,
            description="Select design outputs validated by this activity",
        ),
    ),
    TOPIC_USE_SCENARIOS: (
        DomainTracerRelation(
            relation_name="Related User Requirement",
            target_knowledge_topic=TOPIC_USER,
            allow_multiple=True,
            description="Select the user requirements related to this use scenario.",
        ),
        DomainTracerRelation(
            relation_name="Related System Requirement",
            target_knowledge_topic=TOPIC_SYSTEM,
            allow_multiple=True,
            description="Select the system requirements related to this use scenario.",
        ),
    ),
}


def relation_for(source_topic: str, target_topic: str) -> str | None:
    """Return CertHub relation_name for source→target topic, or None if undefined."""
    if not source_topic or not target_topic:
        raise ValueError("Missing required field: 'source_topic'/'target_topic'")
    for item in _RELATIONS_BY_TOPIC.get(source_topic, ()):
        if item.target_knowledge_topic == target_topic:
            return item.relation_name
    return None
