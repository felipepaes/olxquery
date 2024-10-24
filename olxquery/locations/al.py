from olxquery.types import Location


class AL(Location):
    name = "Estado de AL"
    url = "estado-al"

    class DDD_82(Location):
        name = "Alagoas"
        url = "alagoas"

        class Maceio(Location):
            name = "Maceió"
            url = "maceio"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"
