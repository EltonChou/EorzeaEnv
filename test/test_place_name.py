import pytest
from EorzeaEnv import EorzeaLang, EorzeaPlaceName
from EorzeaEnv.errors import InvalidEorzeaPlaceName


class TestPlaceName:
    def test_default(self):
        EorzeaPlaceName('The Ruby Sea')
        EorzeaPlaceName('rubinsee')
        EorzeaPlaceName('紅玉海')
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName('The Ruby See')

    def test_specified_locale_scope(self):
        EorzeaPlaceName('The Ruby Sea', locale_scopes=[EorzeaLang.EN])
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName(
                'The Ruby Sea',
                locale_scopes=[EorzeaLang.JA, EorzeaLang.DE])

    def test_fuzzy(self):
        EorzeaPlaceName('ruby Sea', strict=False)
        EorzeaPlaceName('rubisee', strict=False)
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName('diamond sea', strict=False)

    def test_fuzzy_with_locale_scope(self):
        EorzeaPlaceName('rubby sea', strict=False, locale_scopes=[
                        EorzeaLang.EN, EorzeaLang.DE])
        with pytest.raises(InvalidEorzeaPlaceName):
            EorzeaPlaceName('rubby sea', strict=False, locale_scopes=[
                            EorzeaLang.JA, EorzeaLang.DE])

    def test_acted_as_string(self):
        place = EorzeaPlaceName('The Ruby Sea')
        assert str(place) == 'The Ruby Sea'

    def test_equal(self):
        the_ruby_sea = EorzeaPlaceName('The Ruby Sea')
        the_ruby_see = EorzeaPlaceName('ruby sea', strict=False)
        assert the_ruby_sea == the_ruby_see

    def test_validate_method(self):
        assert EorzeaPlaceName.validate('The Ruby Sea', is_strict=True)
        assert not EorzeaPlaceName.validate('The Ruby See', is_strict=True)

