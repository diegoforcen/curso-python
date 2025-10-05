from src.primos import es_primo

def test_primos_basicos():
    assert es_primo(2)
    assert es_primo(3)
    assert es_primo(17)

def test_no_primos():
    assert not es_primo(1)
    assert not es_primo(4)
    assert not es_primo(20)