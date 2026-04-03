from typing import Protocol

from EorzeaEnv import EorzeaPlaceName, EorzeaTime


class SpecialWeather(Protocol):
    @property
    def place_name(self) -> EorzeaPlaceName:
        """The place being observed."""
        ...

    @property
    def is_possible(self) -> bool:
        """Return True if this special weather can ever occur at :attr:`place_name`."""
        ...

    def forecast(self, time: EorzeaTime) -> EorzeaTime | None:
        """Return the start time of the special weather within *time*'s weather window.

        Returns ``None`` when the special weather does not appear in that window
        or :attr:`is_possible` is ``False``.
        """
        ...
