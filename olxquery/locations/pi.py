from olxquery.types import Location


class PI(Location):
    name = "Estado de PI"
    url = "estado-pi"

    class DDD_86(Location):
        name = "Teresina, Parnaíba e região"
        url = "regiao-de-teresina-e-parnaiba"

        class Teresina(Location):
            name = "Teresina"
            url = "teresina"

        class OutrasCidades(Location):
            name = "Outras Cidades"
            url = "outras-cidades"

    class DDD_89(Location):
        name = "Picos, Floriano e região"
        url = "regiao-de-picos-e-floriano"

        class TodasAsCidades(Location):
            name = "Todas as cidades"
            url = "todas-as-cidades"
