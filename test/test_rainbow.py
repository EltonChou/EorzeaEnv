from datetime import datetime, timezone

from EorzeaEnv import EorzeaPlaceName, EorzeaRainbow, EorzeaTime, EorzeaWeather


class TestRainbow:
    def test_rainbow(self):
        place_name1 = EorzeaPlaceName("eastern la noscea")
        place_name2 = EorzeaPlaceName("fields of glory")

        the_rainbow = EorzeaRainbow(place_name1)
        impossible_rainbow = EorzeaRainbow(place_name2)

        assert the_rainbow.place_name is place_name1
        assert impossible_rainbow.place_name is place_name2

        et1 = EorzeaTime(datetime(2022, 8, 23, 00, 00, tzinfo=timezone.utc).timestamp())
        et2 = EorzeaTime(datetime(2022, 8, 23, 00, 24, tzinfo=timezone.utc).timestamp())

        print(et1, et2)
        print(et1.get_unix_time(), et2.get_unix_time())

        weather1 = EorzeaWeather.forecast(place_name1, et1, raw=True)
        weather2 = EorzeaWeather.forecast(place_name1, et2, raw=True)
        the_rainbow.append(et1, weather1)
        the_rainbow.append(et2, weather2)

        weather1 = EorzeaWeather.forecast(place_name2, et1, raw=True)
        weather2 = EorzeaWeather.forecast(place_name2, et2, raw=True)
        impossible_rainbow.append(et1, weather1)
        impossible_rainbow.append(et2, weather2)

        assert the_rainbow.is_appear
        assert not impossible_rainbow.is_appear
