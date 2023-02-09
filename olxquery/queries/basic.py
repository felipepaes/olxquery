from . base import BaseQuery
from olxquery.types import Location, Category


class BasicQuery(BaseQuery):

    QUERY_PARAMS = {
        "search": "q",
        "price_min": "ps",
        "price_max": "pe",
    }

    def __init__(self, 
                search: str | None = None, 
                location: Location | None = None, 
                category: Category | None = None, 
                price_min: int | None = None, 
                price_max: int | None = None):
        super().__init__(
                search=search, 
                location=location, 
                category=category, 
                price_min=price_min, 
                price_max=price_max)
