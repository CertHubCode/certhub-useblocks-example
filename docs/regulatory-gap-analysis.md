# SaMD documentation gap analysis — Cadence vs CertHub

**Product:** Sterilisator 20A (example SaMD)  
**Repo evidence pack:** this repository (Sphinx HTML + `evidence/` + ubCode Rendered Report)  
**System of record:** CertHub (requirements, design, V&V content, risk, release record)

This document states what Cadence can prove in Git/CI, what correctly stays in CertHub (including risk), and the **additional steps** needed if you want a release pack that auditors can map to EU MDR and US QMSR/ISO 13485 — without pretending the Sphinx report *is* a full DHR or Technical Documentation.

---

## 1. Terminology (so the report is not “random”)

| You might say | Legacy FDA | ISO 13485 / QMSR (US, 2026+) | EU MDR |
|---|---|---|---|
| Design controls history | DHF | Design & Development File (DDF) §7.3.10 | Tech Doc Annex II (design / V&V parts) |
| How to build / configure the device | DMR | Medical Device File (MDF) §4.2.3 | Annex II device description / manufacturing info |
| Per-unit / per-release build proof | **DHR** | Production / release records §7.5 | Release / batch evidence (not Annex III PMS) |

**Cadence today ≈ engineering DDF slice + thin per-release production record.**  
It is **not** a complete DHR, not a full MDF, and not full EU Annex II/III.

Risk management, GSPR, clinical evaluation, labeling, PMS, and formal approvals belong in **CertHub** (or your QMS). That split is intentional and correct for this showcase.

---

## 2. What this repo delivers today

### Engineering proof (every PR / main / RC)

| Artifact | Location | Proves |
|---|---|---|
| Synced V-model needs | `sphinx/source/generated/` after `make sync` | CertHub content mirrored as Sphinx-Needs |
| CodeLinks impl links | `# @need-ids: DOUT_018` + VERIF markers → `impl-file` / URLs | Design output ↔ source / tests |
| Automated verification | `src/sterilisator_20a/tests/test_sterilisator.py` + JUnit | VERIF_* executed pass/fail |
| Certification gate | `certhub_connector/evidence/verify.py` | Each SYSREQ has DOUT + CodeLinks + passing VERIF |
| Sphinx HTML pack | `sphinx/build/html/` → `evidence/docs/` | Human-readable assurance pack |
| Machine result | `certhub_result.json` + MANIFEST hashes | Baseline identity + per-SYSREQ status |

### Regulatory write-back (full tag `vX.Y.Z` only)

| Artifact | Location | Proves |
|---|---|---|
| Release Record row | CertHub KT `release_record_kt_id` | Version, commit, timestamp, evidence URL, Notes summary |

### Traceability chain (as implemented)

Two jobs: CertHub is the ISO 13485 7.3.2(e) matrix; this repo tags GPSV §5.2.4’s
last hop (code → design specification, tests → that spec). See
[docs/traceability-map.md](traceability-map.md).

```text
CertHub KTs (UREQ/SYSREQ/CREQ/UNITREQ/DOUT/VERIF/VALID) + Tracer
    → make sync → Sphinx-Needs catalog (including unlinked rows)
SYSREQ_* ←Tracer→ DOUT_018 → CodeLinks → src/sterilisator_20a/**
SYSREQ_* ←Tracer→ VERIF_*  → CodeLinks + pytest → tests/ + JUnit
UREQ ←→ VALID              → catalog only (intended use; not pytest)
Gate root = System Requirements (walked via DOUT/VERIF, not stamped on source)
Outbound = one Release Record (not full Tech Doc upload)
Risk controls (62304 5.1.1(c) / ISO 14971) stay in CertHub
```

---

## 3. What correctly lives in CertHub (do not recreate in Sphinx)

Keep these controlled in CertHub; Cadence should only **point** or **summarize**, never own the file:

| Topic | Why CertHub |
|---|---|
| Risk management file (ISO 14971) | Controlled content, reviews, residual risk, links to hazards |
| GSPR / Essential requirements checklist (MDR Annex I) | Formal conformity evidence with clause mapping |
| Clinical evaluation (CER) / clinical data | Clinical process, not engineering CI |
| Usability engineering file (IEC 62366-1) | Separate controlled record set |
| Labeling / IFU / UDI assignment | MDF / Tech Doc manufacturing & identification |
| PMS / PMCF plans & reports (MDR Annex III) | Post-market; not a release engineering pack |
| Design reviews, approvals, e-signatures | QMS / CertHub workflow |
| Change control / CAPA linkage | QMS; Git is supporting evidence only |
| SOUP / cybersecurity / 62304 classification narrative | Controlled SW lifecycle documentation |

