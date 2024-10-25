from olxquery.types import Category


class Eletro(Category):
    name = "Eletrodomesticos"
    url = "eletro"

    class GeladeirasEFreezers(Category):
        name = "Geladeiras e Freezers"
        url = "geladeiras-e-freezers"

    class MaquinasDeLavarESecadoras(Category):
        name = "Máquinas de Lavar e Secadoras"
        url = "maquinas-de-lavar-e-secadoras"
