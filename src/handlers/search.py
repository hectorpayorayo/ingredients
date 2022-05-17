import json
from http import HTTPStatus

from aws_lambda_powertools import Logger

from src.data import enums
from src.services import validation
from src.services.config import ConfigService
from src.services.util import describe_db_instances
from src.services.response import ResponseService

conf_service = ConfigService()
logger = Logger(service=conf_service.LOGGER_SERVICE_NAME)


@ResponseService.pretty_response
def handler(event, _):
    logger.info({"message": "Event information", "event_info": event})

    validate_service = validation.ValidationService(event)
    validate_service.validate_json_schema(enums.SchemaNames.SEARCH.value)

    query_params = event.get("queryStringParameters", {})
    name = query_params.get("name", "")
    path_params = event.get("pathParameters", {})
    owner_id = path_params.get("owner_id", "")

    response = describe_db_instances()
    logger.info({"message": "RDS", "info": response})
    endpoint = response["DBInstances"][0].get("Endpoint", {})

    body = {
        "owner_id": owner_id,
        "name": name,
        "host": endpoint.get("Address"),
        "port": endpoint.get("Port")
    }

    return HTTPStatus.OK, body
