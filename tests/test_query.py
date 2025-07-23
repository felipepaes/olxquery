import pytest

from olxquery.categories import EletronicosECelulares
from olxquery.locations import SP
from olxquery.queries import BasicQuery
from olxquery.queries.base import BaseQuery


def test_base_query_missing_query_params():
    """Test Missing QUERY_PARAMS"""
    with pytest.raises(TypeError):

        class MissingQueryParams(BaseQuery): ...

        MissingQueryParams()


def test_base_query_with_query_params():
    """Test present QUERY_PARAMS"""

    class WithQueryParams(BaseQuery):
        QUERY_PARAMS = {
            "search": "q",
            "price_min": "ps",
            "price_max": "pe",
        }

    assert WithQueryParams()


@pytest.mark.parametrize("search", ["", "nintendo switch"])
def test_basic_query(search):
    query_input = {
        "search": search,
        "location": SP.DDD_11.Guarulhos,
        "category": EletronicosECelulares.Games.Consoles.NintendoSwitch,
        "price_min": 900,
        "price_max": 1500,
    }

    expected = (
        "https://olx.com.br/{category}/{subcategory}/"
        "{product}/{state}/{region}/{city}"
        "?{search}ps={min_price}&pe={max_price}"
    )

    query = BasicQuery(
        search=query_input["search"] if query_input["search"] else None,
        location=query_input["location"],
        category=query_input["category"],
        price_min=query_input["price_min"],
        price_max=query_input["price_max"],
    )

    assert query.url == expected.format(
        search=f"q={query_input['search'].replace(' ', '+')}&" if query_input["search"] else "",
        category=EletronicosECelulares.Games.url,
        subcategory=EletronicosECelulares.Games.Consoles.url,
        product=EletronicosECelulares.Games.Consoles.NintendoSwitch.url,
        state=SP.url,
        region=SP.DDD_11.url,
        city=SP.DDD_11.Guarulhos.url,
        min_price=query_input["price_min"],
        max_price=query_input["price_max"],
    )
