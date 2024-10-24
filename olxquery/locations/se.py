from olxquery.types import Location


class SE(Location):
    name = "Estado de SE"
    url = "estado-se"

    class DDD_79(Location):
        name = "Sergipe"
        url = "sergipe"

        class Aracaju(Location):
            name = "Aracaju"
            url = "aracaju"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"
