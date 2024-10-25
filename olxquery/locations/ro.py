from olxquery.types import Location


class RO(Location):
    name = "Estado de RO"
    url = "estado-ro"

    class DDD_69(Location):
        name = "Rondônia"
        url = "rondônia"

        class PortoVelho(Location):
            name = "Porto Velho"
            url = "porto-velho"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"
