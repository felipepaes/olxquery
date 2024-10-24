from olxquery.types import Location


class AP(Location):
    name = "Estado de AP"
    url = "estado-ap"

    class DDD_96(Location):
        name = "Amapá"
        url = "amapá"

        class Macapa(Location):
            name = "Macapá"
            url = "macapa"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"
