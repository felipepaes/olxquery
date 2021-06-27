from pprint import pprint
from olxquery.queries.base import BaseQuery
from olxquery import categories, locations

mcbook16gb_query = BaseQuery(search='macbook 16gb',
                  location=locations.SP.DDD_11,
                  category=categories.Eletronicos.Computadores,
                  price_min=1500,
                  price_max=3000)

i7query = BaseQuery(search='macbook i7',
                  location=locations.SP.DDD_11,
                  category=categories.Eletronicos.Computadores,
                  price_min=1500,
                  price_max=3000)


pprint(mcbook16gb_query.url)
pprint(mcbook16gb_query.url)
pprint(i7query.url)
pprint(i7query.urls)
