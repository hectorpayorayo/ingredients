import json
from importlib.resources import read_text
import jsonschema
from src.data import schemas


class ValidationService:

    def __init__(self, event):
        self.event = event

    def validate_json_schema(self, schema_name: str):
        """

        :param schema_name:
        :param payload:
        :return:
        """
        schema_body = read_text(
            package=schemas.__package__, resource=f"{schema_name}.json"
        )
        jsonschema.validate(self.event, json.loads(schema_body))
