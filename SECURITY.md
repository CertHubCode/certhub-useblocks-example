# Security policy

## Reporting a vulnerability

Email security issues to CertHub (do not open a public GitHub issue for
undisclosed vulnerabilities). Include the affected command or workflow and
whether a secret was exposed.

## What this repo stores

| Item | In git? |
|------|---------|
| `CERTHUB_API_KEY` | **Never** — `.env` is gitignored; CI uses a GitHub Actions secret |
| Tenant URLs and KT ids | Yes — `certhub.toml` is configuration, not a credential |
| Evidence packs, JUnit, Sphinx HTML | No — gitignored, uploaded as CI artifacts |

Rotate the API key if it appears in a log, gist, or commit. History rewrite does
not remove a leaked key from clones.

## Supply chain notes

Dependencies are locked in `uv.lock`. `make generate-api` fetches OpenAPI specs
from the URLs in `certhub.toml`. Treat those hosts as part of your trust
boundary.
