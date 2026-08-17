Sterilisator 20A — Assurance Evidence
=====================================

CertHub is the certification system of record. This HTML pack is the
**engineering twin**: V-Model content synchronized into Sphinx-Needs, linked to
implementation and automated verification, packaged as release evidence.

Evidence tiers
--------------

============= ======================================== ===================
Stage         What this pack proves                    CertHub write-back
============= ======================================== ===================
Everyday / PR Engineering gate + CI artifact           No
RC tag        Same evidence rehearsal                  No
Full release  Same evidence + Release Record POST      Yes (``vX.Y.Z``)
============= ======================================== ===================

**Start here:** :doc:`dashboard`

.. toctree::
   :maxdepth: 1
   :caption: Assurance pack

   dashboard
   requirements
   design-output
   verification
   validation
   traceability
   release-evidence
