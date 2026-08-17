# Cadence — CertHub SaMD Engineering Loop

Cadence is CertHub’s official SaMD Engineering Loop showcase: controlled
requirements stay in CertHub; this repo syncs them into Sphinx-Needs; then
useblocks (Needs / CodeLinks / Test-Reports) builds an evidence pack from
real Git work on the **Sterilisator 20A** example SaMD (prod SoR: System
Requirements).

## Boundary

| Layer | Where | When |
|-------|--------|------|
| Engineering proof | `evidence/` + GitHub Actions artifacts | Every PR / main / RC run |
| Regulatory record | CertHub **Release Record** KT (`release_record_kt_id`) | Full release tag `vX.Y.Z` only |

`make show` / `make evidence` never write to CertHub. Only `push-evidence --push`
(or the release workflow) POSTs one Release Record row.

## Walkthrough

Step-by-step runbook (GREEN → RED → evidence → release → CertHub UI / change requirement):
[`docs/walkthrough.md`](docs/walkthrough.md). After release, follow the printed Release Record URL;
`make open-requirements` opens the System Requirements SoR for a live edit → re-sync.

## Regulatory scope (EU / US)

Cadence is the **engineering evidence twin** (SYSREQ → DOUT → code → VERIF → gate → Release Record), not a full DHR or EU Technical Documentation pack. Risk, GSPR, CER, PMS, and approvals stay in CertHub.

Checklist of what this repo delivers today vs additional CertHub/QMS steps:
[`docs/regulatory-gap-analysis.md`](docs/regulatory-gap-analysis.md).

## Commands

```bash
cp .env.example .env   # set CERTHUB_API_KEY; edit certhub.toml for tenant URLs/KTs
# Switch prod/dev by commenting ONE flat block in certhub.toml (+ matching API key)
# CI: store the same key as GitHub Actions secret CERTHUB_API_KEY

make sync                 # CertHub → Sphinx-Needs
make show                 # tests + CodeLinks + verify + open dashboard
make evidence             # same gate, writes evidence/ (CI-friendly)

make tag-rc VERSION=1.0.0 RC=1       # annotated RC tag → CI evidence artifact only
make tag-release VERSION=1.0.0       # full tag → evidence artifact + CertHub Release Record

make push-evidence BASELINE=1.0.0          # dry-run RecordCreate JSON
CERTHUB_PUSH=1 make push-evidence BASELINE=1.0.0   # live POST

make confirm BASELINE=0.0.99               # POST → GET proof (needs API key)
# CONFIRM_CLEANUP=1 make confirm BASELINE=0.0.99   # delete after assert

make open-requirements            # open System Requirements KT in CertHub
make open-release-record          # open Release Record KT in CertHub

make break && make show   # RED — VERIF_002 (cycle time) fails, gate BLOCKED
make fix && make show     # back to GREEN

make generate-api         # fetch OpenAPI + regenerate clients; TechDoc/Records Pydantic models
```

`make sync` requires `CERTHUB_API_KEY` and pulls Tech Doc + Records + Tracer use-case links into Sphinx-Needs.

## ubCode (commercial editor trial)

Real-time Sphinx-Needs editing via the **ubCode** extension (`useblocks.ubcode`).
The Marketplace listing is **VS Code only** (not Cursor).

### Setup

1. In **VS Code**, install the extension (repo root recommends it via `.vscode/extensions.json`).
2. Put your license in **macOS** `~/Library/Application Support/ubcode/ubcode.toml` (never commit):

   ```toml
   [license]
   key = "<from useblocks>"
   user = "<your-email>"
   ```

   Or set `UBCODE_LICENSE_KEY` / `UBCODE_LICENSE_USER`. Then **Command Palette → ubCode: Restart language server**.

3. Open this repository in VS Code. Cadence is pinned with
   `ubcode.views.pinnedProject` → `sphinx/source/ubproject.toml`
   (see `.vscode/settings.json`). Needs config is shared with Sphinx via
   [`sphinx/source/ubproject.toml`](sphinx/source/ubproject.toml) (`needs_from_toml` in `conf.py`).

4. Ensure generated needs exist, then refresh ubCode:

   ```bash
   make sync
   ```

   Command Palette → **ubCode: Restart language server** (or refresh Needs Index).
   After a Sphinx HTML build (`make show` / script `needs:json`), Needs JSON loads
   `sphinx/build/html/needs.json` (`needs_build_json = True` in `conf.py`).

### Config notes

- Need RST is written under `sphinx/source/generated/` (same tree as `ubproject.toml`),
  so ubCode indexes it with `[source] respect_gitignore = false` +
  `extend_include = ["generated/**/*.rst"]`. Sphinx still excludes that folder from
  standalone pages (`exclude_patterns`); hand-written pages `.. include:: generated/…`.
- `[needs_json]` — Sphinx-built `sphinx/build/html/needs.json` (`needs_build_json = True`).
  Until the first HTML build, Needs JSON shows “file does not exist”.
- `[parse.extend_directives.test-report]` — Sphinx-Test-Reports directive for ubCode.
- `[reports] directory = "ubcode_reports"` — Jinja templates (starter: `needs_overview.html.j2`).
- Scripts (`ubCode: Run Script in Terminal`): `sync`, `show`, `needs:json`.

Redirect stub `src/sterilisator_20a/ubproject.redirect.toml` points CodeLinks source
markers at `sphinx/source/`.

