from olxquery.types import Location


class SC(Location):
    name = "Estado de SC"
    url = "estado-sc"

    class DDD_47(Location):
        name = "Norte de Santa Catarina"
        url = "norte-de-santa-catarina"

        class RegiaoDeJoinvilleENorteDoEstado(Location):
            name = "Região de Joinville e Norte do Estado"
            url = "regiao-de-joinville-e-norte-do-estado"

        class RegiaoDoValeDoItajai(Location):
            name = "Região do Vale do Itajaí"
            url = "regiao-do-vale-do-itajai"

    class DDD_48(Location):
        name = "Florianópolis e região"
        url = "florianopolis-e-regiao"

        class Centro(Location):
            name = "Centro"
            url = "centro"

        class Continente(Location):
            name = "Continente"
            url = "continente"

        class Leste(Location):
            name = "Leste"
            url = "leste"

        class Norte(Location):
            name = "Norte"
            url = "norte"

        class Sul(Location):
            name = "Sul"
            url = "sul"

        class GrandeFlorianopolis(Location):
            name = "Grande Florianópolis"
            url = "grande-florianopolis"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"

    class DDD_49(Location):
        name = "Oeste de Santa Catarina"
        url = "oeste-de-santa-catarina"

        class RegiaoDeChapeco(Location):
            name = "Região de Chapecó"
            url = "regiao-de-chapeco"

        class RegiaoDeJoacaba(Location):
            name = "Região de Joaçaba"
            url = "regiao-de-joacaba"

        class RegiaoDeXanxereEConcordia(Location):
            name = "Região de Xanxerê e Concórdia"
            url = "regiao-de-xanxere-e-concordia"

        class RegioesDeCuritibanosECDosLages(Location):
            name = "Regiões de Curitibanos e C. dos Lages"
            url = "regioes-de-curitibanos-e-c-dos-lages"
