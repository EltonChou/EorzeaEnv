import pytest
from EorzeaEnv import EorzeaTime
import time


class TestTime:
    def test_weather_period(self):
        timelist = [t for t in EorzeaTime.weather_period(10)]
        assert len(timelist) == 10
        # assert all((type(t) is int for t in timelist))

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

    def test_get_eorzea_timestamp(self):
        ts = time.time()
        assert EorzeaTime.get_eorzea_timestamp(ts) == int(round(ts * (3600 / 175)))

    def test_repr(self):
        et = EorzeaTime.now()
        assert repr(et) == f'EorzeaTime({et.get_unix_time()})'

    def test_act_as_str(self):
        et = EorzeaTime.now()
        assert str(et)
