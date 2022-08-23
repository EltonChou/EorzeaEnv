import math
from datetime import datetime, timezone
from time import time as _time
from typing import Iterator, Literal, Optional, Union

_EORZEA_TIME_CONST = 3600.0 / 175.0
_LOCAL_WEATHER_INTERVAL = 1400
# _EROZEA_WEATHER_INTERVAL = 28800
_DATETIME_ZERO = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)


class EorzeaTime:
    """
    EorzeaTime
    """
    _bell: int
    _minute: int
    _moon: int
    _sun: int
    _year: int

    _last_now_update: int = int(round(_time()))
    _now: Optional['EorzeaTime'] = None

    def __init__(self, timestamp: Optional[float] = None):
        ts = timestamp or _time()
        et = ts * _EORZEA_TIME_CONST
        minutes = et / 60
        bells = minutes / 60
        suns = bells / 24
        moons = suns / 32
        years = moons / 12

        self._minute = int(minutes % 60)
        self._bell = int(bells % 24)
        self._sun = int(suns % 32) + 1
        self._moon = int(moons % 12) + 1
        self._year = int(years)

    @property
    def year(self):
        return self._year

    @property
    def moon(self):
        return self._moon

    @property
    def sun(self):
        return self._sun

    @property
    def hour(self):
        return self.bell

    @property
    def bell(self):
        return self._bell

    @property
    def minute(self):
        return self._minute

    @property
    def moon_phase(self):
        return _calculate_phase(self.sun)

    @property
    def guardian(self):
        return _get_guardian_by_moon(self.moon)

    @property
    def moon_name(self):
        return _calculate_moon(self.moon)

    def get_unix_time(self) -> float:
        years = self.year
        moons = (years * 12) + self.moon - 1
        suns = (moons * 32) + self.sun - 1
        bells = (suns * 24) + self.bell
        minutes = (bells * 60) + self.minute
        seconds = minutes * 60

        return seconds / _EORZEA_TIME_CONST

    @classmethod
    def now(cls):
        now = _time()
        diff = now - cls._last_now_update
        if diff <= 1 and cls._now:
            return cls._now

        cls._now = cls()
        cls._last_now_update = int(round(now))
        return cls._now

    @classmethod
    def weather_period(cls, step: Union[int, Literal['inf']] = 5) -> Iterator[int]:
        """
        generate weather period

        Parameters
        ----------
        step : Union[int, Literal['inf']], optional
            quantity of period you want, by default 5.
            'inf' means infinite.

        Returns
        -------
        Iterator[float]
            a generator of weather period
        """

        ts = int(round(_time()))
        weather_start_ts = ts - (ts % _LOCAL_WEATHER_INTERVAL)

        if not isinstance(step, (int, str)):
            raise TypeError("integer or Literal['inf'] argument required")

        if type(step) is str:
            if step != 'inf':
                raise TypeError("integer or Literal['inf'] argument required")

        current_step = 0

        while True if step == 'inf' else current_step < step:
            yield weather_start_ts
            weather_start_ts += _LOCAL_WEATHER_INTERVAL
            current_step += 1

    @staticmethod
    def get_eorzea_timestamp(timestamp: Optional[float] = None) -> int:
        ts = timestamp or _time()
        return int(round(ts * _EORZEA_TIME_CONST))

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__qualname__,
            self.get_unix_time()
        )

    def __str__(self):
        return "{}({}, {}, {:02d}, {:02d}, Phase:{:.2f}, {})".format(
            self.__class__.__qualname__,
            self.moon_name, self.sun,
            self.hour, self.minute, self.moon_phase,
            self.guardian
        )

    def __lt__(self, that: 'EorzeaTime'):
        return self.get_unix_time() < that.get_unix_time()

    def __le__(self, that: 'EorzeaTime'):
        return self.get_unix_time() <= that.get_unix_time()

    def __eq__(self, that: 'EorzeaTime'):
        return self.get_unix_time() == that.get_unix_time()

    def __ne__(self, that: 'EorzeaTime'):
        return self.get_unix_time() != that.get_unix_time()

    def __ge__(self, that: 'EorzeaTime'):
        return self.get_unix_time() >= that.get_unix_time()

    def __gt__(self, that: 'EorzeaTime'):
        return self.get_unix_time() > that.get_unix_time()


def _get_guardian_by_moon(moon: int) -> str:
    the_twelve = (
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
    )
    return the_twelve[moon - 1]


def _calculate_moon(moon: int) -> str:
    moon_orders = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth"]
    moon_order = moon_orders[math.ceil(moon / 2) - 1]
    moon_type = _astral_or_embral(moon)
    return "{} {} Moon".format(moon_order, moon_type)


def _astral_or_embral(moon: int) -> str:
    return "Astral" if moon % 2 else "Embral"


def _calculate_phase(sun: int) -> float:
    if sun <= 20:
        return 1 - int(abs(20 - sun) / 4) / 4
    else:
        return int(abs(36 - sun) / 4) / 4
