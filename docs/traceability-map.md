# Traceability map — Sterilisator 20A

Static map so a visitor can answer *which requirement maps to which file and
test* without running Sphinx. After `make show`, the same chain appears on
`sphinx/build/html/traceability.html` and in the certification summary.

## Engineering gate (SYSREQ → code → VERIF)

The gate in [`certhub/certhub_connector/evidence/verify.py`](../certhub/certhub_connector/evidence/verify.py)
closes **System Requirements** only.

| Requirement | Intent | Design output | Implementation | Verification | Test |
|-------------|--------|---------------|----------------|--------------|------|
| SYSREQ_001 | Chamber 121°C ± 2°C | DOUT_018 | `src/sterilisator_20a/cycle/controller.py` — `temperature_within_range` | VERIF_001 | `test_sterilization_temperature_accuracy` |
| SYSREQ_002 | Cycle ≤ 60 minutes | DOUT_018 | `src/sterilisator_20a/cycle/controller.py` — `reported_cycle_duration_minutes` / `cycle_within_time_budget` | VERIF_002 | `test_sterilization_cycle_time` |
| SYSREQ_003 | English UI labels | DOUT_018 | `src/sterilisator_20a/ui/messages.py` | VERIF_003 | `test_user_interface_labeling` |
| SYSREQ_004 | Enclosure ≤ 50×40×35 cm | DOUT_018 | `src/sterilisator_20a/enclosure/footprint.py` | VERIF_004 | `test_device_footprint` |

Markers:

- Source: `# @need-ids: DOUT_018` on the functions above
- Tests: `# @need-ids: VERIF_00N` plus `@pytest.mark.certhub_test("VERIF_00N")`

`make break` mutates `reported_cycle_duration_minutes()` so VERIF_002 / SYSREQ_002
go RED. `make fix` restores GREEN.

## What is not in the gate

| Layer | In Sphinx pack? | Closes gate? |
|-------|-----------------|--------------|
| UREQ / CREQ / UNITREQ | Synced from CertHub | No |
| DOUT_001–004 (procedures) | Filtered into the sterilizer graph | No CodeLinks on product source |
| VALID_001–004 | Synced; dashboard KPI is **manual / N/A** | No — validation stays in CertHub |

## Showcase limitations

- One product design output (`DOUT_018`) covers all four SYSREQs. Feature-level
  DOUTs can be added in CertHub later; then split the `@need-ids:` markers.
- CodeLinks `needextend` lists **all** marker URLs per need; the certification
  report cites the **domain-matching** implementation, not always the first hit.

## Regression

[`tests/test_verify_traceability.py`](../tests/test_verify_traceability.py) asserts
each SYSREQ report contains the expected source file / function.
