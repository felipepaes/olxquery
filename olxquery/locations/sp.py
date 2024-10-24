from olxquery.types import Location


class SP(Location):
    name = "Estado de São Paulo"
    url = "estado-sp"

    class DDD_11(Location):
        name = "São Paulo e Região"
        url = "sao-paulo-e-regiao"

        class Centro(Location):
            name = "Região Central de São Paulo Capital"
            url = "centro"

            class Aclimacao(Location):
                name = "Bairro Aclimação"
                url = "aclimacao"

            class BarraFunda(Location):
                name = "Bairro Barra Funda"
                url = "barra-funda"

            class BelaVista(Location):
                name = "Bairro Bela Vista"
                url = "bela-vista"

            class Belem(Location):
                name = "Bairro Belém"
                url = "belem"

            class BomRetiro(Location):
                name = "Bairro Bom Retiro"
                url = "bom-retiro"

            class Cambuci(Location):
                name = "Bairo Cambuci"
                url = "cambuci"

            class CamposEliseos(Location):
                name = "Bairo Campos Elíseos"
                url = "campos-eliseos"

            class Centro(Location):
                name = "Bairro Centro"
                url = "centro"

            class Consolacao(Location):
                name = "Bairro Consolação"
                url = "consolacao"

            class Liberdade(Location):
                name = "Bairro Liberdade"
                url = "liberdade"

            class Republica(Location):
                name = "Bairro República"
                url = "republica"

            class SantaCecilia(Location):
                name = "Bairro Santa Cecília"
                url = "santa-cecilia"

        class ZonaLeste(Location):
            name = "Zona Leste de São Paulo Capital"
            url = "zona-leste"

        class ZonaNorte(Location):
            name = "Zona Noirte de São Paulo Capital"
            url = "zona-norte"

            class CasaVerde(Location):
                name = "Bairro Casa Verde"
                url = "casa-verde"

        class ZonaOeste(Location):
            name = "Zona Oeste de São Paulo Capital"
            url = "zona-oeste"

        class ZonaSul(Location):
            name = "Zona Sul de São Paulo Capital"
            url = "zona-sul"

        class Guarulhos(Location):
            name = "Guarulhos"
            url = "guarulhos"
