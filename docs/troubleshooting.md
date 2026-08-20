# Troubleshooting

## `Missing required field: 'CERTHUB_API_KEY'`

Create `.env` from the example and set the key:

```bash
cp .env.example .env
```

`make sync` loads `.env` from the **repository root**. There is no mock fallback.

## `make sync` returns 401 / 403

The key is invalid, expired, or lacks Records / Tech Doc / Tracer access for
the tenant in `certhub.toml`. Confirm the same key works in the CertHub UI.

## `make sync` returns 404 or empty catalogs

A KT revision id in `certhub.toml` is wrong, or you mixed **revision** ids with
**history** ids. See [onboarding](onboarding.md).

## Fork / PR CI skipped “Cadence evidence”

[`cadence-evidence.yml`](../.github/workflows/cadence-evidence.yml) needs the
`CERTHUB_API_KEY` repository secret. Forks do not get that secret, so the
evidence job is **skipped** (not failed) on PRs from forks.

[`cadence-unit-tests.yml`](../.github/workflows/cadence-unit-tests.yml) must still
pass — it never calls CertHub.

## PlantUML / graphs missing in the HTML pack

Install PlantUML on PATH (`brew install plantuml` or `apt install plantuml`) or
run `make ensure-plantuml` (downloads a local jar). CI installs PlantUML + Graphviz.

The gate still runs without graphs; only needflow diagrams are missing.

## `codelinks: command not found`

[`scripts/run_codelinks.py`](../scripts/run_codelinks.py) prefers the official
`codelinks analyse` CLI, then falls back to grepping `@need-ids:` markers.
The fallback is enough for the certification gate. Install the CodeLinks CLI
only if you want the full analyse JSON.

## ubCode: “Could not find license key”

ubCode is a commercial VS Code extension (not Cursor). Put the license in
`~/Library/Application Support/ubcode/ubcode.toml` (macOS) or set
`UBCODE_LICENSE_KEY` / `UBCODE_LICENSE_USER`. Confirm with useblocks that the
key is bound to your email. See the ubCode section in the README.

## Gate VERIFIED but the implementation column looks wrong

Each SYSREQ should cite the **matching** source file (temperature →
`cycle/controller.py`, UI → `ui/messages.py`, footprint → `enclosure/footprint.py`).
If every row shows the same function, re-run `make show` on a tree that includes
the current `verify.py` picker. See [traceability map](traceability-map.md).

## `make break` left the tree dirty

`make fix` restores `reported_cycle_duration_minutes()`. Do not commit the broken
line.

## Generated OpenAPI clients look huge

That is expected. Hand-written code lives under
`certhub/certhub_connector/{cli,config,api,sync,evidence}/` excluding
`api/clients/`. `make generate-api` is **DEV ONLY** — not needed for Quickstart.
Regenerating from live OpenAPI can rename Tracer (or other) client symbols and
break imports in `api/client.py` until that wrapper is updated. Do not edit
generated client files by hand.
