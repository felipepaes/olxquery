from olxquery.types import Location


class MS(Location):
    name = "Estado de MS"
    url = "estado-ms"

    class DDD_67(Location):
        name = "Mato Grosso do Sul"
        url = "mato-grosso-do-sul"

        class CampoGrande(Location):
            name = "Campo Grande"
            url = "campo-grande"

        class Corumba(Location):
            name = "Corumbá"
            url = "corumba"

        class Dourados(Location):
            name = "Dourados"
            url = "dourados"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"

        class TresLagoas(Location):
            __name = "Três Lagoas"
            url = "tres-lagoas"
