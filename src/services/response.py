import json

from aws_lambda_powertools import Logger
from fastjsonschema import JsonSchemaException

from src.services.config import ConfigService

conf_service = ConfigService()
logger = Logger(service=conf_service.LOGGER_NAME)


class ResponseService:
    @staticmethod
    def pretty_response(func):
        """
        Decorator which generates the response to the api gateway request in json format
        :param func:
        :return:
        """
        def wrap(*args, **kwargs):
            headers = {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json",
                'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload'
            }
            try:
                status_code, response = func(*args, **kwargs)
            except JsonSchemaException as ex:
                logger.info({"message": "BadRequest ERROR", "exception": str(ex)})
                status_code = 400
                response = {'message': str(ex)}
            response = json.dumps(response)
            return {"statusCode": status_code,  "headers": headers, "body": response}
        return wrap