### Sidebar map (what you can do)

| View | Purpose |
|------|---------|
| **Needs Index** | Live browse/filter/group of SYSREQ/DOUT/VERIF (and links); click-through to RST |
| **Needs Graph** | Interactive SYSREQ↔DOUT↔VERIF link graph |
| **Needs JSON** | Tree of Sphinx-built `needs.json` (includes Test-Reports needs after HTML build) |
| **Diagnostics** | RST / needs lint as you type |
| **Std referencing / Site Map** | toctree docs and cross-refs |
| **Reports** | Render `ubcode_reports/*.html.j2` → preview or Open in Browser |
| **Home** | License, restart LS, docs links |

Also useful: RST preview, go-to-definition on need IDs, Diff & impact, MCP / `@pharaoh`
(license-dependent). Docs: <https://ubcode.useblocks.com/>.

Re-export Needs TOML after changing types/fields in `conf.py` (rare — prefer editing
`ubproject.toml` directly):

```bash
cd sphinx/source && uv run export_needs_toml.py
```

If activation fails with “Could not find license key”, confirm with useblocks that the key is provisioned for **ubCode** and bound to your email.

## Layout

| Path | What |
|------|------|
| `certhub/` | Connector, sync snapshots, outbound JSON |
| `certhub/certhub_connector/{cli,config,api,sync,evidence}/` | Hand-written Cadence connector (CLI, config, API wrappers, sync/transform, evidence) |
| `certhub/certhub_connector/api/clients/` | Generated OpenAPI HTTP clients (Tech Doc + Records + Tracer) |
| `certhub/certhub_connector/api/api_models/` | Generated Pydantic models from OpenAPI |
| `evidence/` | CI evidence pack (gitignored): result, junit, `docs/` (Sphinx HTML), MANIFEST |
| `schemas/` | Fetched OpenAPI specs |
| `sphinx/source/` | Hand-written Sphinx assurance pages (dashboard, catalogs, traceability, release evidence) |
| `sphinx/source/ubproject.toml` | Shared Sphinx-Needs + ubCode config (`needs_from_toml`) |
| `sphinx/source/generated/` | Needs RST written by sync / CodeLinks / report (gitignored; included by pages) |
| `sphinx/source/ubcode_reports/` | ubCode Jinja report templates (`.html.j2`) |
| `sphinx/build/` | HTML output (open `dashboard.html`) |
| `sphinx/utils/` | Optional `plantuml.jar` download target (`make ensure-plantuml`) |
| `src/sterilisator_20a/` | The SaMD under test (product code) |
| `src/sterilisator_20a/tests/` | SaMD VERIF suite (VERIF_001–004) |
| `tests/` | Cadence tooling tests (connector, evidence, release) — not SaMD |

## Sphinx evidence pack

| Page | Role |
|------|------|
| `dashboard.html` | Management one-pager: gate status, KPIs, charts, V-model needflow |
| `requirements.html` | Full requirement text + catalog |
| `design-output.html` | Design outputs + CodeLinks `local-url` / `remote-url` |
| `verification.html` | CertHub tests + JUnit report + execution hierarchy |
| `traceability.html` | Link matrices, filtered needflow graph, CodeLinks columns, gap legend |
| `release-evidence.html` | Outbound Release Record story |

**Prerequisites for graphs:** PlantUML on PATH (`brew install plantuml` / apt `plantuml`), or `make ensure-plantuml` for a local jar. CI installs PlantUML + Graphviz (PlantUML layout dependency).

## CertHub sync (inbound)

- Auth: `X-API-Key` from `CERTHUB_API_KEY` · tenant settings in committed `certhub.toml` via Pydantic `TenantSettings` / `CerthubConfig`
- Switch prod/dev by commenting one flat block in `certhub.toml` (and the matching API key in `.env`); never hardcode URLs/KT ids in connector code
- Seven V-Model content KTs (in `certhub.toml`):
  - `user_requirements_kt_id` → `UREQ_*`
  - `system_requirements_kt_id` → System Requirements SoR → `SYSREQ_*`
  - `component_requirements_kt_id` → `CREQ_*`
  - `unit_requirements_kt_id` → `UNITREQ_*`
  - `design_output_kt_id` → `DOUT_*`
  - `verification_kt_id` → `VERIF_*`
  - `validation_kt_id` → `VALID_*`
- Dashboard URLs use history ids (`*_kt_history_id`, `product_history_id`, `ku_history_id`) — not Records revision KT ids
- Live path: Tech Doc KT metadata + seven Records lists + Tracer `POST /traces/batch/list` → Sphinx-Needs
- Cross-need `links` / `verifies` from Tracer `connected_within_use_case` edges only (no keyword/title joins)
- Responses parsed into Pydantic at the client boundary (Tech Doc + Records); Tracer uses generated attrs client models

## CertHub release evidence (outbound)

- KT: `release_record_kt_id` in `certhub.toml` (prod name: **Release Record**)
- Map form fields via schema `properties["certhub-key"]` → component `key`
- First-class: release-number, release-id (commit), generated-at, evidence-url
- Notes (`details`): short plain-text summary (status, compact totals, req id+status lines, result SHA)
- GitHub workflows (repo root):
  - `cadence-evidence.yml` — PR/main → artifacts only
  - `cadence-release.yml` — `vX.Y.Z` / `v*-rc*` → always evidence artifact; CertHub POST only on full release
