from numpy import uint32
from EorzeaEnv.Data.WeatherInfos import weather_infos


class EorzeaWeather:
    """Class EorzeaWeather"""

    _weather_infos = weather_infos

    @classmethod
    def forecast_weather(cls, field, local_time_stamp):
        weather_infos = cls._weather_infos[field]
        target = _calculate_forecast_target(local_time_stamp)

        for info in weather_infos:
            if target < info[0]:
                return info[1]


def _calculate_forecast_target(lt):
    """Thanks to Rogueadyn's SaintCoinach library for this calculation.
        1. Do the magic 'cause for calculations
        2. 16:00 is 0, 00:00 is 8 and 08:00 is 16.
        3. Take Eorzea days since unix epoch.
    """

    bell = lt / 175
    increment = uint32(bell + 8 - (bell % 8)) % 24
    total_days = uint32(lt / 4200)
    calc_base = total_days * 0x64 + increment
    step1 = uint32(calc_base << 0xB) ^ calc_base
    step2 = (step1 >> 8) ^ step1
    return int(step2 % 100)
