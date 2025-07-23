# README

Build urls for scraping the brazilian version of the famous listing website olx.


Work in Progress...

```python
from olxquery.queries import BasicQuery
from olxquery.locations import SP
from olxquery.categories import EletronicosECelulares

query = BasicQuery(
    search="Playstation 4",
    location=SP.DDD_11.ZonaLeste,
    category=EletronicosECelulares.Videogames,
    price_min=700,
    price_max=1200
)

print(query.url)
```

```shell
'https://sp.olx.com.br/sao-paulo-e-regiao/zona-leste/videogames?q=Playstation+4&ps=700&pe=1200'
```
