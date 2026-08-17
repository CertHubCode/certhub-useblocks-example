Verification
============

CertHub verification activities and the pytest / JUnit execution for this build.

Verification definitions
------------------------

Imported from CertHub (``VERIF_*``). Each activity ``verifies`` design inputs.

.. include:: generated/verifications.rst

.. needtable:: Verification catalog
   :filter: type == "verif"
   :columns: id;title;status;verifies;links
   :style: datatables

Execution report
----------------

JUnit from ``reports/junit.xml`` (Sphinx-Test-Reports).

.. test-report:: Sterilisator 20A pytest report
   :id: TR_STERILISATOR_20A
   :file: reports/junit.xml
   :tags: pytest;samd

Execution hierarchy
-------------------

.. needflow:: Test report structure
   :filter: type in ["testfile", "testsuite", "testcase"]
   :show_legend:
