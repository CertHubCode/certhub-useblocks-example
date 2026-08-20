# TMP — CertHub SoR punch list (Sterilisator 20A MVP)

**Temporary. Maintainer only.** Not linked from the README.

Work through this on **prod** (`https://app.certhub.de`) in the Sterilisator 20A
product / Requirements Engineering KU. When every checkbox below is done, tell
the agent in chat — they will run `make sync` and continue Phase 2 (code,
README, Sphinx). **Do not** run `make sync` yourself between sections.

Delete this file when Phase 2 is green (`make show` → VERIFIED, 4/4 SYSREQ PASS).

---

## Product story (what you are modelling)

Clinic staff load instruments, close the door, and start a steam cycle.
Software: chamber **121°C ± 2°C**, cycle **≤ 60 minutes**, **door locked while
running**, **English** status (idle / running / complete / fault).

Target shape (not 1:1 counts):

```text
2 UREQ → 4 SYSREQ → 3 CREQ → 5 UNITREQ → 1 DOUT (DOUT_018)
4 VERIF (system) + 2 VALID (user needs)
```

---

## Critical naming rule

Every record **Name** field must be exactly:

```text
PREFIX_NNN — Title
```

Use an em dash (`—`) or a plain hyphen (`-`). Sync only keeps stable IDs
(`DOUT_018`, `UREQ_001`, …) when this pattern is present. Without it, the
Sterilizer DO syncs as `DOUT_001` and CodeLinks / the gate break.

---

## 0. Hygiene first

- [ ] Unlink SYSREQ_002, SYSREQ_003, SYSREQ_004 from DOUT_015 (EcoSteam),
  ```
  DOUT_016 (MedSteril), DOUT_017 (HydroSter) if those Tracer edges still exist
  ```
- [ ] Hide / archive / obsolete non-Sterilisator catalog DOs you do not want in
  ```
  the needflow (DOUT_005–014, DOUT_019, etc.)
  ```
- [ ] Procedure-only DOs (if any remain) must **not** be linked as the SaMD
  ```
  product DO — that role is **DOUT_018** only
  ```

---

## 1. Create — User Requirements (2 new records)

KT: **User Requirements**.

> Type select uses the live typo `Fucntional` for functional needs — pick that.

### UREQ_001

| Field                                   | Paste                                                                                                                                                                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                                | `UREQ_001 — Safe and effective instrument sterilization`                                                                                                                                                                                          |
| **Description / Requirement Statement** | The operator shall be able to steam-sterilize reusable instruments so that heat-resistant microorganisms are inactivated during intended use, without unloading while the chamber is in an unsafe (in-progress) state.                            |
| **Rationale / Intended Use**            | Intended use in a small clinic: staff need a tabletop steam sterilizer they can trust for instrument reprocessing, with door safety during the cycle.                                                                                             |
| **Type**                                | `Fucntional`                                                                                                                                                                                                                                      |
| **Priority**                            | `high`                                                                                                                                                                                                                                            |
| **Acceptance Criteria**                 | Ten consecutive intended-use cycles each reach the sterilization temperature window (121°C ± 2°C) with no abort; the door remains locked while the cycle is running; operators accept the device for steam sterilization of reusable instruments. |
| **Safety / Risk relevant**              | checked (yes)                                                                                                                                                                                                                                     |
| **Status**                              | `approved` (or `in_review` then approve)                                                                                                                                                                                                          |
| **relates to System Requirement(s)**    | `SYSREQ_001, SYSREQ_003` _(form note only — real traces are Tracer)_                                                                                                                                                                              |

- [x] UREQ_001 created

### UREQ_002

