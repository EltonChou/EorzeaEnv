import math
from time import time as _time


class EorzeaTime:
    """EorzeaTime(moon, sun, hour, minute)"""

    __slots__ = '_moon', '_sun', '_hour', '_minute', '_phase', '_guardian'

    _YEAR = 33177600
    _MOON = 2764800
    _DAY = 86400
    _HOUR = 3600
    _MINUTE = 60
    _SECOND = 1
    _EORZEA_MINUTE = 60
    _EORZEA_BELL = 60
    _EORZEA_SUN = 24
    _EORZEA_MOON = 32
    _EORZEA_YEAR = 12
    _EORZEA_TIME_CONST = 3600.0 / 175.0
    _MILLISECOND_EORZEA_PER_MINUTE = (2 + 11/12) * 1000

    def __new__(cls, moon, sun, hour, minute):
        self = object.__new__(cls)
        hour, minute = _check_time_field(hour, minute)
        moon, sun = _check_date_field(moon, sun)
        phase = _calculate_phase(sun)
        self._moon = _calculate_moon(moon)
        self._sun = sun
        self._hour = hour
        self._minute = minute
        self._phase = _check_phase_field(phase)
        self._guardian = _the_twelve(moon)
        return self

    @property
    def moon(self):
        return self._moon

    @property
    def sun(self):
        return self._sun

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def phase(self):
        return self._phase

    @property
    def guardian(self):
        return self._guardian

    @classmethod
    def now(cls):
        """Eorzea current time."""

        t = _time()
        return cls._fromtimestamp(t)

    @classmethod
    def _fromtimestamp(cls, t):
        et = t * cls._EORZEA_TIME_CONST
        moon = math.ceil(et / cls._MOON % cls._EORZEA_YEAR)
        sun = math.ceil(et / cls._DAY % cls._EORZEA_MOON)
        hh = int(et / cls._HOUR % cls._EORZEA_SUN)
        mm = int(et / cls._MINUTE % cls._EORZEA_BELL)
        return cls(moon, sun, hh, mm)

    @classmethod
    def weather_period(cls, step=5):
        """default step value is 5"""

        time = _weather_period_generator(cls._weather_period_start(), step)
        return time

    @classmethod
    def _weather_period_start(cls):
        t = _time()
        et = t * cls._EORZEA_TIME_CONST
        lt = int(et / 28800) * 28800 / cls._EORZEA_TIME_CONST
        return lt

    def _cls_to_str(self):
        return "{}({}, {}, {:02d}, {:02d}, {:.2f}, {})".format(
            self.__class__.__qualname__,
            self._moon, self._sun,
            self._hour, self._minute, self._phase,
            self._guardian)

    def __repr__(self):
        return self._cls_to_str()

    def __str__(self):
        return self._cls_to_str()


def check_int(func):
    def wrap(*values):
        for value in values:
            if not isinstance(value, int):
                raise TypeError("integer argument required")
        return func(*values)
    return wrap


def _weather_period_generator(min, step):
    if not isinstance(step, int):
        raise TypeError("integer argument required")
    n, i = 0, min
    while n < step:
        yield i
        i += 1400
        n += 1


def _the_twelve(moon):
    the_twelve = [
        "Halone",
        "Menphina",
        "Thaliak",
        "Nymeia",
        "Llymlaen",
        "Oschon",
        "Byregot",
        "Rhalgr",
        "Azeyma",
        "Nald'thal",
        "Nophica",
        "Althyk"
    ]
    return the_twelve[moon - 1]


def _calculate_moon(moon):
    th = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth"]
    M_th = th[math.ceil(moon / 2) - 1]
    M_type = _astral_or_embral(moon)
    return "{} {} Moon".format(M_th, M_type)


def _astral_or_embral(moon):
    return "Astral" if moon % 2 else "Embral"


def _calculate_phase(sun):
    if sun <= 20:
        return 1 - int(abs(20 - sun) / 4) / 4
    if sun > 20:
        return int(abs(36 - sun) / 4) / 4


def _calculate_pphase(sun):
    if sun <= 20:
        return round((sun - 1) / 19, 2)
    if sun >= 20:
        return round(1 - (sun - 20) / 13, 2)


@check_int
def _check_time_field(hour, minute):
    if not 0 <= hour <= 23:
        raise ValueError('hour must be in 0..23', hour)
    if not 0 <= minute <= 59:
        raise ValueError('minute must be in 0..59', minute)
    return hour, minute


@check_int
def _check_date_field(moon, sun):
    if not 1 <= moon <= 12:
        raise ValueError('moon must be in 1..12', moon)
    if not 1 <= sun <= 32:
        raise ValueError('sun must be in 1..32', sun)
    return moon, sun


def _check_phase_field(phase):
    if not 0 <= phase <= 1:
        raise ValueError('phase must be in 0..1', phase)
    return phase


if __name__ == "__main__":
    while True:
        t = str(EorzeaTime.now())
        print("\r"+t, end="")
