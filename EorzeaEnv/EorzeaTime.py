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
    __EORZEA_TIME_CONSTANT = 3600.0 / 175.0
    __MILLISECOND_EORZEA_PER_MINUTE = (2 + 11/12) * 1000

    @classmethod
    def current_time_stamp(cls, lts=None):
        if not lts:
            lts = _dt.now().timestamp()
        return lts * cls.__EORZEA_TIME_CONSTANT

    @classmethod
    def current_stamp_to_local(cls, cts):
        return cts / cls.__EORZEA_TIME_CONSTANT

    @classmethod
    def current_hour(cls, lts=None):
        return int(cls.current_time_stamp(lts) / cls.__HOUR % cls.__EORZEA_SUN)

    @classmethod
    def current_minute(cls, lts=None):
        return int(cls.current_time_stamp(lts) / cls.__MINUTE % cls.__EORZEA_BELL)

    @classmethod
    def current_weather_period_start(cls, lts=None):
        return cls.current_stamp_to_local(
            int(cls.current_time_stamp(lts) / cls.__HOUR)
            * cls.__HOUR)
