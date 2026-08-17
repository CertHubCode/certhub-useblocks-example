# CertHub SoR cleanup (showcase tenant)

Repo-side filters cannot fix wrong Tracer links. Someone with CertHub edit
access on the Sterilisator 20A product should do the following so the synced
catalog matches the code.

## Design outputs

1. **Unlink** SYSREQ_002 / SYSREQ_003 / SYSREQ_004 from legacy catalog devices
   `DOUT_015` (EcoSteam), `DOUT_016` (MedSteril), `DOUT_017` (HydroSter).
2. **Link** product design output `DOUT_018` (Sterilizer 20A) to SYSREQ_001–004.
3. Keep procedure DOUTs (`DOUT_001`–`DOUT_004`) as procedures, not as the SaMD
   implementation. Sphinx already limits the needflow to
   `DOUT_001`–`004` + `DOUT_018`.
4. Hide or archive leftover catalog rows (`DOUT_005`–`014`, `DOUT_019`) that
   are not Sterilisator 20A.

## Unit / user requirements

Scrub infusion-pump (or other product) text from `UNITREQ_*` and `UREQ_*` on
this knowledge unit. Cadence syncs whatever CertHub returns.

## Validation

`VALID_*` stay **manual evidence in CertHub**. They sync into the Sphinx pack
and the dashboard KPI is non-blocking (`manual`). Do not add pytest for VALID
unless the protocol is actually automatable.

## After editing CertHub

```bash
make sync
make show
```

Confirm [docs/traceability-map.md](traceability-map.md) still matches the gate
report (each SYSREQ cites the matching source file).
