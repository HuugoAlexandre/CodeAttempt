import pytest
from buscador import *

a = [10,20,30,40,50,60]
b = Buscador()

def parametros_teste():
    return [
        (a, 10, 0),
        (a, 20, 1),
        (a, 30, 2),
        (a, 40, 3),
        (a, 50, 4),
        (a, 60, 5),
        (a, 70, False),
        (a, 15, False),
        (a, -10, False)
    ]

@pytest.mark.parametrize("lista, valor, esperado", parametros_teste())
def test_busca_binaria_recursiva(lista, valor, esperado):
    assert b.busca_binaria_recursiva(lista, valor) == esperado

@pytest.mark.parametrize("lista, valor, esperado", parametros_teste())
def test_busca_sequencial(lista, valor, esperado):
    assert b.busca_sequencial(lista, valor) == esperado

@pytest.mark.parametrize("lista, valor, esperado", parametros_teste())
def test_binaria(lista, valor, esperado):
    assert b.busca_binaria(lista, valor) == esperado
    