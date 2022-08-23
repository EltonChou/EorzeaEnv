import pytest
from EorzeaEnv import EorzeaTime


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
            EorzeaTime("kappa", 1, 10, 50)  # type: ignore
