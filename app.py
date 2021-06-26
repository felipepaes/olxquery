from pprint import pprint
from olxquery.queries.base import BaseQuery
from olxquery import categories, locations

query = BaseQuery(search='macbook 16gb',
                  location=locations.SP.DDD_11,
                  category=categories.Eletronicos.Computadores,
                  price_min=1500,
                  price_max=3000)

base_url = query.url
urls = query.urls

pprint(base_url)
pprint(urls)
