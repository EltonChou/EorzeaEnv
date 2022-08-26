from EorzeaEnv import EorzeaLang
from EorzeaEnv.Data.PlaceName import place_name
from EorzeaEnv.Data.TerritoryWeather import territory_weather
from EorzeaEnv.Data.Weather import weather
from EorzeaEnv.Data.WeatherRate import weather_rate


def test_data_integrity():
    locales = [EorzeaLang.DE, EorzeaLang.EN, EorzeaLang.FR, EorzeaLang.JA]
    for k in locales:
        place_dict = place_name[k]
        assert place_dict
        for v in place_dict.values():
            territory_index = v['index']
            weather_rate_index = territory_weather[territory_index]
            the_weather_rate = weather_rate[weather_rate_index]
            for weather_target in the_weather_rate:
                assert weather_target[1] in weather
