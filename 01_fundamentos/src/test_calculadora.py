import pytest
from src.calculadora import calcular


def test_suma():
    assert calcular(2, 3, "+") == 5


def test_resta():
    assert calcular(5, 2, "-") == 3


def test_multi():
    assert calcular(4, 3, "*") == 12


def test_division():
    assert calcular(8, 2, "/") == 4


def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        calcular(1, 0, "/")
