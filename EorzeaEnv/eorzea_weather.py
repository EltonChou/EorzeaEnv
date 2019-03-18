import re

from numpy import uint32

from .Data.TerritoryWeather import territory as _territory
from .Data.Weather import weather as _weather
from .Data.WeatherRate import weather_rate as _weather_rate


class EorzeaWeather:
    """About XIV Weather"""

    @staticmethod
    def forecast_weather(placename, timestamp, lang='en', strict=True):
        """Genrate forecast result.

        Parameters
        ----------
        placename : str
            The placename of FFXIV.
        timestamp : float or iterable
            Accept float and iterable.
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

        weather_rate = None
        placename = _parse_placename(placename)
        weather_rate = _get_weather_rate(placename, strict)

        # check timestamp is iterable or not.
        try:
            target = (_calculate_forecast_target(t) for t in timestamp)
            result = [
                _generate_result(ta, weather_rate, lang) for ta in target
            ]
        except TypeError:
            target = _calculate_forecast_target(timestamp)
            result = _generate_result(target, weather_rate, lang)
        finally:
            return result


def _generate_result(target, weather_rate, lang):
    for r, w in _weather_rate[weather_rate]:
        if target < r:
            return _weather[w][lang]


def _get_weather_rate(placename, strict):
    weather_rate = None
    try:
        weather_rate = _territory[placename]
    except KeyError:
        if strict:
            raise KeyError('valid Eorzea placename required')

        for p, r in _territory.items():
            if re.search(p, placename):
                weather_rate = r
    finally:
        if weather_rate is None:
            raise KeyError('valid Eorzea placename required')
        return weather_rate


def _parse_placename(placename):
    placename = placename.lower()
    check_placename = re.search('^the (.*)', placename)

    if check_placename:
        placename = ''.join(check_placename.groups())
    return placename


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
