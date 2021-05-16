class Eletronicos:
    __name = "Eletrônicos e Celulares"
    __url = "eletronicos-e-celulares"

    class Celulares:
        __name = "Celulares e Telefonia Móvel"
        __url = "celulares"

        class Asus:
            __name = "Celulares Asus"
            __url = "celulares/asus"
            __param = "cpt"
            __arg = "2"

        class Iphone:
            __name = "Celulares Iphone"
            __url = "celulares/iphone"
            __param = "cpt"
            __arg = "1"

        class Samsung:
            __name = "Celulares Iphone"
            __url = "celulares/samsung"
            __param = "cpt"
            __arg = "3"

    class Computadores:
        __name = "Computadores e Acessórios"
        __url = "computadores-e-acessorios"

        class Impressoras:
            __name = "Impressoras e Suplementos"
            __url = "computadores-e-acessorios/impressoras-e-suplementos"

        class Notebooks:
            __name = "Notebooks e Netbooks"
            __url = "computadores-e-acessorios/notebook-e-netbook"

        class PC:
            __name = "PCs e Computadores"
            __url = "computadores-e-acessorios/pcs-e-computadores"

        class Tablets:
            __name = "Ipads e Tablets"
            __url = "computadores-e-acessorios/ipad-e-tablet"

    class VideoGames:
        __name = "Video Games"
        __url = "videogames"
