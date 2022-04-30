import os
import json
import requests
class Cmc:
    def __init__(self):
        self.base_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.parameters = {
            'start': '1',
            'limit': '10',
            'convert': 'EUR'
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': os.environ.get('CMC_API_KEY')
        }
    def get_all(self):
        response = requests.get(self.base_url, headers=self.headers, params=self.parameters)
        response_json = response.json()
        return response_json['data']

    def get_by_slug(self, slug):
        self.base_url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
        self.parameters ={'slug': slug}
        response = requests.get("https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest", headers=self.headers, params=self.parameters)
        response_json = response.json()
        return response_json['data']