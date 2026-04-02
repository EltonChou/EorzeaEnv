from __future__ import annotations

import warnings
from typing import Any, Iterable, Literal, Union, overload

from numpy import uint32

from .Data.TerritoryWeather import territory_weather as _territory_weather
from .Data.Weather import weather as _weather
from .Data.WeatherRate import weather_rate as _weather_rate
from .eorzea_lang import EorzeaLang
from .eorzea_place_name import EorzeaPlaceName, FuzzyCutoff

from .eorzea_time import EorzeaTime
from .errors import WeatherRateDataError

Lang = Union[Literal["en", "ja", "de", "fr", "ko", "cn", "tc"], EorzeaLang]
ValidPlaceName = str | EorzeaPlaceName
Timestamp = EorzeaTime | float | int


class EorzeaWeather:
    """
    EoreaWeather
    """

    FUZZY_CUTOFF: FuzzyCutoff = 80

    @classmethod
    def set_fuzzy_cutoff(cls, cutoff: float):
        if cutoff > 100 or cutoff < 0:
            raise ValueError("Cutoff value should be in 0-100.")
        cls.FUZZY_CUTOFF = cutoff

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: ValidPlaceName,
        timestamp: Timestamp,
        *,
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: Literal[False] = False,
    ) -> str: ...

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: ValidPlaceName,
        timestamp: Timestamp,
        *,
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: Literal[True],
    ) -> int: ...

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: ValidPlaceName,
        timestamp: Iterable[Timestamp],
        *,
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: Literal[False] = False,
    ) -> list[str]: ...

    @overload
    @classmethod
    def forecast(
        cls,
        place_name: ValidPlaceName,
        timestamp: Iterable[Timestamp],
        *,
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: Literal[True],
    ) -> list[int]: ...

    @classmethod
    def forecast(
        cls,
        place_name: ValidPlaceName,
        timestamp: Timestamp | Iterable[Timestamp],
        *,
        lang: Lang = EorzeaLang.EN,
        strict: bool = True,
        raw: bool = False,
    ) -> list[str] | list[int] | str | int:
        """Forecast Eorzea weather by place

        Parameters
        ----------
        place_name : str | EorzeaPlaceName
            a valid Eorzea place name
        timestamp : int | float | EorzeaTime | Iterable[int | float | EorzeaTime]
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
        str | list[str] | int | list[int]
            result of forecast

        Raises
        -------
        EorzeaEnv.errors.InvalidEorzeaPlaceName
            When place_name is invalid.
        """
        ...
        if type(place_name) is str:
            warnings.warn(
                "place_name in `str` is deprecated from 2.5.0."
                " Please use the EorzeaPlaceName instead.",
                DeprecationWarning,
            )
            place_name = EorzeaPlaceName(
                place_name, strict, fuzzy_cutoff=cls.FUZZY_CUTOFF
            )

        assert type(place_name) is EorzeaPlaceName
        weather_rate = _territory_weather[place_name.index]

        def make_result(timestamp: EorzeaTime):
            target = _calculate_forecast_target(timestamp)
            result = _generate_result(target, weather_rate)
            if not raw:
                result = cls.get_weather(result, lang)
                assert result
            return result

        if isinstance(timestamp, Iterable):
            return [make_result(_ensure_timestamp(t)) for t in timestamp]

        timestamp = _ensure_timestamp(timestamp)
        result = make_result(timestamp)
        return result

    @staticmethod
    def get_weather(index: int, lang: Lang):
        return _weather[index][lang]


def _ensure_timestamp(timestamp: Any) -> EorzeaTime:
    if type(timestamp) is EorzeaTime:
        return timestamp
    if type(timestamp) in (float, int):
        warnings.warn(
            "timestamp in float and int type is deprecated."
            " It will be unsupported at 2.5.0. Please use EorzeaTime instead.",
            DeprecationWarning,
        )
        return EorzeaTime(timestamp=timestamp)
    raise TypeError("timestamp should be type of int, float, EorzeaTime.")


def _generate_result(target: int, weather_rate: int) -> int:
    for rate, weather in _weather_rate[weather_rate]:
        if target < rate:
            return weather

    raise WeatherRateDataError(
        "No matched rate in data. Please contact with developer."
    )


def _calculate_forecast_target(the_time: EorzeaTime) -> int:
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

    ts = the_time.get_unix_time()

    bell = ts / 175
    increment = uint32(bell + 8 - (bell % 8)) % 24
    total_days = uint32(ts / 4200)
    calc_base = total_days * 0x64 + increment
    step1 = uint32(calc_base << 0xB) ^ calc_base
    step2 = uint32(step1 >> 8) ^ step1
    return int(step2 % 100)
