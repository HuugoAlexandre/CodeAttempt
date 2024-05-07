import pytest
import random
from ordenador import *

b = Ordenador()

def gerar_parametros(num_testes):
    parametros = []
    for _ in range(num_testes):
        lista_aleatoria = [random.randint(1, 10) for _ in range(10)]
        lista_ordenada = sorted(lista_aleatoria)
        parametros.append((lista_aleatoria, lista_ordenada))

    return parametros

@pytest.mark.parametrize("lista, esperado", gerar_parametros(5))
def test_ordernador_merge_sort(lista, esperado):
    assert b.merge_sort(lista) == esperado

@pytest.mark.parametrize("lista, esperado", gerar_parametros(5))
def test_ordenador_bubble_sort(lista, esperado):
    assert b.bubble_sort(lista) == esperado

@pytest.mark.parametrize("lista, esperado", gerar_parametros(5))
def test_ordenador_insertion_sort(lista, esperado):
    assert b.insertion_sort(lista) == esperado  

@pytest.mark.parametrize("lista, esperado", gerar_parametros(5))
def test_selecao_direta(lista, esperado):
    assert b.selecao_direta(lista) == esperado
    