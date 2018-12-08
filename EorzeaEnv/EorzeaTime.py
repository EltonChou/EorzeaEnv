from time import time as _time


class EorzeaTime:
    '''EorzeaTime(hour, minute)
    '''

    __slots__ = '_hour', '_minute'

    _DAY = 86400
    _HOUR = 3600
    _MINUTE = 60
    _SECOND = 1
    _EORZEA_MINUTE = 60
    _EORZEA_BELL = 60
    _EORZEA_SUN = 24
    _EORZEA_TIME_CONST = 3600.0 / 175.0
    _MILLISECOND_EORZEA_PER_MINUTE = (2 + 11/12) * 1000

    def __new__(cls, hour, minute):
        self = object.__new__(cls)
        hour, minute = _check_time_field(hour, minute)
        self._hour = hour
        self._minute = minute
        return self

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @classmethod
    def now(cls):
        '''Eorzea current time
        '''
        t = _time()
        return cls._fromtimestamp(t)

    @classmethod
    def _fromtimestamp(cls, t):
        et = t * cls._EORZEA_TIME_CONST
        h = int(et / cls._HOUR % cls._EORZEA_SUN)
        m = int(et / cls._MINUTE % cls._EORZEA_BELL)
        return cls(h, m)

    @classmethod
    def next_weather_period_start(cls, step=5):
        '''
        default step value is 5
        '''
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

    def __repr__(self):
        return "{}({}, {})".format(
            self.__class__.__qualname__,
            self._hour, self._minute)


def _weather_period_generator(min, step):
        n, i = 0, min
        while n < step:
            yield i
            i += 1400
            n += 1


def _check_time_field(hour, minute):
    hour = _check_int_field(hour)
    minute = _check_int_field(minute)
    if not 0 <= hour <= 23:
        raise ValueError('hour must be in 0..23', hour)
    if not 0 <= minute <= 59:
        raise ValueError('minute must be in 0..59', minute)
    return hour, minute


def _check_int_field(value):
    if isinstance(value, int):
        return value
    raise TypeError("integer argument required")
