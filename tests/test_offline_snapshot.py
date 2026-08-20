"""Committed showcase snapshot must power make show without an API key."""

from __future__ import annotations

from certhub_connector.config.paths import normalized_snapshot_path
from certhub_connector.evidence.verify import (
    CertificationStatus,
    load_normalized_export,
    verify_certification,
)
from certhub_connector.sync.models import CertHubExport


def test_committed_normalized_export_exists() -> None:
    snapshot = normalized_snapshot_path()
    assert snapshot.is_file(), (
        f"Missing {snapshot}. Run make sync and commit normalized_export.json "
        "so clones can make show without CERTHUB_API_KEY."
    )


def test_committed_snapshot_loads_without_api_key(monkeypatch) -> None:
    monkeypatch.delenv("CERTHUB_API_KEY", raising=False)
    # load_normalized_export must not call CerthubConfig.load().
    export = load_normalized_export()
    assert isinstance(export, CertHubExport)
    assert len(export.system_requirements) == 4
    assert len(export.verifications) == 4
    assert any(d.id == "DOUT_018" for d in export.design_outputs)


def test_verify_runs_from_committed_snapshot_without_api_key(
    tmp_path, monkeypatch
) -> None:
    """Gate uses the snapshot + empty CodeLinks/JUnit; no CertHub config."""
    monkeypatch.delenv("CERTHUB_API_KEY", raising=False)

    junit = tmp_path / "junit.xml"
    junit.write_text(
        """<?xml version="1.0"?>
<testsuite>
  <testcase classname="t" name="a"><properties>
    <property name="certhub_test" value="VERIF_001"/>
  </properties></testcase>
  <testcase classname="t" name="b"><properties>
    <property name="certhub_test" value="VERIF_002"/>
  </properties></testcase>
  <testcase classname="t" name="c"><properties>
    <property name="certhub_test" value="VERIF_003"/>
  </properties></testcase>
  <testcase classname="t" name="d"><properties>
    <property name="certhub_test" value="VERIF_004"/>
  </properties></testcase>
</testsuite>
""",
        encoding="utf-8",
    )
    analysis = tmp_path / "codelinks.json"
    analysis.write_text(
        """[
  {"filepath": "src/sterilisator_20a/cycle/controller.py",
   "need_ids": ["DOUT_018"],
   "tagged_scope": "def temperature_within_range"},
  {"filepath": "src/sterilisator_20a/cycle/controller.py",
   "need_ids": ["DOUT_018"],
   "tagged_scope": "def reported_cycle_duration_minutes"},
  {"filepath": "src/sterilisator_20a/safety/door.py",
   "need_ids": ["DOUT_018"],
   "tagged_scope": "def door_must_lock"},
  {"filepath": "src/sterilisator_20a/ui/messages.py",
   "need_ids": ["DOUT_018"],
   "tagged_scope": "def ui_messages"},
  {"filepath": "src/sterilisator_20a/tests/test_sterilisator.py",
   "need_ids": ["VERIF_001"], "tagged_scope": "def test_temp"},
  {"filepath": "src/sterilisator_20a/tests/test_sterilisator.py",
   "need_ids": ["VERIF_002"], "tagged_scope": "def test_time"},
  {"filepath": "src/sterilisator_20a/tests/test_sterilisator.py",
   "need_ids": ["VERIF_003"], "tagged_scope": "def test_door"},
  {"filepath": "src/sterilisator_20a/tests/test_sterilisator.py",
   "need_ids": ["VERIF_004"], "tagged_scope": "def test_ui"}
]
""",
        encoding="utf-8",
    )

    report = verify_certification(codelinks_path=analysis, junit=junit)
    assert report.certification_status == CertificationStatus.VERIFIED
    assert report.ok
    assert len(report.requirements) == 4
