import json
from http import HTTPStatus

from aws_lambda_powertools import Logger

from src.services import validation
from src.services.config import ConfigService
from src.services.db import DB
from src.services.util import describe_db_instances
from src.services.response import ResponseService

conf = ConfigService()
logger = Logger(service=conf.LOGGER_SERVICE_NAME)


@ResponseService.pretty_response
def handler(event, _):
    logger.info({"message": "Event information", "event_info": event})

    validate_service = validation.ValidationService(event)
    validate_service.validate_search()
    name = event.get("queryStringParameters", {}).get("name", "")
    owner_id = event.get("pathParameters").get("owner_id")

    response = describe_db_instances()
    endpoint = response["DBInstances"][0].get("Endpoint", {})

    db = DB(db_name=conf.DB_NAME, host=endpoint.get("Address"), port=endpoint.get("Port"),
            username=conf.DB_USERNAME, password=conf.DB_USER_PASSWORD)

    items = db.search_ingredients_by_name(name=name, owner_id=owner_id)
    response = []
    for item in items:
        response.append({
            "id": item["id"],
            "name": item["name"],
            "owner_id": item["owner_id"]
        })

    return HTTPStatus.OK, {
            "ingredients": response
        }
