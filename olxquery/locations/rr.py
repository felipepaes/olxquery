from olxquery.types import Location


class RR(Location):
    name = "Estado de RR"
    url = "estado-rr"

    class DDD_95(Location):
        name = "Roraima"
        url = "roraima"

        class BoaVista(Location):
            name = "Boa Vista"
            url = "boa-vista"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"
