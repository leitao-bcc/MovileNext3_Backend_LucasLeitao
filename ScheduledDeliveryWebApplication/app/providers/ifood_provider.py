import os
import requests

from app.providers.base_provider import BaseProvider


class IfoodProvider(BaseProvider):

    def __init__(self):
        self.host = os.environ.get('IFOOD_ENDPOINT')

    def run(self, path, method, data={}, headers={}):
        url = self.host + path

        response = requests.request(method, url, data=data, headers=headers)

        if response:
            return response.text

        return None

    def get_catalog(self, **kwargs):
        return self.run('/catalog', 'POST', kwargs)

    def get_merchant(self, merchant_id):
        path = '/merchant/' + str(merchant_id)
        return self.run(path, 'GET')

    def login(self, username, password):
        data = {'username': username, 'password': password}
        return self.run('/auth/login', 'POST', data)

    def post_order(self, **kwargs):
        return self.run('/order', 'POST', kwargs)
