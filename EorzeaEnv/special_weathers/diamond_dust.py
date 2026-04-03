import copy
from collections import deque
from typing import Final, MutableSequence

from ..place_name import EorzeaPlaceName
from ..places import COERTHAS_WESTERN_HIGHLANDS
from ..time import EorzeaTime
from ..weather import WeatherInfo

FAIR_SKIES: Final = 2

_DIAMOND_DUST_PLACES: Final = frozenset([COERTHAS_WESTERN_HIGHLANDS.index])


class EorzeaDiamondDust:
    """Predicts Diamond Dust appearances in Coerthas Western Highlands.

    Use the module-level constant from :mod:`EorzeaEnv.places` as the place argument:

        from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS

    Two conditions trigger Diamond Dust during a period:

    1. Previous weather was not Fair Skies and transitions to Fair Skies at
       ET 08:00 (bell 8). Dust appears ET 08:00–10:00.
    2. Weather is Fair Skies at ET 00:00 (bell 0). Dust appears ET 06:00–08:00.

    :attr:`is_appear` returns True if dust appears at any point during the
    observed period. Check it after each :meth:`observe` call.

    Examples
    --------
    ```python
    from EorzeaEnv import EorzeaTime, EorzeaWeather
    from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS
    from EorzeaEnv.special_weather import EorzeaDiamondDust

    dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
    for et in EorzeaTime.weather_period(step='inf'):
        dd.observe(et, EorzeaWeather.forecast(COERTHAS_WESTERN_HIGHLANDS, et, raw=True))
        if dd.is_appear:
            print(et)
    ```
    """

    _weather_slot: MutableSequence[WeatherInfo]

    def __init__(self, place_name: EorzeaPlaceName) -> None:
        self._place_name = place_name
        self._weather_slot = deque([], maxlen=2)
        self._is_possible = place_name.index in _DIAMOND_DUST_PLACES

    @property
    def place_name(self) -> EorzeaPlaceName:
        return self._place_name

    @property
    def is_possible(self) -> bool:
        return self._is_possible

    @property
    def is_appear(self) -> bool:
        if not self._is_possible or len(self._weather_slot) == 0:
            return False

        current = self._weather_slot[-1]

        # Condition 2: Fair Skies at bell 0 → dust at ET 06:00–08:00
        if current.time.bell == 0 and current.raw_weather == FAIR_SKIES:
            return True

        # Condition 1: transition from non-Fair Skies to Fair Skies at bell 8
        if (
            len(self._weather_slot) == 2
            and current.time.bell == 8
            and current.raw_weather == FAIR_SKIES
        ):
            prev = self._weather_slot[0]
            if prev.raw_weather != FAIR_SKIES:
                return True

        return False

    def observe(self, time: EorzeaTime, raw_weather: int) -> None:
        self._weather_slot.append(
            WeatherInfo(time=copy.copy(time), raw_weather=raw_weather)
        )
