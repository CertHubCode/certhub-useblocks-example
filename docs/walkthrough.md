# Walkthrough — Cadence (CertHub SaMD Engineering Loop)

### Walkthrough video

[![CertHub Cadence walkthrough](https://img.youtube.com/vi/9R5RELvVyeY/hqdefault.jpg)](https://www.youtube.com/watch?v=9R5RELvVyeY)

Run from the repository root.

Local walkthroughs print a polished CertHub CLI (Rich banners / status). CI stays plain (`CI=1` / non-TTY).

## One-liner mental model

| Stage | What happens | CertHub write? | Needs API key? |
|-------|--------------|----------------|----------------|
| Clone / `make show` | Build evidence pack from committed catalog | No | No |
| Everyday work / PR | Same pack; optional `make sync` when the secret is set | No | Only for sync |
| RC tag | Same as above | No | For sync in release CI |
| Full release tag `vX.Y.Z` | Evidence + Release Record in CertHub | **Yes** | Yes |

Tenant URLs and KT ids live in committed [`certhub.toml`](../certhub.toml). The
API key is only for `make sync` and write-back — not for the first `make show`.

---

## Walkthrough script

### 1. Show the engineering gate (GREEN) — no API key

```bash
make install
make show
```

Runs tests → CodeLinks → certification verify → opens the HTML dashboard.
Uses the committed Sphinx-Needs catalogs and
`certhub/generated/normalized_export.json`.
Expect: **VERIFIED**, all `SYSREQ_*` PASS.

### 2. Break it (RED)

```bash
make break
make show
```

Intentionally breaks cycle-time reporting so ``VERIF_002`` fails.
Expect: gate **BLOCKED**, dashboard still opens so you can show the failure.

### 3. Fix it (back to GREEN)

```bash
make fix
make show
```

### 4. Build the evidence pack (what CI does)

```bash
make evidence
```

Same gate as `show`, no browser. Writes `evidence/` (gitignored), including Sphinx HTML under `evidence/docs/` (open `docs/dashboard.html` after downloading the CI artifact).
This is what every PR uploads as a GitHub artifact — still **no** CertHub write.

### 5. Refresh the V-model from CertHub (optional, needs an [API key](https://docs.certhub.de/api/getting-started))

```bash
cp .env.example .env
# set CERTHUB_API_KEY=… — generate yours: https://docs.certhub.de/api/getting-started
make sync
make show
```

Loads the seven V-model knowledge topics plus Tracer use-case edges into
Sphinx-Needs and refreshes the normalized snapshot. Source comments do not change.
`SYSREQ` is in the catalog so the gate can walk Tracer links to `DOUT` /
`VERIF`; it is not stamped on functions.

| Where | What |
|-------|------|
| `certhub.toml` | Tech Doc / Records / Tracer base URLs, seven content KT revision ids + Release Record, dashboard URL fields |
| `.env` / GitHub secret `CERTHUB_API_KEY` | API key (`X-API-Key`) — [create one](https://docs.certhub.de/api/getting-started) |

How to find IDs: [onboarding](onboarding.md).

**GitHub:** only secret `CERTHUB_API_KEY` (no repository variables for URLs/KTs).

### 6. Prove CertHub write-back (optional, needs an [API key](https://docs.certhub.de/api/getting-started))

```bash
make confirm BASELINE=0.0.99
```

Live POST → GET against CertHub Release Record. Look for `matched: True`.
The CLI also prints the Release Record KT dashboard URL (from `certhub.toml`).
Use this to prove the API path without tagging a real release.

### 7. Tag RC / release (CI runs the gate)

Working tree must be clean. Tagging does **not** bump `pyproject.toml` or create a commit — it only creates an annotated tag on HEAD and pushes it. GitHub runs the workflow from that tagged commit (so tag HEAD after the release workflow is on the branch).

```bash
# Optional: RC — same evidence gate as release, artifact in the run, no CertHub write
make tag-rc VERSION=1.0.0 RC=1

# Full release — tag v1.0.0 → evidence artifact + Release Record in CertHub
make tag-release VERSION=1.0.0
```

`make tag-release` prints the Release Record KT URL so you can open CertHub after CI finishes.

What CI does on every version tag (RC and full):

1. `make sync` (needs `CERTHUB_API_KEY` secret)
2. `make evidence`
3. Upload artifact

On full `v1.0.0` only:

4. `CERTHUB_PUSH=1 make push-evidence BASELINE=1.0.0` → Release Record in CertHub

### 8. Show the Release Record in CertHub

After `make tag-release` or `make confirm`, follow the printed URL (or run):

```bash
make open-release-record
```

Download the workflow artifact named `evidence-*` from the GitHub Actions run
(Actions → Cadence release evidence → Artifacts) and open `docs/dashboard.html`
inside the zip. That is the same pack the Release Record `evidence-url` points at.

Point at release-number, commit, evidence-url, and the plain-text Notes.
Say: “Same gate as every PR. Only this tag made it a controlled row.”

### 9. Change a requirement in CertHub (SoR beat)

```bash
make open-requirements
```

Edit one requirement in the CertHub UI, then:

```bash
make sync
make show
```

Show the Sphinx twin updated. No new Release Record was created — engineering follows CertHub.

---

## Command cheat sheet

| Command | What it does |
|---------|----------------|
| `make show` | Local walkthrough: tests + verify + open dashboard (**no API key**) |
| `make evidence` | CI twin of show; writes `evidence/` (incl. `docs/` HTML) |
| `make break` / `make fix` | RED / GREEN gate toggle |
| `make sync` | CertHub → Sphinx-Needs + snapshot (needs API key) |
| `make push-evidence BASELINE=X.Y.Z` | Dry-run: print RecordCreate JSON + Release Record URL |
| `CERTHUB_PUSH=1 make push-evidence …` | Live POST (same as release CI) |
| `make confirm BASELINE=X.Y.Z` | Live POST→GET proof + dashboard URL |
| `make open-requirements` | Open Requirements KT in CertHub |
| `make open-release-record` | Open Release Record KT in CertHub |
| `make tag-rc VERSION=X.Y.Z RC=N` | Push `vX.Y.Z-rc.N` → evidence artifact only |
| `make tag-release VERSION=X.Y.Z` | Push `vX.Y.Z` → artifact **+** CertHub; prints KT URL |

---

## What this demonstrates

1. **CertHub** holds the V-model *records* and Tracer matrix (ISO 13485 7.3.2(e)).
2. **This repo** tags only the last hop: `DOUT_*` on source, `VERIF_*` on tests
   (FDA GPSV §5.2.4). `SYSREQ` is not on functions; the gate walks Tracer.
3. **Cadence** is the SaMD engineering loop: Git twin + evidence gate + release write-back.
4. **useblocks** turns Git work into an evidence pack.
5. **PRs** prove engineering quality (artifact); they do not create regulatory records.
6. **RC tags** rehearse the same gate and store the pack on the run; they do not write CertHub.
7. **Release tags** close the loop: one Release Record in CertHub for that baseline.
8. After a release or `make confirm`, open the printed CertHub URL to see the controlled row.
9. Edit a requirement in CertHub, then re-sync — engineering follows the SoR. Unlinked
   catalog rows stay; leftover product text is cleaned in CertHub, not by syncing less.
