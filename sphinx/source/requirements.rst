Requirements
============

V-model requirements imported from CertHub (SoR): user → system → component →
unit. Sphinx IDs (``SYSREQ_*``, ``UREQ_*``, …) follow the prefixed Name fields.
The stable CertHub identity is ``external_id``.

System Requirements
-------------------

.. include:: generated/system_requirements.rst

.. needtable:: System Requirements catalog
   :filter: type == "sysreq"
   :columns: id;title;req_type;priority;status;justification;external_id
   :style: datatables

User Requirements
-----------------

.. include:: generated/user_requirements.rst

.. needtable:: User Requirements
   :filter: type == "ureq"
   :columns: id;title;priority;status;external_id
   :style: datatables

Component Requirements
----------------------

.. include:: generated/component_requirements.rst

.. needtable:: Component Requirements
   :filter: type == "creq"
   :columns: id;title;status;external_id
   :style: datatables

Unit Requirements
-----------------

.. include:: generated/unit_requirements.rst

.. needtable:: Unit Requirements
   :filter: type == "unitreq"
   :columns: id;title;status;external_id
   :style: datatables
