import pytest

from EorzeaEnv import EorzeaTime


class TestTime:
    def test_step(self):
        timelist = [t for t in EorzeaTime.weather_period(10)]
        assert len(timelist) is 10

    def test_time(self):
        assert isinstance(EorzeaTime.now().minute, int)
        assert isinstance(EorzeaTime.now().hour, int)
        test_time = (
            (13, 1, 10, 50),
            (12, 35, 10, 50),
            (12, 1, 25, 50),
            (12, 1, 10, 61)
        )
        with pytest.raises(ValueError):
            for t in test_time:
                M, S, h, m = t
                EorzeaTime(M, S, h, m)
        with pytest.raises(TypeError):
            EorzeaTime("kappa", 1, 10, 50)
