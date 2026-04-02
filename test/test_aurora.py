from EorzeaEnv import EorzeaPlaceName, EorzeaTime, EorzeaWeather
from EorzeaEnv.aurora import EorzeaAurora
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


class TestAuroraIsAppear:
    def test_appear_when_fair_skies_at_bell_0(self):
        # Find a timestamp where bell == 0 and weather is Fair Skies
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw == FAIR_SKIES:
                aurora.observe(et, raw)
                assert aurora.is_appear
                break

    def test_not_appear_when_fair_skies_but_not_bell_0(self):
        # bell 8 or bell 16 with Fair Skies should not trigger aurora
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell != 0 and raw == FAIR_SKIES:
                aurora.observe(et, raw)
                assert not aurora.is_appear
                break

    def test_not_appear_when_bell_0_but_not_fair_skies(self):
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            if et.bell == 0 and raw != FAIR_SKIES:
                aurora.observe(et, raw)
                assert not aurora.is_appear
                break

    def test_not_appear_when_not_possible(self):
        other = EorzeaPlaceName("Eastern La Noscea")
        aurora = EorzeaAurora(other)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(other, et, raw=True)
            if et.bell == 0:
                aurora.observe(et, raw)
                assert not aurora.is_appear
                break

    def test_no_observation_returns_false(self):
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        assert not aurora.is_appear

    def test_aurora_appears_in_old_sharlayan(self):
        aurora = EorzeaAurora(OLD_SHARLAYAN)
        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            raw = EorzeaWeather.forecast(OLD_SHARLAYAN, et, raw=True)
            if et.bell == 0 and raw == FAIR_SKIES:
                aurora.observe(et, raw)
                assert aurora.is_appear
                break

    def test_used_with_weather_period_generator(self):
        aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
        aurora_times = []
        expected_count = 3

        for et in EorzeaTime.weather_period(step="inf", from_=0.0):
            aurora.observe(
                et, EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
            )
            if aurora.is_appear:
                aurora_times.append(et)
            if len(aurora_times) == expected_count:
                break

        assert len(aurora_times) == expected_count
