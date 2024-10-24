from olxquery.types import BasicType


class BaseTypeFixture(BasicType):
    pass


class SomeType(BaseTypeFixture):
    name = "Type Fixture"
    url = "root-url"

    class Level1_1(BaseTypeFixture):
        name = "Type Fixture Level 1-1"
        url = "level1-1"

    class Level1_2(BaseTypeFixture):
        name = "Type Fixture Level 1-2"
        url = "level1-2"

        class Level1_2_1(BaseTypeFixture):
            name = "Type Fixture Level 2"
            url = "level1-2-1-url"


def test_get_url():
    """Test all levels of get_url()"""
    # root level
    expected = SomeType.get_url()
    assert expected == SomeType.url
    # one level
    expected = f"{SomeType.url}/{SomeType.Level1_1.url}"
    assert expected == SomeType.Level1_1.get_url()
    # two levels
    expected = (
        f"{SomeType.url}/{SomeType.Level1_2.url}/{SomeType.Level1_2.Level1_2_1.url}"
    )
    assert expected == SomeType.Level1_2.Level1_2_1.get_url()


def test_is_root():
    """Root level should be ommited if is_root is True"""
    expected = f"{SomeType.Level1_2.url}/{SomeType.Level1_2.Level1_2_1.url}"
    SomeType.is_root = True
    assert expected == SomeType.Level1_2.Level1_2_1.get_url()
