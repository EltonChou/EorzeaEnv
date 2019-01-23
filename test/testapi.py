import unittest
import os
from EorzeaEnv.EorzeaApi import Xivapi


class TestApi (unittest.TestCase):
    def setUp(self):
        self.Xivapi = Xivapi.Client(os.getenv('XIV_API_KEY'))

    def test_api(self):
        r = self.Xivapi.content()
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main(verbosity=2)
