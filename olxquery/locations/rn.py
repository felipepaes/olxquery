from olxquery.types import Location


class RN(Location):
    name = "Estado de RN"
    url = "estado-rn"

    class DDD_84(Location):
        name = "Rio Grande do Norte"
        url = "rio-grande-do-norte"

        class Natal(Location):
            name = "Natal"
            url = "natal"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"
