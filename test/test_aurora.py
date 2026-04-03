import copy

from EorzeaEnv import EorzeaPlaceName, EorzeaTime, EorzeaWeather, EorzeaAurora
from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS, OLD_SHARLAYAN

FAIR_SKIES = 2


class TestAuroraConstants:
    def test_constants_are_place_names(self):
        assert isinstance(COERTHAS_WESTERN_HIGHLANDS, EorzeaPlaceName)
        assert isinstance(OLD_SHARLAYAN, EorzeaPlaceName)

    def test_constant_names(self):
        assert COERTHAS_WESTERN_HIGHLANDS.value == "Coerthas Western Highlands"
        assert OLD_SHARLAYAN.value == "Old Sharlayan"


class TestAuroraPlaceName:
    def test_place_name_property(self):
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        assert aurora.place_name is COERTHAS_WESTERN_HIGHLANDS


class TestAuroraIsPossible:
    def test_is_possible_for_valid_places(self):
        assert EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS).is_possible
        assert EorzeaAurora(OLD_SHARLAYAN).is_possible

    def test_is_not_possible_for_other_place(self):
        other = EorzeaPlaceName("Eastern La Noscea")
        assert not EorzeaAurora(other).is_possible


class TestAuroraForecast:
    def test_forecast_returns_none_for_impossible_place(self):
        aurora = EorzeaAurora(EorzeaPlaceName("Eastern La Noscea"))
        for et in EorzeaTime.weather_period(step=5, from_=0.0):
            assert aurora.forecast(et) is None

    def test_forecast_returns_window_start_when_aurora_appears(self):
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw == FAIR_SKIES:
                result = aurora.forecast(et)
                assert result is not None
                assert result.bell == 0
                assert (
                    result.get_unix_time() == et.weather_period_start().get_unix_time()
                )
                break

    def test_forecast_returns_same_start_for_any_time_within_aurora_window(self):
        # bells 0-3 in a Fair Skies window all return the same start
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw == FAIR_SKIES:
                start = aurora.forecast(et)
                assert start is not None
                # bell 1, 2, 3 are inside ET 00:00-04:00 and same window
                for offset_bell in [1, 2, 3]:
                    later = copy.copy(et)
                    later.bell = offset_bell
                    result = aurora.forecast(later)
                    assert result is not None
                    assert result.get_unix_time() == start.get_unix_time()
                break

    def test_forecast_returns_none_at_bell_4_and_beyond(self):
        # ET 04:00 (bell 4) is outside the aurora window
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw == FAIR_SKIES:
                for outside_bell in [4, 5, 7]:
                    later = copy.copy(et)
                    later.bell = outside_bell
                    assert aurora.forecast(later) is None
                break

    def test_forecast_returns_none_when_not_fair_skies(self):
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw != FAIR_SKIES:
                assert aurora.forecast(et) is None
                break

    def test_forecast_returns_none_when_window_does_not_start_at_bell_0(self):
        # Windows at bell 8 or 16 can never produce aurora
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            if et.bell != 0:
                assert aurora.forecast(et) is None
                break

    def test_forecast_works_for_old_sharlayan(self):
        aurora = EorzeaAurora(OLD_SHARLAYAN)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(OLD_SHARLAYAN, et, raw=True)
            if et.bell == 0 and raw == FAIR_SKIES:
                assert aurora.forecast(et) is not None
                break

    def test_forecast_collects_multiple_aurora_times(self):
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        aurora_times = []
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            result = aurora.forecast(et)
            if result is not None:
                aurora_times.append(result)
            if len(aurora_times) == 3:
                break
        assert len(aurora_times) == 3