| Field                                   | Paste                                                                                                                                                                               |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                                | `UREQ_002 — Operable in a clinic workflow`                                                                                                                                          |
| **Description / Requirement Statement** | Clinic staff shall finish a sterilization cycle within a treatment-room timebox and understand cycle status and alerts in English.                                                  |
| **Rationale / Intended Use**            | Throughput for several loads per clinic session, plus MDR user-information expectations for unambiguous English status and alerts.                                                  |
| **Type**                                | `Fucntional`                                                                                                                                                                        |
| **Priority**                            | `high`                                                                                                                                                                              |
| **Acceptance Criteria**                 | Ten consecutive cycles each complete in 60 minutes or less; operators correctly identify idle, running, complete, and fault states from the English UI in normal and fault scripts. |
| **Safety / Risk relevant**              | unchecked (no)                                                                                                                                                                      |
| **Status**                              | `approved`                                                                                                                                                                          |
| **relates to System Requirement(s)**    | `SYSREQ_002, SYSREQ_004`                                                                                                                                                            |

- [x] UREQ_002 created

---

## 2. Edit — System Requirements (4 existing records)

KT: **System Requirements**. Keep the existing records; change **Name** and body.
Drop “is better” from SYSREQ_001. **Replace footprint** on SYSREQ_004 with
English cycle status. **Replace UI labeling** on SYSREQ_003 with door interlock.

### SYSREQ_001 (was: temperature / “is better”)

| Field                      | Paste                                                                       |
| -------------------------- | --------------------------------------------------------------------------- |
| **Name**                   | `SYSREQ_001 — Sterilization temperature range`                              |
| **Description**            | Device shall achieve and maintain sterilization temperature of 121°C ± 2°C. |
| **Justification**          | Ensures effective microbial inactivation.                                   |
| **Type**                   | `functional`                                                                |
| **Priority**               | `high`                                                                      |
| **Requirement concerning** | Equipment (keep or set sensibly)                                            |

- [x] SYSREQ_001 updated

### SYSREQ_002 (was: cycle time)

| Field             | Paste                                         |
| ----------------- | --------------------------------------------- |
| **Name**          | `SYSREQ_002 — Sterilization cycle time`       |
| **Description**   | Total cycle time shall not exceed 60 minutes. |
| **Justification** | Optimizes throughput for clinical operations. |
| **Type**          | `functional`                                  |
| **Priority**      | `high`                                        |

- [x] SYSREQ_002 updated

### SYSREQ_003 (was: User interface labeling → **Door interlock**)

| Field             | Paste                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Name**          | `SYSREQ_003 — Door interlock`                                                                                                     |
| **Description**   | A sterilization cycle shall not start unless the chamber door is closed. The door shall remain locked while the cycle is running. |
| **Justification** | Prevents operator exposure and incomplete sterilization from door opening during an active cycle.                                 |
| **Type**          | `functional`                                                                                                                      |
| **Priority**      | `high`                                                                                                                            |

- [x] SYSREQ_003 rewritten as door interlock

### SYSREQ_004 (was: Device footprint → **English cycle status**)

| Field             | Paste                                                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**          | `SYSREQ_004 — English cycle status`                                                                                                      |
| **Description**   | The user interface shall display cycle state and alerts in English, covering idle, running, complete, fault, and door-locked conditions. |
| **Justification** | Compliance with MDR user-information expectations; clinic staff must read status without translation.                                    |
| **Type**          | `regulatory` (or functional if that fits the form better)                                                                                |
| **Priority**      | `high`                                                                                                                                   |

- [x] SYSREQ_004 rewritten as English cycle status (no footprint)

---

## 3. Edit — Component Requirements (rewrite 3; obsolete 1)

KT: **Component Requirements**. Fields are mainly **Name**, **Description**,
**Rationale**.

### CREQ_001 (reuse record — was temperature rationale)

| Field           | Paste                                                                                                                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Name**        | `CREQ_001 — Cycle engine`                                                                                                                                                                                                      |
| **Description** | The cycle-control software component shall run a sterilization cycle (idle → running → complete or fault), evaluate chamber peak temperature against 121°C ± 2°C, and accept a cycle only when total duration is ≤ 60 minutes. |
| **Rationale**   | Implements SYSREQ_001 and SYSREQ_002. Implementation: `src/sterilisator_20a/cycle/controller.py`.                                                                                                                              |

- [x] CREQ_001 rewritten

### CREQ_002 (reuse record — was cycle-time rationale → **Door safety**)

