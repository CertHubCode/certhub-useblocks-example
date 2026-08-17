from enum import Enum


class RelationType(str, Enum):
    AUTO_BASED_ON_SCHEMA = "auto_based_on_schema"
    AUTO_BASED_ON_SUBMISSION_TEMPLATE = "auto_based_on_submission_template"
    AUTO_BASED_ON_TEMPLATE = "auto_based_on_template"
    AUTO_DOCUMENT_PART_OF_SUBMISSION = "auto_document_part_of_submission"
    AUTO_REFERENCED_BY_DOMAIN_OBJECT = "auto_referenced_by_domain_object"
    AUTO_REFERENCED_DOMAIN_OBJECT_CONTAINS_EXTERNAL_FILE = (
        "auto_referenced_domain_object_contains_external_file"
    )
    AUTO_REFERENCED_EXTERNAL_FILE = "auto_referenced_external_file"
    AUTO_REFERENCED_GLOBAL_ELEMENT = "auto_referenced_global_element"
    AUTO_REFERENCED_IN_PROCESS_MODELLER = "auto_referenced_in_process_modeller"
    AUTO_REFERENCED_IN_TEXT_EDITOR = "auto_referenced_in_text_editor"
    AUTO_REFERENCED_PRODUCT_DATA_COLLECTION = "auto_referenced_product_data_collection"
    AUTO_SCHEMA_FOR = "auto_schema_for"
    AUTO_SUBMISSION_CONTAINS_DOCUMENT = "auto_submission_contains_document"
    AUTO_SUBMISSION_TEMPLATE_CONTAINS_TEMPLATE = (
        "auto_submission_template_contains_template"
    )
    AUTO_TEMPLATE_PART_OF_SUBMISSION_TEMPLATE = (
        "auto_template_part_of_submission_template"
    )
    CONNECTED_WITHIN_USE_CASE = "connected_within_use_case"
    CONTRIBUTES_TO = "contributes_to"
    HAS_PARENT = "has_parent"
    IS_MENTIONED_BY = "is_mentioned_by"
    IS_PARENT = "is_parent"
    IS_RELATED = "is_related"
    MENTIONS = "mentions"

    def __str__(self) -> str:
        return str(self.value)
