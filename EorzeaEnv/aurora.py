import copy
from dataclasses import dataclass
from typing import Final

from .place_name import EorzeaPlaceName
from .places import COERTHAS_WESTERN_HIGHLANDS, OLD_SHARLAYAN
from .time import EorzeaTime

FAIR_SKIES: Final = 2

_AURORA_PLACES: Final = frozenset(
    [COERTHAS_WESTERN_HIGHLANDS.index, OLD_SHARLAYAN.index]
)


@dataclass
class _WeatherInfo:
    time: EorzeaTime
    raw_weather: int


class EorzeaAurora:
    """Predicts Aurora appearances for a given Eorzea location.

    Aurora only occurs in Coerthas Western Highlands and Old Sharlayan.
    Use the module-level constants from :mod:`EorzeaEnv.places` as the place argument:

        from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS

    Aurora appears when the weather is Fair Skies in the ET 00:00–08:00
    period (bell 0). Check :attr:`is_appear` after each :meth:`observe` call.

    Examples
    --------
    ```python
    from EorzeaEnv import EorzeaTime, EorzeaWeather
    from EorzeaEnv.aurora import EorzeaAurora
    from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS

    aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
    for et in EorzeaTime.weather_period(step='inf'):
        aurora.observe(
            et, EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True)
        )
        if aurora.is_appear:
            print(et)
    ```
    """

    def __init__(self, place_name: EorzeaPlaceName) -> None:
        self._place_name = place_name
        self._last: _WeatherInfo | None = None
        self._is_possible = place_name.index in _AURORA_PLACES

    @property
    def place_name(self) -> EorzeaPlaceName:
        return self._place_name

    @property
    def is_possible(self) -> bool:
        return self._is_possible

    @property
    def is_appear(self) -> bool:
        if self._last is None or not self._is_possible:
            return False
        return self._last.raw_weather == FAIR_SKIES and self._last.time.bell == 0

    def observe(self, time: EorzeaTime, raw_weather: int) -> None:
        self._last = _WeatherInfo(time=copy.copy(time), raw_weather=raw_weather)
