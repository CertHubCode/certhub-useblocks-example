## Summary

<!-- What changed and why. -->

## Test plan

- [ ] `make test` (connector + SaMD tests, no API key)
- [ ] If the SYSREQ → DOUT → code → VERIF chain changed: `make sync && make show` and check [docs/traceability-map.md](../docs/traceability-map.md) (source markers stay `DOUT_*` / tests stay `VERIF_*`)
