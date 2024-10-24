from olxquery.types import Location


class CE(Location):
    name = "Estado de CE"
    url = "estado-ce"

    class DDD_85(Location):
        name = "Fortaleza e região"
        url = "fortaleza-e-regiao"

        class Fortaleza(Location):
            name = "Fortaleza"
            url = "fortaleza"

        class GrandeFortaleza(Location):
            name = "Grande Fortaleza"
            url = "grande-fortaleza"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"

    class DDD_88(Location):
        name = "Juazeiro do Norte, Sobral e região"
        url = "regiao-de-juazeiro-do-norte-e-sobral"
