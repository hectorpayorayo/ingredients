import json
from http import HTTPStatus

from aws_lambda_powertools import Logger

from src.data import enums
from src.services import validation
from src.services.config import ConfigService
from src.services.response import ResponseService

conf_service = ConfigService()
logger = Logger(service=conf_service.LOGGER_NAME)


@ResponseService.pretty_response
def handler(event, _):
    logger.info({"message": "Event information", "event_info": event})

    validate_service = validation.ValidationService(event)
    validate_service.validate_json_schema(enums.SchemaNames.SEARCH.value)

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
    }

    return HTTPStatus.OK, body
