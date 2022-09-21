import re
from dataclasses import dataclass
from typing import List, Mapping, Union

from rapidfuzz import process as fuzz_process

from .Data.PlaceName import PlaceInfoDict
from .Data.PlaceName import place_name as _place_names
from .eorzea_lang import EorzeaLang
from .errors import InvalidEorzeaPlaceName

FuzzyCutoff = Union[int, float]
LocaleScope = Union[EorzeaLang, str]

DEFAULT_CUTOFF = 80
DEFAULT_LOCALE_SCOPES: List[LocaleScope] = [
    EorzeaLang.EN,
    EorzeaLang.JA,
    EorzeaLang.FR,
    EorzeaLang.DE,
    EorzeaLang.KO,
    EorzeaLang.ZH_SC,
]


@dataclass
class PlaceInfo:
    index: int
    place_name: str


class EorzeaPlaceName:
    """EorzeaPlaceName

    An EorzeaPlaceName instance is always a valid place name in EorzeaEnv.


    Parameters
    ----------
    place_name : str
        should be a valid Eorzea place name.
    strict : bool
        True: strict mode.
        False: fuzzy mode.
        by default True.
    locale_scopes : List[LocaleScope]
        Locale scope for searching placename, by default full scopes.
    fuzzy_cutoff : int | float
        The cutoff score used in fuzzy mode, should be 100 <= value <= 0, by default 80.

    Raises
    ----------
    :class:`EorzeaEnv.errors.InvalidEorzeaPlaceName`
        When place_name is invalid.
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
        place_name: Union[str, "EorzeaPlaceName"],
        strict: bool,
        locale_scopes: List[LocaleScope] = DEFAULT_LOCALE_SCOPES,
        fuzzy_cutoff: FuzzyCutoff = DEFAULT_CUTOFF,
    ) -> bool:
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
