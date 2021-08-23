from . base import AbstractBaseQuery
from olxquery.types import Location, Category


class BasicQuery(AbstractBaseQuery):

    QUERY_PARAMS = {
        "search": "q",
        "price_min": "ps",
        "price_max": "pe",
    }

    def __init__(self, 
                search: str = None, 
                location: Location = None, 
                category: Category = None, 
                price_min: int = None, 
                price_max: int = None):
        super().__init__(
                search=search, 
                location=location, 
                category=category, 
                price_min=price_min, 
                price_max=price_max)
