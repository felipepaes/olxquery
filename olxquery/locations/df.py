from olxquery.types import Location


class DF(Location):
    name = "Estado de DF"
    url = "estado-df"

    class DDD_61(Location):
        name = "Distrito Federal e região"
        url = "distrito-federal-e-regiao"

        class Brasilia(Location):
            name = "Brasília"
            url = "brasilia"

            class LagoNorte(Location):
                name = "RA XVIII Lago Norte"
                url = "ra-xviii---lago-norte"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"
