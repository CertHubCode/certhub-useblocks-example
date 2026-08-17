from enum import Enum


class NodeType(str, Enum):
    DOCUMENT = "Document"
    EXTERNALFILE = "ExternalFile"
    FILE = "File"
    FORM = "Form"
    GLOBALELEMENT = "GlobalElement"
    KNOWLEDGETOPIC = "KnowledgeTopic"
    KNOWLEDGETOPICSCHEMA = "KnowledgeTopicSchema"
    KNOWLEDGEUNIT = "KnowledgeUnit"
    KNOWLEDGEUNITSCHEMA = "KnowledgeUnitSchema"
    PRODUCT = "Product"
    PRODUCTFAMILY = "ProductFamily"
    RECORD = "Record"
    SOP = "SOP"
    SUBMISSION = "Submission"
    SUBMISSIONTEMPLATE = "SubmissionTemplate"
    TEMPLATE = "Template"
    WORKINSTRUCTION = "WorkInstruction"

    def __str__(self) -> str:
        return str(self.value)
