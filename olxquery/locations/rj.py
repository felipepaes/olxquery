from olxquery.types import Location


class RJ(Location):
    name = "Estado de RJ"
    url = "estado-rj"

    class DDD_21:
        name = "Rio de Janeiro e região"
        url = "rio-de-janeiro-e-regiao"

        class Centro:
            name = "Centro"
            url = "centro"

        class ZonaNorte:
            name = "Zona Norte"
            url = "zona-norte"

        class ZonaOeste:
            name = "Zona Oeste"
            url = "zona-oeste"

        class ZonaSul:
            name = "Zona Sul"
            url = "zona-sul"
