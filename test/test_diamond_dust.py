import copy

from EorzeaEnv import EorzeaPlaceName, EorzeaTime, EorzeaWeather, EorzeaDiamondDust
from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS

FAIR_SKIES = 2
_WEATHER_INTERVAL = 1400


class TestDiamondDustConstants:
    def test_constant_is_place_name(self):
        assert isinstance(COERTHAS_WESTERN_HIGHLANDS, EorzeaPlaceName)

    def test_constant_name(self):
        assert COERTHAS_WESTERN_HIGHLANDS.value == "Coerthas Western Highlands"


class TestDiamondDustPlaceName:
    def test_place_name_property(self):
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        assert dd.place_name is COERTHAS_WESTERN_HIGHLANDS


class TestDiamondDustIsPossible:
    def test_is_possible_for_coerthas(self):
        assert EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS).is_possible

    def test_is_not_possible_for_other_place(self):
        other = EorzeaPlaceName("Eastern La Noscea")
        assert not EorzeaDiamondDust(other).is_possible


class TestDiamondDustForecast:
    def test_forecast_returns_none_for_impossible_place(self):
        dd = EorzeaDiamondDust(EorzeaPlaceName("Eastern La Noscea"))
        for et in EorzeaTime.weather_period(step=5, from_=0.0):
            assert dd.forecast(et) is None

    def test_condition2_returns_bell_6_for_any_time_in_dust_window(self):
        # Condition 2: Fair Skies window at bell 0, time in bells 6-7 → dust at bell 6
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw == FAIR_SKIES:
                for dust_bell in [6, 7]:
                    t = copy.copy(et)
                    t.bell = dust_bell
                    result = dd.forecast(t)
                    assert result is not None
                    assert result.bell == 6
                break

    def test_condition2_returns_none_outside_dust_window(self):
        # Bells 0-5 and 8+ are outside ET 06:00-08:00
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw == FAIR_SKIES:
                for outside_bell in [0, 1, 5]:
                    t = copy.copy(et)
                    t.bell = outside_bell
                    assert dd.forecast(t) is None
                break

    def test_condition1_transition_to_fair_skies_returns_bell_8(self):
        # Condition 1: bell-8 window, Fair Skies, prev not Fair Skies → dust at bell 8
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 8 and raw == FAIR_SKIES:
                prev_raw = EorzeaWeather.forecast(
                    COERTHAS_WESTERN_HIGHLANDS,
                    EorzeaTime(et.get_unix_time() - _WEATHER_INTERVAL),
                    raw=True,
                )
                if prev_raw != FAIR_SKIES:
                    for dust_bell in [8, 9]:
                        t = copy.copy(et)
                        t.bell = dust_bell
                        result = dd.forecast(t)
                        assert result is not None
                        assert result.bell == 8
                    break

    def test_condition1_returns_none_when_prev_also_fair_skies(self):
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 8 and raw == FAIR_SKIES:
                prev_raw = EorzeaWeather.forecast(
                    COERTHAS_WESTERN_HIGHLANDS,
                    EorzeaTime(et.get_unix_time() - _WEATHER_INTERVAL),
                    raw=True,
                )
                if prev_raw == FAIR_SKIES:
                    assert dd.forecast(et) is None
                    break

    def test_condition1_returns_none_outside_dust_window(self):
        # Bell 10+ is outside ET 08:00-10:00
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 8 and raw == FAIR_SKIES:
                prev_raw = EorzeaWeather.forecast(
                    COERTHAS_WESTERN_HIGHLANDS,
                    EorzeaTime(et.get_unix_time() - _WEATHER_INTERVAL),
                    raw=True,
                )
                if prev_raw != FAIR_SKIES:
                    t = copy.copy(et)
                    t.bell = 10
                    assert dd.forecast(t) is None
                    break

    def test_forecast_returns_none_when_no_condition_met(self):
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if raw != FAIR_SKIES:
                assert dd.forecast(et) is None
                break

    def test_forecast_collects_multiple_dust_times(self):
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        dust_times = []
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            result = dd.forecast(et)
            if result is not None:
                dust_times.append(result)
            if len(dust_times) == 3:
                break
        assert len(dust_times) == 3
