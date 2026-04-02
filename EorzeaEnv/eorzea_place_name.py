from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Final, List, Mapping

from rapidfuzz import process as fuzz_process

from .Data.PlaceName import PlaceInfoDict
from .Data.PlaceName import place_name as _place_names
from .eorzea_lang import EorzeaLang
from .errors import InvalidEorzeaPlaceName

FuzzyCutoff = int | float
LocaleScope = EorzeaLang | str

DEFAULT_CUTOFF: Final = 80
DEFAULT_LOCALE_SCOPES: Final[List[LocaleScope]] = [
    EorzeaLang.EN,
    EorzeaLang.JA,
    EorzeaLang.FR,
    EorzeaLang.DE,
    EorzeaLang.KO,
    EorzeaLang.ZH_TC,
    EorzeaLang.ZH_SC,
]


@dataclass
class PlaceInfo:
    index: int
    place_name: str


class EorzeaPlaceName:
    """Validates and normalizes an FFXIV location name.

    An ``EorzeaPlaceName`` instance is always a valid place name in EorzeaEnv.
    Construction raises :class:`EorzeaEnv.errors.InvalidEorzeaPlaceName` if the
    name cannot be resolved.

    Parameters
    ----------
    place_name : str
        A valid Eorzea place name (case-insensitive, leading "the" is stripped).
    strict : bool
        ``True`` for strict (exact) matching, ``False`` for fuzzy matching.
        By default ``True``.
    locale_scopes : List[LocaleScope]
        Locales to search when resolving the name. By default all supported
        locales (EN, JA, FR, DE, KO, ZH_TC, ZH_SC).
    fuzzy_cutoff : float
        Minimum similarity score for fuzzy matching (0–100). By default 80.

    Raises
    ------
    :class:`EorzeaEnv.errors.InvalidEorzeaPlaceName`
        When the place name cannot be resolved.

    Examples
    --------
    Strict mode (default) accepts substrings and any locale:

    ```python
    EorzeaPlaceName('The Ruby Sea')  # EorzeaPlaceName('The Ruby Sea')
    EorzeaPlaceName('the ruby sea')  # EorzeaPlaceName('The Ruby Sea')
    EorzeaPlaceName('ruby sea')      # EorzeaPlaceName('The Ruby Sea')
    EorzeaPlaceName('rubinsee')      # EorzeaPlaceName('Rubinsee')
    EorzeaPlaceName('紅玉海')         # EorzeaPlaceName('紅玉海')
    ```

    Restrict to specific locales:

    ```python
    scopes = [EorzeaLang.JA, EorzeaLang.DE]
    EorzeaPlaceName('rubinsee', locale_scopes=scopes)      # EorzeaPlaceName('Rubinsee')
    EorzeaPlaceName('The Ruby Sea', locale_scopes=scopes)  # raises
    ```

    Fuzzy mode tolerates typos:

    ```python
    # EorzeaPlaceName('The Ruby Sea')
    EorzeaPlaceName('the ruby see', strict=False)
    # EorzeaPlaceName('紅玉海')
    EorzeaPlaceName('紅玉貝', strict=False, fuzzy_cutoff=66)
    ```
    """

    __index: int
    __value: str

    def __init__(
        self,
        place_name: str,
        strict: bool = True,
        locale_scopes: List[LocaleScope] = DEFAULT_LOCALE_SCOPES,
        fuzzy_cutoff: FuzzyCutoff = DEFAULT_CUTOFF,
    ) -> None:
        place_info = _validate_place_name(
            place_name,
            is_strict=strict,
            fuzzy_cutoff=fuzzy_cutoff,
            locale_scopes=locale_scopes,
        )

        self.__index = place_info.index
        self.__value = place_info.place_name

    @property
    def value(self):
        return self.__value

    @property
    def index(self):
        return self.__index

    @staticmethod
    def validate(
        place_name: str | EorzeaPlaceName,
        strict: bool,
        locale_scopes: List[LocaleScope] = DEFAULT_LOCALE_SCOPES,
        fuzzy_cutoff: FuzzyCutoff = DEFAULT_CUTOFF,
    ) -> bool:
        """Check whether a place name is valid without raising an exception.

        An ``EorzeaPlaceName`` instance always returns ``True``. For strings,
        validation follows the same rules as the constructor.

        Parameters
        ----------
        place_name : str | EorzeaPlaceName
            The place name to validate.
        strict : bool
            ``True`` for strict (exact) matching, ``False`` for fuzzy matching.
        locale_scopes : List[LocaleScope]
            Locales to search. By default all supported locales.
        fuzzy_cutoff : float
            Minimum similarity score for fuzzy matching (0–100). By default 80.

        Returns
        -------
        bool
            ``True`` if the place name is valid, ``False`` otherwise.

        Examples
        --------
        ```python
        EorzeaPlaceName.validate('The Ruby Sea', strict=True)   # True
        EorzeaPlaceName.validate('nowhere land', strict=True)   # False
        EorzeaPlaceName.validate('ruby see', strict=False)      # True  (fuzzy)
        EorzeaPlaceName.validate(EorzeaPlaceName('ruby sea'), strict=True)  # True
        ```
        """
        if type(place_name) is EorzeaPlaceName:
            return True

        if type(place_name) is str:
            try:
                place_info = _validate_place_name(
                    place_name, strict, locale_scopes, fuzzy_cutoff
                )
                return bool(place_info)
            except InvalidEorzeaPlaceName:
                return False

        return False

    def __str__(self):
        return self.value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}')"

    def __eq__(self, that: object) -> bool:
        if isinstance(that, EorzeaPlaceName):
            return that.index == self.index and that.value == self.value

        return False


def _validate_place_name(
    place_name: str,
    is_strict: bool,
    locale_scopes: List[LocaleScope],
    fuzzy_cutoff: FuzzyCutoff,
) -> PlaceInfo:
    if type(place_name) is not str:
        raise TypeError(
            f"place_name should be `str`. ({place_name} is {type(place_name)})"
        )
    if fuzzy_cutoff > 100 or fuzzy_cutoff < 0:
        raise ValueError("Cutoff value should be in 0-100.")

    possible_place_name = None
    place_name = place_name.lower()
    place_name = re.sub("^the ", "", place_name)
    place_names_reference = _bulid_reference_by_locales(locale_scopes)

    if is_strict:
        place_info = place_names_reference.get(place_name)
        if place_info:
            return PlaceInfo(**place_info)

    else:
        result = fuzz_process.extractOne(
            place_name, place_names_reference.keys(), score_cutoff=fuzzy_cutoff
        )

        if result:
            possible_place_name, score, index = result
            place_info = place_names_reference.get(possible_place_name)
            if place_info:
                return PlaceInfo(**place_info)

    raise InvalidEorzeaPlaceName(place_name=place_name, is_strict=is_strict)


def _bulid_reference_by_locales(
    locales: List[LocaleScope],
) -> Mapping[str, PlaceInfoDict]:
    dictionary: Mapping[str, PlaceInfoDict] = {}
    for locale in locales:
        dictionary.update(_place_names[locale])  # type: ignore

    return dictionary
