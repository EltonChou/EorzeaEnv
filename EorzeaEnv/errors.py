class EorzeaEnvError(Exception):
    ...


class InvalidEorzeaPlaceName(EorzeaEnvError, ValueError):
    def __init__(self, *, place_name: str, is_strict: bool) -> None:
        mode_msg = 'strict' if is_strict else 'fuzzy'
        message = f'`{place_name}` is not a valid Eorzea placename in {mode_msg} mode.)'
        super().__init__(message)


class WeatherRateDataError(EorzeaEnvError):
    ...
