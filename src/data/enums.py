from enum import unique, Enum


@unique
class ErrorMessage(Enum):
    OWNER_REQUIRED = "owner_id field is required"
    OWNER_NUMERIC = "owner_id field must be numeric"
    NAME_REQUIRED = "name field is required"
