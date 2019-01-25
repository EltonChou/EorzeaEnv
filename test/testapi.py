import unittest
import os
from EorzeaEnv.EorzeaApi import XivApi


class TestApi (unittest.TestCase):
    def setUp(self):
        self.xivapi = XivApi.Client(os.getenv('XIV_API_KEY'), test_mode=True)

    def test_api(self):
        r = self.xivapi.content()
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main(verbosity=2)
