from enum import Enum


class RequirementUseCase(str, Enum):
    DESIGN_INPUT = "design_input"
    DESIGN_OUTPUT = "design_output"
    REQUIREMENTS = "requirements"
    SYSTEM_REQUIREMENTS = "system_requirements"
    USER_REQUIREMENTS = "user_requirements"
    VALIDATION = "validation"
    VERIFICATION = "verification"

    def __str__(self) -> str:
        return str(self.value)
