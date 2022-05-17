from src.data import enums
from src.data.exceptions import BadRequestException


class ValidationService:
    def __init__(self, event):
        self.event = event

    def validate_search(self):
        query_params = self.event.get("queryStringParameters", {})
        if "name" in query_params:
            raise BadRequestException(enums.ErrorMessage.NAME_REQUIRED.value)
        if "owner_id" in query_params:
            raise BadRequestException(enums.ErrorMessage.OWNER_REQUIRED.value)

