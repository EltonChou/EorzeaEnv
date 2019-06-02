import warnings
import re

from numpy import uint32

from .Data.TerritoryWeather import territory as _territory
from .Data.Weather import weather as _weather
from .Data.WeatherRate import weather_rate as _weather_rate


class EorzeaWeather:
    """
    EoreaWeather
    """

    @staticmethod
    def forecast(placename: str, timestamp, lang='en', strict=True) -> str:
        """
        forecast

        Parameters
        ----------
        placename : str
            valid placename from FFXIV

        timestamp : [float or array_like of float]
            timestamp or timestamp in array_like

        lang : str, optional
            languages support [en, jp, de, fr], by default 'en'

        strict : bool, optional
            search mode, strict or fuzzy, by default True

        Raises
        -------
        KeyError
            when placename invalid

        Returns
        -------
        [str or array_like]
            forecast result in array_like or str
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

    @staticmethod
    def forecast_weather(*args, **kwargs):
        warnings.warn(
            'forecast_weather is deprecated, use forecaset instead.',
            DeprecationWarning
        )


def _generate_result(target: int, weather_rate: int, lang: str) -> str:
    for r, w in _weather_rate[weather_rate]:
        if target < r:
            return _weather[w][lang]


def _get_weather_rate(placename: str, strict: bool) -> int:
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


def _parse_placename(placename: str) -> str:
    """
    trim `the`

    Parameters
    ----------
    placename : str
        valid placename from FFXIV starts with `the`

    Returns
    -------
    str
        trimmed placename
    """
    placename = placename.lower()
    check_placename = re.search('^the (.*)', placename)

    if check_placename:
        placename = ''.join(check_placename.groups())
    return placename


def _calculate_forecast_target(lt: float) -> int:
    """
    Thanks to Rogueadyn's SaintCoinach library for this calculation
    --------------
    [1] Do the magic 'cause for calculations

    [2] 16:00 is 0, 00:00 is 8 and 08:00 is 16.

    [3] Take Eorzea days since unix epoch.

    Parameters
    ----------
    lt : float
        local timestamp

    Returns
    -------
    int
        weather period start
    """

    bell = lt / 175
    increment = uint32(bell + 8 - (bell % 8)) % 24
    total_days = uint32(lt / 4200)
    calc_base = total_days * 0x64 + increment
    step1 = uint32(calc_base << 0xB) ^ calc_base
    step2 = (step1 >> 8) ^ step1
    return int(step2 % 100)
