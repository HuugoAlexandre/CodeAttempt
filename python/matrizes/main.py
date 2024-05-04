def cria_matriz(num_linha, num_coluna, valor=0):
    matriz = []
    for _ in range(num_linha):
        linha = []
        matriz.append(linha)
        for _ in range(num_coluna):
            linha.append(valor)

    return matriz

def mat_mul(A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    
    if num_colunas_A == num_linhas_B:
        C = cria_matriz(num_linhas_A, num_colunas_B)
        for linha in range(num_linhas_A):
            for coluna in range(num_colunas_B):
                for k in range(num_colunas_A):
                    C[linha][coluna] += A[linha][k] * B[k][coluna]
        return C
    else:
        return 'As matrizes recebidas não podem ser multiplicadas.'
    
a = [[1,2,3], [4,5,6]]
b = [[1, 2], [3, 4], [5, 6]]
print(mat_mul(a,b))