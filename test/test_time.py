import time
from datetime import datetime

import pytest
from EorzeaEnv import EorzeaTime


class TestTime:
    def test_weather_period(self):
        timelist = [t for t in EorzeaTime.weather_period(10)]
        assert len(timelist) == 10

        count = 0
        for _ in EorzeaTime.weather_period(step="inf"):
            count += 1
            if count == 1000:
                break

        assert count == 1000

        with pytest.raises(TypeError):
            for _ in EorzeaTime.weather_period("many"):  # type: ignore
                pass

        with pytest.raises(TypeError):
            for _ in EorzeaTime.weather_period([1, 2, 3]):  # type: ignore
                pass

        future_date = datetime(3000, 3, 3, 3, 3)
        for t in EorzeaTime.weather_period(step=10, from_=future_date.timestamp()):
            assert t.get_unix_time() > datetime.now().timestamp()

    def test_time_operator(self):
        t1 = EorzeaTime(12345678)
        t2 = EorzeaTime(12345700)

        assert t1 < t2
        assert t1 <= t2
        assert t1 != t2
        assert not t1 >= t2
        assert not t1 > t1

        fixed_ts = time.time()
        t1 = EorzeaTime(fixed_ts)
        t2 = EorzeaTime(fixed_ts)
        assert t1 == t2

        t1 = EorzeaTime.now()
        t2 = EorzeaTime.now()
        assert t1 == t2

        with pytest.raises(TypeError):
            assert t1 > 1
        with pytest.raises(TypeError):
            assert t1 >= 1
        with pytest.raises(TypeError):
            assert not t1 <= 1
        with pytest.raises(TypeError):
            assert t1 < 1
        assert t1 != 1
        assert not t1 == 1

    def test_positive_rollover(self):
        et = EorzeaTime()
        et.minute = 59
        et.bell = 23
        et.sun = 32
        et.moon = 12
        et.year = 999

        et.minute += 1

        assert et.minute == 0
        assert et.bell == 0
        assert et.sun == 1
        assert et.moon == 1
        assert et.year == 1000

        et.minute += 121

        assert et.minute == 1
        assert et.bell == 2

        et.bell += 49

        assert et.bell == 3
        assert et.sun == 3

    def test_negative_rollover(self):
        et = EorzeaTime()
        et.minute = 0
        et.bell = 0
        et.sun = 1
        et.moon = 2
        et.year = 1000

        et.minute -= 1

        assert et.minute == 59
        assert et.bell == 23
        assert et.sun == 32
        assert et.moon == 1

        et.minute -= 119

        assert et.minute == 0
        assert et.bell == 22

        et.bell -= 48

        assert et.minute == 0
        assert et.bell == 22
        assert et.sun == 30
        assert et.moon == 1

        et.moon -= 11

        assert et.moon == 2
        assert et.year == 999

    def test_property(self):
        ts = 12700000
        et = EorzeaTime(ts)
        assert et.guardian == "Nophica"
        assert et.moon_phase == 0.75
        assert et.moon_name == "Sixth Astral Moon"

        ts = 12879000
        et = EorzeaTime(ts)
        assert et.guardian == "Althyk"
        assert et.moon_phase == 0.50
        assert et.moon_name == "Sixth Embral Moon"

    def test_repr(self):
        et = EorzeaTime.now()
        assert repr(et) == f"EorzeaTime({et.get_unix_time()})"

    def test_act_as_str(self):
        et = EorzeaTime.now()
        assert str(et)

    def test_weather_period_start(self):
        # window 8818 covers [12345200, 12346600); start is 12345200
        et = EorzeaTime(12346000)
        start = et.weather_period_start()
        assert start.get_unix_time() == 12345200

        # any time within the same window shares the same start
        assert EorzeaTime(12345200).weather_period_start().get_unix_time() == 12345200
        assert EorzeaTime(12346599).weather_period_start().get_unix_time() == 12345200

        # a time in the next window has a different start
        assert EorzeaTime(12346600).weather_period_start().get_unix_time() == 12346600

    def test_prev_weather_period_start(self):
        # window 8818: [12345200, 12346600), prev window 8817: [12343800, 12345200)
        et = EorzeaTime(12346000)
        prev = et.prev_weather_period_start()
        assert prev.get_unix_time() == 12343800

        # any time in the same window yields the same prev start
        assert (
            EorzeaTime(12345200).prev_weather_period_start().get_unix_time() == 12343800
        )
        assert (
            EorzeaTime(12346599).prev_weather_period_start().get_unix_time() == 12343800
        )

    def test_is_same_weather_period(self):
        # window 8818 covers [12345200, 12346600)
        t1 = EorzeaTime(12345200)
        t2 = EorzeaTime(12346599)
        assert t1.is_same_weather_period(t2)
        assert t2.is_same_weather_period(t1)

        # 12346600 starts window 8819
        t3 = EorzeaTime(12346600)
        assert not t1.is_same_weather_period(t3)

    def test_is_next_weather_period(self):
        # window 8818: [12345200, 12346600), window 8819: [12346600, 12348000)
        t1 = EorzeaTime(12345200)
        t2 = EorzeaTime(12346600)
        assert t1.is_next_weather_period(t2)
        assert t2.is_next_weather_period(t1)

        # two windows apart — not adjacent
        t3 = EorzeaTime(12348000)
        assert not t1.is_next_weather_period(t3)

        # same window — not adjacent
        t4 = EorzeaTime(12346000)
        assert not t1.is_next_weather_period(t4)
