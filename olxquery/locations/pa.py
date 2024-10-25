from olxquery.types import Location


class PA(Location):
    name = "Estado de PA"
    url = "estado-pa"

    class DDD_91(Location):
        name = "Região de Belém"
        url = "regiao-de-belem"

        class Belem(Location):
            name = "Belém"
            url = "belem"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"

    class DDD_93(Location):
        name = "Região de Santarém"
        url = "regiao-de-santarem"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"

    class DDD_94(Location):
        name = "Região de Marabá"
        url = "regiao-de-maraba"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"
