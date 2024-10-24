from olxquery.types import Location


class BA(Location):
    name = "Estado de BA"
    url = "estado-ba"

    class DDD_71(Location):
        name = "Salvador"
        url = "grande-salvador"

        class Salvador(Location):
            name = "Salvador"
            url = "salvador"

        class GrandeSalvador(Location):
            name = "Grande Salvador"
            url = "grande-salvador"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"

    class DDD_73(Location):
        name = "Sul da Bahia"
        url = "sul-da-bahia"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"

    class DDD_74(Location):
        name = "Juazeiro, Jacobina e região"
        url = "regiao-de-juazeiro-e-jacobina"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"

    class DDD_75(Location):
        name = "F. de Santana, Alagoinhas e região"
        url = "regiao-de-feira-de-santana-e-alagoinhas"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"

    class DDD_77(Location):
        name = "V da Conquista, Barreiras e região"
        url = "regiao-de-vitoria-da-conquista-e-barreiras"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"
