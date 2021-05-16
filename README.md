# README

Build urls for scraping the brazilian version of the famous listing website olx.


Work in Progress...

```python
from pprint import pprint

from olxquery.queries.base import BaseQuery
from olxquery.locations import SP
from olxquery.categories import Eletronicos

query = BaseQuery(
    search="Playstation 4",
    location=SP.DDD_11.ZonaLeste,
    category=Eletronicos.VideoGames,
    price_min=700,
    price_max=1200
)

pprint(query.url)
print("---------")
pprint(query.urls)
```

```
'https://sp.olx.com.br/sao-paulo-e-regiao/zona-leste/videogames?q=Playstation+4&ps=700&pe=1200'
---------
['https://sp.olx.com.br/sao-paulo-e-regiao/zona-leste/videogames?q=Playstation+4&ps=700&pe=1200',
 'https://sp.olx.com.br/sao-paulo-e-regiao/zona-leste/videogames?q=Playstation+4&ps=700&pe=1200&o=2']
```
