import pytest
from EorzeaEnv import EorzeaLang, EorzeaTime, EorzeaWeather
from EorzeaEnv.errors import InvalidEorzeaPlaceName


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
            'sea of clouds', 1542591400
        ) == 'Fog'
        assert EorzeaWeather.forecast(
            'asdfUpper aetheroacoustic exploratory sitea dsf',
            1542591400.045,
            strict=False
        ) == 'Fair Skies'

        with pytest.raises(TypeError):
            EorzeaWeather.forecast(
                'sea of clouds', '1542591400'  # type: ignore
            )

    def test_field(self):
        weathers = EorzeaWeather.forecast(
            'Eureka Pyros', EorzeaTime.weather_period(10))

        for weather in weathers:
            assert isinstance(weather, str)

        with pytest.raises(ValueError):
            EorzeaWeather.forecast(
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

    def test_placename_error(self):
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaWeather.forecast('!!!!!!!!!!!!!!', 145354.99, strict=True)

        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaWeather.forecast('kadsf', 1214, strict=False)

    def test_cutoff_setter(self):
        EorzeaWeather.set_fuzzy_cutoff(50)
        assert EorzeaWeather.FUZZY_CUTOFF == 50

        with pytest.raises(ValueError):
            EorzeaWeather.set_fuzzy_cutoff(500)

    def test_get_weather_name_by_weather_index_and_lang(self):
        weather = EorzeaWeather.get_weather(index=10, lang=EorzeaLang.JA)
        assert weather == "雷雨"

    def test_get_weather_result_as_raw_value(self):
        raw_weather = EorzeaWeather.forecast(
            'Eureka Pagos',
            1542651599.999,
            raw=True
        )
        assert raw_weather == 4
