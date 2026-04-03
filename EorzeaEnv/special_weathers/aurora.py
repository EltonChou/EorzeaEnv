from typing import Final

from ..place_name import EorzeaPlaceName
from ..places import COERTHAS_WESTERN_HIGHLANDS, OLD_SHARLAYAN
from ..time import EorzeaTime
from ..weather import EorzeaWeather
from ._constants import FAIR_SKIES

_AURORA_PLACES: Final = frozenset(
    [COERTHAS_WESTERN_HIGHLANDS.index, OLD_SHARLAYAN.index]
)

# Aurora lasts ET 00:00–04:00; bell 4 is the first bell outside the window
_AURORA_END_BELL: Final = 4


class EorzeaAurora:
    """Predicts Aurora appearances for a given Eorzea location.

    Aurora only occurs in Coerthas Western Highlands and Old Sharlayan.
    Use the module-level constants from :mod:`EorzeaEnv.places` as the place argument:

        from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS

    Examples
    --------
    ```python
    from EorzeaEnv import EorzeaTime
    from EorzeaEnv.places import COERTHAS_WESTERN_HIGHLANDS
    from EorzeaEnv.special_weathers import EorzeaAurora

    aurora = EorzeaAurora(COERTHAS_WESTERN_HIGHLANDS)
    for et in EorzeaTime.weather_period(step='inf'):
        result = aurora.forecast(et)
        if result is not None:
            print(result)
    ```
    """

    def __init__(self, place_name: EorzeaPlaceName) -> None:
        self._place_name = place_name
        self._is_possible = place_name.index in _AURORA_PLACES

    @property
    def place_name(self) -> EorzeaPlaceName:
        return self._place_name

    @property
    def is_possible(self) -> bool:
        return self._is_possible

    def forecast(self, time: EorzeaTime) -> EorzeaTime | None:
        """Return the aurora start time if aurora appears during *time*.

        Aurora occurs when the weather window containing *time* has Fair Skies
        at ET 00:00 (bell 0), and *time* itself falls within ET 00:00–04:00.
        Returns the ET 00:00 start of that window, or ``None``.
        """
        if not self._is_possible:
            return None

        window_start = time.weather_window_start()
        if window_start.bell != 0:
            return None

        if time.bell >= _AURORA_END_BELL:
            return None

        if (
            EorzeaWeather.forecast(self._place_name, window_start, raw=True)
            == FAIR_SKIES
        ):
            return window_start
        return None
