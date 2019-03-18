import pytest

from EorzeaEnv import EorzeaTime
from EorzeaEnv import EorzeaWeather


class TestForecast:
    def test_forecast(self):
        assert EorzeaWeather.forecast_weather(
            'Eureka Pagos', 1542651599.999
        ) == 'Fog'
        assert EorzeaWeather.forecast_weather(
            'Eureka Pyros', 1542591400.045
        ) == 'Umbral Wind'
        assert EorzeaWeather.forecast_weather(
            'Sigmascape V4.0', 1542591400.045
        ) == 'Dimensional Disruption'
        assert EorzeaWeather.forecast_weather(
            'Bowl of Embers', 1542591400.045
        ) == 'Heat Waves'
        assert EorzeaWeather.forecast_weather(
            'the ruby sea', 1542591400.045
        ) == 'Fair Skies'
        assert EorzeaWeather.forecast_weather(
            'sea of clouds', 1542591400.045
        ) == 'Fog'
        assert EorzeaWeather.forecast_weather(
            'asdfUpper aetheroacoustic exploratory sitea dsf',
            1542591400.045,
            strict=False
        ) == 'Fair Skies'
        assert EorzeaWeather.forecast_weather(
            'Eureka Hydatos', 1542591400.045
        ) == 'Thunderstorms'

    def test_field(self):
        for t in (EorzeaTime.weather_period(10)):
            weather = EorzeaWeather.forecast_weather('Eureka Pyros', t)
            assert isinstance(weather, str)

        with pytest.raises(KeyError):
            pyros_weather = EorzeaWeather.forecast_weather(
                'EuPyros', 1542591400.045
            )

    def test_localize(self):
        assert EorzeaWeather.forecast_weather(
            'Eureka Pagos',
            1542651599.999,
            lang='en'
        ) == 'Fog'
        assert EorzeaWeather.forecast_weather(
            'Eureka Pagos',
            1542651599.999,
            lang='ja'
        ) == '霧'
        assert EorzeaWeather.forecast_weather(
            'Eureka Pagos',
            1542651599.999,
            lang='de'
        ) == 'Neblig'
        assert EorzeaWeather.forecast_weather(
            'Eureka Pagos',
            1542651599.999,
            lang='fr'
        ) == 'Brouillard'
