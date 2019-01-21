import unittest
import os
from EorzeaEnv import EorzeaApi


class TestApi (unittest.TestCase):
    def setUp(self):
        self.xivapi = EorzeaApi.Xivapi(os.getenv('XIV_API_KEY'))

    def test_api(self):
        r = self.xivapi.get('servers')
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main(verbosity=2)
