import pytest
from EorzeaEnv import EorzeaLang, EorzeaTime, EorzeaWeather


class TestForecast:
    def test_forecast(self):
        assert EorzeaWeather.forecast(
            'Eureka Pagos', 1542651599.999
        ) == 'Fog'
        assert EorzeaWeather.forecast(
            'Eureka Pyros', 1542591400.045
        ) == 'Umbral Wind'
        assert EorzeaWeather.forecast(
            'Sigmascape V4.0', 1542591400.045
        ) == 'Dimensional Disruption'
        assert EorzeaWeather.forecast(
            'Bowl of Embers', 1542591400.045
        ) == 'Heat Waves'
        assert EorzeaWeather.forecast(
            'the ruby sea', 1542591400.045
        ) == 'Fair Skies'
        assert EorzeaWeather.forecast(
            'sea of clouds', 1542591400.045
        ) == 'Fog'
        assert EorzeaWeather.forecast(
            'asdfUpper aetheroacoustic exploratory sitea dsf',
            1542591400.045,
            strict=False
        ) == 'Fair Skies'

    def test_field(self):
        weathers = EorzeaWeather.forecast(
            'Eureka Pyros', EorzeaTime.weather_period(10))

        for weather in weathers:
            assert isinstance(weather, str)

        with pytest.raises(ValueError):
            pyros_weather = EorzeaWeather.forecast(
                'EuPyros', 1542591400.045
            )

    def test_localize(self):
        assert EorzeaWeather.forecast(
            'Eureka Pagos',
            1542651599.999,
            lang=EorzeaLang.EN
        ) == 'Fog'
        assert EorzeaWeather.forecast(
            'Eureka Pagos',
            1542651599.999,
            lang=EorzeaLang.JA
        ) == '霧'
        assert EorzeaWeather.forecast(
            'Eureka Pagos',
            1542651599.999,
            lang=EorzeaLang.DE
        ) == 'Neblig'
        assert EorzeaWeather.forecast(
            'Eureka Pagos',
            1542651599.999,
            lang=EorzeaLang.FR
        ) == 'Brouillard'
