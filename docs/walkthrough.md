# Walkthrough — Cadence (CertHub SaMD Engineering Loop)

Run from the repository root.

Local walkthroughs print a polished CertHub CLI (Rich banners / status). CI stays plain (`CI=1` / non-TTY).

## Configure

Tenant URLs, KT revision ids, and dashboard history ids live in committed [`certhub.toml`](../certhub.toml) — edit that file for a customer tenant (safe to keep in git). The showcase file uses **prod** CertHub hosts. Read settings only via `TenantSettings.load()` / `CerthubConfig.load()` (no ad-hoc toml parsing; no hardcoded URLs/KT ids in connector code).

```bash
cp .env.example .env
# set CERTHUB_API_KEY=… in .env  (the only secret; prod key for the showcase tenant)
```

| Where | What |
|-------|------|
| `certhub.toml` | Tech Doc / Records / Tracer base URLs, seven content KT revision ids + Release Record, dashboard URL fields |
| `.env` / GitHub secret `CERTHUB_API_KEY` | API key (`X-API-Key`) |

`make sync` requires `CERTHUB_API_KEY` (no mock fallback). Product / KU revision for write-back are resolved from Tech Doc at push time (from the Release Record KT). The SoR is **System Requirements** (sterilizer content).

**GitHub:** only secret `CERTHUB_API_KEY` (no repository variables for URLs/KTs).

---

## One-liner mental model

| Stage | What happens | CertHub write? |
|-------|--------------|----------------|
| Everyday work / PR | Build evidence pack, upload CI artifact | No |
| RC tag | Same as above | No |
| Full release tag `vX.Y.Z` | Evidence + Release Record in CertHub | **Yes** |

---

## Walkthrough script

### 1. Pull requirements into the repo

```bash
make sync
```

Loads requirements from CertHub (Tech Doc + Records + Tracer use-case links) into Sphinx-Needs.

### 2. Show the engineering gate (GREEN)

```bash
make show
```

Runs tests → CodeLinks → certification verify → opens the HTML dashboard.  
Expect: **VERIFIED**, all `SYSREQ_*` PASS.

### 3. Break it (RED)

```bash
make break
make show
```

Intentionally breaks cycle-time reporting so ``VERIF_002`` fails.  
Expect: gate **BLOCKED**, dashboard still opens so you can show the failure.

### 4. Fix it (back to GREEN)

```bash
make fix
make show
```

### 5. Build the evidence pack (what CI does)

```bash
make evidence
```

Same gate as `show`, no browser. Writes `evidence/` (gitignored), including Sphinx HTML under `evidence/docs/` (open `docs/dashboard.html` after downloading the CI artifact).  
This is what every PR uploads as a GitHub artifact — still **no** CertHub write.

### 6. Prove CertHub write-back (optional, needs API key)

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

1. `make sync`
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
| `make sync` | CertHub → Sphinx-Needs |
| `make show` | Local walkthrough: tests + verify + open dashboard |
| `make evidence` | CI twin of show; writes `evidence/` (incl. `docs/` HTML) |
| `make break` / `make fix` | RED / GREEN gate toggle |
| `make push-evidence BASELINE=X.Y.Z` | Dry-run: print RecordCreate JSON + Release Record URL |
| `CERTHUB_PUSH=1 make push-evidence …` | Live POST (same as release CI) |
| `make confirm BASELINE=X.Y.Z` | Live POST→GET proof + dashboard URL |
| `make open-requirements` | Open Requirements KT in CertHub |
| `make open-release-record` | Open Release Record KT in CertHub |
| `make tag-rc VERSION=X.Y.Z RC=N` | Push `vX.Y.Z-rc.N` → evidence artifact only |
| `make tag-release VERSION=X.Y.Z` | Push `vX.Y.Z` → artifact **+** CertHub; prints KT URL |

---

## What to say in the walkthrough

1. **CertHub** is the system of record for requirements.  
2. **Cadence** is the SaMD Engineering Loop: Git twin + evidence gate + release write-back.  
3. **useblocks** turns Git work into an evidence pack.  
4. **PRs** prove engineering quality (artifact), they do not create regulatory records.  
5. **RC tags** rehearse the same gate and store the pack on the run; they do not write CertHub.  
6. **Release tags** close the loop: one Release Record in CertHub for that baseline.  
7. **Open the printed CertHub URL** so the audience sees the controlled row.  
8. **Edit a requirement in CertHub**, re-sync — engineering follows the SoR.
