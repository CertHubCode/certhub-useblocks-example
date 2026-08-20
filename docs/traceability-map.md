# Traceability map — Sterilisator 20A

Static map so a visitor can answer *which requirement maps to which file and
test* without running Sphinx. After `make show`, the same chain appears on
`sphinx/build/html/traceability.html` and in the certification summary.

This page is also the Cadence statement of **what to mark in code and why**.
The product-level argument (design-control matrix vs last hop into source)
lives in CertHub’s
[V-model guide](https://docs.certhub.de/1.5%20Implementation%20Guides/v-model-software-outside-certhub).

## Two jobs

**Job 1 — the matrix (CertHub, synced here).**
[ISO 13485:2016](https://www.iso.org/standard/59752.html) **7.3.2(e)** requires
documented methods to ensure traceability of design **outputs** to design
**inputs**. That method is a bidirectional table of records (user needs,
inputs, outputs, verification, validation), not a comment in a `.py` file.
[IEC 62304:2006+A1:2015](https://www.iso.org/standard/64686.html) **5.1.1(c)**
says the software plan shall address TRACEABILITY among system requirements,
software requirements, system tests, and risk-control measures. Cadence
syncs the seven V-model knowledge topics plus Tracer edges so that matrix is
visible in Sphinx. Risk-control measures stay in CertHub (ISO 14971); this
pack does not export them.

**Job 2 — this git baseline (markers in `src/`).**
FDA
[General Principles of Software Validation](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-principles-software-validation)
(2002) §5.2.4 asks for a **source code traceability analysis**: modules and
functions trace to an element of the **software design specification**, and
tests trace to that same specification. That specification is a design
output (`DOUT_*`), not a system requirement (`SYSREQ_*`).

Verification then confirms that the **output meets the input**
(ISO 13485 **7.3.6** / [21 CFR 820.30(f)](https://www.law.cornell.edu/cfr/text/21/820.30)).
If you stamp `SYSREQ` on functions, you skip the layer verification is defined
against.

```text
CertHub Tracer                          This repository
SYSREQ ←→ DOUT  ─────────────────────►  # @need-ids: DOUT_018   (source)
SYSREQ ←→ VERIF ─────────────────────►  # @need-ids: VERIF_00N  (tests)
                                        @pytest.mark.certhub_test(...)
UREQ   ←→ VALID                         synced; not pytest
```

Rule of thumb: **sync the V-model; in code, tag only what software actually
implements or verifies. Unlinked rows are fine. Wrong-product rows are a
system-of-record problem, not a reason to sync less.**

## What to mark in code

| Where | Marker | Why |
|-------|--------|-----|
| Product source | `# @need-ids: DOUT_*` only | GPSV §5.2.4: code → design specification |
| SaMD tests | `# @need-ids: VERIF_*` **and** `@pytest.mark.certhub_test("VERIF_*")` | Sphinx link + JUnit property the gate reads |
| `SYSREQ` / `UREQ` / `CREQ` / `UNITREQ` / `VALID` | **Do not** put these on functions | They belong in the matrix (Job 1). Tracer already connects them to the DOUT/VERIF you tagged. |

The pytest marker is the contractual link for the certification gate. The
`# @need-ids:` comment on tests is for the Sphinx / CodeLinks pack. Keep both.

Rows with no marker still belong in the pack. Procedure design outputs
(`DOUT_001`–`004` here) are not software; leaving them unmarked is correct.
An input with no output is a dropped requirement — hiding it by syncing fewer
topics would hide the 7.3.2(e) finding.

Validation stays out of pytest because [21 CFR 820.30(g)](https://www.law.cornell.edu/cfr/text/21/820.30)
/ ISO 13485 **7.3.7** ask whether the device meets **user needs and intended
use**, not whether a unit test passed.

## Engineering gate (SYSREQ → code → VERIF)

The gate in [`certhub/certhub_connector/evidence/verify.py`](../certhub/certhub_connector/evidence/verify.py)
closes **System Requirements** only. It walks Tracer links to a design output
and a verification, then CodeLinks + JUnit for this baseline. UREQ / CREQ /
UNITREQ / VALID are in the catalog and do not close the gate.

| Requirement | Intent | Design output | Implementation | Verification | Test |
|-------------|--------|---------------|----------------|--------------|------|
| SYSREQ_001 | Chamber 121°C ± 2°C | DOUT_018 | `src/sterilisator_20a/cycle/controller.py` — `temperature_within_range` | VERIF_001 | `test_sterilization_temperature_accuracy` |
| SYSREQ_002 | Cycle ≤ 60 minutes | DOUT_018 | `src/sterilisator_20a/cycle/controller.py` — `reported_cycle_duration_minutes` / `cycle_within_time_budget` | VERIF_002 | `test_sterilization_cycle_time` |
| SYSREQ_003 | English UI labels | DOUT_018 | `src/sterilisator_20a/ui/messages.py` | VERIF_003 | `test_user_interface_labeling` |
| SYSREQ_004 | Enclosure ≤ 50×40×35 cm | DOUT_018 | `src/sterilisator_20a/enclosure/footprint.py` | VERIF_004 | `test_device_footprint` |

`make break` mutates `reported_cycle_duration_minutes()` so VERIF_002 / SYSREQ_002
go RED. `make fix` restores GREEN.

## What is not in the gate

| Layer | In Sphinx pack? | Closes gate? |
|-------|-----------------|--------------|
| UREQ / CREQ / UNITREQ | Synced from CertHub (Job 1 catalog) | No |
| DOUT_001–004 (procedures) | In the catalog; needflow keeps the sterilizer chain readable | No CodeLinks on product source — on purpose |
| VALID_001–004 | Synced; dashboard KPI is **manual / N/A** | No — intended-use evidence stays in CertHub |

## Showcase limitations

- One product design output (`DOUT_018`) covers all four SYSREQs. A real
  product would split feature-level DOUTs in CertHub, then split the
  `@need-ids:` markers. Do not retag procedure DOUTs (`DOUT_001`–`004`) as
  software.
- CodeLinks `needextend` lists **all** marker URLs per need; the certification
  report cites the **domain-matching** implementation, not always the first hit.
- Source comments are one method for GPSV’s last hop. The standards require
  the traces, not this marker syntax.

## Regression

[`tests/test_verify_traceability.py`](../tests/test_verify_traceability.py) asserts
each SYSREQ report contains the expected source file / function.
