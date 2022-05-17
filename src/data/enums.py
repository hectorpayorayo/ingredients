from enum import unique, Enum


@unique
class ErrorMessage(Enum):
    OWNER_REQUIRED = "owner_id field is required"
    NAME_REQUIRED = "name field is required"
