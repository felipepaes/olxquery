from olxquery.locations import SP


def test_location():
    assert "estado-sp" == SP.get_url()
    assert "estado-sp/sao-paulo-e-regiao" == SP.DDD_11.get_url()
    assert "estado-sp/sao-paulo-e-regiao/zona-norte" == SP.DDD_11.ZonaNorte.get_url()
    assert (
        "estado-sp/sao-paulo-e-regiao/zona-norte/casa-verde"
        == SP.DDD_11.ZonaNorte.CasaVerde.get_url()
    )
