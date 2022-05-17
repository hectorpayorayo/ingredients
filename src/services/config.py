import os
import boto3


class ConfigService:
    def __init__(self):
        self.DB_NAME: str = os.getenv("DB_NAME")
        self.DB_USERNAME: str = os.getenv("DB_USERNAME")
        self.DB_USER_PASSWORD: str = os.getenv("DB_USER_PASSWORD")
        self.LOGGER_SERVICE_NAME: str = os.getenv("LOGGER_SERVICE_NAME")
        self.DB_INSTANCE_IDENTIFIER = os.getenv("DB_INSTANCE_IDENTIFIER")
        self.rds_client = boto3.client('rds')