**Principle:** Sphinx/ubCode = **engineering twin for a git baseline**. CertHub = **controlled SoR + formal release record**.

---

## 4. EU + US checklist — coverage map

Legend: **Done** = Cadence can show it for Sterilisator 20A · **Partial** = present but incomplete · **CertHub** = owned there · **Gap** = neither (needs work)

### 4.1 Design & development (DHF / DDF / Annex II design)

| Item | Status | Notes |
|---|---|---|
| User needs / UREQ | Done | `UREQ_001`–`002` sterilizer needs; VALID links to UREQ |
| System requirements (SoR) | Done | Gate root; `SYSREQ_001`–`004` (temp, time, door, English UI) |
| Component / unit requirements | Done | 3 CREQ + 5 UNITREQ synced; not in gate |
| Design outputs | Done | Product DO `DOUT_018` + CodeLinks |
| Implementation ↔ DOUT | Done | CodeLinks to `src/sterilisator_20a/` (cycle, safety, UI) |
| Architecture / detailed design docs | Gap | Thin simulation code; no formal SW architecture KT in pack |
| Design reviews | CertHub | Not in evidence pack |
| Verification protocols + results | Done | VERIF in CertHub; execution in pytest/JUnit/Sphinx |
| Validation protocols + results | Done (manual) | `VALID_001`–`002` → UREQ; **not in the engineering gate** |
| Traceability matrix | Done | Sphinx matrices + (after fix) needflow graph + ubCode chain report |
| Risk ↔ requirements | CertHub | Keep in CertHub; optional future: show risk IDs as links only |

### 4.2 Medical device / master file (DMR / MDF / Annex II description)

| Item | Status | Notes |
|---|---|---|
| Device description / intended use | CertHub | Product/KU in Tech Doc |
| Software version / config identity | Partial | Git tag + commit in result/Release Record |
| Build / install instructions | Gap | Not packaged as IFU/install record |
| SBOM / dependencies | Gap | Optional CI addition later |
| Labeling / UDI | CertHub | |

### 4.3 Production / release record (DHR / §7.5)

| Item | Status | Notes |
|---|---|---|
| Release identity (version) | Done | `vX.Y.Z` + Release Record `release-number` |
| Build identity (commit) | Done | `release-id` / `certhub_result.json` commit |
| Acceptance / gate result | Done | VERIFIED / BLOCKED + per-SYSREQ lines in Notes |
| Evidence pack pointer | Done | `evidence-url` + CI artifacts |
| Quantity / lot (hardware-style) | N/A / Gap | For pure SaMD often “one release unit”; document policy in CertHub |
| UDI / unique device identifier on release | CertHub / Gap | Extend Release Record schema if required |
| Authorized release signature | CertHub | Approver workflow — not in Cadence POST today |
| Manufacturing deviations | CertHub | |

### 4.4 EU extras

| Item | Status | Notes |
|---|---|---|
| Classification rationale | CertHub | |
| GSPR checklist | CertHub | |
| CER | CertHub | |
| PMS / PMCF | CertHub | Annex III — out of engineering loop |
| Cybersecurity / MDCG guidance evidence | CertHub + Gap | Can later attach scan reports into evidence pack |

---

## 5. What we enhance in Cadence (repo) vs what needs CertHub/process work

### 5.1 Done or doable in this repo (engineering loop)

These are the improvements that belong in Cadence code/docs (implementation track):

1. **Traceability graph with edges** — filtered `needflow` (`links` / `verifies` / `validates`); orphan previous-gen DOUTs excluded (**done** in Cadence).
2. **ubCode Rendered Report → code chain** — per SYSREQ: DOUT → `impl-file` / local / remote URLs → VERIF → JUnit result (**done**).
3. **Show CodeLinks fields** on need layouts / Sphinx tables (`impl-file`; `local-url` / `remote-url` come from sphinx-codelinks — do not redeclare in `ubproject.toml`) (**done**).
4. **Sphinx tables** — DOUT/VERIF columns include implementation URLs; certification summary lists implementation (**done**).
5. **This gap analysis** — pack mapped to EU/US checklists; CertHub boundaries explicit (**done**).
6. **Optional later (still repo):**
   - Split `DOUT_018` into feature-level design outputs in CertHub, then split
     the `@need-ids:` markers (do **not** put CodeLinks on procedure
     `DOUT_001`–`004`)
   - Stronger UREQ↔VALID Tracer links once sterilizer UREQs are clean in CertHub
   - PDF/LaTeX builder if customers need a single signed PDF twin

