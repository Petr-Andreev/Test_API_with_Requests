import requests
from endpoinst.base_endpoint import Endpoint

class UpdateObject(Endpoint):

    def update_by_id(self, object_id, payload):
        self.response = requests.put(
            f"https://api.restful-api.dev/objects/{object_id}",
            json=payload)
        self.response_json = self.response.json()

    def check_response_payload(self, name, data):
        assert self.response_json['name'] == name
        assert self.response_json['data'] == data
