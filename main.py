# ruff: noqa: E402

from pprint import pprint

from olxquery.categories import EletronicosECelulares
from olxquery.locations import DF, SP
from olxquery.queries import BasicQuery

query = BasicQuery(
    search="",
    location=DF.DDD_61.Brasilia.LagoNorte,
    # location=SP.DDD_11,
    # location=SP.DDD_11.Guarulhos,
    category=EletronicosECelulares.Games.Consoles.NintendoSwitch,
    price_min=900,
    price_max=1500,
)


pprint(query.url)
print("---------")
# pprint(query.urls)


print(EletronicosECelulares.get_url())

print(EletronicosECelulares.CelularesETelefonia.get_url())


print(EletronicosECelulares.CelularesETelefonia.Apple.get_url())

print(EletronicosECelulares.Games.Consoles.Playstation4.get_url())


print(
    BasicQuery(
        location=SP.DDD_11,
        category=EletronicosECelulares.CelularesETelefonia.Apple.IPhone12,
        price_min=1200,
        price_max=2000,
    ).url
)
