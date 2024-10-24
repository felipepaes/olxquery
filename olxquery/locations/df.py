from olxquery.types import Location


class DF(Location):
    name = "Estado de DF"
    url = "estado-df"

    class DDD_61(Location):
        name = "Distrito Federal e região"
        url = "distrito-federal-e-região"

        class Brasilia(Location):
            name = "Brasília"
            url = "brasilia"

            class LargoNorte(Location):
                name = "RA XVIII Lago Norte"
                url = "ra-xviii---lago-norte"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"
