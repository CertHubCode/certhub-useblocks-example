# Contributing

This repository is CertHub’s public Cadence example. Changes should keep the
Sterilisator 20A loop understandable to someone cloning it cold.

## Development

```bash
make install
cp .env.example .env   # CERTHUB_API_KEY for sync only
uv run pytest tests    # no CertHub required
make sync && make show # full loop
```

Python 3.12+ and [uv](https://docs.astral.sh/uv/) are required.

## What belongs where

- Product behaviour: `src/sterilisator_20a/` + `src/sterilisator_20a/tests/`
- Connector / gate / evidence: `certhub/certhub_connector/` + `tests/`
- Generated HTTP clients: `make generate-api` — do not hand-edit `api/clients/`
- Tenant IDs: `certhub.toml` (showcase) or `certhub.toml.example` (placeholders)

## Pull requests

- Keep diffs focused. Do not commit `.env`, `evidence/`, `sphinx/build/`, or
  `sphinx/source/generated/*.rst`.
- Unit tests in `tests/` must pass without an API key.
- If you change the SYSREQ → code → VERIF chain, update
  [`docs/traceability-map.md`](docs/traceability-map.md) and
  `tests/test_verify_traceability.py`.

## GitHub topics

Suggested repository topics: `certhub`, `samd`, `sphinx-needs`, `useblocks`, `traceability`, `medical-device`.

Use the GitHub templates. Include the command you ran, whether you used the
showcase tenant or your own `certhub.toml`, and a redacted snippet of the error
(never paste API keys).
