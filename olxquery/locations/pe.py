from olxquery.types import Location


class PE(Location):
    name = "Estado de PE"
    url = "estado-pe"

    class DDD_81(Location):
        name = "Grande Recife"
        url = "grande-recife"

        class Recife(Location):
            name = "Recife"
            url = "recife"

        class GrandeRecife(Location):
            name = "Grande Recife"
            url = "grande-recife"
