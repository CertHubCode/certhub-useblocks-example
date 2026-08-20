# TMP — CertHub SoR checklist (maintainer only)

**Temporary.** Not linked from the README. Work through this in the Sterilisator 20A
product on **prod** (`https://app.certhub.de`), then delete this file.

After each section:

```bash
make sync && make show
```

Confirm the Sphinx needflow / matrix still looks right.

---

## Design outputs / Tracer

- [ ] Unlink SYSREQ_002, SYSREQ_003, SYSREQ_004 from DOUT_015 (EcoSteam), DOUT_016 (MedSteril), DOUT_017 (HydroSter)
- [ ] Link DOUT_018 (Sterilizer 20A) to SYSREQ_001–004
- [ ] Keep DOUT_001–004 as procedures only (not SaMD implementation)
- [ ] Hide or archive DOUT_005–014 and DOUT_019 (non-Sterilisator catalog)

## Requirements text

- [ ] Scrub infusion-pump / other-product text from all UREQ_* on this KU
- [ ] Scrub same from UNITREQ_*
- [ ] Spot-check CREQ_* titles/body are Sterilisator 20A only

## Verification / validation

- [ ] Confirm VERIF_001–004 still match the four SYSREQs (and pytest markers in the repo)
- [ ] Fix VALID_* Tracer links: prefer VALID → UREQ (user needs), not random SYSREQ
- [ ] Confirm VALID content is Sterilisator-only; leave status **manual** in CertHub (no pytest unless the protocol is automatable)

## Hygiene after QA writes

- [ ] In the Release Record KT UI, remove leftover demo rows from `make confirm` / push tests (e.g. baseline `0.0.99`) — **UI only**; the public Records API cannot delete

## Done criteria

- [ ] `make sync && make show` → VERIFIED, 4/4 SYSREQ PASS
- [ ] Traceability needflow shows SYSREQ ↔ DOUT_018 ↔ VERIF without EcoSteam / MedSteril / HydroSter
- [ ] No foreign-product text in synced UREQ / UNITREQ pages
- [ ] Delete this TMP file and any remaining “someone must clean CertHub” language from public docs
