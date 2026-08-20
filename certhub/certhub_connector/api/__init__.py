"""CertHub API boundary.

- ``clients/`` — generated attrs HTTP stubs (``openapi-python-client``), public
  ``x-public`` operations only. Do not edit; regenerate with ``make generate-api``.
- ``api_models/`` — generated Pydantic models (``datamodel-code-generator``) for
  Tech Doc and Records response/request bodies.
- ``client`` — thin wrappers that call the attrs clients and return Pydantic
  models (or a raw Tracer ``results`` dict). Never expose attrs types upward.
- ``filter_public`` — OpenAPI filter used by the Makefile before codegen.
"""

from certhub_connector.api.client import RecordsClient, TechDocClient, TracerClient

__all__ = ["RecordsClient", "TechDocClient", "TracerClient"]
