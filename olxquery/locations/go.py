from olxquery.types import Location


class GO(Location):
    name = "Estado de GO"
    url = "estado-go"

    class DDD_62(Location):
        name = "Grande Goiânia e Anápolis"
        url = "grande-goiania-e-anapolis"

        class RegiaoCampinas(Location):
            name = "Região Campinas"
            url = "regiao-campinas"

        class RegiaoCentral(Location):
            name = "Região Central"
            url = "regiao-central"

        class RegiaoLeste(Location):
            name = "Região Leste"
            url = "regiao-leste"

        class RegiaoMacambiraECascavel(Location):
            name = "Região Macambira e Cascavél"
            url = "regiao-macambira-e-cascavel"

        class RegiaoMendanha(Location):
            name = "Região Mendanha"
            url = "regiao-mendanha"

        class RegiaoNoroeste(Location):
            name = "Região Noroeste"
            url = "regiao-noroeste"

        class RegiaoNorte(Location):
            name = "Região Norte"
            url = "regiao-norte"

        class RegiaoOeste(Location):
            name = "Região Oeste"
            url = "regiao-oeste"

        class RegiaoSudeste(Location):
            name = "Região Sudeste"
            url = "regiao-sudeste"

        class RegiaoSudoeste(Location):
            name = "Região Sudoeste"
            url = "regiao-sudoeste"

        class RegiaoSul(Location):
            name = "Região Sul"
            url = "regiao-sul"

        class ValeDoMeiaPonte(Location):
            name = "Vale do Meia Ponte"
            url = "vale-do-meia-ponte"

        class GrandeGoiania(Location):
            name = "Grande Goiânia"
            url = "grande-goiania"

        class OutrasCidades(Location):
            name = "Outras cidades"
            url = "outras-cidades"

    class DDD_64(Location):
        name = "Rio Verde, Caldas Novas e região"
        url = "regiao-de-rio-verde-e-caldas-novas"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"
