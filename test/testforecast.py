import unittest

from EorzeaEnv.EorzeaTime import EorzeaTime
from EorzeaEnv.EorzeaWeather import EorzeaWeather


class TestForecast (unittest.TestCase):
    def test_forecast(self):
        pagos_weather = EorzeaWeather.forecast_weather(
            "Eureka Pagos", 1542651599.999)
        pyros_weather = EorzeaWeather.forecast_weather(
            "Eureka Pyros", 1542591400.045)
        self.assertEqual(pagos_weather, "Fog")
        self.assertEqual(pyros_weather, "Umbral Wind")

    def test_field(self):
        for t in (EorzeaTime.weather_period(10)):
            weather = EorzeaWeather.forecast_weather("Eureka Pyros", t)
            self.assertIsInstance(weather, str)

    def test_step(self):
        timelist = [t for t in (EorzeaTime.weather_period(10))]
        self.assertEqual(len(timelist), 10)

    def test_time(self):
        self.assertIsInstance(EorzeaTime.now().minute, int)
        self.assertIsInstance(EorzeaTime.now().hour, int)
        with self.assertRaises(ValueError):
            EorzeaTime(26, 77, 1)
        with self.assertRaises(ValueError):
            EorzeaTime(8, 70, 1)
        with self.assertRaises(TypeError):
            EorzeaTime("kappa", 40, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
