from olxquery.types import Location


class PR(Location):
    name = "Estado de PR"
    url = "estado-pr"

    class DDD_41(Location):
        name = "Curitiba e região"
        url = "regiao-de-curitiba-e-paranagua"

        class BairroNovo(Location):
            name = "Bairro Novo"
            url = "bairro-novo"

        class BoaVista(Location):
            name = "Boa Vista"
            url = "boa-vista"

        class Boqueirao(Location):
            name = "Boqueirão"
            url = "boqueirao"

        class Cajuru(Location):
            name = "Cajuru"
            url = "cajuru"

        class CidadeIndustrial(Location):
            name = "Cidade Industrial"
            url = "cidade-industrial"

        class FazendinhaPortao(Location):
            name = "Fazendinha Portão"
            url = "fazendinha-portao"

        class Matriz(Location):
            name = "Matriz"
            url = "matriz"

        class Pinheirinho(Location):
            name = "Pinheirinho"
            url = "pinheirinho"

        class SantaFelicidade(Location):
            name = "Santa Felicidade"
            url = "santa-felicidade"

        class GrandeCuritiba(Location):
            name = "Grande Curitiba"
            url = "grande-curitiba"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"

    class DDD_42(Location):
        name = "Pta Grossa, Guarapuava e região"
        url = "regiao-de-ponta-grossa-e-guarapuava"

        class RegiaoDeGuarapuava(Location):
            name = "Região de Guarapuava"
            url = "regiao-de-guarapuava"

        class RegiaoDePontaGrossaETelemacoBorba(Location):
            name = "Região de Ponta Grossa e Telêmaco Borba"
            url = "regiao-de-ponta-grossa-e-telemaco-borba"

        class SudesteParanaense(Location):
            name = "Sudeste Paranaense"
            url = "sudeste-paranaense"

    class DDD_43(Location):
        name = "Londrina e região"
        url = "regiao-de-londrina"

        class CentroNorteParanaense(Location):
            name = "Centro-norte Paranaense"
            url = "centro-norte-paranaense"

        class NordesteParanaense(Location):
            name = "Nordeste Paranaense"
            url = "nordeste-paranaense"

        class RegiaoDeLondrina(Location):
            name = "Região de Londrina"
            url = "regiao-de-londrina"

    class DDD_44(Location):
        name = "Maringá e região"
        url = "regiao-de-maringa"

        class CentroOesteParanaense(Location):
            name = "Centro-oeste Paranaense"
            url = "centro-oeste-paranaense"

        class NorteParanaense(Location):
            name = "Norte Paranaense"
            url = "norte-paranaense"

        class OesteParanaense(Location):
            name = "Oeste Paranaense"
            url = "oeste-paranaense"

        class RegiaoDeMaringa(Location):
            name = "Região de Maringá"
            url = "regiao-de-maringa"

    class DDD_45(Location):
        name = "Foz do Iguaçu, Cascavel e região"
        url = "regiao-de-foz-do-iguacu-e-cascavel"

        class RegiaoDeCascavel(Location):
            name = "Região de Cascavel"
            url = "regiao-de-cascavel"

        class RegiaoDeFozDoIguacu(Location):
            name = "Região de Foz do Iguaçu"
            url = "regiao-de-foz-do-iguacu"

    class DDD_46(Location):
        name = "F. Beltrão e Pato Branco e região"
        url = "regiao-de-francisco-beltrao-e-pato-branco"

        class CentroSulParanaense(Location):
            name = "Centro-sul Paranaense"
            url = "centro-sul-paranaense"

        class SudoesteParanaense(Location):
            name = "Sudoeste Paranaense"
            url = "sudoeste-paranaense"
