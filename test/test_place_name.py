import pytest
from EorzeaEnv import EorzeaLang, EorzeaPlaceName
from EorzeaEnv.errors import InvalidEorzeaPlaceName


class TestPlaceName:
    @pytest.mark.parametrize(
        ("place"),
        [
            "The Ruby Sea",
            "the ruby sea",
            "ruby sea",
            "rubinsee",
            "紅玉海",
            "수투 훈련장",
            "福隆戴爾藥學院兒科病房",
        ],
    )
    def test_default(self, place: str):
        EorzeaPlaceName(place)

    def test_default_fuzzy_cutoff(self):
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName("The Ruby See")

    @pytest.mark.parametrize(
        ("place", "lang"),
        [
            ("The Ruby Sea", EorzeaLang.EN),
            ("rubinsee", EorzeaLang.DE),
            ("mer de rubis", EorzeaLang.FR),
            ("紅玉海", EorzeaLang.JA),
            ("红玉海", EorzeaLang.ZH_SC),
            ("紅玉海", EorzeaLang.ZH_TC),
        ],
    )
    def test_specified_locale_scopes(self, place: str, lang: EorzeaLang):
        EorzeaPlaceName(place, locale_scopes=[lang])

    def test_invalid_eorzea_palce_name_for_certain_scope(self):
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName(
                "The Ruby Sea",
                locale_scopes=[
                    EorzeaLang.JA,
                    EorzeaLang.DE,
                    EorzeaLang.ZH_TC,
                    EorzeaLang.ZH_SC,
                    EorzeaLang.FR,
                ],
            )

    def test_fuzzy(self):
        EorzeaPlaceName("ruby Sea", strict=False)
        EorzeaPlaceName("rubisee", strict=False)
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName("diamond sea", strict=False)

    def test_fuzzy_with_locale_scope(self):
        EorzeaPlaceName(
            "rubby sea", strict=False, locale_scopes=[EorzeaLang.EN, EorzeaLang.DE]
        )
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName(
                "rubby sea", strict=False, locale_scopes=[EorzeaLang.JA, EorzeaLang.DE]
            )

    def test_acted_as_string(self):
        place = EorzeaPlaceName("The Ruby Sea")
        assert str(place) == "The Ruby Sea"

    def test_equal(self):
        the_ruby_sea = EorzeaPlaceName("The Ruby Sea")
        the_ruby_see = EorzeaPlaceName("ruby sea", strict=False)
        assert the_ruby_sea == the_ruby_see
        assert not the_ruby_sea == "The Ruby Sea"

    def test_validate_method(self):
        assert EorzeaPlaceName.validate("The Ruby Sea", strict=True)
        assert not EorzeaPlaceName.validate("The Ruby See", strict=True)
        with pytest.raises(ValueError):
            EorzeaPlaceName.validate("The Ruby Sea", strict=True, fuzzy_cutoff=120)
        ruby_sea = EorzeaPlaceName("The Ruby Sea")
        assert EorzeaPlaceName.validate(ruby_sea, strict=True)
        assert not EorzeaPlaceName.validate(1, strict=False)  # type: ignore

    def test_place_name_property(self):
        place_name = EorzeaPlaceName("The Ruby Sea")
        assert type(place_name.index) is int
        assert type(place_name.value) is str

    def test_bad_type_place_name(self):
        with pytest.raises(TypeError):
            EorzeaPlaceName(1)  # type: ignore

    def test_repr(self):
        place = EorzeaPlaceName("The Ruby Sea")
        assert eval(repr(place)) == place
