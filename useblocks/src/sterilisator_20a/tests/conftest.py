"""Pytest hooks: emit CertHub VERIF IDs into JUnit XML properties."""

from __future__ import annotations

import pytest


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers",
        "certhub_test(test_id): associate this test with a CertHub VERIF_* ID",
    )


@pytest.fixture(autouse=True)
def _certhub_junit_properties(request: pytest.FixtureRequest, record_property) -> None:
    marker = request.node.get_closest_marker("certhub_test")
    if marker is None:
        return
    if not marker.args:
        raise ValueError("certhub_test marker requires a VERIF id argument")
    test_id = marker.args[0]
    if not test_id:
        raise ValueError("Missing required field: certhub_test id")
    record_property("certhub_test", test_id)
    record_property("verifies", test_id)
