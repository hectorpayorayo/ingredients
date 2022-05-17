import json

from src.handlers import search
from src.services.db import DB


def test_get_ingredients(mocker):
    expected = {
        "ingredients": [
            {"id": 0, "name": "carrot", "owner_id": 111},
            {"id": 2, "name": "apple", "owner_id": None},
            {"id": 3, "name": "onion", "owner_id": 111}
        ]
    }
    describe_db_instances_resource = mocker.patch.object(
        search, "describe_db_instances")
    describe_db_instances_resource.return_value = {
        "DBInstances": [{
            "Endpoint": {
                "Address": "xxxxxxx",
                "Port": 0000
            }
        }]
    }

    mocker.patch.object(DB, 'search_ingredients_by_name')
    DB.search_ingredients_by_name.return_value = [
        {"id": 0, "name": "carrot", "owner_id": 111},
        {"id": 2, "name": "apple", "owner_id": None},
        {"id": 3, "name": "onion", "owner_id": 111}]

    response = search.handler({
        "queryStringParameters":{
            "name": "lemon",
            "owner_id": 111
        }
    }, None)

    assert json.loads(response["body"]) == expected
    assert response["statusCode"] == 200


def test_get_empty_ingredients(mocker):
    expected = {
        "ingredients": []
    }
    describe_db_instances_resource = mocker.patch.object(
        search, "describe_db_instances")
    describe_db_instances_resource.return_value = {
        "DBInstances": [{
            "Endpoint": {
                "Address": "xxxxxxx",
                "Port": 0000
            }
        }]
    }

    mocker.patch.object(DB, 'search_ingredients_by_name')
    DB.search_ingredients_by_name.return_value = []

    response = search.handler({
        "queryStringParameters":{
            "name": "lemon",
            "owner_id": 111
        }
    }, None)

    assert json.loads(response["body"]) == expected
    assert response["statusCode"] == 200


def test_validation_error(mocker):
    expected = {
        "message": "owner_id field must be numeric"
    }

    response = search.handler({
        "queryStringParameters":{
            "name": "lemon",
            "owner_id": "aaaaa"
        }
    }, None)

    assert json.loads(response["body"]) == expected
    assert response["statusCode"] == 400


def test_validation_error_empty_field(mocker):
    expected = {
        "message": "name field is required"
    }

    response = search.handler({
        "queryStringParameters":{
            "owner_id": "aaaaa"
        }
    }, None)

    assert json.loads(response["body"]) == expected
    assert response["statusCode"] == 400