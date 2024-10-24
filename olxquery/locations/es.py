from olxquery.types import Location


class ES(Location):
    name = "Estado de ES"
    url = "estado-es"

    class DDD_27(Location):
        name = "Norte do Espírito Santo"
        url = "norte-do-espirito-santo"

        class Vitoria(Location):
            name = "Vitória"
            url = "vitoria"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"

        class VilaVelha(Location):
            name = "Vila Velha"
            url = "vila-velha"

        class AfonsoClaudioERegiao(Location):
            name = "Afonso Cláudio e região"
            url = "afonso-claudio-e-regiao"

        class GuarapariERegiao(Location):
            name = "Guarapari e região"
            url = "guarapari-e-regiao"

        class RegiaoDeColatinaENovaVenecia(Location):
            name = "Região de Colatina e Nova Venécia"
            url = "regiao-de-colatina-e-nova-venecia"

        class RegiaoDeLinharesESaoMateus(Location):
            name = "Região de Linhares e São Mateus"
            url = "regiao-de-linhares-e-sao-mateus"

        class SantaTeresaERegiao(Location):
            name = "Santa Teresa e região"
            url = "santa-teresa-e-regiao"

    class DDD_28(Location):
        name = "Sul do Espírito Santo"
        url = "sul-do-espirito-santo"

        class AfonsoClaudioERegiao(Location):
            name = "Afonso Cláudio e região"
            url = "afonso-claudio-e-regiao"

        class CachoeiroDeItapemirimERegiaoSul(Location):
            name = "Cachoeiro de Itapemirim e Região sul"
            url = "cachoeiro-de-itapemirim-e-regiao-sul"

        class GuarapariERegiao(Location):
            name = "Guarapari e região"
            url = "guarapari-e-regiao"
