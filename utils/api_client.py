# utils/api_client.py

import requests

class APIClient:

    def get(self, url):

        response = requests.get(url)

        return response

    def post(self, url, payload):

        response = requests.post(
            url,
            data=payload
        )

        return response

    def put(self, url, payload):

        response = requests.put(
            url,
            data=payload
        )

        return response

    def delete(self, url, payload):

        response = requests.delete(
            url,
            data=payload
        )

        return response