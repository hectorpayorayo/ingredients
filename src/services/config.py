import os

import boto3


class ConfigService:
    def __init__(self):
        self.DB_NAME: str = os.getenv("DB_NAME")
        self.DB_USERNAME: str = os.getenv("DB_USERNAME")
        self.DB_USER_PASSWORD: str = os.getenv("DB_USER_PASSWORD")
        self.DB_PORT: str = 5432
        self.DB_INSTANCE_IDENTIFIER = os.getenv("DB_INSTANCE_IDENTIFIER")
        self.rds_client = boto3.client('rds')


