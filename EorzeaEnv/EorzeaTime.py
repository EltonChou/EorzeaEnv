from datetime import datetime as _dt


class EorzeaTime:
    __YEAR = 33177600
    __MONTH = 2764800
    __DAY = 86400
    __HOUR = 3600
    __MINUTE = 60
    __SECOND = 1
    __EORZEA_MINUTE = 60
    __EORZEA_BELL = 60
    __EORZEA_SUN = 24
    __EORZEA_TIME_CONST = 3600.0 / 175.0
    __MILLISECOND_EORZEA_PER_MINUTE = (2 + 11/12) * 1000

    def __init__(self, lts=None):
        self._localtimestamp = lts or _dt.now().timestamp()
        self._current_stamp = self._localtimestamp * self.__EORZEA_TIME_CONST

    @property
    def localtimestamp(self):
        return self._localtimestamp

    @property
    def current_stamp(self):
        return self._current_stamp

    @localtimestamp.setter
    def localtimestamp(self, x):
        self._localtimestamp = x

    @current_stamp.setter
    def current_stamp(self, x):
        self._current_stamp = x

    @classmethod
    def current_hour(cls):
        return int(_dt.now().timestamp() / cls.__HOUR % cls.__EORZEA_SUN)

    @classmethod
    def current_minute(cls):
        return int(_dt.now().timestamp() / cls.__MINUTE % cls.__EORZEA_BELL)

    def current_stamp_to_local(self, cts):
        return cts / self.__EORZEA_TIME_CONST

    def weather_period_start(self):
        return self.current_stamp_to_local(
            (int(self.current_stamp / 28800) * 28800))

    def next_weather_period_start(self, step=None):
        if not step:
            step = 5
        if step > 10:
            step = 10
        nextTime = list(range(step))
        for i in range(step):
            if i is not 0:
                self.current_stamp = (self.current_stamp + 28800)
            nextTime[i] = self.weather_period_start()
        return nextTime
