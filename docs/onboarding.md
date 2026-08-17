# Onboarding — showcase tenant vs your own CertHub

Cadence ships a **working showcase tenant** in committed [`certhub.toml`](../certhub.toml).
That is the fastest first run. Real adopters later replace those IDs with their own
CertHub product.

The API key is the only secret. Tenant URLs and knowledge-topic (KT) ids are
configuration, not credentials.

## Two paths

| Path | When | What you edit |
|------|------|----------------|
| **Showcase tenant** (default) | Clone, demo, CI against CertHub’s example Sterilisator 20A | `.env` only (`CERTHUB_API_KEY`) |
| **Your own tenant** | Adopt Cadence on a real product | Copy [`certhub.toml.example`](../certhub.toml.example) → `certhub.toml` and fill every key |

Ask CertHub for a showcase API key if you do not already have one. The key must
match the environment in `certhub.toml` (prod vs dev).

## Repository setup (GitHub Actions)

Full evidence and release workflows need a repository secret:

1. GitHub → **Settings** → **Secrets and variables** → **Actions**
2. New repository secret named `CERTHUB_API_KEY`
3. Value = the same key you put in `.env`

Without that secret:

- [`cadence-unit-tests.yml`](../.github/workflows/cadence-unit-tests.yml) still runs (no CertHub call)
- [`cadence-evidence.yml`](../.github/workflows/cadence-evidence.yml) and [`cadence-release.yml`](../.github/workflows/cadence-release.yml) cannot `make sync`

Forks do not inherit secrets. Open a PR from a fork and expect unit tests only,
unless a maintainer runs the evidence workflow with the secret.

## Bring-your-own tenant

1. Create (or pick) a product and knowledge unit in CertHub with the seven V-model
   content KTs plus a **Release Record** KT.
2. Copy the example file:

   ```bash
   cp certhub.toml.example certhub.toml
   ```

3. Fill **revision** ids (Records API) and **history** ids (dashboard URLs).

### Where to copy IDs in the CertHub UI

| `certhub.toml` key | Where it lives in CertHub |
|--------------------|---------------------------|
| `*_base_url` | Your Tech Doc / Records / Tracer API hosts (from CertHub or your CSM) |
| `dashboard_base_url` | App host, e.g. `https://app.certhub.de` |
| `product_history_id` | Product URL path: `/dashboard/products/<this>/…` |
| `ku_history_id` | Knowledge unit URL path segment after the product |
| `product_version` | Version selector on the product (`0.1`, `1.0`, …) |
| `*_kt_id` | KT **revision** id used by the Records API (open the KT → API / revision id) |
| `*_kt_history_id` | KT **history** id in the dashboard query string `knowledgeTopicId=` |

Records and dashboard ids are **not** interchangeable. Mixing them produces 404s
or empty syncs.

4. Put a matching API key in `.env`.
5. `make sync && make show`.

If sync succeeds but the gate is empty, the KTs probably still hold a different
product’s content. Cadence maps whatever CertHub returns; it does not invent
Sterilisator requirements.

## Switch prod / dev

[`certhub.toml`](../certhub.toml) keeps one **flat** active key set. Comment the
inactive block. Point `.env` at the API key for that environment. Never hardcode
URLs or KT ids in connector code.

## Related

- [Troubleshooting](troubleshooting.md)
- [Architecture](architecture.md)
- [Walkthrough](walkthrough.md)
