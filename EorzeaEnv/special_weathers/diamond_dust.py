import copy
from typing import Final

from ..place_name import EorzeaPlaceName
from ..places import COERTHAS_WESTERN_HIGHLANDS
from ..time import EorzeaTime
from ..weather import EorzeaWeather
from ._constants import FAIR_SKIES

_DIAMOND_DUST_PLACES: Final = frozenset([COERTHAS_WESTERN_HIGHLANDS.index])

# Condition 2: Fair Skies at bell 0 → dust at ET 06:00–08:00 (bells 6–7)
_COND2_WINDOW_BELL: Final = 0
_COND2_START_BELL: Final = 6
_COND2_END_BELL: Final = 8

# Condition 1: transition to Fair Skies at bell 8 → dust at ET 08:00–10:00 (bells 8–9)
_COND1_WINDOW_BELL: Final = 8
_COND1_END_BELL: Final = 10


class EorzeaDiamondDust:
    """Predicts Diamond Dust appearances in Coerthas Western Highlands.

    Use the module-level constant from :mod:`EorzeaEnv.places` as the place argument:

        from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS

    Two conditions trigger Diamond Dust:

    1. Weather is Fair Skies at ET 00:00 (bell 0). Dust appears ET 06:00–08:00.
    2. Previous weather was not Fair Skies and transitions to Fair Skies at
       ET 08:00 (bell 8). Dust appears ET 08:00–10:00.

    Examples
    --------
    ```python
    from EorzeaEnv import EorzeaTime
    from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS
    from EorzeaEnv.special_weathers import EorzeaDiamondDust

    dd = EorzeaDiamondDust(COERTHAS_WESTERN_HIGHLANDS)
    for et in EorzeaTime.weather_period(step='inf'):
        result = dd.forecast(et)
        if result is not None:
            print(result)
    ```
    """

    def __init__(self, place_name: EorzeaPlaceName) -> None:
        self._place_name = place_name
        self._is_possible = place_name.index in _DIAMOND_DUST_PLACES

    @property
    def place_name(self) -> EorzeaPlaceName:
        return self._place_name

    @property
    def is_possible(self) -> bool:
        return self._is_possible

    def forecast(self, time: EorzeaTime) -> EorzeaTime | None:
        """Return the dust start time if Diamond Dust appears during *time*.

        Checks which weather window contains *time*, evaluates the appropriate
        condition, and returns the ET start of the dust period, or ``None``.
        """
        if not self._is_possible:
            return None

        window_start = time.weather_window_start()

        if window_start.bell == _COND2_WINDOW_BELL:
            if _COND2_START_BELL <= time.bell < _COND2_END_BELL:
                if (
                    EorzeaWeather.forecast(self._place_name, window_start, raw=True)
                    == FAIR_SKIES
                ):
                    result = copy.copy(window_start)
                    result.bell = _COND2_START_BELL
                    return result

        elif window_start.bell == _COND1_WINDOW_BELL:
            if time.bell < _COND1_END_BELL:
                if (
                    EorzeaWeather.forecast(self._place_name, window_start, raw=True)
                    == FAIR_SKIES
                ):
                    prev_raw = EorzeaWeather.forecast(
                        self._place_name, time.prev_weather_window_start(), raw=True
                    )
                    if prev_raw != FAIR_SKIES:
                        return copy.copy(window_start)

        return None
