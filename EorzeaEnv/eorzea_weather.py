try:
    from typing import Iterable, List, Literal, Union, overload
    Lang = Literal['en', 'jp', 'de', 'fr']
except:
    from typing import Iterable, List, Union, overload
    Lang = str


from numpy import uint32

from .Data.TerritoryWeather import territory_weather as _territory_weather
from .Data.Weather import weather as _weather
from .Data.WeatherRate import weather_rate as _weather_rate
from .eorzea_lang import EorzeaLang
from .eorzea_place_name import EorzeaPlaceName
from .errors import WeatherRateDataError


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
        timestamp: Iterable[Union[int, float]],
        lang: Lang = EorzeaLang.EN,
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
        place_name: Union[str, EorzeaPlaceName],
        timestamp: Union[int, float],
        lang: Lang = EorzeaLang.EN,
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
    def forecast(cls, place_name, timestamp, lang='en', strict=True):
        if type(place_name) is not EorzeaPlaceName:
            place_name = EorzeaPlaceName(
                place_name, strict, fuzzy_cutoff=cls.FUZZY_CUTOFF)

        weather_rate = _territory_weather[place_name.index]

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


def _calculate_forecast_target(local_timestamp: Union[int, float]) -> int:
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
