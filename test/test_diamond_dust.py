from EorzeaEnv import EorzeaPlaceName, EorzeaTime, EorzeaWeather
from EorzeaEnv.special_weather import EorzeaDiamondDust
from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS

FAIR_SKIES = 2


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


class TestDiamondDustIsAppear:
    def test_condition1_non_fair_skies_transitions_to_fair_skies_at_bell_8(self):
        # Condition 1: prev != Fair Skies, current == Fair Skies at bell 8
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 8 and raw == FAIR_SKIES:
                # Need a preceding period with non-Fair Skies
                # Go back one period (8 bells = 1400 real seconds)
                prev_unix = et.get_unix_time() - 1400
                prev_et = EorzeaTime(prev_unix)
                prev_raw = EorzeaWeather.forecast(
                    COERTHAS_WESTERN_HIGHLANDS, prev_et, raw=True
                )
                if prev_raw != FAIR_SKIES:
                    dd.observe(prev_et, prev_raw)
                    dd.observe(et, raw)
                    assert dd.is_appear
                    break

    def test_condition1_not_appear_when_prev_also_fair_skies_at_bell_8(self):
        # Condition 1 requires prev != Fair Skies; if prev is also Fair Skies, no dust
        # from cond1. bell==8 here so cond2 (bell==0) cannot fire either.
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 8 and raw == FAIR_SKIES:
                prev_unix = et.get_unix_time() - 1400
                prev_et = EorzeaTime(prev_unix)
                prev_raw = EorzeaWeather.forecast(
                    COERTHAS_WESTERN_HIGHLANDS, prev_et, raw=True
                )
                if prev_raw == FAIR_SKIES:
                    dd.observe(prev_et, prev_raw)
                    dd.observe(et, raw)
                    assert not dd.is_appear
                    break

    def test_condition2_fair_skies_at_bell_0(self):
        # Condition 2: Fair Skies at bell 0
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw == FAIR_SKIES:
                dd.observe(et, raw)
                assert dd.is_appear
                break

    def test_not_appear_when_bell_0_not_fair_skies(self):
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw != FAIR_SKIES:
                dd.observe(et, raw)
                assert not dd.is_appear
                break

    def test_not_appear_when_not_possible(self):
        other = EorzeaPlaceName("Eastern La Noscea")
        dd = EorzeaDiamondDust(other)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(other, et, raw=True)
            if et.bell == 0:
                dd.observe(et, raw)
                assert not dd.is_appear
                break

    def test_no_observation_returns_false(self):
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        assert not dd.is_appear

    def test_used_with_weather_period_generator(self):
        dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
        dust_times = []
        expected_count = 3

        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            dd.observe(
                et, EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            )
            if dd.is_appear:
                dust_times.append(et)
            if len(dust_times) == expected_count:
                break

        assert len(dust_times) == expected_count
