## Summary

<!-- What changed and why. -->

## Test plan

- [ ] `make test` (connector + SaMD tests, no API key)
- [ ] `make show` works offline (committed snapshot); if CertHub content changed: `make sync` and commit catalogs + `normalized_export.json`
- [ ] If the SYSREQ → DOUT → code → VERIF chain changed: `make show` and check [docs/traceability-map.md](../docs/traceability-map.md) (source markers stay `DOUT_*` / tests stay `VERIF_*`)
