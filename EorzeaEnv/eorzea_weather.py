import re

try:
    from typing import Iterable, List, Literal, overload
    Lang = Literal['en', 'jp', 'de', 'fr']
except:
    from typing import Iterable, List, overload
    Lang = str

from numpy import uint32

from .Data.TerritoryWeather import territory as _territory
from .Data.Weather import weather as _weather
from .Data.WeatherRate import weather_rate as _weather_rate


class EorzeaWeather:
    """
    EoreaWeather
    """

    @overload
    @staticmethod
    def forecast(
        placename: str,
        timestamp: Iterable[float],
        lang: Lang = "en",
        strict: bool = True
    ) -> List[str]:
        """Forecast Eorzea weather by place

        Parameters
        ----------
        placename : str
            a valid Eorzea place name
        timestamp : Iterable[float]
            unix timestamp
        lang : Lang, optional
            Recommend use `EorzeaEnv.EorzeaLang`
            valid lang from ffxiv , by default "en"
        strict : bool, optional
            option of search mode, by default True
            + `True` for strict mode
            + `False` for fuzzy mode

        Returns
        -------
        List[str]
            result of forecast

        Raises
        -------
        ValueError
            when using invalid place name
        """
        ...

    @overload
    @staticmethod
    def forecast(
        placename: str,
        timestamp: float,
        lang: Lang = "en",
        strict: bool = True
    ) -> str:
        """Forecast Eorzea weather by place

        Parameters
        ----------
        placename : str
            a valid Eorzea place name
        timestamp : float
            unix timestamp
        lang : Lang, optional
            Recommend use `EorzeaEnv.EorzeaLang`
            valid lang from ffxiv , by default "en"
        strict : bool, optional
            option of search mode, by default True
            + `True` for strict mode
            + `False` for fuzzy mode

        Returns
        -------
        str
            result of forecast

        Raises
        -------
        ValueError
            when using invalid place name
        """
        ...

    @staticmethod
    def forecast(placename, timestamp, lang="en", strict=True):
        placename = _parse_placename(placename)
        weather_rate = _get_weather_rate(placename, strict)

        if isinstance(timestamp, Iterable):
            targets = (_calculate_forecast_target(t) for t in timestamp)
            result = [
                _generate_result(target, weather_rate, lang) for target in targets
            ]

            return result

        if isinstance(timestamp, float):
            target = _calculate_forecast_target(timestamp)
            result = _generate_result(target, weather_rate, lang)

            return result


def _generate_result(target: int, weather_rate: int, lang: str) -> str:
    for rate, weather in _weather_rate[weather_rate]:
        if target < rate:
            return _weather[weather][lang]


def _get_weather_rate(placename: str, strict: bool) -> int:
    weather_rate = None
    try:
        weather_rate = _territory[placename]
    except KeyError:
        if strict:
            raise ValueError('valid Eorzea placename required')

        for place, rate in _territory.items():
            if re.search(place, placename):
                weather_rate = rate
    finally:
        if weather_rate is None:
            raise ValueError('valid Eorzea placename required')
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


def _calculate_forecast_target(local_timestamp: float) -> int:
    """
    Thanks to Rogueadyn's SaintCoinach library for this calculation
    --------------
    [1] Do the magic 'cause for calculations

    [2] 16:00 is 0, 00:00 is 8 and 08:00 is 16.

    [3] Take Eorzea days since unix epoch.

    Parameters
    ----------
    local_timestamp : float
        local timestamp

    Returns
    -------
    int
        weather period start
    """

    bell = local_timestamp / 175
    increment = uint32(bell + 8 - (bell % 8)) % 24
    total_days = uint32(local_timestamp / 4200)
    calc_base = total_days * 0x64 + increment
    step1 = uint32(calc_base << 0xB) ^ calc_base
    step2 = (step1 >> 8) ^ step1
    return int(step2 % 100)