| Field           | Paste                                                                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Name**        | `CREQ_002 — Door safety`                                                                                                                               |
| **Description** | The door-safety software component shall inhibit cycle start when the door is open and require the door to remain locked while cycle state is running. |
| **Rationale**   | Implements SYSREQ_003. Implementation: `src/sterilisator_20a/safety/door.py` (added in repo Phase 2).                                                  |

- [x] CREQ_002 rewritten as door safety

### CREQ_003 (reuse record — was labeling rationale)

| Field           | Paste                                                                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**        | `CREQ_003 — Operator UI`                                                                                                                                  |
| **Description** | The UI software component shall expose English status and alert strings for each cycle state (idle, running, complete, fault) and door-locked conditions. |
| **Rationale**   | Implements SYSREQ_004. Implementation: `src/sterilisator_20a/ui/messages.py`.                                                                             |

- [x] CREQ_003 rewritten

### CREQ_004 (was footprint rationale)

- [ ] **Obsolete or delete CREQ_004** so it does not appear in the needflow
  ```
  (set status obsolete/superseded if the form has it, or remove the record)
  ```

---

## 4. Create — Unit Requirements (5 new records)

KT: **Unit Requirements**. Name field on the form may be labelled oddly
(`textfield_5azvqs`) — still paste `UNITREQ_00N — …` into **Name**.

### UNITREQ_001

| Field                                   | Paste                                                                                                         |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Name**                                | `UNITREQ_001 — Peak temperature window`                                                                       |
| **Description / Requirement Statement** | `temperature_within_range` shall return true if and only if peak chamber temperature is in [119.0, 123.0] °C. |
| **Type**                                | `functional`                                                                                                  |
| **Acceptance Criteria**                 | Boundaries at ±2.0°C pass; ±2.1°C fail. Implemented in `cycle/controller.py`.                                 |
| **Priority**                            | `high`                                                                                                        |
| **Status**                              | `approved`                                                                                                    |
| **relates to -> Component Req**         | `CREQ_001`                                                                                                    |
| **relates to -> Verification**          | `VERIF_001`                                                                                                   |

- [x] UNITREQ_001 created

### UNITREQ_002

| Field                                   | Paste                                                                                                                                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                                | `UNITREQ_002 — Cycle duration acceptance`                                                                                                                         |
| **Description / Requirement Statement** | `reported_cycle_duration_minutes` shall reject negative durations; `cycle_within_time_budget` shall return true if and only if reported duration is ≤ 60 minutes. |
| **Type**                                | `performance`                                                                                                                                                     |
| **Acceptance Criteria**                 | 0, 45, and 60 minutes pass; negative duration raises `SterilizerError`. Implemented in `cycle/controller.py`.                                                     |
| **Priority**                            | `high`                                                                                                                                                            |
| **relates to -> Component Req**         | `CREQ_001`                                                                                                                                                        |
| **relates to -> Verification**          | `VERIF_002`                                                                                                                                                       |

- [x] UNITREQ_002 created

### UNITREQ_003

| Field                                   | Paste                                                                                                                                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Name**                                | `UNITREQ_003 — Cycle states`                                                                                                                                                         |
| **Description / Requirement Statement** | After `start_cycle` returns, cycle state shall be `complete` when temperature and duration both pass, otherwise `fault`. The returned result shall not leave the cycle in `running`. |
| **Type**                                | `functional`                                                                                                                                                                         |
| **Acceptance Criteria**                 | Passing temp+time → `complete`; failing temp or time → `fault`. Exercised by VERIF_001 and VERIF_002.                                                                                |
| **Priority**                            | `medium`                                                                                                                                                                             |
| **relates to -> Component Req**         | `CREQ_001`                                                                                                                                                                           |
| **relates to -> Verification**          | `VERIF_001, VERIF_002`                                                                                                                                                               |

- [x] UNITREQ_003 created

### UNITREQ_004

