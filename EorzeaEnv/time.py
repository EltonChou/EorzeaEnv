from __future__ import annotations

import math
from datetime import datetime, timezone
from time import time as _time
from typing import Final, Iterator, Literal, Optional

_EORZEA_TIME_CONST: Final = 3600.0 / 175.0
_LOCAL_WEATHER_INTERVAL: Final = 1400
# _EROZEA_WEATHER_INTERVAL = 28800
_DATETIME_ZERO: Final = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
_GUARDIANS: Final = (
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
    "Althyk",
)
_MOON_PREFIXS: Final = ("First", "Second", "Third", "Fourth", "Fifth", "Sixth")


class EorzeaTime:
    """Converts Unix timestamps to Eorzea in-game time.

    Examples
    --------
    ```python
    et = EorzeaTime.now()
    str(et)       # 'EorzeaTime(Sixth Embral Moon, 11, 21, 56, Phase:0.50, Althyk)'
    et.moon_name  # 'Sixth Embral Moon'
    et.sun        # 11
    et.hour       # 21
    et.minute     # 56
    et.moon_phase # 0.5
    et.guardian   # 'Althyk'
    et.get_unix_time()    # 1661114514
    et.get_eorzea_time()  # 34177649220
    ```

    Generate weather periods (each step is one 8-bell weather window):

    ```python
    periods = tuple(EorzeaTime.weather_period(step=3))
    periods = tuple(EorzeaTime.weather_period(step=3, from_=1661184000.0))

    # Use step='inf' for an infinite generator
    for t in EorzeaTime.weather_period(step='inf'):
        ...
    ```
    """

    _bell: int
    _minute: int
    _moon: int
    _sun: int
    _year: int

    _last_now_update: int = int(round(_time()))
    _now: Optional["EorzeaTime"] = None

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

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def moon(self):
        return self._moon

    @moon.setter
    def moon(self, value):
        self._moon = value
        while self._moon < 1:
            self._moon += 12
            self.year = self.year - 1

        while self._moon > 12:
            self._moon -= 12
            self.year = self.year + 1

    @property
    def sun(self):
        return self._sun

    @sun.setter
    def sun(self, value):
        self._sun = value
        while self._sun < 1:
            self._sun += 32
            self.moon = self.moon - 1

        while self._sun > 32:
            self._sun -= 32
            self.moon = self.moon + 1

    @property
    def hour(self):
        return self.bell

    @property
    def bell(self):
        return self._bell

    @bell.setter
    def bell(self, value):
        self._bell = value
        while self._bell < 0:
            self._bell += 24
            self.sun = self.sun - 1

        while self._bell >= 24:
            self._bell -= 24
            self.sun = self.sun + 1

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        self._minute = value
        while self._minute < 0:
            self._minute += 60
            self.bell = self.bell - 1

        while self._minute >= 60:
            self._minute -= 60
            self.bell = self.bell + 1

    @property
    def moon_phase(self):
        return _calculate_phase(self.sun)

    @property
    def guardian(self):
        return _get_guardian_by_moon(self.moon)

    @property
    def moon_name(self):
        return _calculate_moon(self.moon)

    def get_eorzea_time(self) -> int:
        years = self.year
        moons = (years * 12) + self.moon - 1
        suns = (moons * 32) + self.sun - 1
        bells = (suns * 24) + self.bell
        minutes = (bells * 60) + self.minute
        seconds = minutes * 60

        return seconds

    def get_unix_time(self) -> int:
        et = self.get_eorzea_time()
        return round(et / _EORZEA_TIME_CONST)

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
    def weather_period(
        cls, step: int | Literal["inf"] = 5, from_: Optional[float] = None
    ) -> Iterator["EorzeaTime"]:
        """
        generate weather period

        Parameters
        ----------
        step : int | Literal['inf'], optional
            quantity of period you want, by default 5.
            'inf' means infinite.

        from_ : Optional[float]
            The base timestamp for calculate the weather period.

        Returns
        -------
        Iterator[EorzeaTime]
            a generator of weather period.
        """

        if not isinstance(step, (int, str)):
            raise TypeError("integer or Literal['inf'] argument required")

        if type(step) is str:
            if step != "inf":
                raise TypeError("integer or Literal['inf'] argument required")

        ts = from_ or _time()
        weather_start = cls(timestamp=ts - (ts % _LOCAL_WEATHER_INTERVAL))

        current_step = 0
        while True if step == "inf" else current_step < step:
            yield weather_start
            weather_start.bell = weather_start.bell + 8
            current_step += 1

    def __repr__(self):
        return "{}({})".format(self.__class__.__qualname__, self.get_unix_time())

    def __str__(self):
        return "{}({}, {}, {:02d}, {:02d}, Phase:{:.2f}, {})".format(
            self.__class__.__qualname__,
            self.moon_name,
            self.sun,
            self.hour,
            self.minute,
            self.moon_phase,
            self.guardian,
        )

    def weather_period_start(self) -> "EorzeaTime":
        """Return a new EorzeaTime at the start of this time's 8-bell weather period."""
        ts = self.get_unix_time()
        return EorzeaTime(ts - (ts % _LOCAL_WEATHER_INTERVAL))

    def prev_weather_period_start(self) -> "EorzeaTime":
        """Return a new EorzeaTime at the start of the preceding weather period."""
        ts = self.get_unix_time()
        return EorzeaTime(ts - (ts % _LOCAL_WEATHER_INTERVAL) - _LOCAL_WEATHER_INTERVAL)

    def is_same_weather_period(self, that: "EorzeaTime") -> bool:
        """Return True if both times fall within the same 8-bell weather period."""
        return (
            self.get_unix_time() // _LOCAL_WEATHER_INTERVAL
            == that.get_unix_time() // _LOCAL_WEATHER_INTERVAL
        )

    def is_next_weather_period(self, that: "EorzeaTime") -> bool:
        """Return True if the two times are in adjacent weather periods."""
        return (
            abs(
                self.get_unix_time() // _LOCAL_WEATHER_INTERVAL
                - that.get_unix_time() // _LOCAL_WEATHER_INTERVAL
            )
            == 1
        )

    def __lt__(self, that: object):
        if isinstance(that, self.__class__):
            return self.get_unix_time() < that.get_unix_time()
        return NotImplemented

    def __le__(self, that: object):
        if isinstance(that, self.__class__):
            return self.get_unix_time() <= that.get_unix_time()
        return NotImplemented

    def __eq__(self, that: object):
        if isinstance(that, self.__class__):
            return self.get_unix_time() == that.get_unix_time()
        return NotImplemented

    def __ne__(self, that: object):
        if isinstance(that, self.__class__):
            return self.get_unix_time() != that.get_unix_time()
        return NotImplemented

    def __ge__(self, that: object):
        if isinstance(that, self.__class__):
            return self.get_unix_time() >= that.get_unix_time()
        return NotImplemented

    def __gt__(self, that: object):
        if isinstance(that, self.__class__):
            return self.get_unix_time() > that.get_unix_time()
        return NotImplemented


def _get_guardian_by_moon(moon: int) -> str:
    return _GUARDIANS[moon - 1]


def _calculate_moon(moon: int) -> str:
    moon_order = _MOON_PREFIXS[math.ceil(moon / 2) - 1]
    moon_type = _astral_or_embral(moon)
    return "{} {} Moon".format(moon_order, moon_type)


def _astral_or_embral(moon: int) -> str:
    return "Astral" if moon % 2 else "Embral"


def _calculate_phase(sun: int) -> float:
    if sun <= 20:
        return 1 - int(abs(20 - sun) / 4) / 4
    else:
        return int(abs(36 - sun) / 4) / 4
