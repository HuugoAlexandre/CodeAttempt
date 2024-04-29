"""
Devolve a soma de todos os inteiros entre 1 e 'n' que são comprimento da hipotenusa
de algum triângulo retângulo com catetos inteiros.
"""

def soma_hipotenusa(n):
    soma = 0
    for i in range(1, n + 1):
        if é_hipotenusa(i):
            soma += i
    return soma

def é_hipotenusa(n):
    for a in range(1, n + 1):
        for b in range(a, n + 1 ):
            if a ** 2 + b ** 2 == n ** 2:
                return True
    return False

hi = int(input('Numero: '))
print(soma_hipotenusa(25))
