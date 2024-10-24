from olxquery.categories import EletronicosECelulares


def test_category():
    assert (
        EletronicosECelulares.Games.Consoles.NintendoSwitch.get_url()
        == "games/consoles-de-video-game/nintendo-switch"
    )
    assert (
        EletronicosECelulares.Games.Consoles.Playstation4.get_url()
        == "games/consoles-de-video-game/playstation-4"
    )
    assert (
        EletronicosECelulares.CelularesETelefonia.Apple.IPhone12.get_url()
        == "celulares/apple/iphone-12"
    )
