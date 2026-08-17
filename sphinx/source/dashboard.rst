Assurance Dashboard
===================

Management view of the certification gate for this build. Drill into
:doc:`requirements`, :doc:`design-output`, :doc:`verification`, :doc:`validation`,
:doc:`traceability`, or :doc:`release-evidence` for detail.

What this pack is for (medical device)
--------------------------------------

**Sterilisator 20A** is the example **SaMD** (Software as a Medical Device) under
test. This HTML pack is the **engineering evidence twin** for one git baseline:
controlled design inputs from CertHub, linked to implementation and automated
verification.

.. list-table:: Regulatory meaning of this evidence pack
   :header-rows: 1
   :widths: 28 72

   * - Regulatory use
     - Meaning in this dashboard
   * - **Design / development evidence**
       (legacy **DHF**; ISO 13485 **DDF** §7.3.10; EU MDR Annex II design / V&V)
     - The chain SYSREQ → Design Output → CodeLinks → VERIF → JUnit proves
       *this build was designed and verified* — not the full risk file, CER,
       or GSPR checklist.
   * - **Per-release production record**
       (legacy **DHR**; ISO 13485 §7.5 production / release records)
     - On full tag ``vX.Y.Z``, the gate result posts to CertHub **Release
       Record** (version, commit, evidence URL, Notes): thin proof that this
       software unit was released green.
   * - **Not in this pack**
     - Risk (ISO 14971), GSPR, clinical evaluation, labeling, PMS / PMCF, and
       formal approvals stay in **CertHub**. Detail:
       ``docs/regulatory-gap-analysis.md``.

.. admonition:: Regulatory boundary
   :class: note

   Auditors use this pack to answer: *for this baseline, which requirement is
   implemented where, and which test passed?* Controlled regulatory content and
   release authorization live in CertHub — this dashboard does not replace a
   full Technical Documentation or Device History File.

Gate status
-----------

.. include:: generated/certification_summary.rst

KPIs
----

================ ============================================================
Measure          Value
================ ============================================================
System Reqs      :need_count:`type == "sysreq" and is_need`
Design Output    :need_count:`type == "dout" and is_need`
Verification     :need_count:`type == "verif" and is_need`
Validation       :need_count:`type == "valid" and is_need`
Executed         :need_count:`type == "testcase" and is_need`
Failed share     :need_count:`type == "testcase" and result == "failure" ? type == "testcase"`
================ ============================================================

Validation (non-blocking)
-------------------------

``VALID_*`` protocols are **manual evidence in CertHub**. They appear in this
pack for completeness. They do **not** close the SYSREQ → VERIF engineering
gate (KPI: N/A / manual). See :doc:`validation`.

Execution results
-----------------

.. needpie:: Executed tests by result
   :labels: Passed, Failed, Skipped
   :legend:
   :colors: green,red,yellow

   type == "testcase" and result == "passed"
   type == "testcase" and result == "failure"
   type == "testcase" and result == "skipped"

Artifact inventory
------------------

.. needbar:: Needs by type
   :xlabels: sysreq, dout, verif, valid
   :ylabels: count
   :legend:

   type == "sysreq", type == "dout", type == "verif", type == "valid"

Traceability flow
-----------------

System Requirement → Design Output → Verification (``links`` / ``verifies``).

.. needflow:: V-model excerpt
   :filter: type in ["sysreq", "dout", "verif", "valid"]
   :link_types: links, verifies, validates
   :show_link_names:
   :show_legend:

System Requirements overview
----------------------------

.. needtable:: System Requirements
   :filter: type == "sysreq"
   :columns: id;title;priority;status;external_id
   :style: datatables

Further reading
---------------

* :doc:`requirements` — requirement hierarchy (User → System → Component → Unit)
* :doc:`design-output` — design outputs and CodeLinks to source
* :doc:`verification` — verification activities and JUnit results
* :doc:`validation` — validation protocols
* :doc:`traceability` — linked needflow graph, matrices, CodeLinks, gap legend
* :doc:`release-evidence` — outbound Release Record payload
