from par import es_par_logico


def test_par_positivo():
    assert es_par_logico(2)


def test_impar_positivo():
    assert not es_par_logico(3)


def test_cero():
    assert es_par_logico(0)


def test_par_negativo():
    assert es_par_logico(-2)


def test_impar_negativo():
    assert not es_par_logico(-3)


def test_par_grande():
    assert es_par_logico(1000000)


def test_impar_grande():
    assert not es_par_logico(1000001)
