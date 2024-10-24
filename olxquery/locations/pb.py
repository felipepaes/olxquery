from olxquery.types import Location


class PB(Location):
    name = "Estado de PB"
    url = "estado-pb"

    class DDD_83(Location):
        name = "Paraíba"
        url = "paraíba"

        class JoaoPessoa(Location):
            name = "João Pessoa"
            url = "joao-pessoa"

        class CampinaGrandeGuarabiraERegiao(Location):
            name = "Campina Grande, Guarabira e região"
            url = "campina-grande-guarabira-e-regiao"

        class MonteiroPicuiERegiao(Location):
            name = "Monteiro, Picuí e região"
            url = "monteiro-picui-e-regiao"

        class PatosSousaERegiao(Location):
            name = "Patos, Sousa e região"
            url = "patos-sousa-e-regiao"

        class SantaRitaBayeuxERegiao(Location):
            name = "Santa Rita, Bayeux e região"
            url = "santa-rita-bayeux-e-regiao"
