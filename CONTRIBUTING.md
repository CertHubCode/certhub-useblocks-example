# Contributing

This repository is CertHub’s public Cadence example. Changes should keep the
Sterilisator 20A loop understandable to someone cloning it cold.

## Development

```bash
make install
cp .env.example .env   # CERTHUB_API_KEY for sync only
make test              # connector + SaMD tests (no CertHub required)
make sync && make show # full loop
```

Python 3.12+ and [uv](https://docs.astral.sh/uv/) are required.

## What belongs where

- Product behaviour: `src/sterilisator_20a/` + `src/sterilisator_20a/tests/`
- Connector / gate / evidence: `certhub/certhub_connector/` + `tests/`
- Generated HTTP clients: `make generate-api` is **DEV ONLY** — fetches OpenAPI,
  filters to `x-public` operations, regenerates `api/clients/` and
  `api/api_models/` (can break `api/client.py` imports after OpenAPI renames).
  Do not hand-edit generated trees.
- Tenant IDs: `certhub.toml` (showcase) or `certhub.toml.example` (placeholders)

## Pull requests

- Keep diffs focused. Do not commit `.env`, `evidence/`, `sphinx/build/`,
  `certhub/generated/`, or per-build Sphinx fragments
  (`codelinks_needextend.rst`, `certification_summary.rst`).
- When showcase CertHub content changes, run `make sync` and **do** commit the
  seven catalog RST files under `sphinx/source/generated/` (requirements,
  design outputs, verifications, validations) so public clones stay browsable.
- Offline tests must pass without an API key: `make test`.
- If you change the SYSREQ → code → VERIF chain, update
  [`docs/traceability-map.md`](docs/traceability-map.md) and
  `tests/test_verify_traceability.py`.

## GitHub topics

Suggested repository topics: `certhub`, `samd`, `sphinx-needs`, `useblocks`, `traceability`, `medical-device`.

Use the GitHub templates. Include the command you ran, whether you used the
showcase tenant or your own `certhub.toml`, and a redacted snippet of the error
(never paste API keys).
