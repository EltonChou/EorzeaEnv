import warnings
from typing import Iterable, List, Literal, Union, overload

from numpy import uint32

from .Data.TerritoryWeather import territory_weather as _territory_weather
from .Data.Weather import weather as _weather
from .Data.WeatherRate import weather_rate as _weather_rate
from .eorzea_lang import EorzeaLang
from .eorzea_place_name import EorzeaPlaceName
from .eorzea_time import EorzeaTime
from .errors import WeatherRateDataError

Lang = Union[Literal['en', 'ja', 'de', 'fr'], EorzeaLang]


class EorzeaWeather:
    """
    EoreaWeather
    """
    FUZZY_CUTOFF: Union[int, float] = 80

    @classmethod
    def set_fuzzy_cutoff(cls, cutoff: Union[int, float]):
        if cutoff > 100 or cutoff < 0:
            raise ValueError('cutoff value should be in 0-100.')
        cls.FUZZY_CUTOFF = cutoff

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: Union[str, EorzeaPlaceName],
        timestamp: Iterable[Union[int, float, EorzeaTime]],
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: Literal[False] = False
    ) -> List[str]: ...

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: Union[str, EorzeaPlaceName],
        timestamp: Iterable[Union[int, float, EorzeaTime]],
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: Literal[True] = True
    ) -> List[int]: ...

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: Union[str, EorzeaPlaceName],
        timestamp: Iterable[Union[int, float, EorzeaTime]],
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: bool = False
    ) -> Union[List[int], List[str]]: ...

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: Union[str, EorzeaPlaceName],
        timestamp: Union[int, float, EorzeaTime],
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: Literal[False] = False
    ) -> str: ...

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: Union[str, EorzeaPlaceName],
        timestamp: Union[int, float, EorzeaTime],
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: Literal[True] = True
    ) -> int: ...

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: Union[str, EorzeaPlaceName],
        timestamp: Union[int, float, EorzeaTime],
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: bool = False
    ) -> Union[str, int]: ...

    @classmethod
    def forecast(
            cls,
            place_name: Union[str, EorzeaPlaceName],
            timestamp: Union[int, float, EorzeaTime, Iterable[Union[int, float, EorzeaTime]]],
            lang: Lang = EorzeaLang.EN,
            strict: bool = True,
            raw: bool = False
    ) -> Union[str, int, List[str], List[int]]:
        """Forecast Eorzea weather by place

        Parameters
        ----------
        place_name : Union[str, EorzeaPlaceName]
            a valid Eorzea place name
        timestamp : Union[int, float, EorzeaTime, Iterable[Union[int, float, EorzeaTime]]]
            unix timestamp or EorzeaTime instance.
            int and float type supporting would be removed from 2.5.0
        lang : Lang, optional
            Recommend use `EorzeaEnv.EorzeaLang`
            valid lang from ffxiv , by default "en"
        strict : bool, optional
            option of search mode, by default True
            + `True` for strict mode
            + `False` for fuzzy mode
        raw : bool, optional
            option for return raw weather value instead of weather name.

        Returns
        -------
        Union[str, List[str], int,  List[int]]
            result of forecast

        Raises
        -------
        EorzeaEnv.errors.InvalidEorzeaPlaceName
            When place_name is invalid.
        """
        ...
        if type(place_name) is str:
            place_name = EorzeaPlaceName(
                place_name, strict, fuzzy_cutoff=cls.FUZZY_CUTOFF)

        assert type(place_name) is EorzeaPlaceName
        weather_rate = _territory_weather[place_name.index]

        if isinstance(timestamp, Iterable):
            if _check_iterable_timestamp(timestamp):
                targets = (
                    _calculate_forecast_target(t)
                    for t in timestamp
                )
                result = [
                    _generate_result(target, weather_rate, lang, raw=raw)
                    for target in targets
                ]

                return result  # type: ignore

        if isinstance(timestamp, (float, int, EorzeaTime)):
            target = _calculate_forecast_target(timestamp)
            result = _generate_result(target, weather_rate, lang, raw=raw)

            return result

        raise TypeError(
            "timestamp should be type of Iterable[Union[int, flaot]], int, float."
        )

    @staticmethod
    def get_weather(index: int, lang: Lang):
        return _weather[index][lang]


def _check_iterable_timestamp(timestamp: Iterable[Union[int, float, EorzeaTime]]) -> bool:
    return all(
        type(t) is int or type(t) is float or type(t) is EorzeaTime
        for t in timestamp
    )


@overload
def _generate_result(target: int, weather_rate: int, lang: str, raw: Literal[True]) -> int: ...
@overload
def _generate_result(target: int, weather_rate: int, lang: str, raw: Literal[False]) -> str: ...
@overload
def _generate_result(target: int, weather_rate: int, lang: str, raw: bool = False) -> Union[int, str]: ...


def _generate_result(target: int, weather_rate: int, lang: str, raw: bool = False) -> Union[int, str]:
    for rate, weather in _weather_rate[weather_rate]:
        if target < rate:
            return weather if raw else _weather[weather][lang]

    raise WeatherRateDataError("No matched rate in data. Please contact with developer.")


def _calculate_forecast_target(the_time: Union[int, float, EorzeaTime]) -> int:
    """
    Thanks to Rogueadyn's SaintCoinach library for this calculation
    --------------
    [1] Do the magic 'cause for calculations

    [2] 16:00 is 0, 00:00 is 8 and 08:00 is 16.

    [3] Take Eorzea days since unix epoch.

    Parameters
    ----------
    the_time : EorzeaTime
        time to calculate the target.

    Returns
    -------
    int
        weather period start
    """

    if isinstance(the_time, EorzeaTime):
        the_time = the_time.get_unix_time()
    else:
        warnings.warn("timestamp in float and int type would be deprecated at 2.5.0", DeprecationWarning)

    bell = the_time / 175
    increment = uint32(bell + 8 - (bell % 8)) % 24
    total_days = uint32(the_time / 4200)
    calc_base = total_days * 0x64 + increment
    step1 = uint32(calc_base << 0xB) ^ calc_base
    step2 = uint32(step1 >> 8) ^ step1
    return int(step2 % 100)
