from olxquery.types import Location


class MA(Location):
    name = "Estado de MA"
    url = "estado-ma"

    class DDD_98(Location):
        name = "Região de São Luís"
        url = "regiao-de-sao-luis"

        class SaoLuis(Location):
            name = "São Luís"
            url = "sao-luis"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"

    class DDD_99(Location):
        name = "Imperatriz, Caxias e região"
        url = "regiao-de-imperatriz-e-caxias"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"
