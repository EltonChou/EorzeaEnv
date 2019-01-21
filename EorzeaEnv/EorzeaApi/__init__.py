import requests

API_BASE = 'https://xivapi.com/'


class Client:

    __slots__ = 'api_key', 'language'

    def __init__(self, api_key, language='en'):
        self.api_key = api_key
        self.language = language

    @property
    def params(self):
        return {
            'key': self.api_key,
            'language': self.language
        }

    def get(self, endpoint):
        url = request_url(endpoint)
        r = requests.get(url, params=self.params)
        return r


def request_url(endpoint):
    return "{}{}".format(API_BASE, endpoint)
