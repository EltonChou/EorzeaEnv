import unittest
from EorzeaEnv.EorzeaWeather import EorzeaWeather
from EorzeaEnv.EorzeaTime import EorzeaTime


class TestForecast (unittest.TestCase):
    def setUp(self):
        self.ew = EorzeaWeather()
        self.et = EorzeaTime()

    def tearDown(self):
        self.ew = None
        self.et = None

    def test_thunder(self):
        weather = self.ew.forecast_weather("Eureka Pagos", 1542651599.999)
        self.assertEqual(weather, "Fog")

    def test_umbral_wind(self):
        weather = self.ew.forecast_weather("Eureka Pyros", 1542591400.045)
        self.assertEqual(weather, "Umbral Wind")

    def test_pyros(self):
        weather = self.ew.forecast_weather(
            "Eureka Pyros", self.et.next_weather_period_start(1)[0])
        self.assertEqual(weather, "Snow")

    def test_list_len(self):
        self.assertEqual(len(self.et.next_weather_period_start()), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
