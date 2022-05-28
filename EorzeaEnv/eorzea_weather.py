try:
    from typing import Iterable, List, Literal, Union, overload, Type
    Lang = Literal['en', 'jp', 'de', 'fr']
except:
    from typing import Iterable, List, Union, overload, Type
    Lang = str

import re

from numpy import uint32
from rapidfuzz import process as fuzz_process

from .Data.TerritoryWeather import territory as _territory
from .Data.Weather import weather as _weather
from .Data.WeatherRate import weather_rate as _weather_rate
from .errors import InvalidEorzeaPlaceName, WeatherRateDataError


FuzzyCutoff = Union[int, float]


class EorzeaWeather:
    """
    EoreaWeather
    """
    FUZZY_CUTOFF: FuzzyCutoff = 80

    @classmethod
    def set_fuzzy_cutoff(cls, cutoff: FuzzyCutoff):
        if cutoff > 100 or cutoff < 0:
            raise ValueError('cutoff value should be in 0-100.')
        cls.FUZZY_CUTOFF = cutoff

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: str,
        timestamp: Iterable[float],
        lang: Lang = "en",
        strict: bool = True
    ) -> List[str]:
        """Forecast Eorzea weather by place

        Parameters
        ----------
        place_name : str
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
        EorzeaEnv.errors.InvalidEorzeaPlaceName
            When place_name is invalid.
        """
        ...

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: str,
        timestamp: float,
        lang: Lang = "en",
        strict: bool = True
    ) -> str:
        """Forecast Eorzea weather by place

        Parameters
        ----------
        place_name : str
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
        EorzeaEnv.errors.InvalidEorzeaPlaceName
            When place_name is invalid.
        """
        ...

    @classmethod
    def forecast(cls, place_name, timestamp, lang="en", strict=True):
        place_name = _parse_place_name(place_name, strict, cls.FUZZY_CUTOFF)
        weather_rate = _territory[place_name]

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

    raise WeatherRateDataError(
        "No matched rate in data. Please contact with developer."
    )


def _parse_place_name(place_name: str, is_strict: bool, fuzzy_cutoff: FuzzyCutoff) -> str:
    possible_place_name = None
    place_name = place_name.lower()

    check_place_name = re.search('^the (.*)', place_name)
    if check_place_name:
        place_name = ''.join(check_place_name.groups())

    if is_strict:
        if place_name in _territory.keys():
            return place_name
        else:
            raise InvalidEorzeaPlaceName(
                place_name=place_name, is_strict=is_strict)
    else:
        result = fuzz_process.extractOne(
            place_name, _territory.keys(), score_cutoff=fuzzy_cutoff)
        if not result:
            raise InvalidEorzeaPlaceName(
                place_name=place_name, is_strict=is_strict)

        possible_place_name, score, index = result

    return possible_place_name


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