### 5.2 Additional steps outside “random Sphinx polish” (CertHub + QMS)

Use this as the enhancement backlog for a **real** SaMD DHR/Tech Doc program. Cadence stays the engineering twin.

| # | Step | Owner | Outcome |
|---|---|---|---|
| 1 | Confirm sterilizer-only content on User / System / Component / Unit / DOUT / VERIF / VALID KTs | CertHub content | SoR matches the product under test |
| 2 | Keep risk file complete and link hazards ↔ SYSREQ/DOUT in CertHub Tracer | CertHub | Risk stays SoR; optional later: export risk IDs into Sphinx as read-only refs |
| 3 | Maintain GSPR checklist with evidence pointers (including “see Release Record baseline X / evidence URL”) | CertHub | Annex I conformity without duplicating CI in Sphinx |
| 4 | CER / clinical pathway as required by class | CertHub / clinical | Out of Cadence |
| 5 | Extend Release Record schema: UDI/software version ID, approver, config/SBOM hash, environment | CertHub schema + Cadence `push_evidence` | Closer to production-record (DHR-equivalent) |
| 6 | Release authorization workflow (who may POST / who signs) | CertHub QMS | Formal release, not only CI green |
| 7 | IEC 62304 software safety classification + SOUP list as controlled KTs | CertHub | Lifecycle narrative |
| 8 | Labeling / IFU / install instructions in MDF-equivalent KT | CertHub | |
| 9 | PMS / PMCF plans (Annex III) | CertHub | Not part of `make evidence` |
| 10 | Document the boundary in QMS SOP: “engineering evidence = Cadence pack; controlled records = CertHub” | QMS | Auditors get one story |

---

## 6. Target report shape (so pages follow the checklist)

Structure the **Rendered Report** and Sphinx pack around this outline:

1. **Identity** — product, version, commit, gate status  
2. **Design inputs** — SYSREQ (and pointer to full CertHub SoR)  
3. **Design outputs + implementation (code)** — DOUT + CodeLinks URLs  
4. **Verification** — VERIF ↔ JUnit  
5. **Validation** — VALID status; show gaps explicitly  
6. **Traceability graph + matrices**  
7. **Release / production record** — payload that POSTs on `vX.Y.Z`  
8. **Out of scope appendix** — risk, GSPR, CER, PMS, labeling → **CertHub**

Anything not in 1–7 should not appear as if Cadence “owns” it.

---

## 7. Realization model (short)

```text
┌─────────────────────────────────────────────────────────┐
│ CertHub (SoR)                                           │
│  Requirements · DOUT · VERIF · VALID                    │
│  Risk · GSPR · CER · Labeling · PMS · Approvals         │
│  Release Record (per vX.Y.Z)                            │
└─────────────┬───────────────────────────────▲───────────┘
              │ make sync                      │ push-evidence
              ▼                                │ (full release only)
┌─────────────────────────────────────────────┴───────────┐
│ This repo / CI                                          │
│  CodeLinks on DOUT · pytest on VERIF · gate · Sphinx    │
│  ubCode Rendered Report (SYSREQ via Tracer → DOUT → test)│
└─────────────────────────────────────────────────────────┘
```

**Success criterion for Cadence:** an auditor can open the evidence pack or Rendered Report and answer “for this baseline, which requirement is implemented where and which test passed?” — then follow CertHub for risk and regulatory files.

---

## 8. Implementation status of Cadence UX fixes

| Fix | Status |
|---|---|
| `traceability.rst`: filtered `needflow` (edges; sterilizer DOUTs only) | Done |
| `ubcode_reports/needs_overview.html.j2`: SYSREQ→DOUT→code→VERIF→result | Done |
| `ubproject.toml` CodeLinks layout shows `impl-file` / `local-url` / `remote-url` (URL fields registered by sphinx-codelinks — do not redeclare in TOML) | Done |
| Sphinx DOUT/VERIF tables + certification summary chain headers | Done |

Re-run `make show`, open Traceability + ubCode Reports, and confirm SYSREQ rows show `impl-file` / GitHub links.

---

## 9. What “full DHR for SaMD” would still require after Cadence is green

Even with perfect code traceability, a marketable SaMD release file set still needs CertHub/QMS items in §5.2 (especially **5, 6, 2, 3**). Cadence should not invent risk or GSPR HTML; it should remain the reproducible engineering proof attached to each Release Record.
