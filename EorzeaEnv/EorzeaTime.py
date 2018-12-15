from time import time as _time
import math
from decimal import Decimal


class EorzeaTime:
    """EorzeaTime(hour, minute)"""

    __slots__ = '_hour', '_minute', '_phase'

    _DAY = 86400
    _HOUR = 3600
    _MINUTE = 60
    _SECOND = 1
    _EORZEA_MINUTE = 60
    _EORZEA_BELL = 60
    _EORZEA_SUN = 24
    _EORZEA_MOON = 32
    _EORZEA_TIME_CONST = 3600.0 / 175.0
    _MILLISECOND_EORZEA_PER_MINUTE = (2 + 11/12) * 1000

    def __new__(cls, hour, minute, phase):
        self = object.__new__(cls)
        hour, minute = _check_time_field(hour, minute)
        phase = _check_phase_field(phase)
        self._hour = hour
        self._minute = minute
        self._phase = phase
        return self

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def phase(self):
        return self._phase

    @classmethod
    def now(cls):
        """Eorzea current time."""

        t = _time()
        return cls._fromtimestamp(t)

    @classmethod
    def _fromtimestamp(cls, t):
        et = t * cls._EORZEA_TIME_CONST
        hh = int(et / cls._HOUR % cls._EORZEA_SUN)
        mm = int(et / cls._MINUTE % cls._EORZEA_BELL)
        sun = math.ceil(et / cls._DAY % cls._EORZEA_MOON)
        moon_phase = _calculate_pphase(sun)
        return cls(hh, mm, moon_phase)

    @classmethod
    def weather_period(cls, step=5):
        """default step value is 5"""

        if not isinstance(step, int):
            raise ValueError("step argument must be an 'int' instance")

        time = _weather_period_generator(cls._weather_period_start(), step)
        return time

    @classmethod
    def _weather_period_start(cls):
        t = _time()
        et = t * cls._EORZEA_TIME_CONST
        lt = int(et / 28800) * 28800 / cls._EORZEA_TIME_CONST
        return lt

    def _cls_to_str(self):
        return "{}({:02d}, {:02d}, {:.2f})".format(
            self.__class__.__qualname__,
            self._hour, self._minute, self._phase)

    def __repr__(self):
        return self._cls_to_str()

    def __str__(self):
        return self._cls_to_str()


def _weather_period_generator(min, step):
    n, i = 0, min
    while n < step:
        yield i
        i += 1400
        n += 1


def _calculate_phase(sun):
    sun = _check_sun_field(sun)
    if sun <= 20:
        return 1 - int(abs(20 - sun) / 4) / 4
    if sun > 20:
        return int(abs(36 - sun) / 4) / 4


def _calculate_pphase(sun):
    if sun <= 20:
        return round((sun - 1) / 19, 2)
    if sun >= 20:
        return round(1 - (sun - 20) / 13, 2)


def _check_time_field(hour, minute):
    hour = _check_int_field(hour)
    minute = _check_int_field(minute)
    if not 0 <= hour <= 23:
        raise ValueError('hour must be in 0..23', hour)
    if not 0 <= minute <= 59:
        raise ValueError('minute must be in 0..59', minute)
    return hour, minute


def _check_sun_field(sun):
    if not 1 <= sun <= 32:
        raise ValueError('sun must be in 1..32', sun)
    return sun


def _check_phase_field(phase):
    if not 0 <= phase <= 1:
        raise ValueError('phase must be in 0..1', phase)
    return phase


def _check_int_field(value):
    if not isinstance(value, int):
        raise TypeError("integer argument required")
    return value