| Field                                   | Paste                                                                                                                                                                             |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                                | `UNITREQ_004 — Door start-inhibit and lock`                                                                                                                                       |
| **Description / Requirement Statement** | Cycle start with door open shall be refused. `door_must_lock` shall be true if and only if cycle state is `running`. `door_may_open` shall be true for idle, complete, and fault. |
| **Type**                                | `safety`                                                                                                                                                                          |
| **Acceptance Criteria**                 | Open door cannot start; locked while running; may open on idle/complete/fault. Implemented in `safety/door.py` (repo Phase 2).                                                    |
| **Priority**                            | `high`                                                                                                                                                                            |
| **Safety / Risk relevant**              | checked                                                                                                                                                                           |
| **relates to -> Component Req**         | `CREQ_002`                                                                                                                                                                        |
| **relates to -> Verification**          | `VERIF_003`                                                                                                                                                                       |

- [x] UNITREQ_004 created

### UNITREQ_005

| Field                                   | Paste                                                                                                                                                                                 |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                                | `UNITREQ_005 — English state labels`                                                                                                                                                  |
| **Description / Requirement Statement** | English UI payload shall cover idle, running, complete, and fault states plus a door-locked alert; non-English language or empty required strings shall fail the English-label check. |
| **Type**                                | `interface`                                                                                                                                                                           |
| **Acceptance Criteria**                 | English payload passes; non-English payload fails. Implemented in `ui/messages.py`.                                                                                                   |
| **Priority**                            | `high`                                                                                                                                                                                |
| **relates to -> Component Req**         | `CREQ_003`                                                                                                                                                                            |
| **relates to -> Verification**          | `VERIF_004`                                                                                                                                                                           |

- [x] UNITREQ_005 created

---

## 5. Edit — Design Output (critical ID)

KT: **Design Output**. Edit the existing Sterilizer 20A record (currently syncs
as `DOUT_001` because Name lacks the prefix).

| Field             | Paste                                                                                                                                                                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**          | `DOUT_018 — Sterilizer 20A`                                                                                                                                                                                                                                                       |
| **Individual ID** | `DOUT_018`                                                                                                                                                                                                                                                                        |
| **Description**   | Sterilisator 20A cycle-control SaMD for a tabletop steam sterilizer: software evaluates sterilization cycle temperature and duration, enforces door interlock while running, and presents English operator status (idle, running, complete, fault). Not a hardware catalog entry. |
| **Specification** | Implementation in `src/sterilisator_20a/` (`cycle/controller.py`, `safety/door.py`, `ui/messages.py`). CodeLinks markers: `# @need-ids: DOUT_018`.                                                                                                                                |

- [x] Name is exactly `DOUT_018 — Sterilizer 20A` (so sync emits **DOUT_018**, not DOUT_001)
- [x] Description has **no** “previous generation / 8 trays / color touchscreen / pre-vacuum” text
- [x] Individual ID set to `DOUT_018` if the field exists

> Relates-to-SR on the DO form may allow only one system requirement. Prefer
> Tracer undirected edges DOUT_018 ↔ SYSREQ_001–004 if the graph UI allows
> multiple. Always link each VERIF and both VALIDs to DOUT_018 (below).

---

## 6. Edit — Verification (4 existing; fix text + unlink cross-wires)

KT: **Verification**. Unlink wrong SYSREQ edges first, then set fields.

### VERIF_001

| Field                    | Paste                                                                                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                 | `VERIF_001 — Temperature accuracy test`                                                                                                                           |
| **Test Method**          | Execute automated test `test_sterilization_temperature_accuracy` (`@pytest.mark.certhub_test("VERIF_001")`) in `src/sterilisator_20a/tests/test_sterilisator.py`. |
| **Acceptance Criteria**  | `temperature_within_range` true at 121°C and ±2.0°C; false at ±2.1°C; a nominal cycle at 121°C / 45 min reports temperature OK.                                   |
| **Expected Test Result** | Passed (automated)                                                                                                                                                |
| **Expected Test Status** | `passed`                                                                                                                                                          |

- [ ] VERIF_001 text updated
- [ ] VERIF_001 does **not** verify SYSREQ_004 (unlink if present)

### VERIF_002

