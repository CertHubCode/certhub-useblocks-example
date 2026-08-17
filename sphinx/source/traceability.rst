Traceability
============

Cross-cutting view of the V-model chain for this build:

::

    System Requirement → Design Output → Verification → Automated result
    User Requirement ← Validation

Gap states (from the certification gate)
----------------------------------------

================ ============================================================
Status           Meaning
================ ============================================================
verified         Design Output + CodeLinks impl + passing verification
not_implemented  Design Output linked but no CodeLinks marker on DOUT
not_tested       Implemented but no linked VERIF / JUnit property
failed           Linked verification executed and failed
missing_dout     System requirement has no linked Design Output
================ ============================================================

Traceability graph
------------------

Linked V-model graph (edges from ``links`` / ``verifies`` / ``validates``).
Orphan previous-generation Design Outputs are excluded so the sterilizer chain
stays readable.

.. needflow:: Traceability graph
   :filter: type in ["sysreq", "verif", "valid"] or id in ["DOUT_001", "DOUT_002", "DOUT_003", "DOUT_004", "DOUT_018"]
   :link_types: links, verifies, validates
   :show_link_names:
   :show_legend:

System Requirement ↔ Design Output → code
-------------------------------------------

.. needtable:: System Requirements
   :filter: type == "sysreq"
   :columns: id;title;status
   :style: datatables

.. needtable:: Design Output → inputs and code
   :filter: type == "dout" and id in ["DOUT_001", "DOUT_002", "DOUT_003", "DOUT_004", "DOUT_018"]
   :columns: id;title;links;impl-file;local-url;remote-url
   :style: datatables

Design Output → implementation
--------------------------------

CodeLinks ``needextend`` rows (``impl-file``, ``local-url``, ``remote-url``):

.. include:: generated/codelinks_needextend.rst

Verification → System Requirement
---------------------------------

.. needtable:: Verifications
   :filter: type == "verif"
   :columns: id;title;verifies;links;impl-file;local-url;remote-url
   :style: datatables

Validation → User Requirement
-----------------------------

.. needtable:: Validations
   :filter: type == "valid"
   :columns: id;title;links
   :style: datatables

Verification → executed result
--------------------------------

.. needtable:: Executed results linked to CertHub verification
   :filter: type == "testcase"
   :columns: id;title;result;certhub_test;links
   :style: datatables
   :style_row: tr_[[copy("result")]]
