import copy
from typing import Final

from ..Data.TerritoryWeather import territory_weather as _territory_weather
from ..Data.WeatherRate import weather_rate as _weather_rate
from ..place_name import EorzeaPlaceName
from ..time import EorzeaTime
from ..weather import EorzeaWeather
from ._constants import RAINY_WEATHERS
from .protocols import SpecialWeather

_RAINBOW_BELL: Final = 6


class EorzeaRainbow(SpecialWeather):
    """Predicts rainbow appearances for a given Eorzea location.

    A rainbow appears when rainy weather (Rain, Showers, or Thunder Storms)
    transitions to any clear weather, during sun phases 27–32 or 1–6, between
    ET 06:00 and 18:00.

    Examples
    --------
    ```python
    from datetime import datetime
    from EorzeaEnv import EorzeaPlaceName, EorzeaRainbow, EorzeaTime

    place = EorzeaPlaceName('東ラノシア')
    rainbow = EorzeaRainbow(place_name=place)

    rainbow_times = []
    for t in EorzeaTime.weather_period(step='inf'):
        result = rainbow.forecast(t)
        if result is not None:
            rainbow_times.append(datetime.fromtimestamp(result.get_unix_time()))
        if len(rainbow_times) == 20:
            break
    ```
    """

    def __init__(self, place_name: EorzeaPlaceName) -> None:
        self._place_name = place_name
        self._is_possible = _is_rainbow_possible(place_name)

    @property
    def place_name(self) -> EorzeaPlaceName:
        return self._place_name

    @property
    def is_possible(self) -> bool:
        return self._is_possible

    def forecast(self, time: EorzeaTime) -> EorzeaTime | None:
        """Return the rainbow start time if a rainbow appears in *time*'s window.

        Returns ``None`` when no rainbow occurs or :attr:`is_possible` is ``False``.
        """
        if not self._is_possible:
            return None

        if not _check_sun(time.sun):
            return None

        raw = EorzeaWeather.forecast(self._place_name, time, raw=True)
        if raw in RAINY_WEATHERS:
            return None

        prev = time.prev_weather_window_start()
        prev_raw = EorzeaWeather.forecast(self._place_name, prev, raw=True)
        if prev_raw not in RAINY_WEATHERS:
            return None

        result = copy.copy(time)
        result.bell = _RAINBOW_BELL
        return result


def _is_rainbow_possible(place_name: EorzeaPlaceName) -> bool:
    weather_rate_index = _territory_weather[place_name.index]
    weather_rate = _weather_rate[weather_rate_index]
    possible_weathers: set[int] = {w[1] for w in weather_rate}
    return bool(
        possible_weathers - RAINY_WEATHERS and RAINY_WEATHERS & possible_weathers
    )


def _check_sun(sun: int) -> bool:
    return sun >= 27 or sun <= 6