| Field                    | Paste                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                 | `VERIF_002 — Cycle time test`                                                                                                                                 |
| **Test Method**          | Execute automated test `test_sterilization_cycle_time` (`@pytest.mark.certhub_test("VERIF_002")`). This is the Cadence `make break` / `make fix` demo target. |
| **Acceptance Criteria**  | Budget true at 0 / 45 / 60 minutes; negative duration raises; nominal cycle duration OK.                                                                      |
| **Expected Test Result** | Passed (automated)                                                                                                                                            |
| **Expected Test Status** | `passed`                                                                                                                                                      |

- [ ] VERIF_002 text updated

### VERIF_003 (was: UI readability → **Door interlock test**)

| Field                    | Paste                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Name**                 | `VERIF_003 — Door interlock test`                                                                                |
| **Test Method**          | Execute automated test `test_door_interlock` (`@pytest.mark.certhub_test("VERIF_003")`) — added in repo Phase 2. |
| **Acceptance Criteria**  | Cycle cannot start with door open; door must lock while running; door may open on idle / complete / fault.       |
| **Expected Test Result** | Passed (automated)                                                                                               |
| **Expected Test Status** | `passed`                                                                                                         |

- [ ] VERIF_003 rewritten as door interlock (not UI readability)

### VERIF_004 (was: Footprint compatibility → **English UI test**)

| Field                    | Paste                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Name**                 | `VERIF_004 — English UI test`                                                                                       |
| **Test Method**          | Execute automated test `test_user_interface_labeling` (`@pytest.mark.certhub_test("VERIF_004")`).                   |
| **Acceptance Criteria**  | English state labels for idle / running / complete / fault (and door-locked alert) pass; non-English payload fails. |
| **Expected Test Result** | Passed (automated)                                                                                                  |
| **Expected Test Status** | `passed`                                                                                                            |

- [ ] VERIF_004 rewritten as English UI (not footprint)
- [ ] VERIF_004 does **not** verify SYSREQ_003 (unlink if present)

---

## 7. Edit — Validation (keep 2; obsolete 2)

KT: **Validation**. Manual / **n/a** — not in the engineering gate. Prefer
VALID → **UREQ**, not SYSREQ.

### VALID_001

| Field                         | Paste                                                                                                                         |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Name**                      | `VALID_001 — Intended-use sterilization`                                                                                      |
| **Validation regarding**      | `UREQ_001`                                                                                                                    |
| **Validation Method**         | Ten consecutive intended-use sterilization cycles with independent temperature logging and observed door behaviour.           |
| **Sample Size**               | `10`                                                                                                                          |
| **Sample Size Justification** | Small clinic intended-use sample for the Cadence showcase protocol.                                                           |
| **Acceptance Criteria**       | Each cycle peak temperature in 121°C ± 2°C; door remained locked while running; door could be opened after complete or fault. |
| **Expected Result**           | Protocol pass (manual)                                                                                                        |
| **Status**                    | `n/a` (or `in_progress` — leave manual, no pytest)                                                                            |

- [ ] VALID_001 rewritten; targets UREQ_001

### VALID_002

| Field                         | Paste                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                      | `VALID_002 — Clinic operability`                                                                                                  |
| **Validation regarding**      | `UREQ_002`                                                                                                                        |
| **Validation Method**         | Ten consecutive full cycles timed end-to-end; operators identify cycle states from the English UI using normal and fault scripts. |
| **Sample Size**               | `10`                                                                                                                              |
| **Sample Size Justification** | Matches intended-use throughput and labeling check for the showcase.                                                              |
| **Acceptance Criteria**       | Each cycle ≤ 60 minutes; operators correctly identify idle, running, complete, and fault from English status/alerts.              |
| **Expected Result**           | Protocol pass (manual)                                                                                                            |
| **Status**                    | `n/a`                                                                                                                             |

- [ ] VALID_002 rewritten; targets UREQ_002

### VALID_003 and VALID_004

- [ ] **Obsolete or delete VALID_003** (old UI validation leftover)
- [ ] **Obsolete or delete VALID_004** (old footprint validation leftover)

---

