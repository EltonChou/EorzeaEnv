import unittest
import os
from EorzeaEnv import EorzeaApi


class TestApi (unittest.TestCase):
    def setUp(self):
        self.xivapi = EorzeaApi.Client(os.getenv('XIV_API_KEY'))

    def test_api(self):
        r = self.xivapi.get('servers')
        print(r.status_code)
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main(verbosity=2)
