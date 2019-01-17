from numpy import uint32
from EorzeaEnv.Data.TerritoryWeather import territory as _territory
from EorzeaEnv.Data.WeatherRate import weather_rate as _wr
from EorzeaEnv.Data.WeatherLocalize import weather_localize as _localize


class EorzeaWeather:
    """About XIV Weather"""

    @staticmethod
    def forecast_weather(placename, timestamp, lang='en'):
        """Genrate forecast result.

        Parameters
        ----------
        field : str
            The placename of FFXIV.
        timestamp : float
            The timestamp of weather changing.
        lang: Optional str
            The language of result.

        Returns:
        ----------
        string
            The result of forecast.

        Raises:
        ----------
        KeyError
            When placename invalid.

        """
        try:
            weather_group = _territory[placename]
        except KeyError:
            raise KeyError("valid FFXIV placename required")

        target = _calculate_forecast_target(timestamp)

        for rate in _wr[weather_group]:
            if target < rate[0]:
                return _localize[rate[1]][lang]


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
