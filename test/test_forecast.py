from unittest import mock

import pytest

from EorzeaEnv import EorzeaLang, EorzeaPlaceName, EorzeaTime, EorzeaWeather
from EorzeaEnv.errors import WeatherRateDataError


class MockDict(dict):
    def __getitem__(self, __k):
        return ()


class TestForecast:
    def test_legacy_forecast(self):
        assert (
            EorzeaWeather.forecast(EorzeaPlaceName("sea of clouds"), 1542591400)
            == "Fog"
        )
        assert EorzeaWeather.forecast("sea of clouds", EorzeaTime(1542591400)) == "Fog"

    def test_forecast(self):
        assert (
            EorzeaWeather.forecast(
                EorzeaPlaceName("Eureka Pagos"), EorzeaTime(1542651599.999)
            )
            == "Fog"
        )
        assert (
            EorzeaWeather.forecast(
                EorzeaPlaceName("Eureka Pyros"), EorzeaTime(1542591400.045)
            )
            == "Umbral Wind"
        )
        assert (
            EorzeaWeather.forecast(
                EorzeaPlaceName("Sigmascape V4.0"), EorzeaTime(1542591400.045)
            )
            == "Dimensional Disruption"
        )
        assert (
            EorzeaWeather.forecast(
                EorzeaPlaceName("Bowl of Embers"), EorzeaTime(1542591400.045)
            )
            == "Heat Waves"
        )
        assert (
            EorzeaWeather.forecast(
                EorzeaPlaceName("the ruby sea"), EorzeaTime(1542591400.045)
            )
            == "Fair Skies"
        )
        assert (
            EorzeaWeather.forecast(
                EorzeaPlaceName("sea of clouds"), EorzeaTime(1542591400)
            )
            == "Fog"
        )
        assert (
            EorzeaWeather.forecast(
                EorzeaPlaceName(
                    "asdfUpper aetheroacoustic exploratory sitea dsf", strict=False
                ),
                EorzeaTime(1542591400.045),
                strict=False,
            )
            == "Fair Skies"
        )

        with pytest.raises(TypeError):
            EorzeaWeather.forecast(
                EorzeaPlaceName("sea of clouds"), "1542591400"  # type: ignore
            )

    def test_field(self):
        weathers = EorzeaWeather.forecast(
            EorzeaPlaceName("Eureka Pyros"), EorzeaTime.weather_period(10)
        )

        for weather in weathers:
            assert isinstance(weather, str)

    def test_localize(self):
        eureka_pagos = EorzeaPlaceName("Eureka Pagos")
        assert (
            EorzeaWeather.forecast(
                eureka_pagos, EorzeaTime(1542651599.999), lang=EorzeaLang.EN
            )
            == "Fog"
        )
        assert (
            EorzeaWeather.forecast(
                eureka_pagos, EorzeaTime(1542651599.999), lang=EorzeaLang.JA
            )
            == "霧"
        )
        assert (
            EorzeaWeather.forecast(
                eureka_pagos, EorzeaTime(1542651599.999), lang=EorzeaLang.DE
            )
            == "Neblig"
        )
        assert (
            EorzeaWeather.forecast(
                eureka_pagos, EorzeaTime(1542651599.999), lang=EorzeaLang.FR
            )
            == "Brouillard"
        )

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
            EorzeaPlaceName("Eureka Pagos"), EorzeaTime(1542651599.999), raw=True
        )
        assert raw_weather == 4

    @mock.patch("EorzeaEnv.eorzea_weather._weather_rate", MockDict())
    def test_weather_data_missing(self):
        with pytest.raises(WeatherRateDataError):
            EorzeaWeather.forecast(
                EorzeaPlaceName("Eureka Pagos"), EorzeaTime(1542651599.999), raw=True
            )
