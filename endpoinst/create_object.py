import requests

class CreateObject:
    response = None
    response_json = None
    def new_object(self, payload):
        self.response = requests.post("https://api.restful-api.dev/objects", json=payload)
        self.response_json = self.response.json()
