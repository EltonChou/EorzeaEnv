import time
from datetime import datetime

import pytest
from EorzeaEnv import EorzeaTime


class TestTime:
    def test_weather_period(self):
        timelist = [t for t in EorzeaTime.weather_period(10)]
        assert len(timelist) == 10

        count = 0
        for _ in EorzeaTime.weather_period(step='inf'):
            count += 1
            if count == 1000:
                break

        assert count == 1000

        with pytest.raises(TypeError):
            for _ in EorzeaTime.weather_period('many'):  # type: ignore
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

    def test_property(self):
        ts = 12700000
        et = EorzeaTime(ts)
        assert et.guardian == 'Nophica'
        assert et.moon_phase == 0.75
        assert et.moon_name == 'Sixth Astral Moon'

        ts = 12879000
        et = EorzeaTime(ts)
        assert et.guardian == 'Althyk'
        assert et.moon_phase == 0.50
        assert et.moon_name == 'Sixth Embral Moon'

        et = EorzeaTime()
        et.moon += 13
        et.sun += 33
        et.bell += 26
        et.minute += 65
        et.moon -= 13
        et.sun -= 33
        et.bell -= 26
        et.minute -= 65

    def test_repr(self):
        et = EorzeaTime.now()
        assert repr(et) == f'EorzeaTime({et.get_unix_time()})'

    def test_act_as_str(self):
        et = EorzeaTime.now()
        assert str(et)
