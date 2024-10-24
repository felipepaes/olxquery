from olxquery.types import Location


class TO(Location):
    name = "Estado de Tocantins"
    url = "estado-to"

    class DDD_63(Location):
        name = "Tocantins"
        url = "tocantins"

        class Palmas(Location):
            name = "Palmas"
            url = "palmas"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"
