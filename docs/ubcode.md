# Optional: ubCode and ubTrace

Cadence already works without commercial useblocks products: `make sync` /
`make show` use open-source Sphinx-Needs, CodeLinks, and Test-Reports only.
Install the products below when you want live IDE feedback or a browser
dashboard on the **same** RST / `ubproject.toml` / CodeLinks files.

## ubCode — VS Code IDE

[ubCode](https://ubcode.useblocks.com/) (`useblocks.ubcode`) gives real-time
Needs Index, graph, diagnostics, and MCP. The Marketplace listing is **VS Code
only** (not Cursor). Free for public OSS repos; a license is required for
private use.

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
   [`sphinx/source/ubproject.toml`](../sphinx/source/ubproject.toml) (`needs_from_toml` in `conf.py`).

4. The V-model catalog RST already ships under `sphinx/source/generated/`.
   To refresh from CertHub (needs an [API key](https://docs.certhub.de/api/getting-started)) and then refresh ubCode:

   ```bash
   make sync
   ```

   Command Palette → **ubCode: Restart language server** (or refresh Needs Index).
   After a Sphinx HTML build (`make show` / script `needs:json`), Needs JSON loads
   `sphinx/build/html/needs.json` (`needs_build_json = True` in `conf.py`).

### Config notes

- Catalog Need RST (requirements, design outputs, verifications, validations) is
  committed under `sphinx/source/generated/` so a public clone can browse without
  CertHub. `make sync` overwrites those files from the SoR. Per-build fragments
  (`codelinks_needextend.rst`, `certification_summary.rst`) stay gitignored.
  ubCode indexes the tree with `[source] respect_gitignore = false` +
  `extend_include = ["generated/**/*.rst"]`. Sphinx still excludes that folder from
  standalone pages (`exclude_patterns`); hand-written pages `.. include:: generated/…`.
- `[needs_json]` — Sphinx-built `sphinx/build/html/needs.json` (`needs_build_json = True`).
  Until the first HTML build, Needs JSON shows “file does not exist”.
- `[parse.extend_directives.test-report]` — Sphinx-Test-Reports directive for ubCode.
- `[reports] directory = "ubcode_reports"` — Jinja templates (starter: `needs_overview.html.j2`).
- Scripts (`ubCode: Run Script in Terminal`): `sync`, `show`, `needs:json`.

Redirect stub `src/sterilisator_20a/ubproject.redirect.toml` points CodeLinks source
markers at `sphinx/source/`.

### What you get in the IDE

| View | Purpose |
|------|---------|
| **Needs Index** | Live browse/filter/group of SYSREQ/DOUT/VERIF; click-through to RST |
| **Needs Graph** | Interactive SYSREQ↔DOUT↔VERIF link graph |
| **Needs JSON** | Tree of Sphinx-built `needs.json` (includes Test-Reports after HTML build) |
| **Diagnostics** | RST / needs lint as you type |
| **Reports** | Render `ubcode_reports/*.html.j2` → preview or Open in Browser |

Also useful: RST preview, go-to-definition on need IDs, Diff & impact, MCP
(license-dependent). Docs: <https://ubcode.useblocks.com/>.

Re-export Needs TOML after changing types/fields in `conf.py` (rare — prefer editing
`ubproject.toml` directly):

```bash
cd sphinx/source && uv run export_needs_toml.py
```

If activation fails with “Could not find license key”, confirm with useblocks that the key is provisioned for **ubCode** and bound to your email.

## ubTrace — web dashboard (not in this example)

[ubTrace](https://ubtrace.useblocks.com/latest/) is useblocks’ paid browser
layer for large-team Sphinx-Needs analysis (coverage, search, RBAC). It uses
the same Sphinx-Needs data model. This repository ships Sphinx HTML via
`make show` / `make evidence` and does **not** run an ubTrace server — treat
ubTrace as a later plug-in when your team outgrows static HTML.
