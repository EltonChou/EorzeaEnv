from datetime import datetime

from EorzeaEnv import EorzeaPlaceName, EorzeaRainbow, EorzeaTime, EorzeaWeather

_WEATHER_INTERVAL = 1400
_EASTERN_LA_NOSCEA = "Eastern La Noscea"
_FIELDS_OF_GLORY = "a future rewritten"


class TestRainbowPlaceName:
    def test_place_name_property(self):
        place = EorzeaPlaceName(_EASTERN_LA_NOSCEA)
        assert EorzeaRainbow(place).place_name is place


class TestRainbowIsPossible:
    def test_is_possible_for_valid_place(self):
        assert EorzeaRainbow(EorzeaPlaceName(_EASTERN_LA_NOSCEA)).is_possible

    def test_is_not_possible_for_non_rainy_place(self):
        assert not EorzeaRainbow(EorzeaPlaceName(_FIELDS_OF_GLORY)).is_possible


class TestRainbowForecast:
    def test_forecast_returns_none_for_impossible_place(self):
        rainbow = EorzeaRainbow(EorzeaPlaceName(_FIELDS_OF_GLORY))
        for et in EorzeaTime.weather_period(step=5, from_=0.0):
            assert rainbow.forecast(et) is None

    def test_forecast_returns_bell_6_when_rainbow_appears(self):
        place = EorzeaPlaceName(_EASTERN_LA_NOSCEA)
        rainbow = EorzeaRainbow(place)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            result = rainbow.forecast(et)
            if result is not None:
                assert result.bell == 6
                break

    def test_forecast_returns_none_when_current_is_rainy(self):
        from EorzeaEnv.special_weathers.rainbow import RAINY_WEATHERS

        place = EorzeaPlaceName(_EASTERN_LA_NOSCEA)
        rainbow = EorzeaRainbow(place)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(place, et, raw=True)
            if raw in RAINY_WEATHERS:
                assert rainbow.forecast(et) is None
                break

    def test_forecast_returns_none_when_prev_not_rainy(self):
        from EorzeaEnv.special_weathers.rainbow import RAINY_WEATHERS

        place = EorzeaPlaceName(_EASTERN_LA_NOSCEA)
        rainbow = EorzeaRainbow(place)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(place, et, raw=True)
            prev_raw = EorzeaWeather.forecast(
                place,
                EorzeaTime(et.get_unix_time() - _WEATHER_INTERVAL),
                raw=True,
            )
            if raw not in RAINY_WEATHERS and prev_raw not in RAINY_WEATHERS:
                assert rainbow.forecast(et) is None
                break

    def test_forecast_collects_multiple_rainbow_times(self):
        place = EorzeaPlaceName("東ラノシア")
        rainbow = EorzeaRainbow(place)
        rainbow_times: list[datetime] = []
        for et in EorzeaTime.weather_period(
            step="inf", from_=datetime(2022, 8, 25, 0, 0).timestamp()
        ):
            result = rainbow.forecast(et)
            if result is not None:
                rainbow_times.append(datetime.fromtimestamp(result.get_unix_time()))
            if len(rainbow_times) == 5:
                break
        assert len(rainbow_times) == 5
