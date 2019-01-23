import requests


API_BASE = 'https://xivapi.com/'


class Client:

    __slots__ = 'api_key'

    def __init__(self, api_key):
        self.api_key = api_key

    @property
    def key(self):
        return {'key': self.api_key}

    def get(self, endpoint, params={}):
        url = request_url(endpoint)
        r = requests.get(url, params={**self.key, **params})
        return r

    def search(self, **kwargs):
        return self.get('search', kwargs)

    def lore(self, string):
        return self.get('lore', {"string": string})

    def content(self, content=None, **kwargs):
        if not content:
            return self.get('content')

        return self.get(content, params=kwargs)

    def schema(self, content):
        return self.get('{}/schema'.format(content))

    def servers(self):
        return self.get('servers')

    def servers_dc(self):
        return self.get('servers/dc')

    def character(self, id, **kwargs):
        return self.get('character/{}'.format(id), params=kwargs)

    def character_search(self, name, server=None, page=None):
        params = {
            "name": name,
            "server": server,
            "page": page
        }
        return self.get('character/search', params=params)

    def character_verification(self, id):
        return self.get('character/{}/verification'.format(id))

    def character_update(self, id):
        return self.get('character/{}/update'.format(id))

    def freecompany(self, id, **kwargs):
        return self.get('freecompany/{}'.format(id))

    def freecompany_search(self, name, server=None, page=None):
        params = {
            "name": name,
            "server": server,
            "page": page
        }
        return self.get('freecompany/search', params=params)

    def linkshell(self, id, **kwargs):
        return self.get('linkshell/{}'.format(id))

    def linkshell_search(self, name, server=None, page=None):
        params = {
            "name": name,
            "server": server,
            "page": page
        }
        return self.get('linkshell/search')

    def pvpteam(self, id):
        return self.get('pvpteam/{}'.format(id))

    def pvpteam_search(self, name, server=None, page=None):
        params = {
            "name": name,
            "server": server,
            "page": page
        }
        return self.get('pvpteam/search')

    def market_price(self, server, item_id):
        return self.get('market/{}/items/{}'.format(server, item_id))

    def market_price_history(self, server, item_id):
        return self.get('market/{}/items/{}/history'.format(server, item_id))

    def market_category(self, server, category_id):
        return self.get('market/{}/category/{}'.format(server, category_id))

    def market_categories(self):
        return self.get('market/categories')

    def patchlist(self):
        return self.get('patchlist')


def request_url(endpoint):
    return '{}{}'.format(API_BASE, endpoint)
