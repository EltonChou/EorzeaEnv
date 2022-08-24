from datetime import datetime
from EorzeaEnv import EorzeaWeather, EorzeaPlaceName, EorzeaRainbow


class TestRainbow:
    def test_rainbow(self):
        place_name1 = EorzeaPlaceName("eastern la noscea")
        place_name2 = EorzeaPlaceName("fields of glory")

        the_rainbow = EorzeaRainbow(place_name1)
        impossible_rainbow = EorzeaRainbow(place_name2)

        assert the_rainbow.place_name is place_name1
        assert impossible_rainbow.place_name is place_name2

        lt1 = datetime(2022, 8, 23, 00, 00).timestamp()
        lt2 = datetime(2022, 8, 23, 00, 24).timestamp()

        weather1 = EorzeaWeather.forecast(place_name1, lt1, raw=True)
        weather2 = EorzeaWeather.forecast(place_name1, lt2, raw=True)
        the_rainbow.append(lt1, weather1)
        the_rainbow.append(lt2, weather2)

        weather1 = EorzeaWeather.forecast(place_name2, lt1, raw=True)
        weather2 = EorzeaWeather.forecast(place_name2, lt2, raw=True)
        impossible_rainbow.append(lt1, weather1)
        impossible_rainbow.append(lt2, weather2)

        assert the_rainbow.is_appear
        assert not impossible_rainbow.is_appear
