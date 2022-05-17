from src.services.config import ConfigService
conf_service = ConfigService()


def describe_db_instances():
    return conf_service.rds_client.describe_db_instances(
        DBInstanceIdentifier=conf_service.DB_INSTANCE_IDENTIFIER
    )


