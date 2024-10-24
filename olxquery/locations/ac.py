from olxquery.types import Location


class AC(Location):
    name = "Estado de AC"
    url = "estado-ac"

    class DDD_68(Location):
        name = "Acre"
        url = "acre"

        class RioBranco(Location):
            name = "Rio Branco"
            url = "rio-branco"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"
