import pytest
from EorzeaEnv import EorzeaLang, EorzeaPlaceName
from EorzeaEnv.errors import InvalidEorzeaPlaceName


class TestPlaceName:
    def test_default(self):
        EorzeaPlaceName("The Ruby Sea")
        EorzeaPlaceName("the ruby sea")
        EorzeaPlaceName("ruby sea")
        EorzeaPlaceName("rubinsee")
        EorzeaPlaceName("紅玉海")
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName("The Ruby See")

    def test_specified_locale_scope(self):
        EorzeaPlaceName("The Ruby Sea", locale_scopes=[EorzeaLang.EN])
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName(
                "The Ruby Sea", locale_scopes=[EorzeaLang.JA, EorzeaLang.DE]
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
