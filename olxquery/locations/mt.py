from olxquery.types import Location


class MT(Location):
    name = "Estado de MT"
    url = "estado-mt"

    class DDD_65(Location):
        name = "Cuiabá e região"
        url = "regiao-de-cuiaba"

        class Cuiaba(Location):
            name = "Cuiabá"
            url = "cuiaba"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"

    class DDD_66(Location):
        name = "Rondonópolis, Sinop e região"
        url = "regiao-de-rondonopolis-e-sinop"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"
