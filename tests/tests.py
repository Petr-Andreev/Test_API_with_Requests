import requests
import pytest

from endpoinst.create_object import CreateObject
from endpoinst.get_object import GetObject
from endpoinst.update_object import UpdateObject
from endpoinst.delete_object import DeleteObject

payload = {
        "name": "Apple MacBook Pro 21",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "M3",
            "Hard disk size": "1 TB"
        }
    }


def test_create_object():
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(payload['name'])


def test_get_object(obj_id):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_id(obj_id)
    get_obj_endpoint.check_response_is_200()

def test_update_object(obj_id):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_by_id(obj_id, payload)
    update_object_endpoint.check_response_payload(payload['name'], payload['data'])
    update_object_endpoint.check_response_is_200()


def test_delete_object(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_by_id(obj_id)
    delete_object_endpoint.check_response_is_200()
    get_object_endpoint = GetObject()
    get_object_endpoint.get_by_id(obj_id)
    get_object_endpoint.check_response_is_404()
