Release Evidence
================

Gate summary for this build and how it maps to the CertHub Release Record.

Summary
-------

.. include:: generated/certification_summary.rst

Outbound payload
----------------

After ``make show`` / ``make evidence``, see
``certhub/generated/certhub_result.json`` (also copied into ``evidence/``).

================== ============================================================
Trigger            CertHub Release Record
================== ============================================================
PR / main          Artifact only — no POST
RC ``v*-rc*``      Artifact only — no POST
Full ``vX.Y.Z``    POST to Release Record KT (``make push-evidence``)
================== ============================================================

The Release Record stores release number, commit, timestamp, evidence URL,
and a short Notes summary. Machine-readable detail stays in the evidence pack.

Visual charts and the V-model graph live on the :doc:`dashboard`.
