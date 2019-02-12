import unittest

from EorzeaEnv import EorzeaTime
from EorzeaEnv import EorzeaWeather


class TestForecast (unittest.TestCase):
    def test_forecast(self):
        pagos_weather = EorzeaWeather.forecast_weather(
            "Eureka Pagos", 1542651599.999
        )
        pyros_weather = EorzeaWeather.forecast_weather(
            "Eureka Pyros", 1542591400.045
        )
        sigma_weather = EorzeaWeather.forecast_weather(
            "Sigmascape V4.0", 1542591400.045
        )
        ember_weather = EorzeaWeather.forecast_weather(
            "Bowl of Embers", 1542591400.045
        )
        ruby_weather = EorzeaWeather.forecast_weather(
            "the ruby sea", 1542591400.045
        )
        sea_weather = EorzeaWeather.forecast_weather(
            "sea of clouds", 1542591400.045
        )
        zero_weather = EorzeaWeather.forecast_weather(
            "asdfUpper aetheroacoustic exploratory sitea dsf",
            1542591400.045,
            strict=False
        )
        hydatos_weather = EorzeaWeather.forecast_weather(
            "Eureka Hydatos", 1542591400.045
        )
        self.assertEqual(pagos_weather, "Fog")
        self.assertEqual(pyros_weather, "Umbral Wind")
        self.assertEqual(sigma_weather, "Dimensional Disruption")
        self.assertEqual(ember_weather, "Heat Waves")
        self.assertEqual(ruby_weather, 'Fair Skies')
        self.assertEqual(sea_weather, 'Fog')
        self.assertEqual(zero_weather, 'Fair Skies')
        self.assertEqual(hydatos_weather, 'Thunderstorms')

    def test_field(self):
        for t in (EorzeaTime.weather_period(10)):
            weather = EorzeaWeather.forecast_weather("Eureka Pyros", t)
            self.assertIsInstance(weather, str)

        with self.assertRaises(KeyError):
            pyros_weather = EorzeaWeather.forecast_weather(
                "EuPyros", 1542591400.045
            )

    def test_localize(self):
        localized_en_weather = EorzeaWeather.forecast_weather(
            "Eureka Pagos",
            1542651599.999,
            lang="en"
        )
        localized_ja_weather = EorzeaWeather.forecast_weather(
            "Eureka Pagos",
            1542651599.999,
            lang="ja"
        )
        localized_de_weather = EorzeaWeather.forecast_weather(
            "Eureka Pagos",
            1542651599.999,
            lang="de"
        )
        localized_fr_weather = EorzeaWeather.forecast_weather(
            "Eureka Pagos",
            1542651599.999,
            lang="fr"
        )
        self.assertEqual(localized_ja_weather, "霧")
        self.assertEqual(localized_fr_weather, "Brouillard")
        self.assertEqual(localized_de_weather, "Neblig")

    def test_step(self):
        timelist = [t for t in EorzeaTime.weather_period(10)]
        self.assertEqual(len(timelist), 10)

    def test_time(self):
        self.assertIsInstance(EorzeaTime.now().minute, int)
        self.assertIsInstance(EorzeaTime.now().hour, int)
        with self.assertRaises(ValueError):
            EorzeaTime(13, 1, 10, 50)
        with self.assertRaises(ValueError):
            EorzeaTime(12, 35, 10, 50)
        with self.assertRaises(ValueError):
            EorzeaTime(12, 1, 25, 50)
        with self.assertRaises(ValueError):
            EorzeaTime(12, 1, 10, 61)
        with self.assertRaises(TypeError):
            EorzeaTime("kappa", 1, 10, 50)

if __name__ == "__main__":
    unittest.main()
