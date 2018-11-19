import unittest
from eorzea.EorzeaWeather import EorzeaWeather


class TestForecast (unittest.TestCase):
    def setUp(self):
        self.ew = EorzeaWeather()

    def tearDown(self):
        self.ew = None

    def test_thunder(self):
        weather = self.ew.forecast_next_weather("Eureka Pyros", 1542590000045)
        self.assertEqual(weather, "Thunder")

    def test_umbral_wind(self):
        weather = self.ew.forecast_next_weather("Eureka Pyros", 1542591400045)
        self.assertEqual(weather, "Umbral Wind")

if __name__ == "__main__":
    unittest.main(verbosity=2)
