import copy
from collections import deque
from dataclasses import dataclass
from typing import MutableSequence, Set

from .Data.TerritoryWeather import territory_weather as _territory_weather
from .Data.WeatherRate import weather_rate as _weather_rate
from .eorzea_place_name import EorzeaPlaceName
from .eorzea_time import EorzeaTime

RAINY_WEATHERS = {7, 8, 10}


@dataclass
class WeatherInfo:
    time: EorzeaTime
    raw_weather: int


class EorzeaRainbow:
    _weather_slot: MutableSequence[WeatherInfo]
    _is_possible: bool
    _place_name: EorzeaPlaceName

    def __init__(self, place_name: EorzeaPlaceName) -> None:
        self._place_name = place_name
        self._weather_slot = deque([], maxlen=2)
        self._is_possible = _is_rainbow_possible(place_name)

    @property
    def place_name(self):
        return self._place_name

    @property
    def is_possible(self):
        return self._is_possible

    @property
    def is_appear(self):
        if len(self._weather_slot) == 2 and self.is_possible:
            prev_weather, current_weather = self._weather_slot
            if (
                prev_weather.raw_weather in RAINY_WEATHERS
                and current_weather.raw_weather not in RAINY_WEATHERS
            ):
                if (
                    _check_sun(current_weather.time.sun)
                    and current_weather.time > prev_weather.time
                ):
                    time_ticket = _generate_time_ticket(current_weather.time)
                    return 600 <= time_ticket <= 1800
        return False

    def append(self, time: EorzeaTime, raw_weather: int):
        self._weather_slot.append(
            WeatherInfo(time=copy.copy(time), raw_weather=raw_weather)
        )


def _is_rainbow_possible(place_name: EorzeaPlaceName) -> bool:
    weather_rate_index = _territory_weather[place_name.index]
    weather_rate = _weather_rate[weather_rate_index]
    possible_weathers: Set[int] = {w[1] for w in weather_rate}
    return bool(
        possible_weathers - RAINY_WEATHERS and RAINY_WEATHERS & possible_weathers
    )


def _check_sun(sun: int):
    return sun >= 27 or sun <= 6


def _generate_time_ticket(time: EorzeaTime) -> int:
    return time.hour * 100 + time.minute
