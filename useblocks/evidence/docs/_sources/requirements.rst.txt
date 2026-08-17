Requirements
============

System Requirements imported from CertHub (SoR). Sphinx IDs (``SYSREQ_*``) follow
the requirement topic number. The stable CertHub identity is ``external_id``.

.. include:: generated/system_requirements.rst

Overview
--------

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
