from enum import Enum


class InputType(str, Enum):
    CHECKBOX = "checkbox"
    CHECKLIST = "checklist"
    DATE = "date"
    DATETIME = "datetime"
    NUMBER = "number"
    RADIO = "radio"
    SELECT = "select"
    TAGLIST = "taglist"
    TEXTAREA = "textarea"
    TEXTFIELD = "textfield"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
