from olxquery.types import Location


class AM(Location):
    name = "Estado de AM"
    url = "estado-am"

    class DDD_92(Location):
        name = "Região de Manaus"
        url = "regiao-de-manaus"

        class Manaus(Location):
            name = "Manaus"
            url = "manaus"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"

    class DDD_97(Location):
        name = "Leste do Amazonas"
        url = "leste-do-amazonas"

        class RegiaoDoCentroAmazonense(Location):
            name = "Região do Centro Amazonense"
            url = "regiao-do-centro-amazonense"

        class RegiaoDoNorteAmazonense(Location):
            name = "Região do Norte Amazonense"
            url = "regiao-do-norte-amazonense"

        class RegiaoDoSudoesteAmazonense(Location):
            name = "Região do Sudoeste Amazonense"
            url = "regiao-do-sudoeste-amazonense"

        class RegiaoDoSulAmazonense(Location):
            name = "Região do Sul Amazonense"
            url = "regiao-do-sul-amazonense"
