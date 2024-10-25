from olxquery.types import Location


class RS(Location):
    name = "Estado de RS"
    url = "estado-rs"

    class DDD_51(Location):
        name = "Porto Alegre e região"
        url = "regioes-de-porto-alegre-torres-e-santa-cruz-do-sul"

        class CampusPuc(Location):
            name = "Campus PUC"
            url = "campus-puc"

        class Centro(Location):
            name = "Centro"
            url = "centro"

        class ExtremoSul(Location):
            name = "Extremo Sul"
            url = "extremo-sul"

        class Leste(Location):
            name = "Leste"
            url = "leste"

        class MoinhosDeVento(Location):
            name = "Moinhos de Vento"
            url = "moinhos-de-vento"

        class Norte(Location):
            name = "Norte"
            url = "norte"

        class PraiaDeBelas(Location):
            name = "Praia de Belas"
            url = "praia-de-belas"

        class Sul(Location):
            name = "Sul"
            url = "sul"

        class Ufrgs(Location):
            name = "UFRGS"
            url = "ufrgs"

        class GrandePortoAlegre(Location):
            name = "Grande Porto Alegre"
            url = "grande-porto-alegre"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"

    class DDD_53(Location):
        name = "Pelotas, Bagé, Rio Gde e região"
        url = "regioes-de-pelotas-rio-grande-e-bage"

        class RegiaoDeBage(Location):
            name = "Região de Bagé"
            url = "regiao-de-bage"

        class SudesteRioGrandense(Location):
            name = "Sudeste Rio-grandense"
            url = "sudeste-rio-grandense"

    class DDD_54(Location):
        name = "Caxias do Sul e região"
        url = "regioes-de-caxias-do-sul-e-passo-fundo"

        class RegiaoDeCarazinho(Location):
            name = "Região de Carazinho"
            url = "regiao-de-carazinho"

        class RegiaoDeCaxiasDoSul(Location):
            name = "Região de Caxias do Sul"
            url = "regiao-de-caxias-do-sul"

        class RegiaoDeErechim(Location):
            name = "Região de Erechim"
            url = "regiao-de-erechim"

        class RegiaoDeGramadoECanela(Location):
            name = "Região de Gramado e Canela"
            url = "regiao-de-gramado-e-canela"

        class RegiaoDeNaoMeToqueESoledade(Location):
            name = "Região de Não Me Toque e Soledade"
            url = "regiao-de-nao-me-toque-e-soledade"

        class RegiaoDePassoFundo(Location):
            name = "Região de Passo Fundo"
            url = "regiao-de-passo-fundo"

        class RegiaoDeVacaria(Location):
            name = "Região de Vacaria"
            url = "regiao-de-vacaria"

    class DDD_55(Location):
        name = "Sta Maria, Cruz Alta e região"
        url = "regioes-de-santa-maria-uruguaiana-e-cruz-alta"

        class NoroesteDoEstado(Location):
            name = "Noroeste do Estado"
            url = "noroeste-do-estado"

        class NorteDoEstado(Location):
            name = "Norte do Estado"
            url = "norte-do-estado"

        class OesteDoEstado(Location):
            name = "Oeste do Estado"
            url = "oeste-do-estado"

        class RegiaoDeCruzAltaEIjui(Location):
            name = "Região de Cruz Alta e Ijuí"
            url = "regiao-de-cruz-alta-e-ijui"

        class RegiaoDeSantaMaria(Location):
            name = "Região de Santa Maria"
            url = "regiao-de-santa-maria"