## 8. Tracer edges (`connected_within_use_case`)

Form “relates to …” text fields are **not** traces. Sync only reads Tracer
use-case edges. After records exist, create / fix these links:

### Descent (left of V)

- [ ] UREQ_001 —Leads to→ SYSREQ_001
- [ ] UREQ_001 —Leads to→ SYSREQ_003
- [ ] UREQ_002 —Leads to→ SYSREQ_002
- [ ] UREQ_002 —Leads to→ SYSREQ_004
- [ ] SYSREQ_001 —Results in→ CREQ_001
- [ ] SYSREQ_002 —Results in→ CREQ_001
- [ ] SYSREQ_003 —Results in→ CREQ_002
- [ ] SYSREQ_004 —Results in→ CREQ_003
- [ ] CREQ_001 —Results in→ UNITREQ_001
- [ ] CREQ_001 —Results in→ UNITREQ_002
- [ ] CREQ_001 —Results in→ UNITREQ_003
- [ ] CREQ_002 —Results in→ UNITREQ_004
- [ ] CREQ_003 —Results in→ UNITREQ_005

### Design output

- [ ] DOUT_018 —Relates to SR→ SYSREQ_001 (and SYSREQ_002–004 if multiple edges allowed)
- [ ] DOUT_018 —Relates to CR→ CREQ_001, CREQ_002, CREQ_003 (as many as UI allows)
- [ ] DOUT_018 —Relates to UR→ UNITREQ_001–005 (as many as UI allows)

### Verification (right of V)

- [ ] SYSREQ_001 —Verified By→ VERIF_001 (and VERIF_001 —Verifies SR→ SYSREQ_001)
- [ ] SYSREQ_002 —Verified By→ VERIF_002
- [ ] SYSREQ_003 —Verified By→ VERIF_003
- [ ] SYSREQ_004 —Verified By→ VERIF_004
- [ ] VERIF_001 —Verifies UR→ UNITREQ_001 (optional but preferred)
- [ ] VERIF_002 —Verifies UR→ UNITREQ_002
- [ ] VERIF_003 —Verifies UR→ UNITREQ_004
- [ ] VERIF_004 —Verifies UR→ UNITREQ_005
- [ ] VERIF_001–004 —Verifies DO→ DOUT_018
- [ ] VERIF_001–004 —Verifies CR→ matching CREQ (001→001, 002→001, 003→002, 004→003) if UI allows

### Validation

- [ ] VALID_001 —Validates→ UREQ_001
- [ ] VALID_002 —Validates→ UREQ_002
- [ ] VALID_001 —Validates DO→ DOUT_018
- [ ] VALID_002 —Validates DO→ DOUT_018
- [ ] VALID\_\* do **not** randomly link to SYSREQ

### Remove bad edges

- [ ] No VERIF_001 ↔ SYSREQ_004
- [ ] No VERIF_004 ↔ SYSREQ_003
- [ ] No SYSREQ ↔ EcoSteam / MedSteril / HydroSter DOs
- [ ] No CREQ_004 / VALID_003 / VALID_004 in the live graph (obsolete or deleted)

---

## 9. Done in CertHub — then stop

When every checkbox above is done:

1. Reply in chat: **CertHub MVP punch list is done** (or similar).
2. The agent will run `make sync`, confirm Sphinx IDs
   (`UREQ_001`–`002`, `UNITREQ_001`–`005`, `DOUT_018`, 3 CREQs, 2 VALIDs),
   then implement Phase 2 (door + cycle states in code, README product section,
   gate hints, Sphinx needflow).
3. After Phase 2 is green, delete this TMP file.

### Spot-check before you ping the agent

- [ ] Record Names all use `PREFIX_NNN — Title`
- [ ] No footprint / 8-tray / infusion-pump / other-product text on Sterilisator records
- [ ] Door = SYSREQ_003 / CREQ_002 / VERIF_003; English UI = SYSREQ_004 / CREQ_003 / VERIF_004
- [ ] VALID → UREQ only (plus DOUT)
- [ ] Product DO Name starts with `DOUT_018 —`
