import pytest
import main

@pytest.mark.parametrize('A, B, esperado', [
    ([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]], [[22, 28], [49, 64]]),
    ([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]], [[9, 12, 15], [19, 26, 33]]),
    ([[1,2,3], [2,3,1]], [[2,3], [1,2]], 'As matrizes recebidas não podem ser multiplicadas.')
])
def test_mat_mul(A, B, esperado):
    assert main.mat_mul(A, B) == esperado