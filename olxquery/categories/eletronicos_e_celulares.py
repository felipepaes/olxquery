from olxquery.types import Category


class EletronicosECelulares(Category):
    name = "Eletrônicos e celulares"
    url = "eletronicos-e-celulares"
    is_root = True

    class CelularesETelefonia(Category):
        name = "Celulares e telefonia"
        url = "celulares"

        class Apple(Category):
            name = "Celulares Apple"
            url = "apple"

            class IPhone12(Category):
                name = "Apple Iphone 12"
                url = "iphone-12"

    class Games(Category):
        name = "Games"
        url = "games"

        class Consoles(Category):
            name = "Consoles"
            url = "consoles-de-video-game"

            class Playstation4(Category):
                name = "Playstation 4"
                url = "playstation-4"

            class NintendoSwitch(Category):
                name = "Nintendo Switch"
                url = "nintendo-switch"
