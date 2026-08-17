from enum import Enum


class AutomaticTraceSource(str, Enum):
    DOCUMENT_CREATION = "document_creation"
    EXTERNAL_FILE_REFERENCE = "external_file_reference"
    GLOBAL_ELEMENT_REFERENCE = "global_element_reference"
    PROCESS_MODELLER = "process_modeller"
    SCHEMA_ASSOCIATION = "schema_association"
    SUBMISSION_CREATION = "submission_creation"
    SUBMISSION_CREATION_FROM_TEMPLATE = "submission_creation_from_template"
    SUBMISSION_TEMPLATE_CREATION = "submission_template_creation"
    TEXT_EDITOR = "text_editor"

    def __str__(self) -> str:
        return str(self.value)
